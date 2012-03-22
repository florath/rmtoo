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
from rmtoo.lib.logging.EventLogging import logger

class MemLogStore:
    '''This is an in memory log message storage.
       It is mainly used when reading in old / historic requirements. When
       there are problems reading them, these problems are logged into the
       MemLog storage.'''

    @staticmethod            
    def __format(lid, msg, efile, eline):
        rval = "%3d:" % lid
        if efile!=None:
            rval += "%s:" % efile
        if eline!=None:
            rval += "%s:" % eline
        rval += "%s" % msg
        return rval

    # Convenience functions
    def debug(self, lid, msg, efile=None, eline=None):
        logger.debug(self.__format(lid, msg, efile, eline))

    def info(self, lid, msg, efile=None, eline=None):
        logger.info(self.__format(lid, msg, efile, eline))

    def warning(self, lid, msg, efile=None, eline=None):
        logger.warn(self.__format(lid, msg, efile, eline))

    def error(self, lid, msg, efile=None, eline=None):
        logger.error(self.__format(lid, msg, efile, eline))

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
    def __eq__(self, other):
        return type(self) == type(other) and self.logs == other.logs

