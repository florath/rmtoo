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

    def __init__(self, eid, msg):
        self.eid = eid
        self.msg = msg

    def __str__(self):
        return str(self.eid) + ": " + self.msg

