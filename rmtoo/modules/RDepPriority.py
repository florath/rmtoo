#
# Hirachical Priority computation
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

class RDepPriority:
    depends_on = ["RDepDependsOn", "RDepMasterNoPrio", "RDepNoDirectedCircles"]

    def __init__(self, opts, config):
        self.opts = opts
        self.config = config

    def type(self):
        return "reqdeps"
    
    def set_modules(self, mods):
        self.mods = mods

