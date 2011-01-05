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

class TxtParser:

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
