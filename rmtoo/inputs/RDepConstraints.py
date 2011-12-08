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
from rmtoo.lib.digraph.TopologicalSort import topological_sort
from rmtoo.lib.RMTException import RMTException

class RDepConstraints(Digraph.Node):
    depends_on = ["RDepDependsOn", "RDepSolvedBy"]

    def __init__(self, config):
        Digraph.Node.__init__(self, "RDepConstraints")
        self.config = config

    def type(self):
        return set(["reqdeps", ])

    def set_modules(self, mods):
        self.mods = mods

    # Extracts the name of the constrains file name
    @staticmethod
    def get_ctr_name(s):
        i = s.find("(")
        if i == -1:
            print("+++ Error: no '(' in constraints")
            print("ASSERT %s" % s)
            # Throw: does not contain (
            assert(False)
        return s[:i]


    # Execute the unification of the CE3s:
    # From the list of all incoming nodes and the value of the current node
    # compute the new value of the current node
    def unite_ce3s(self, reqset, ce3set):
        # The ce3s must be executed in topological order.
        ce3tsort = topological_sort(reqset)
        for r in ce3tsort:
            # Have a look for incoming nodes
            ince3s = []
            for i in r.outgoing:
                ince3s.append(ce3set.get(i.get_id()))
            lce3 = ce3set.get(r.get_id())
            lce3.unite(ince3s)

    # The constrains value gets a dictionary from the name of the
    # constraints to the object.
    def rewrite(self, reqset):
        reqset.resolve_ce3()
        return True
