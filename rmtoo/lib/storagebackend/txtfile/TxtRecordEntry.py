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
        self.content_raw = [se[0], se[1]]
        self.comment_raw = se[2]
        # Parse the rest
        tag, value = TxtParser.split_tag_line(se[0])
        value += TxtParser.extract_continuation_lines(se[1])
        comment = TxtParser.extract_comment(se[2])
        RecordEntry.__init__(self, tag, value, comment)

    def to_string(self):
        add_content = TxtParser.add_newlines(self.content_raw[1])
        add_comment = TxtParser.add_newlines(self.comment_raw)
        r = self.content_raw[0] + '\n' + add_content + add_comment
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

        return l.get_tag() + ": " + l.get_content() + "\n" + comment
