#
# Requirement Management Toolset
#
#   Memory Logging Store
#
#   There is the need (e.g. for the RequirementSet) to store logs in
#   memory - including a unique log-number, file name, line number and
#   so on.
#   This is needed because historic RequirementSets might have some
#   problems parsing them.
#   Also this makes is easier to write test cases handling error
#   messages. 
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

import time
from rmtoo.lib.RMTException import RMTException

# This represents one memory log message.
# It contains some deep information about the file and line number. 
# Also it contains a unique log message.
class MemLog:

    # Log-levels

    debug = 20
    info = 30
    warning = 40
    error = 50

    levels = set([debug, info, warning, error])

    # Checks the level: only the defined levels are allowed.
    def check_level(self):
        if self.level not in self.levels:
            raise RMTException(52, "Invalid level in log message")

    # The log message is constant.
    def __init__(self, lid, level, msg, efile=None, eline=None):
        self.timestamp = time.time()
        self.lid = lid
        self.level = level
        self.check_level()
        self.efile = efile
        self.eline = eline
        self.msg = msg

    # This is mostly a second constructor for a message which can be
    # called with a list
    @staticmethod
    def create_ml(l):
        llen=len(l)
        assert(llen>=3)
        assert(llen<=5)

        ml = MemLog(l[0], l[1], l[2])

        if llen>3:
            ml.efile = l[3]
        else:
            ml.efile = None

        if llen>4:
            ml.eline = l[4]
        else:
            ml.eline = None
        return ml

    def write_log(self, fd):
        if self.level==self.error:
            fd.write("+++ Error:")
        elif self.level==self.warning:
            fd.write("+++ Warning:")

        fd.write("%3d:" % self.lid)

        if self.efile!=None:
            fd.write("%s:" % self.efile)
        if self.eline!=None:
            fd.write("%s:" % self.eline)
        
        fd.write("%s" % self.msg)
        fd.write("\n")

    def __eq__(self, other):
        return self.lid==other.lid \
            and self.level==other.level \
            and self.efile==other.efile \
            and self.eline==other.eline \
            and self.msg==other.msg

# This is an in memory log message storage.
# It is mainly used when reading in old / historic requirments. When
# there are problems reading them, these problems are logged into the
# MemLog storage.
class MemLogStore:

    def __init__(self):
        self.logs = []

    def log(self, lid, level, msg, efile=None, eline=None):
        self.logs.append(MemLog(lid, level, msg, efile, eline))

    def write_log(self, fd):
        for l in self.logs:
            l.write_log(fd)

    # Convinience functions
    def debug(self, lid, msg, efile=None, eline=None):
        self.logs.append(MemLog(lid, MemLog.debug, msg, efile, eline))

    def info(self, lid, msg, efile=None, eline=None):
        self.logs.append(MemLog(lid, MemLog.info, msg, efile, eline))

    def warning(self, lid, msg, efile=None, eline=None):
        self.logs.append(MemLog(lid, MemLog.warning, msg, efile, eline))

    def error(self, lid, msg, efile=None, eline=None):
        self.logs.append(MemLog(lid, MemLog.error, msg, efile, eline))

    # Method for creating a fully new blown set of log messages:
    # usable for e.g. test cases.
    @staticmethod
    def create_mls(ll):
        mls = MemLogStore()
        for l in ll:
            mls.logs.append(MemLog.create_ml(l))
        return mls

    # For comparison (also mostly used in test-cases) the eq operator
    # must be defined.
    def __eq__(self, other):
        return self.logs==other.logs

    def mls(self):
        return self
