'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Logging Formatter

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''


class LogFormatter:

    @staticmethod
    def format(lid, msg, efile=None, eline=None):
        rval = "%3d:" % lid
        if efile is not None:
            rval += "%s:" % efile
        if eline is not None:
            rval += "%s:" % eline
        rval += "%s" % msg
        return rval

    @staticmethod
    def rmte(rmte):
        return LogFormatter.format(rmte.get_id(), rmte.get_msg(),
                                   rmte.get_efile(), rmte.get_eline())


#    # Construct log message from exception
#    def error_from_rmte(self, rmte):
#        self.logs.append(MemLogFile(rmte.get_id(), LogLevel.error(),
#                                    rmte.get_msg(), rmte.get_efile(),
#                                    rmte.get_eline()))
#
#    # Method for creating a fully new blown set_value of log messages:
#    # usable for e.g. test cases.
#    @staticmethod
#    def create_mls(ll):
#        mls = MemLogStore()
#        for l in ll:
#            if len(l) <= 3:
#                mls.logs.append(MemLog.create_ml(l))
#            else:
#                mls.logs.append(MemLogFile.create_ml(l))
#        return mls
#
#    # For writing test cases it is very helpful to get the internal
#    # representation of the object.
#    def to_list(self):
#        r = []
#        for m in self.logs:
#            r.append(m.to_list())
#        return r
#
#    # For comparison (also mostly used in test-cases) the eq operator
#    # must be defined.
#    def __eq__(self, other):
#        return type(self) == type(other) and self.logs == other.logs
