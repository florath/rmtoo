#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# Constrains implementation
#
# (c) 2011 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.CE3 import CE3
from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.logging.EventLogging import tracer

class RDepConstraints(Digraph.Node):
    depends_on = ["RDepDependsOn", "RDepSolvedBy"]

    def __init__(self, config):
        Digraph.Node.__init__(self, "RDepConstraints")
        self.config = config

    def type(self):
        return set(["reqdeps", ])

    def set_modules(self, mods):
        self.mods = mods

    # The constrains value gets a dictionary from the name of the
    # constraints to the object.
    def rewrite(self, reqset):
        tracer.debug("Called.")
        reqset.resolve_ce3()
        tracer.debug("Finished.")
        return True
