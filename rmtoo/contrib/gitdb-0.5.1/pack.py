"""Contains PackIndexFile and PackFile implementations"""
from gitdb.exc import (
						BadObject,
						UnsupportedOperation
						)
from util import (
					zlib,
					LazyMixin,
					unpack_from,
					file_contents_ro_filepath,
					)

from fun import (
					pack_object_header_info,
					is_equal_canonical_sha,
					type_id_to_type_map,
					write_object,
					stream_copy, 
					chunk_size,
					delta_types,
					OFS_DELTA, 
					REF_DELTA,
					msb_size
				)

try:
	from _fun import PackIndexFile_sha_to_index
except ImportError:
	pass
# END try c module

from base import (		# Amazing !
						OInfo,
						OStream,
						OPackInfo,
						OPackStream,
						ODeltaPackInfo,
						ODeltaPackStream,
					)
from stream import (
						DecompressMemMapReader,
						DeltaApplyReader,
						Sha1Writer,
						NullStream,
					)

from struct import (
						pack,
						unpack,
					)

from itertools import izip
import array
import os
import sys

__all__ = ('PackIndexFile', 'PackFile', 'PackEntity')

 

	
#{ Utilities 

def pack_object_at(data, offset, as_stream):
	"""
	:return: Tuple(abs_data_offset, PackInfo|PackStream)
		an object of the correct type according to the type_id  of the object.
		If as_stream is True, the object will contain a stream, allowing  the
		data to be read decompressed.
	:param data: random accessable data containing all required information
	:parma offset: offset in to the data at which the object information is located
	:param as_stream: if True, a stream object will be returned that can read 
		the data, otherwise you receive an info object only"""
	data = buffer(data, offset)
	type_id, uncomp_size, data_rela_offset = pack_object_header_info(data)
	total_rela_offset = None				# set later, actual offset until data stream begins
	delta_info = None
	
	# OFFSET DELTA
	if type_id == OFS_DELTA:
		i = data_rela_offset
		c = ord(data[i])
		i += 1
		delta_offset = c & 0x7f
		while c & 0x80:
			c = ord(data[i])
			i += 1
			delta_offset += 1
			delta_offset = (delta_offset << 7) + (c & 0x7f)
		# END character loop
		delta_info = delta_offset
		total_rela_offset = i
	# REF DELTA
	elif type_id == REF_DELTA:
		total_rela_offset = data_rela_offset+20
		ref_sha = data[data_rela_offset:total_rela_offset]
		delta_info = ref_sha
	# BASE OBJECT
	else:
		# assume its a base object
		total_rela_offset = data_rela_offset
	# END handle type id
	
	abs_data_offset = offset + total_rela_offset
	if as_stream:
		stream = DecompressMemMapReader(buffer(data, total_rela_offset), False, uncomp_size)
		if delta_info is None:
			return abs_data_offset, OPackStream(offset, type_id, uncomp_size, stream)
		else:
			return abs_data_offset, ODeltaPackStream(offset, type_id, uncomp_size, delta_info, stream)
	else:
		if delta_info is None:
			return abs_data_offset, OPackInfo(offset, type_id, uncomp_size)
		else:
			return abs_data_offset, ODeltaPackInfo(offset, type_id, uncomp_size, delta_info)
		# END handle info
	# END handle stream
		
#} END utilities



