'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Memory Logging Store

  There is the need (e.g. for the RequirementSet) to store logs in
  memory - including a unique log-number, file name, line number and
  so on.
  This is needed because historic RequirementSets might have some
  problems when parsing them - and a throw (which includes an abort)
  is not what is wanted.
  Also this makes is easier to write test cases handling error
  messages. 
   
 (c) 2010-2011 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from rmtoo.lib.logging.MemLog import MemLog
from rmtoo.lib.logging.MemLogFile import MemLogFile
from rmtoo.lib.logging.LogLevel import LogLevel

# This is an in memory log message storage.
# It is mainly used when reading in old / historic requirments. When
# there are problems reading them, these problems are logged into the
# MemLog storage.
class MemLogStore(object):

    def __init__(self):
        super(MemLogStore, self).__init__()
        self.logs = []

    def log(self, lid, level, msg, efile=None, eline=None):
        if efile == None and eline == None:
            self.logs.append(MemLog(lid, level, msg))
        else:
            self.logs.append(MemLogFile(lid, level, msg, efile, eline))

    def write_log(self, file_descriptor):
        for l in self.logs:
            l.write_log(file_descriptor)

    # TODO Duplicate of log()
    def internal_log(self, lid, level, msg, efile=None, eline=None):
        if efile == None and eline == None:
            self.logs.append(MemLog(lid, level, msg))
        else:
            self.logs.append(MemLogFile(lid, level, msg, efile, eline))

    # Convenience functions
    def trace(self, lid, msg, efile=None, eline=None):
        self.internal_log(lid, LogLevel.trace(), msg, efile, eline)

    def debug(self, lid, msg, efile=None, eline=None):
        self.internal_log(lid, LogLevel.debug(), msg, efile, eline)

    def info(self, lid, msg, efile=None, eline=None):
        self.internal_log(lid, LogLevel.info(), msg, efile, eline)

    def warning(self, lid, msg, efile=None, eline=None):
        self.internal_log(lid, LogLevel.warning(), msg, efile, eline)

    def error(self, lid, msg, efile=None, eline=None):
        self.internal_log(lid, LogLevel.error(), msg, efile, eline)

    # Construct log message from exception
    def error_from_rmte(self, rmte):
        self.logs.append(MemLogFile(rmte.get_id(), LogLevel.error(),
                                    rmte.get_msg(), rmte.get_efile(),
                                    rmte.get_eline()))

    # Method for creating a fully new blown set_value of log messages:
    # usable for e.g. test cases.
    @staticmethod
    def create_mls(ll):
        mls = MemLogStore()
        for l in ll:
            if len(l) <= 3:
                mls.logs.append(MemLog.create_ml(l))
            else:
                mls.logs.append(MemLogFile.create_ml(l))
        return mls

    # For writing test cases it is very helpful to get the internal
    # representation of the object.
    def to_list(self):
        r = []
        for m in self.logs:
            r.append(m.to_list())
        return r

    # For comparison (also mostly used in test-cases) the eq operator
    # must be defined.
    # TODO: DO NOT USE THIS, BECAUSE THEN ALL CHECKS FOR NONE
    #   DOES NOT WORK
    def __eq__(self, other):
        return type(self) == type(other) and self.logs == other.logs

    def get_mls(self):
        return self
