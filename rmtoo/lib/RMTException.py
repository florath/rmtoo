#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# Common Exception
#
# (c) 2010-2011,2017 by flonatel
#
# For licencing details see COPYING
#


class RMTException(Exception):

    def __init__(self, lid, msg, efile=None, eline=None):
        self.lid = lid
        self.lmsg = msg
        self.lefile = efile
        self.leline = eline

    def __str__(self):
        r = "[%4d]:" % self.lid
        if self.lefile is not None:
            r += "%s:" % self.lefile
        if self.leline is not None:
            r += "%d:" % self.leline
        r += " %s" % self.lmsg
        return r

    # Deprecated: use get_id()
    def id(self):
        return self.lid

    def get_id(self):
        return self.lid

    def get_msg(self):
        return self.lmsg

    def get_efile(self):
        return self.lefile

    def get_eline(self):
        return self.leline
