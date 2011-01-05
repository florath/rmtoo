#
# rmtoo 
#   Free and Open Source Requirements Management Tool
#
#  Text Record Input / Output class
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

    # Parse everything from a string
    def parse(self, s):
        # Split up into lines
        sl = s.split("\n")
        self.comment = TxtParser.extract_record_comment(sl)

        print("COMMENT: '%s'" % self.comment)
        print("REST: '%s'" % sl)

        rp = self.split_entries(sl)
        for i in rp:
            self.append(TxtRecordEntry(i))
