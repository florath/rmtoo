#
# rmtoo 
#   Free and Open Source Requirements Management Tool
#
#  Text Parser
#
# (c) 2010-2011 by flonatel
#
# For licencing details see COPYING
#

import re

class TxtParser:

    re_tag_line = re.compile("^[a-zA-Z0-9_ ]*:.*$")

    # Checks if the given line is empty or a comment.
    @staticmethod
    def is_comment_or_empty(line):
        if len(line)==0:
            return True
        if len(line)==1 and line[0]=='\n':
            return True
        if line[0]=='#':
            return True
        return False

    # This takes a record as input and splits it up into two:
    # o the initial comment
    # o the rest
    @staticmethod
    def extract_record_comment(sl):
        comment = []
        for i in xrange(0, len(sl)-1):
            if not TxtParser.is_comment_or_empty(sl[i]):
                del(sl[0:i])
                return comment
            comment.append(sl[i])

    # Splits off the first record from the given string list.
    # The record is returned and the string list is shortened.
    # Precondition: it can be assumed that len(sl)>0
    @staticmethod
    def split_next_record(sl):
        i = 0
        sl_len = len(sl)
        # The first line must contain the tag.
        if not TxtParser.re_tag_line.match(sl[i]):
            raise SomethingsWrong()
        i+=1
        # This can be followed by optional lines starting with a
        # space.
        while i<sl_len and len(sl[i])>0 and sl[i][0]==" ":
            i+=1
        i_end_of_continue = i
        # Optional comments and empty lines can follow
        while i<sl_len and TxtParser.is_comment_or_empty(sl[i]):
            i+=1
        # At the end of the record now - move all lines from the sl
        # to the rec
        rec = [sl[0], sl[1:i_end_of_continue], sl[i_end_of_continue:i]]
        del(sl[0:i])
        return rec

    # This method splits up the given string in seperate entries which
    # represent a entry record each.
    @staticmethod
    def split_entries(sl):
        print("INPUT %s" % sl)
        doc = []
        while len(sl)>0:
            doc.append(TxtParser.split_next_record(sl))
            print("DOC %s" % doc)
        return doc
