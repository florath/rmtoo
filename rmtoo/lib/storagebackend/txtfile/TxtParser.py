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

from rmtoo.lib.RMTException import RMTException

import re

class TxtParser:

    re_tag_line = re.compile("^[a-zA-Z0-9_ ]+:.*$")

    # Checks if the given line is empty or a comment.
    @staticmethod
    def is_comment_or_empty(line):
        if len(line)==0:
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
        return comment

    # Splits off the first record from the given string list.
    # The record is returned and the string list is shortened.
    # Precondition: it can be assumed that len(sl)>0
    @staticmethod
    def split_next_record(sl, rid, lineno):
        i = 0
        sl_len = len(sl)
        # The first line must contain the tag.
        if not TxtParser.re_tag_line.match(sl[i]):
            raise RMTException(79, "%s:%d: Expected tag line not found"
                               % (rid, lineno))
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
    def split_entries(sl, rid):
        mls = MemLogStore()
        doc = []
        lineno = 0
        success = True
        while len(sl)>0:
            try:
                nr = TxtParser.split_next_record(sl, rid, lineno)
                doc.append(nr)
                lineno += len(nr)
            except RMTException, rmte:
                # This is a hint that the tag line could not correctly be
                # parsed.
                mls.error(rmte.lid, rmte.msg, rmte.efile)
                # Remove the errornous line
                del(sl[0])
                lineno += 1
                success = False
        return success, doc, mls

    # Takes a raw comment as input and converts it to a user readable
    # string.
    @staticmethod
    def extract_comment(cl):
        s = ""
        for l in cl:
            # Empty lines -> \n
            if len(l)==0:
                s += "\n"
                continue
            # All other lines: cut of the leading '#'
            s += l[1:] + "\n"
        return s

    # Splits up a tag line into tag and rest
    @staticmethod
    def split_tag_line(line):
        # Line must not be empty
        assert(len(line)>0)
        colon_pos = line.find(':')
        # There must be a colon
        assert(colon_pos>=0)
        rest = line[colon_pos+1:]
        # Special case: when the rest starts with a white space, delete
        # those.
        rest = rest.lstrip()
        return line[0:colon_pos], rest

    # Extract the contents of the contination lines
    @staticmethod
    def extract_continuation_lines(lines):
        return "".join(lines)

    # Add the 'lost' newlines to the raw string - return string
    @staticmethod
    def add_newlines(sl):
        if len(sl)==0:
            return ""
        return '\n'.join(sl) + '\n'

