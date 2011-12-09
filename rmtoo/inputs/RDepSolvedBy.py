#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# The straight forward way to define dependencies.
#
# (c) 2010-2011 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.Requirement import Requirement

class RDepSolvedBy(Digraph.Node):
    depends_on = []
    tag = "Solved by"

    def __init__(self, config):
        Digraph.Node.__init__(self, "RDepSolvedBy")
        self.config = config

    def type(self):
        return set(["reqdeps", ])

    def set_modules(self, mods):
        self.mods = mods

    def rewrite(self, reqset):
        # Solved by: is (historically) seen the default.
        if self.tag not in \
           self.config.get_value_default(
                'requirements.input.dependency_notation', set(["Solved by", ])):
            assert False
            return True
        return reqset.resolve_solved_by()
