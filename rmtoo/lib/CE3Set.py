#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# Constraint Execution and Evaluation Environment Set
#
# (c) 2011 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.CE3 import CE3

class CE3Set:

    def __init__(self):
        # This holds all the requirements CE3s
        self.ce3s = {}
        # ??? NEEDED? self.global_ce3 = None

    def insert(self, name, ce3):
        self.ce3s[name] = ce3

    def get(self, name):
        return self.ce3s[name]

    def len(self):
        return len(self.ce3s)
