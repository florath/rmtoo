'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Common Exception

 (c) 2010-2011,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''


class RMTException(Exception):
    """Generic rmtoo exception.

    This exception is used to provide the user some more
    insigths about the problem as well as it implements
    an interface that the exceptions can be checked -
    depending on a unique id.
    """

    def __init__(self, lid, msg, efile=None, eline=None):
        Exception.__init__(self)
        self.lid = lid
        self.lmsg = msg
        self.lefile = efile
        self.leline = eline

    def __str__(self):
        ex_str = "[%4d]:" % self.lid
        if self.lefile is not None:
            ex_str += "%s:" % self.lefile
        if self.leline is not None:
            ex_str += "%d:" % self.leline
        ex_str += " %s" % self.lmsg
        return ex_str

    def get_id(self):
        """Returns the ID of the exception"""
        return self.lid

    def get_msg(self):
        """Returns the message of the exception"""
        return self.lmsg

    def get_efile(self):
        """Returns the file name of the exception"""
        return self.lefile

    def get_eline(self):
        """Returns the file number of the exception"""
        return self.leline