class PackIndexFile(LazyMixin):
	"""A pack index provides offsets into the corresponding pack, allowing to find
	locations for offsets faster."""
	
	# Dont use slots as we dynamically bind functions for each version, need a dict for this
	# The slots you see here are just to keep track of our instance variables
	# __slots__ = ('_indexpath', '_fanout_table', '_data', '_version', 
	#				'_sha_list_offset', '_crc_list_offset', '_pack_offset', '_pack_64_offset')

	# used in v2 indices
	_sha_list_offset = 8 + 1024

	def __init__(self, indexpath):
		super(PackIndexFile, self).__init__()
		self._indexpath = indexpath
	
	def _set_cache_(self, attr):
		if attr == "_packfile_checksum":
			self._packfile_checksum = self._data[-40:-20]
		elif attr == "_packfile_checksum":
			self._packfile_checksum = self._data[-20:]
		elif attr == "_data":
			# Note: We don't lock the file when reading as we cannot be sure
			# that we can actually write to the location - it could be a read-only
			# alternate for instance
			self._data = file_contents_ro_filepath(self._indexpath)
		else:
			# now its time to initialize everything - if we are here, someone wants
			# to access the fanout table or related properties
			
			# CHECK VERSION
			self._version = (self._data[:4] == '\377tOc' and 2) or 1
			if self._version == 2:
				version_id = unpack_from(">L", self._data, 4)[0] 
				assert version_id == self._version, "Unsupported index version: %i" % version_id
			# END assert version
			
			# SETUP FUNCTIONS
			# setup our functions according to the actual version
			for fname in ('entry', 'offset', 'sha', 'crc'):
				setattr(self, fname, getattr(self, "_%s_v%i" % (fname, self._version)))
			# END for each function to initialize
			
			
			# INITIALIZE DATA
			# byte offset is 8 if version is 2, 0 otherwise
			self._initialize()
		# END handle attributes
		

	#{ Access V1
	
	def _entry_v1(self, i):
		""":return: tuple(offset, binsha, 0)"""
		return unpack_from(">L20s", self._data, 1024 + i*24) + (0, ) 
	
	def _offset_v1(self, i):
		"""see ``_offset_v2``"""
		return unpack_from(">L", self._data, 1024 + i*24)[0]
	
	def _sha_v1(self, i):
		"""see ``_sha_v2``"""
		base = 1024 + (i*24)+4
		return self._data[base:base+20]
		
	def _crc_v1(self, i):
		"""unsupported"""
		return 0
		
	#} END access V1
	
	#{ Access V2
	def _entry_v2(self, i):
		""":return: tuple(offset, binsha, crc)"""
		return (self._offset_v2(i), self._sha_v2(i), self._crc_v2(i))
	
	def _offset_v2(self, i):
		""":return: 32 or 64 byte offset into pack files. 64 byte offsets will only 
			be returned if the pack is larger than 4 GiB, or 2^32"""
		offset = unpack_from(">L", self._data, self._pack_offset + i * 4)[0]
		
		# if the high-bit is set, this indicates that we have to lookup the offset
		# in the 64 bit region of the file. The current offset ( lower 31 bits )
		# are the index into it
		if offset & 0x80000000:
			offset = unpack_from(">Q", self._data, self._pack_64_offset + (offset & ~0x80000000) * 8)[0]
		# END handle 64 bit offset
		
		return offset
		
	def _sha_v2(self, i):
		""":return: sha at the given index of this file index instance"""
		base = self._sha_list_offset + i * 20
		return self._data[base:base+20]
		
	def _crc_v2(self, i):
		""":return: 4 bytes crc for the object at index i"""
		return unpack_from(">L", self._data, self._crc_list_offset + i * 4)[0] 
		
	#} END access V2
	
	#{ Initialization
	
	def _initialize(self):
		"""initialize base data"""
		self._fanout_table = self._read_fanout((self._version == 2) * 8)
		
		if self._version == 2:
			self._crc_list_offset = self._sha_list_offset + self.size() * 20
			self._pack_offset = self._crc_list_offset + self.size() * 4
			self._pack_64_offset = self._pack_offset + self.size() * 4
		# END setup base
		
	def _read_fanout(self, byte_offset):
		"""Generate a fanout table from our data"""
		d = self._data
		out = list()
		append = out.append
		for i in range(256):
			append(unpack_from('>L', d, byte_offset + i*4)[0])
		# END for each entry
		return out
	
	#} END initialization
		
	#{ Properties
	def version(self):
		return self._version
		
	def size(self):
		""":return: amount of objects referred to by this index"""
		return self._fanout_table[255]
		
	def path(self):
		""":return: path to the packindexfile"""
		return self._indexpath
		
	def packfile_checksum(self):
		""":return: 20 byte sha representing the sha1 hash of the pack file"""
		return self._data[-40:-20]
		
	def indexfile_checksum(self):
		""":return: 20 byte sha representing the sha1 hash of this index file"""
		return self._data[-20:]
		
	def offsets(self):
		""":return: sequence of all offsets in the order in which they were written
		:note: return value can be random accessed, but may be immmutable"""
		if self._version == 2:
			# read stream to array, convert to tuple
			a = array.array('I')	# 4 byte unsigned int, long are 8 byte on 64 bit it appears
			a.fromstring(buffer(self._data, self._pack_offset, self._pack_64_offset - self._pack_offset))
			
			# networkbyteorder to something array likes more
			if sys.byteorder == 'little':
				a.byteswap()
			return a
		else:
			return tuple(self.offset(index) for index in xrange(self.size()))
		# END handle version
		
	def sha_to_index(self, sha):
		"""
		:return: index usable with the ``offset`` or ``entry`` method, or None
			if the sha was not found in this pack index
		:param sha: 20 byte sha to lookup"""
		first_byte = ord(sha[0])
		get_sha = self.sha
		lo = 0					# lower index, the left bound of the bisection
		if first_byte != 0:
			lo = self._fanout_table[first_byte-1]
		hi = self._fanout_table[first_byte]		# the upper, right bound of the bisection
		
		# bisect until we have the sha
		while lo < hi:
			mid = (lo + hi) / 2
			c = cmp(sha, get_sha(mid))
			if c < 0:
				hi = mid
			elif not c:
				return mid
			else:
				lo = mid + 1
			# END handle midpoint
		# END bisect
		return None
		
	def partial_sha_to_index(self, partial_bin_sha, canonical_length):
		"""
		:return: index as in `sha_to_index` or None if the sha was not found in this
			index file
		:param partial_bin_sha: an at least two bytes of a partial binary sha
		:param canonical_length: lenght of the original hexadecimal representation of the 
			given partial binary sha
		:raise AmbiguousObjectName:"""
		if len(partial_bin_sha) < 2:
			raise ValueError("Require at least 2 bytes of partial sha")
		
		first_byte = ord(partial_bin_sha[0])
		get_sha = self.sha
		lo = 0					# lower index, the left bound of the bisection
		if first_byte != 0:
			lo = self._fanout_table[first_byte-1]
		hi = self._fanout_table[first_byte]		# the upper, right bound of the bisection
		
		# fill the partial to full 20 bytes
		filled_sha = partial_bin_sha + '\0'*(20 - len(partial_bin_sha))
		
		# find lowest 
		while lo < hi:
			mid = (lo + hi) / 2
			c = cmp(filled_sha, get_sha(mid))
			if c < 0:
				hi = mid
			elif not c:
				# perfect match
				lo = mid
				break
			else:
				lo = mid + 1
			# END handle midpoint
		# END bisect
		
		if lo < self.size():
			cur_sha = get_sha(lo)
			if is_equal_canonical_sha(canonical_length, partial_bin_sha, cur_sha):
				next_sha = None
				if lo+1 < self.size():
					next_sha = get_sha(lo+1)
				if next_sha and next_sha == cur_sha:
					raise AmbiguousObjectName(partial_bin_sha)
				return lo
			# END if we have a match
		# END if we found something
		return None
		
	if 'PackIndexFile_sha_to_index' in globals():
		# NOTE: Its just about 25% faster, the major bottleneck might be the attr 
		# accesses
		def sha_to_index(self, sha):
			return PackIndexFile_sha_to_index(self, sha)
	# END redefine heavy-hitter with c version  
	
	#} END properties
	
	
