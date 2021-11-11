'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Logging Formatter

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''


class LogFormatter(object):
    """Class for handling Log Formatting"""

    @staticmethod
    def format(lid, msg, efile=None, eline=None):
        """Format a log message"""
        rval = "%3d:" % lid
        if efile is not None:
            rval += "%s:" % efile
        if eline is not None:
            rval += "%s:" % eline
        rval += "%s" % msg
        return rval

    @staticmethod
    def rmte(rmte):
        """Logs a rmtoo Exception"""
        return LogFormatter.format(rmte.get_id(), rmte.get_msg(),
                                   rmte.get_efile(), rmte.get_eline())
