#
# rmtoo 
#   Free and Open Source Requirements Management Tool
#
# Text Record Input / Output class
#
# This is the parser and output module for the standard text file
# format. 
#
# (c) 2010-2011 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.storagebackend.Record import Record
from rmtoo.lib.storagebackend.txtfile.TxtParser import TxtParser
from rmtoo.lib.storagebackend.txtfile.TxtRecordEntry import TxtRecordEntry

class TxtRecord(Record):

    @classmethod
    def from_string(cls, s):
        obj = cls()
        obj.parse(s)
        return obj

    @classmethod
    def from_fd(cls, fd):
        obj = cls()
        # Because there is only a very limited interface for some VCSes
        # the whole file is read in at once.
        obj.parse(fd.read())
        return obj

    # Remove the last empty line - which might be a relict from the split.
    def maybe_remove_last_empty_line(self, sl):
        sl_len = len(sl)
        if sl_len==0:
            return
        if len(sl[sl_len-1])==0:
            del(sl[sl_len-1])
        return

    # Parse everything from a string
    def parse(self, s):
        # Split up into lines
        sl = s.split("\n")
        self.maybe_remove_last_empty_line(sl)
        self.comment_raw = TxtParser.extract_record_comment(sl)
        self.set_comment(TxtParser.extract_comment(self.comment_raw))

        rp = TxtParser.split_entries(sl)
        for i in rp:
            self.llist.append(TxtRecordEntry(i))
        return 

    # Convert to string
    def to_string(self):
        s = TxtParser.add_newlines(self.comment_raw)
        for l in self.llist:
            # There is the need to check for the type: only the
            # TxtRecordEntry provide a (for this method) usable
            # output.
            if isinstance(l, TxtRecordEntry):
                s += l.to_string()
            else:
                # If this is another RecordEntry, at least get some
                # infos from this.
                s += TxtRecordEntry.format_entry(l)
        return s
