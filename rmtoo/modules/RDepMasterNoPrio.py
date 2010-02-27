#
# Checks that the master requirment has no priority
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

class RDepMasterNoPrio:
    # The dependecy graph is needed.
    depends_on = ["RDepDependsOn", ]

    def __init__(self, opts, config):
        self.opts = opts
        self.config = config

    def type(self):
        return "reqdeps"
    
    def set_modules(self, mods):
        self.mods = mods