class PackFile(LazyMixin):
	"""A pack is a file written according to the Version 2 for git packs
	
	As we currently use memory maps, it could be assumed that the maximum size of
	packs therefor is 32 bit on 32 bit systems. On 64 bit systems, this should be 
	fine though.
	
	:note: at some point, this might be implemented using streams as well, or 
		streams are an alternate path in the case memory maps cannot be created
		for some reason - one clearly doesn't want to read 10GB at once in that 
		case"""
	
	__slots__ = ('_packpath', '_data', '_size', '_version')
	
	# offset into our data at which the first object starts
	first_object_offset = 3*4		# header bytes
	footer_size = 20				# final sha
	
	def __init__(self, packpath):
		self._packpath = packpath
		
	def _set_cache_(self, attr):
		if attr == '_data':
			self._data = file_contents_ro_filepath(self._packpath)
			
			# read the header information
			type_id, self._version, self._size = unpack_from(">4sLL", self._data, 0)
			
			# TODO: figure out whether we should better keep the lock, or maybe
			# add a .keep file instead ?
		else: # must be '_size' or '_version'
			# read header info - we do that just with a file stream
			type_id, self._version, self._size = unpack(">4sLL", open(self._packpath).read(12))
		# END handle header
		
	def _iter_objects(self, start_offset, as_stream=True):
		"""Handle the actual iteration of objects within this pack"""
		data = self._data
		content_size = len(data) - self.footer_size
		cur_offset = start_offset or self.first_object_offset
		
		null = NullStream()
		while cur_offset < content_size:
			data_offset, ostream = pack_object_at(data, cur_offset, True)
			# scrub the stream to the end - this decompresses the object, but yields
			# the amount of compressed bytes we need to get to the next offset
				
			stream_copy(ostream.read, null.write, ostream.size, chunk_size)
			cur_offset += (data_offset - ostream.pack_offset) + ostream.stream.compressed_bytes_read()
			
			
			# if a stream is requested, reset it beforehand
			# Otherwise return the Stream object directly, its derived from the 
			# info object
			if as_stream:
				ostream.stream.seek(0)
			yield ostream
		# END until we have read everything
		
	#{ Pack Information
	
	def size(self):
		""":return: The amount of objects stored in this pack""" 
		return self._size
		
	def version(self):
		""":return: the version of this pack"""
		return self._version
		
	def data(self):
		"""
		:return: read-only data of this pack. It provides random access and usually
			is a memory map"""
		return self._data
		
	def checksum(self):
		""":return: 20 byte sha1 hash on all object sha's contained in this file"""
		return self._data[-20:]
	
	def path(self):
		""":return: path to the packfile"""
		return self._packpath
	#} END pack information
	
	#{ Pack Specific
	
	def collect_streams(self, offset):
		"""
		:return: list of pack streams which are required to build the object
			at the given offset. The first entry of the list is the object at offset, 
			the last one is either a full object, or a REF_Delta stream. The latter
			type needs its reference object to be locked up in an ODB to form a valid
			delta chain.
			If the object at offset is no delta, the size of the list is 1.
		:param offset: specifies the first byte of the object within this pack"""
		out = list()
		while True:
			ostream = pack_object_at(self._data, offset, True)[1]
			out.append(ostream)
			if ostream.type_id == OFS_DELTA:
				offset = ostream.pack_offset - ostream.delta_info
			else:
				# the only thing we can lookup are OFFSET deltas. Everything
				# else is either an object, or a ref delta, in the latter 
				# case someone else has to find it
				break
			# END handle type
		# END while chaining streams
		return out

	#} END pack specific
	
	#{ Read-Database like Interface
	
	def info(self, offset):
		"""Retrieve information about the object at the given file-absolute offset
		
		:param offset: byte offset
		:return: OPackInfo instance, the actual type differs depending on the type_id attribute"""
		return pack_object_at(self._data, offset or self.first_object_offset, False)[1]
		
	def stream(self, offset):
		"""Retrieve an object at the given file-relative offset as stream along with its information
		
		:param offset: byte offset
		:return: OPackStream instance, the actual type differs depending on the type_id attribute"""
		return pack_object_at(self._data, offset or self.first_object_offset, True)[1]
		
	def stream_iter(self, start_offset=0):
		"""
		:return: iterator yielding OPackStream compatible instances, allowing 
			to access the data in the pack directly.
		:param start_offset: offset to the first object to iterate. If 0, iteration 
			starts at the very first object in the pack.
		:note: Iterating a pack directly is costly as the datastream has to be decompressed
			to determine the bounds between the objects"""
		return self._iter_objects(start_offset, as_stream=True)
		
	#} END Read-Database like Interface
	
	
