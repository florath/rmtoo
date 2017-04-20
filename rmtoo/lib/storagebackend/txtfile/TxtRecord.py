'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Text Record Input / Output class

  This is the parser and output module for the standard text file
  format.

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from rmtoo.lib.Encoding import Encoding
from rmtoo.lib.storagebackend.Record import Record
from rmtoo.lib.storagebackend.txtfile.TxtParser import TxtParser
from rmtoo.lib.storagebackend.txtfile.TxtRecordEntry import TxtRecordEntry
from rmtoo.lib.logging import logger
from rmtoo.lib.logging.LogFormatter import LogFormatter


class TxtRecord(Record):

    def __init__(self, tioconfig):
        '''PRIVATE constructor!
           Please use the from_xxx methods for creating objects of
           TxtRecord from client code.'''
        super(TxtRecord, self).__init__()
        self.tioconfig = tioconfig
        self.comment_raw = None

    # There is the need to have something like
    # is_usable

    @classmethod
    def from_string(cls, in_str, rid, tioconfig):
        '''Construct a TxtRecord from a given string.
           rid is the Requirement ID.'''
        Encoding.check_unicode(in_str)
        obj = cls(tioconfig)
        obj.parse(in_str, rid)
        return obj

    # Construct a TxtRecord from a given file descriptior
    # rid is the Requirement ID
    @classmethod
    def from_fd(cls, fd, rid, tioconfig):
        obj = cls(tioconfig)
        # Because there is only a very limited interface for some VCSes
        # the whole file is read in at once.
        obj.parse(fd.read(), rid)
        return obj

    # Write to filesystem
    def write_fd(self, fd):
        for l in self:
            l.write_fd(fd)

    # Remove the last empty line - which might be a relict from the split.
    def maybe_remove_last_empty_line(self, sl):
        sl_len = len(sl)
        if sl_len == 0:
            return
        if len(sl[sl_len - 1]) == 0:
            del(sl[sl_len - 1])
        return

    # Check if the given lines are too long (or not)
    def check_line_length(self, sl, rid):
        max_line_length = self.tioconfig.get_max_line_length()
        lineno = 0
        for l in sl:
            lineno += 1
            if len(l) > max_line_length:
                logger.error(LogFormatter.format(
                    80, "line too long: is [%d], "
                    "max allowed [%d]" % (len(l), max_line_length),
                    rid, lineno))
                self._set_not_usable()

    # Parse everything from a string
    def parse(self, s, rid):
        # Split up into lines
        Encoding.check_unicode(s)
        sl = s.split("\n")
        self.check_line_length(sl, rid)
        self.maybe_remove_last_empty_line(sl)
        self.comment_raw = TxtParser.extract_record_comment(sl)
        for c in self.comment_raw:
            Encoding.check_unicode(c)
        self.set_comment(TxtParser.extract_comment(self.comment_raw))
        Encoding.check_unicode(self.get_comment())

        success, rp = TxtParser.split_entries(
            sl, rid, self, len(self.comment_raw) + 1)
        # If there was an error during the split already - stop
        # processing here
        if not success:
            self._set_not_usable()
            return

        for i in rp:
            self.append(TxtRecordEntry(i))
        return

    # Convert to string
    def to_string(self):
        s = TxtParser.add_newlines(self.comment_raw)
        for l in self:
            # There is the need to check for the type: only the
            # TxtRecordEntry provides a (for this method) usable
            # output.
            if isinstance(l, TxtRecordEntry):
                s += l.to_string()
            else:
                # If this is another RecordEntry, at least get some
                # infos from this.
                s += TxtRecordEntry.format_entry(l)
        return s
