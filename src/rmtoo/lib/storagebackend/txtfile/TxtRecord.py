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
    """The (plain) text specialization of the record"""

    def __init__(self, tioconfig):
        '''PRIVATE constructor!
        Please use the from_xxx methods for creating objects of
        TxtRecord from client code.
        '''
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

    @classmethod
    def from_fd(cls, file_des, rid, tioconfig):
        """Construct a TxtRecord from a given file descriptior
        rid is the Requirement ID.
        """
        obj = cls(tioconfig)
        # Because there is only a very limited interface for some VCSes
        # the whole file is read in at once.
        obj.parse(file_des.read(), rid)
        return obj

    def write_fd(self, file_des):
        """Write to filesystem"""
        for element in self:
            element.write_fd(file_des)

    @staticmethod
    def maybe_remove_last_empty_line(split_lines):
        """Remove the last empty line

        which might be a relict from the split.
        """
        sl_len = len(split_lines)
        if sl_len == 0:
            return
        if not split_lines[sl_len - 1]:
            del split_lines[sl_len - 1]
        return

    def check_line_length(self, split_lines, rid):
        """Check if the given lines are too long (or not)"""
        max_line_length = self.tioconfig.get_max_line_length()
        lineno = 0
        for line in split_lines:
            lineno += 1
            if len(line) > max_line_length:
                logger.error(LogFormatter.format(
                    80, "line too long: is [%d], "
                    "max allowed [%d]" % (len(line), max_line_length),
                    rid, lineno))
                self._set_not_usable()

    def parse(self, record, rid):
        """Parse everything from a string"""
        # Split up into lines
        Encoding.check_unicode(record)
        split_lines = record.split("\n")
        self.check_line_length(split_lines, rid)
        self.maybe_remove_last_empty_line(split_lines)
        self.comment_raw = TxtParser.extract_record_comment(split_lines)
        for comment in self.comment_raw:
            Encoding.check_unicode(comment)
        self.set_comment(TxtParser.extract_comment(self.comment_raw))
        Encoding.check_unicode(self.get_comment())

        success, parsed_record = TxtParser.split_entries(
            split_lines, rid, self, len(self.comment_raw) + 1)
        # If there was an error during the split already - stop
        # processing here
        if not success:
            self._set_not_usable()
            return

        for i in parsed_record:
            self.append(TxtRecordEntry(i))
        return

    def to_string(self):
        """Convert to string"""
        rstring = TxtParser.add_newlines(self.comment_raw)
        for line in self:
            # There is the need to check for the type: only the
            # TxtRecordEntry provides a (for this method) usable
            # output.
            if isinstance(line, TxtRecordEntry):
                rstring += line.to_string()
            else:
                # If this is another RecordEntry, at least get some
                # infos from this.
                rstring += TxtRecordEntry.format_entry(line)
        return rstring
