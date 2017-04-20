'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Txt Record Entry Class
   This class hold additionally the original raw representation of
   each record entry.

 (c) 2011-2011,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from rmtoo.lib.Encoding import Encoding
from rmtoo.lib.storagebackend.txtfile.TxtParser import TxtParser
from rmtoo.lib.storagebackend.RecordEntry import RecordEntry
from rmtoo.lib.StringHelper import StringHelper


class TxtRecordEntry(RecordEntry):

    def __init__(self, se):
        '''There must be three entries:
           1) initial line with tag
           2) possible empty list of continue lines (starting with space)
           3) possible empty list of comment and / or empty lines.'''
        assert(len(se) == 3)
        self.content_raw = None
        self.comment_raw = None
        self.tag_raw = None
        self.__setup(se)

    def __setup(self, se):
        '''Store the raw input for possible later output.'''
        Encoding.check_unicode(se[0])
        self.tag_raw = se[0]
        Encoding.check_unicode_list(se[1])
        self.content_raw = se[1]
        Encoding.check_unicode_list(se[2])
        self.comment_raw = se[2]
        # Parse the rest
        tag = self.tag_raw[0:-1]
        value = "".join(se[1])
        comment = TxtParser.extract_comment(se[2])
        RecordEntry.__init__(self, tag, value, comment)

    def to_string(self):
        add_content = TxtParser.add_newlines(self.content_raw)
        add_comment = TxtParser.add_newlines(self.comment_raw)
        r = self.tag_raw + add_content + add_comment
        return r

    def __str__(self):
        return self.to_string()

    @staticmethod
    def format_entry(l):
        '''For 'Normal' RecordEntries there is the need to convert them
           into Txt ones.'''
    # TODO This is a minimalistic implementation - which works.
    # Maybe add text wrapping.
        comment = ""
        if l.get_comment() is not None:
            comment = "# " + l.get_comment()

        return l.get_tag() + ": " + l.get_content() + "\n" + comment

    def write_fd(self, fd):
        '''Write record entry to filesystem.'''
        if self.content_raw is not None:
            fd.write(self.tag_raw)
            fd.write(StringHelper.join_ate(u"\n", self.content_raw))
        else:
            fd.write(self.get_tag())
            fd.write(": ")
            fd.write(self.get_content())
            fd.write("\n")

        if self.comment_raw is not None:
            fd.write(StringHelper.join_ate(u"\n", self.comment_raw))
        else:
            fd.write("# ")
            fd.write(self.get_comment())
            fd.write("\n")

    def set_content(self, c):
        '''There is the need to clean up the raw stored content.'''
        RecordEntry.set_content(self, c)
        self.content_raw = None

    def set_comment(self, c):
        ''' Set the comment.'''
        RecordEntry.set_comment(self, c)
        self.comment_raw = None

    def get_content_with_nl(self):
        return self.content_raw
