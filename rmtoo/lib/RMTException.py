#
# Requirement Management Toolset
#
# Common Exception
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

class RMTException(Exception):

    def __init__(self, lid, msg, efile=None):
        self.lid = lid
        self.msg = msg
        self.efile = efile

    def __str__(self):
        return "%3d: %s" % (self.lid, self.msg)

    def id(self):
        return self.lid
