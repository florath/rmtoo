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

class MemLog:

    def __init__(self, lid, level, efile, eline, msg):
        self.timestamp = time.time()
        self.lid = lid
        self.level = level
        self.efile = efile
        self.eline = eline
        self.msg = msg


class MemLogStore:

    def __init__(self):
        self.logs = []

    def log(self, lid, level, efile, eline, msg):
        self.logs.append(MemLog(lid, level, efile, eline, msg))
