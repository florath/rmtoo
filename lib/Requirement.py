#
# Requirement Management Toolset
#  class Requirement
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

class Requirement:

    def __init__(self, fd, rid):
        self.req = {}
        self.id = rid
        self.read(fd)

    def read(self, fd):
        pass
