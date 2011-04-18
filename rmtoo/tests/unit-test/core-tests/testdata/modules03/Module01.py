#
# Requirement Management Toolset
#  Test Module
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

class Module01:
    depends_on = ["Module02"]

    def __init__(self, opts, config):
        pass

    def type(self):
        return set(["reqdeps", ])

    def set_modules(self, mods):
        pass
