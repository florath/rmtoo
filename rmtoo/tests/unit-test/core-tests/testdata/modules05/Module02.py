#
# Requirement Management Toolset
#  Test Module
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.digraph.Digraph import Digraph

class Module02(Digraph.Node):
    depends_on = ["Module01"]

    def __init__(self, opts, config):
        Digraph.Node.__init__(self, "Module02")

    def type(self):
        return "reqtag"

    def set_modules(self, mods):
        pass

    def rewrite(self, rid, reqs):
        return "SameTag", None
