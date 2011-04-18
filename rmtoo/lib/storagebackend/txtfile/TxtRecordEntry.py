#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# Txt Record Entry Class
#  This class hold additionally the original raw representation of
#  each record entry. When the 
#
# (c) 2011 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.storagebackend.txtfile.TxtParser import TxtParser
from rmtoo.lib.storagebackend.RecordEntry import RecordEntry
from rmtoo.lib.StringHelper import StringHelper

class TxtRecordEntry(RecordEntry):

    def __init__(self, se):
        # There must be three entries:
        # 1) initial line with tag
        # 2) possible empty list of continue lines (starting with space)
        # 3) possible empty list of comment and / or empty lines
        assert(len(se)==3)

        self.setup(se)

    def setup(self, se):
        # Store the raw input for possible later output
        self.tag_raw = se[0]
        self.content_raw = se[1]
        self.comment_raw = se[2]
        # Parse the rest
        tag = self.tag_raw[0:-1]
#        tag, value = TxtParser.split_tag_line(se[0])
        value = "".join(se[1])
# TxtParser.extract_continuation_lines(se[1])
        comment = TxtParser.extract_comment(se[2])
        RecordEntry.__init__(self, tag, value, comment)

    def to_string(self):
        add_content = TxtParser.add_newlines(self.content_raw)
        add_comment = TxtParser.add_newlines(self.comment_raw)
        r = self.tag_raw + add_content + add_comment
        return r

    # For 'Normal' RecordEntries there is the need to convert them
    # into Txt ones.
    # XXX This is a minimalistic implementation - which works.
    # Maybe add text wrapping.
    @staticmethod
    def format_entry(l):
        comment = ""
        if l.get_comment()!=None:
            comment = "# " + l.get_comment()

        print("TTTTTTT [%s]" % l.get_tag())

        return l.get_tag() + ": " + l.get_content() + "\n" + comment

    # Write record entry to filesystem
    def write_fd(self, fd):
        if self.content_raw!=None:
            fd.write(self.tag_raw)
            fd.write(StringHelper.join_ate("\n", self.content_raw))
        else:
            fd.write(self.get_tag())
            fd.write(": ")
            fd.write(self.get_content())
            fd.write("\n")
            
        if self.comment_raw!=None:
            fd.write(StringHelper.join_ate("\n", self.comment_raw))
        else:
            fd.write("# ")
            fd.write(self.get_comment())
            fd.write("\n")

    # There is the need to clean up the raw stored content
    def set_content(self, c):
        RecordEntry.set_content(self, c)
        self.content_raw = None

    # Same for comment
    def set_comment(self, c):
        RecordEntry.set_comment(self, c)
        self.comment_raw = None

    def get_content_with_nl(self):
        return self.content_raw

