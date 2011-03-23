#
# Requirement Management Toolset
#  Test Module
#
# (c) 2010-2011 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.RMTException import RMTException

class Module01(Digraph.Node):
    depends_on = []

    def __init__(self, opts, config):
        Digraph.Node.__init__(self, "Module01")

    def type(self):
        return set(["reqtag", ])

    def set_modules(self, mods):
        pass

    def rewrite(self, rid, reqs):
        raise RMTException(55, "TCExcept")
