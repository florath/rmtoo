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
        for i in xrange(0, len(sl)):
            if not TxtParser.is_comment_or_empty(sl[i]):
                del(sl[0:i])
                return comment
            comment.append(sl[i])
        del(sl[:])
        return comment

    comment_in_req = "Compatibility info: Comments will be reordered " \
        "when they are re-written with rmtoo-tools. Please consult " \
        "rmtoo-req-format(5) or rmtoo-topic-format(5)"

    # Splits off the first record from the given string list.
    # The record is returned and the string list is shortened.
    # Precondition: it can be assumed that len(sl)>0
    @staticmethod
    def split_next_record(sl, rid, lineno, mls):
        i = 0
        sl_len = len(sl)
        # The first line must contain the tag.
        if not TxtParser.re_tag_line.match(sl[i]):
            raise RMTException(79, "Expected tag line not found",
                               rid, lineno)
        i+=1
##      This is what is needed - to be compatible with the old
##      specification. 
        content = []
        comment = []
        while i<sl_len:
            if TxtParser.re_tag_line.match(sl[i]):
                break
            elif len(sl[i])>0 and sl[i][0]==" ":
                content.append(sl[i])
                if len(comment)>0:
                    # This is the possible problematic case where
                    # continuation lines are intermixed with comments.
                    mls.info(80, TxtParser.comment_in_req,
                             rid, lineno+i)
                    print("SL 0 '%s'/'%s'" % (rid, lineno+1))
                    print("SL 1 '%s'" % sl[i])
                    print("SL 2 '%s'" % content)
                    print("SL 3 '%s'" % comment)
            elif TxtParser.is_comment_or_empty(sl[i]):
                comment.append(sl[i])
            i+=1
        rec = [sl[0], content, comment]
        del(sl[0:i])

        print("PPPPPPPPPPPPPPP '%s'"  % rec)

        return rec

## This is, what I really want - but what is not needed
##
##        # This can be followed by optional lines starting with a
##        # space.
##        while i<sl_len and len(sl[i])>0 and sl[i][0]==" ":
##            i+=1
##        i_end_of_continue = i
##        # Optional comments and empty lines can follow
##        while i<sl_len and TxtParser.is_comment_or_empty(sl[i]):
##            i+=1
##        # At the end of the record now - move all lines from the sl
##        # to the rec
##        rec = [sl[0], sl[1:i_end_of_continue], sl[i_end_of_continue:i]]
##        del(sl[0:i])
##        return rec

    # This method splits up the given string in seperate entries which
    # represent a entry record each.
    # The lineno offset is the line number of the first line given in 
    # the sl array.
    @staticmethod
    def split_entries(sl, rid, mls, lineno_offset):
        doc = []
        lineno = lineno_offset
        success = True
        while len(sl)>0:
            try:
                nr = TxtParser.split_next_record(sl, rid, lineno, mls)
                doc.append(nr)
                lineno += 1 + len(nr[1]) + len(nr[2])
            except RMTException, rmte:
                # This is a hint that the tag line could not correctly
                # parsed.
                mls.error_from_rmte(rmte)
                # Remove the errornous line
                del(sl[0])
                lineno += 1
                success = False
        print("UUUUUUUUUUUPPPPPPPPPPPPPPPPP '%s'" % success)
        print("UUUUUUUUUUUPPPPPPPPPPPPPPPPP '%s'" % doc)
        return success, doc

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

