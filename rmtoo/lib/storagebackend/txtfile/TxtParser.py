'''
 rmtoo
   Free and Open Source Requirements Management Tool

 Text Parser

 (c) 2011,2017 by flonatel

 For licensing details see COPYING
'''
import re

from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.logging.LogFormatter import LogFormatter
from rmtoo.lib.logging import logger


class TxtParser(object):

    re_tag_line = re.compile("^([a-zA-Z][a-zA-Z0-9_ ]*:)(.*)$")

    @staticmethod
    def is_comment_or_empty(line):
        '''Checks if the given line is empty or a comment.'''
        if len(line) == 0:
            return True
        if line[0] == '#':
            return True
        return False

    @staticmethod
    def extract_record_comment(sl):
        '''This takes a record as input and splits it up into two:
           o the initial comment
           o the rest'''
        comment = []
        for i in range(0, len(sl)):
            if not TxtParser.is_comment_or_empty(sl[i]):
                del(sl[0:i])
                return comment
            comment.append(sl[i])
        del(sl[:])
        return comment

    comment_in_req = "Compatibility info: Comments will be reordered " \
        "when they are re-written with rmtoo-tools. Please consult " \
        "rmtoo-req-format(5) or rmtoo-topic-format(5)"

    @staticmethod
    def split_next_record(sl, rid, lineno, mls):
        '''Splits off the first record from the given string list.
           The record is returned and the string list is shortened.
           Precondition: it can be assumed that len(sl)>0'''
        i = 0
        sl_len = len(sl)
        # The first line must contain the tag.
        retl = TxtParser.re_tag_line.match(sl[i])
        if not retl:
            raise RMTException(79, "Expected tag line not found",
                               rid, lineno)

        content = []
        comment = []

        # Split first line: the Tag is everyting including the ':'
        # The content starts directly after this ':'
        tag = retl.group(1)
        content.append(retl.group(2))

        i += 1
        # This is what is needed - to be compatible with the old
        # specification.
        while i < sl_len:
            if TxtParser.re_tag_line.match(sl[i]):
                break
            elif len(sl[i]) > 0 and sl[i][0] == " ":
                content.append(sl[i])
                if len(comment) > 0:
                    # This is the possible problematic case where
                    # continuation lines are intermixed with comments.
                    logger.info(LogFormatter.format(
                        80, TxtParser.comment_in_req,
                        rid, lineno+i))
            elif TxtParser.is_comment_or_empty(sl[i]):
                comment.append(sl[i])
            i += 1
        rec = [tag, content, comment]
        del sl[0:i]
        return rec

# This is, what I really want - but what is not needed
#
#        # This can be followed by optional lines starting with a
#        # space.
#        while i<sl_len and len(sl[i])>0 and sl[i][0]==" ":
#            i+=1
#        i_end_of_continue = i
#        # Optional comments and empty lines can follow
#        while i<sl_len and TxtParser.is_comment_or_empty(sl[i]):
#            i+=1
#        # At the end of the record now - move all lines from the sl
#        # to the rec
#        rec = [sl[0], sl[1:i_end_of_continue], sl[i_end_of_continue:i]]
#        del(sl[0:i])
#        return rec

    @staticmethod
    def split_entries(sl, rid, mls, lineno_offset):
        '''This method splits up the given string in seperate entries which
           represent a entry record each.
           The lineno offset is the line number of the first line given in
           the sl array.'''
        doc = []
        lineno = lineno_offset
        success = True
        while len(sl) > 0:
            try:
                nr = TxtParser.split_next_record(sl, rid, lineno, mls)
                doc.append(nr)
                lineno += len(nr[1]) + len(nr[2])
            except RMTException as rmte:
                # This is a hint that the tag line could not correctly
                # parsed.
                logger.error(LogFormatter.rmte(rmte))
                # Remove the errornous line
                del sl[0]
                lineno += 1
                success = False
        return success, doc

    @staticmethod
    def extract_comment(cl):
        '''Takes a raw comment as input and converts it to a user readable
           string.'''
        s = u""
        for l in cl:
            # Empty lines -> \n
            if len(l) == 0:
                s += "\n"
                continue
            # All other lines: cut of the leading '#'
            s += l[1:] + "\n"
        return s

    @staticmethod
    def add_newlines(sl):
        '''Add the 'lost' newlines to the raw string - return string.'''
        if len(sl) == 0:
            return ""
        return '\n'.join(sl) + '\n'
