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

    error = 50

    # The log message is constant.
    def __init__(self, lid, level, msg, efile=None, eline=None):
        self.timestamp = time.time()
        self.lid = lid
        self.level = level
        self.efile = efile
        self.eline = eline
        self.msg = msg

    def write_log(self, fd):
        if self.level==self.error:
            fd.write("+++ Error:")
        else:
            raise RMTException(52, "Invalid level in log message")

        fd.write("%3d:" % self.lid)

        if self.efile!=None:
            fd.write("%s:" % self.efile)
        if self.eline!=None:
            fd.write("%s:" % self.eline)
        
        fd.write("%s" % self.msg)
        fd.write("\n")

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
    def error(self, lid, msg, efile=None, eline=None):
        self.logs.append(MemLog(lid, MemLog.error, msg, efile, eline))

