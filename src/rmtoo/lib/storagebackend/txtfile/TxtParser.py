'''
 rmtoo
   Free and Open Source Requirements Management Tool

 Text Parser

 (c) 2011,2017 by flonatel

 For licensing details see COPYING
'''
from __future__ import unicode_literals

import re

from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.logging.LogFormatter import LogFormatter
from rmtoo.lib.logging import logger


class TxtParser(object):
    """Parses a text representation"""

    re_tag_line = re.compile("^([a-zA-Z][a-zA-Z0-9_ ]*:)(.*)$")

    @staticmethod
    def is_comment_or_empty(line):
        '''Checks if the given line is empty or a comment.'''
        if not line:
            return True
        if line[0] == '#':
            return True
        return False

    @staticmethod
    def extract_record_comment(split_lines):
        '''This takes a record as input and splits it up into two:
           o the initial comment
           o the rest
        '''
        comment = []
        for i in range(0, len(split_lines)):
            if not TxtParser.is_comment_or_empty(split_lines[i]):
                del split_lines[0:i]
                return comment
            comment.append(split_lines[i])
        del split_lines[:]
        return comment

    comment_in_req = "Compatibility info: Comments will be reordered " \
        "when they are re-written with rmtoo-tools. Please consult " \
        "rmtoo-req-format(5) or rmtoo-topic-format(5)"

    @staticmethod
    def split_next_record(split_lines, rid, lineno, _mls):
        '''Splits off the first record from the given string list.
        The record is returned and the string list is shortened.
        Precondition: it can be assumed that len(sl)>0
        '''
        i = 0
        sl_len = len(split_lines)
        # The first line must contain the tag.
        retl = TxtParser.re_tag_line.match(split_lines[i])
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
            if TxtParser.re_tag_line.match(split_lines[i]):
                break
            elif split_lines[i] and split_lines[i][0] == " ":
                content.append(split_lines[i])
                if comment:
                    # This is the possible problematic case where
                    # continuation lines are intermixed with comments.
                    logger.info(LogFormatter.format(
                        80, TxtParser.comment_in_req,
                        rid, lineno+i))
            elif TxtParser.is_comment_or_empty(split_lines[i]):
                comment.append(split_lines[i])
            i += 1
        rec = [tag, content, comment]
        del split_lines[0:i]
        return rec

    @staticmethod
    def split_entries(split_lines, rid, mls, lineno_offset):
        '''This method splits up the given string in seperate entries which
        represent a entry record each.
        The lineno offset is the line number of the first line given in
        the sl array.
        '''
        doc = []
        lineno = lineno_offset
        success = True
        while split_lines:
            try:
                next_record \
                    = TxtParser.split_next_record(
                        split_lines, rid, lineno, mls)
                doc.append(next_record)
                lineno += len(next_record[1]) + len(next_record[2])
            except RMTException as rmte:
                # This is a hint that the tag line could not correctly
                # parsed.
                logger.error(LogFormatter.rmte(rmte))
                # Remove the errornous line
                del split_lines[0]
                lineno += 1
                success = False
        return success, doc

    @staticmethod
    def extract_comment(comment_lines):
        '''Takes a raw comment as input and converts it to a user readable
        string.
        '''
        rstring = ""
        for line in comment_lines:
            # Empty lines -> \n
            if not line:
                rstring += "\n"
                continue
            # All other lines: cut of the leading '#'
            rstring += line[1:] + "\n"
        return rstring

    @staticmethod
    def add_newlines(split_lines):
        '''Add the 'lost' newlines to the raw string - return string.'''
        if not split_lines:
            return ""
        return '\n'.join(split_lines) + '\n'
