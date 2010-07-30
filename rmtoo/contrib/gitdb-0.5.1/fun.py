"""Contains basic c-functions which usually contain performance critical code
Keeping this code separate from the beginning makes it easier to out-source
it into c later, if required"""

from exc import (
	BadObjectType
	)

from util import zlib
decompressobj = zlib.decompressobj

import mmap

# INVARIANTS
OFS_DELTA = 6
REF_DELTA = 7
delta_types = (OFS_DELTA, REF_DELTA)

type_id_to_type_map = 	{
							0 : "",				# EXT 1
							1 : "commit",
							2 : "tree",
							3 : "blob",
							4 : "tag",
							5 : "",				# EXT 2
							OFS_DELTA : "OFS_DELTA", 	# OFFSET DELTA
							REF_DELTA : "REF_DELTA"		# REFERENCE DELTA
						}

type_to_type_id_map = dict(
							commit=1, 
							tree=2,
							blob=3,
							tag=4,
							OFS_DELTA=OFS_DELTA,
							REF_DELTA=REF_DELTA
						)

# used when dealing with larger streams
chunk_size = 1000*mmap.PAGESIZE

__all__ = ('is_loose_object', 'loose_object_header_info', 'msb_size', 'pack_object_header_info', 
			'write_object', 'loose_object_header', 'stream_copy', 'apply_delta_data', 
			'is_equal_canonical_sha' )

#{ Routines

def is_loose_object(m):
	"""
	:return: True the file contained in memory map m appears to be a loose object.
		Only the first two bytes are needed"""
	b0, b1 = map(ord, m[:2])
	word = (b0 << 8) + b1
	return b0 == 0x78 and (word % 31) == 0

def loose_object_header_info(m):
	"""
	:return: tuple(type_string, uncompressed_size_in_bytes) the type string of the 
		object as well as its uncompressed size in bytes.
	:param m: memory map from which to read the compressed object data"""
	decompress_size = 8192		# is used in cgit as well
	hdr = decompressobj().decompress(m, decompress_size)
	type_name, size = hdr[:hdr.find("\0")].split(" ")
	return type_name, int(size)
	
def pack_object_header_info(data):
	"""
	:return: tuple(type_id, uncompressed_size_in_bytes, byte_offset)
		The type_id should be interpreted according to the ``type_id_to_type_map`` map
		The byte-offset specifies the start of the actual zlib compressed datastream
	:param m: random-access memory, like a string or memory map"""
	c = ord(data[0])				# first byte
	i = 1							# next char to read
	type_id = (c >> 4) & 7			# numeric type
	size = c & 15					# starting size
	s = 4							# starting bit-shift size
	while c & 0x80:
		c = ord(data[i])
		i += 1
		size += (c & 0x7f) << s
		s += 7
	# END character loop
	
	try:
		return (type_id, size, i)
	except KeyError:
		# invalid object type - we could try to be smart now and decode part 
		# of the stream to get the info, problem is that we had trouble finding 
		# the exact start of the content stream
		raise BadObjectType(type_id)
	# END handle exceptions
	
def msb_size(data, offset=0):
	"""
	:return: tuple(read_bytes, size) read the msb size from the given random 
		access data starting at the given byte offset"""
	size = 0
	i = 0
	l = len(data)
	hit_msb = False
	while i < l:
		c = ord(data[i+offset])
		size |= (c & 0x7f) << i*7
		i += 1
		if not c & 0x80:
			hit_msb = True
			break
		# END check msb bit
	# END while in range
	if not hit_msb:
		raise AssertionError("Could not find terminating MSB byte in data stream")
	return i+offset, size 
	
def loose_object_header(type, size):
	"""
	:return: string representing the loose object header, which is immediately
		followed by the content stream of size 'size'"""
	return "%s %i\0" % (type, size)
		