class PackEntity(LazyMixin):
	"""Combines the PackIndexFile and the PackFile into one, allowing the 
	actual objects to be resolved and iterated"""
	
	__slots__ = (	'_index',			# our index file 
					'_pack', 			# our pack file
					'_offset_map'		# on demand dict mapping one offset to the next consecutive one
					)
	
	IndexFileCls = PackIndexFile
	PackFileCls = PackFile
	
	def __init__(self, pack_or_index_path):
		"""Initialize ourselves with the path to the respective pack or index file"""
		basename, ext = os.path.splitext(pack_or_index_path)
		self._index = self.IndexFileCls("%s.idx" % basename)			# PackIndexFile instance
		self._pack = self.PackFileCls("%s.pack" % basename)			# corresponding PackFile instance
		
	def _set_cache_(self, attr):
		# currently this can only be _offset_map
		offsets_sorted = sorted(self._index.offsets())
		last_offset = len(self._pack.data()) - self._pack.footer_size
		assert offsets_sorted, "Cannot handle empty indices"
		
		offset_map = None
		if len(offsets_sorted) == 1:
			offset_map = { offsets_sorted[0] : last_offset }
		else:
			iter_offsets = iter(offsets_sorted)
			iter_offsets_plus_one = iter(offsets_sorted)
			iter_offsets_plus_one.next()
			consecutive = izip(iter_offsets, iter_offsets_plus_one)
			
			offset_map = dict(consecutive)
			
			# the last offset is not yet set
			offset_map[offsets_sorted[-1]] = last_offset
		# END handle offset amount
		self._offset_map = offset_map
	
	def _sha_to_index(self, sha):
		""":return: index for the given sha, or raise"""
		index = self._index.sha_to_index(sha)
		if index is None:
			raise BadObject(sha)
		return index
	
	def _iter_objects(self, as_stream):
		"""Iterate over all objects in our index and yield their OInfo or OStream instences"""
		indexfile = self._index
		_object = self._object
		for index in xrange(indexfile.size()):
			sha = indexfile.sha(index)
			yield _object(sha, as_stream, index)
		# END for each index
	
	def _object(self, sha, as_stream, index=-1):
		""":return: OInfo or OStream object providing information about the given sha
		:param index: if not -1, its assumed to be the sha's index in the IndexFile"""
		# its a little bit redundant here, but it needs to be efficient
		if index < 0:
			index = self._sha_to_index(sha)
		if sha is None:
			sha = self._index.sha(index)
		# END assure sha is present ( in output )
		offset = self._index.offset(index)
		type_id, uncomp_size, data_rela_offset = pack_object_header_info(buffer(self._pack._data, offset))
		if as_stream:
			if type_id not in delta_types:
				packstream = self._pack.stream(offset)
				return OStream(sha, packstream.type, packstream.size, packstream.stream)
			# END handle non-deltas
			
			# produce a delta stream containing all info
			# To prevent it from applying the deltas when querying the size, 
			# we extract it from the delta stream ourselves
			streams = self.collect_streams_at_offset(offset)
			buf = streams[0].read(512)
			offset, src_size = msb_size(buf)
			offset, target_size = msb_size(buf, offset)
			
			streams[0].stream.seek(0)				# assure it can be read by the delta reader
			dstream = DeltaApplyReader.new(streams)
			
			return OStream(sha, dstream.type, target_size, dstream) 
		else:
			if type_id not in delta_types:
				return OInfo(sha, type_id_to_type_map[type_id], uncomp_size)
			# END handle non-deltas
			
			# deltas are a little tougher - unpack the first bytes to obtain
			# the actual target size, as opposed to the size of the delta data
			streams = self.collect_streams_at_offset(offset)
			buf = streams[0].read(512)
			offset, src_size = msb_size(buf)
			offset, target_size = msb_size(buf, offset)
			
			# collect the streams to obtain the actual object type
			if streams[-1].type_id in delta_types:
				raise BadObject(sha, "Could not resolve delta object")
			return OInfo(sha, streams[-1].type, target_size) 
		# END handle stream
	
	#{ Read-Database like Interface
	
	def info(self, sha):
		"""Retrieve information about the object identified by the given sha
		
		:param sha: 20 byte sha1
		:raise BadObject:
		:return: OInfo instance, with 20 byte sha"""
		return self._object(sha, False)
		
	def stream(self, sha):
		"""Retrieve an object stream along with its information as identified by the given sha
		
		:param sha: 20 byte sha1
		:raise BadObject: 
		:return: OStream instance, with 20 byte sha"""
		return self._object(sha, True)

	def info_at_index(self, index):
		"""As ``info``, but uses a PackIndexFile compatible index to refer to the object"""
		return self._object(None, False, index)
	
	def stream_at_index(self, index):
		"""As ``stream``, but uses a PackIndexFile compatible index to refer to the 
		object"""
		return self._object(None, True, index)
		
	#} END Read-Database like Interface
	
	#{ Interface 

	def pack(self):
		""":return: the underlying pack file instance"""
		return self._pack
		
	def index(self):
		""":return: the underlying pack index file instance"""
		return self._index
		
	def is_valid_stream(self, sha, use_crc=False):
		"""
		Verify that the stream at the given sha is valid.
		
		:param use_crc: if True, the index' crc for the sha is used to determine
		:param sha: 20 byte sha1 of the object whose stream to verify
		whether the compressed stream of the object is valid. If it is 
			a delta, this only verifies that the delta's data is valid, not the 
			data of the actual undeltified object, as it depends on more than 
			just this stream.
			If False, the object will be decompressed and the sha generated. It must
			match the given sha
			
		:return: True if the stream is valid
		:raise UnsupportedOperation: If the index is version 1 only
		:raise BadObject: sha was not found"""
		if use_crc:
			if self._index.version() < 2:
				raise UnsupportedOperation("Version 1 indices do not contain crc's, verify by sha instead")
			# END handle index version
			
			index = self._sha_to_index(sha)
			offset = self._index.offset(index)
			next_offset = self._offset_map[offset]
			crc_value = self._index.crc(index)
			
			# create the current crc value, on the compressed object data
			# Read it in chunks, without copying the data
			crc_update = zlib.crc32
			pack_data = self._pack.data()
			cur_pos = offset
			this_crc_value = 0
			while cur_pos < next_offset:
				rbound = min(cur_pos + chunk_size, next_offset)
				size = rbound - cur_pos
				this_crc_value = crc_update(buffer(pack_data, cur_pos, size), this_crc_value)
				cur_pos += size
			# END window size loop
			
			# crc returns signed 32 bit numbers, the AND op forces it into unsigned
			# mode ... wow, sneaky, from dulwich.
			return (this_crc_value & 0xffffffff) == crc_value
		else:
			shawriter = Sha1Writer()
			stream = self._object(sha, as_stream=True)
			# write a loose object, which is the basis for the sha
			write_object(stream.type, stream.size, stream.read, shawriter.write)
			
			assert shawriter.sha(as_hex=False) == sha
			return shawriter.sha(as_hex=False) == sha
		# END handle crc/sha verification
		return True

	def info_iter(self):
		"""
		:return: Iterator over all objects in this pack. The iterator yields
			OInfo instances"""
		return self._iter_objects(as_stream=False)
		
	def stream_iter(self):
		"""
		:return: iterator over all objects in this pack. The iterator yields
			OStream instances"""
		return self._iter_objects(as_stream=True)
		
	def collect_streams_at_offset(self, offset):
		"""
		As the version in the PackFile, but can resolve REF deltas within this pack
		For more info, see ``collect_streams``
		
		:param offset: offset into the pack file at which the object can be found"""
		streams = self._pack.collect_streams(offset)
		
		# try to resolve the last one if needed. It is assumed to be either
		# a REF delta, or a base object, as OFFSET deltas are resolved by the pack
		if streams[-1].type_id == REF_DELTA:
			stream = streams[-1]
			while stream.type_id in delta_types:
				if stream.type_id == REF_DELTA:
					sindex = self._index.sha_to_index(stream.delta_info)
					if sindex is None:
						break
					stream = self._pack.stream(self._index.offset(sindex))
					streams.append(stream)
				else:
					# must be another OFS DELTA - this could happen if a REF 
					# delta we resolve previously points to an OFS delta. Who 
					# would do that ;) ? We can handle it though
					stream = self._pack.stream(stream.delta_info)
					streams.append(stream)
				# END handle ref delta
			# END resolve ref streams
		# END resolve streams
		
		return streams
		
	def collect_streams(self, sha):
		"""
		As ``PackFile.collect_streams``, but takes a sha instead of an offset.
		Additionally, ref_delta streams will be resolved within this pack.
		If this is not possible, the stream will be left alone, hence it is adivsed
		to check for unresolved ref-deltas and resolve them before attempting to 
		construct a delta stream.
		
		:param sha: 20 byte sha1 specifying the object whose related streams you want to collect
		:return: list of streams, first being the actual object delta, the last being 
			a possibly unresolved base object.
		:raise BadObject:"""
		return self.collect_streams_at_offset(self._index.offset(self._sha_to_index(sha)))
		
		
		
	#} END interface
