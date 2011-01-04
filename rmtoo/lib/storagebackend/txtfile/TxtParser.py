#
# rmtoo 
#  Text Parser class
#
# This is the parser for the standard text file format.
#
# (c) 2010-2011 by flonatel
#
# For licencing details see COPYING
#

class TxtParser:

    @classmethod
    def from_string(cls, s):
        obj = cls()
        obj.parse(s)
        return obj

    @classmethod
    def from_fd(cls, fd):
        obj = cls()
        # Because there is only a very limited interface for some VCS
        # the whole file in read at once.
        obj.parse(fd.read())
        return obj

    # Parse everything from a string
    def parse(self, s):
        # fill in self.content
        pass

    def get_list(self):
        return self.content