def write_object(type, size, read, write, chunk_size=chunk_size):
	"""
	Write the object as identified by type, size and source_stream into the 
	target_stream
	
	:param type: type string of the object
	:param size: amount of bytes to write from source_stream
	:param read: read method of a stream providing the content data
	:param write: write method of the output stream
	:param close_target_stream: if True, the target stream will be closed when
		the routine exits, even if an error is thrown
	:return: The actual amount of bytes written to stream, which includes the header and a trailing newline"""
	tbw = 0												# total num bytes written
	
	# WRITE HEADER: type SP size NULL
	tbw += write(loose_object_header(type, size))
	tbw += stream_copy(read, write, size, chunk_size)
	
	return tbw

def stream_copy(read, write, size, chunk_size):
	"""
	Copy a stream up to size bytes using the provided read and write methods, 
	in chunks of chunk_size
	
	:note: its much like stream_copy utility, but operates just using methods"""
	dbw = 0												# num data bytes written
	
	# WRITE ALL DATA UP TO SIZE
	while True:
		cs = min(chunk_size, size-dbw)
		# NOTE: not all write methods return the amount of written bytes, like
		# mmap.write. Its bad, but we just deal with it ... perhaps its not 
		# even less efficient
		# data_len = write(read(cs))
		# dbw += data_len
		data = read(cs)
		data_len = len(data)
		dbw += data_len
		write(data)
		if data_len < cs or dbw == size:
			break
		# END check for stream end
	# END duplicate data
	return dbw
	
	
def apply_delta_data(src_buf, src_buf_size, delta_buf, delta_buf_size, target_file):
	"""
	Apply data from a delta buffer using a source buffer to the target file, 
	which will be written to
	
	:param src_buf: random access data from which the delta was created
	:param src_buf_size: size of the source buffer in bytes
	:param delta_buf_size: size fo the delta buffer in bytes
	:param delta_buf: random access delta data
	:param target_file: file like object to write the result to
	:note: transcribed to python from the similar routine in patch-delta.c"""
	i = 0
	twrite = target_file.write
	db = delta_buf
	while i < delta_buf_size:
		c = ord(db[i])
		i += 1
		if c & 0x80:
			cp_off, cp_size = 0, 0
			if (c & 0x01):
				cp_off = ord(db[i])
				i += 1
			if (c & 0x02):
				cp_off |= (ord(db[i]) << 8)
				i += 1
			if (c & 0x04):
				cp_off |= (ord(db[i]) << 16)
				i += 1
			if (c & 0x08):
				cp_off |= (ord(db[i]) << 24)
				i += 1
			if (c & 0x10):
				cp_size = ord(db[i])
				i += 1
			if (c & 0x20):
				cp_size |= (ord(db[i]) << 8)
				i += 1
			if (c & 0x40):
				cp_size |= (ord(db[i]) << 16)
				i += 1
				
			if not cp_size: 
				cp_size = 0x10000
			
			rbound = cp_off + cp_size
			if (rbound < cp_size or
			    rbound > src_buf_size):
				break
			twrite(buffer(src_buf, cp_off, cp_size))
		elif c:
			twrite(db[i:i+c])
			i += c
		else:
			raise ValueError("unexpected delta opcode 0")
		# END handle command byte
	# END while processing delta data
	
	# yes, lets use the exact same error message that git uses :)
	assert i == delta_buf_size, "delta replay has gone wild"
	
	
def is_equal_canonical_sha(canonical_length, match, sha1):
	"""
	:return: True if the given lhs and rhs 20 byte binary shas
		The comparison will take the canonical_length of the match sha into account, 
		hence the comparison will only use the last 4 bytes for uneven canonical representations
	:param match: less than 20 byte sha
	:param sha1: 20 byte sha"""
	binary_length = canonical_length/2
	if match[:binary_length] != sha1[:binary_length]:
		return False
		
	if canonical_length - binary_length and \
		(ord(match[-1]) ^ ord(sha1[len(match)-1])) & 0xf0:
		return False
	# END handle uneven canonnical length
	return True
	
#} END routines

