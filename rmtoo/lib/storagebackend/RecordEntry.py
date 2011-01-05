#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# Record Entry Class
#  This base class holds one entry in the record.
#  Different storage backends can inherit from this class - but must
#  handle newly added entries from this base class.
#
# (c) 2011 by flonatel
#
# For licencing details see COPYING
#

# Note: all things must be done via methods (do not change an entry
# directly!)  This gives the underlaying (inherited) class the chance
# to overwrite these settings and do other things which might be
# needed. 

class RecordEntry:

    def get_tag(self):
        pass

    def get_content(self):
        pass

    def get_comment(self):
        pass

