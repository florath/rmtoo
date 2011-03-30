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

    def __init__(self, tag, content, comment=None):
        self.tag = tag
        self.content = content
        self.comment = comment

    def get_tag(self):
        return self.tag

    def get_content(self):
        return self.content.lstrip()

    def set_content(self, c):
        self.content = c

    def set_comment(self, c):
        self.comment = c

    def get_comment(self):
        return self.comment

    def write_fd(self, fd):
        fd.write(self.get_tag())
        fd.write(": ")
        fd.write(self.get_content())
        fd.write("\n")

        fd.write("# ")
        fd.write(self.get_comment())
        fd.write("\n")
