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

from rmtoo.lib.CE3Set import CE3Set
from rmtoo.lib.CE3 import CE3
from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.digraph.TopologicalSort import topological_sort

class RDepConstraints(Digraph.Node):
    depends_on = ["RDepDependsOn", "RDepSolvedBy"]
    
    def __init__(self, opts, config):
        Digraph.Node.__init__(self, "RDepConstraints")
        self.opts = opts
        self.config = config

    def type(self):
        return set(["reqdeps", ])
    
    def set_modules(self, mods):
        self.mods = mods

    # Extracts the name of the constrains file name
    @staticmethod
    def get_ctr_name(s):
        i = s.find("(")
        if i==-1:
            # Throw: does not contain (
            assert(False)
        return s[:i]

    # Create the local Constraint Execution Environments
    # and evaluate the given statements
    def create_local_ce3s(self, reqset):
        ce3set = CE3Set()
        for k, v in reqset.reqs.items():
            ce3 = CE3()
            cstrnts = v.get_value("Constraints")
            if cstrnts!=None:
                sval = cstrnts.get_content().split()
                for s in sval:
                    ctr_name = self.get_ctr_name(s)
                    rcs = reqset.constraints[ctr_name]
                    ce3.eval(rcs, ctr_name, s)
            # Store the fresh create CE3 into the ce3set
            ce3set.insert(k, ce3)
        return ce3set

    # Execute the unification of the CE3s:
    # From the list of all incoming nodes and the value of the current node
    # compute the new value of the current node
    def unite_ce3s(self, reqset, ce3set):
        # The ce3s must be executed in topological order.
        ce3tsort = topological_sort(reqset)
        print("CETORET %s" % ce3tsort)
        for r in ce3tsort:
            # Have a look for incoming nodes
            ince3s = []
            for i in r.outgoing:
                print("INCOMING %s -> %s" % (r.get_id(), i.get_id()))
                ince3s.append(ce3set.get(i.get_id()))
            lce3 = ce3set.get(r.get_id())
            lce3.unite(ince3s)

    def distribute_constraints(self, reqset):
        
        def distribute_constraints_req(req):
            for n in req.outgoing:
                pass

        distribute_constraints_req(reqset.graph_master_node)

    # The constrains value gets a dictionary from the name of the
    # constraints to the object.
    def rewrite(self, reqset):
        # The first step is to create local Constraint Execution Environments
        ce3set = self.create_local_ce3s(reqset)
        # Evaluate all the CE3 in topological order
        self.unite_ce3s(reqset, ce3set)
        assert(False)

        print("TTTTTTTTTTTTTTTTTT %s" % reqset.graph_master_node)
        self.set_initial_constraints(reqset)
        self.distribute_constraints(reqset)

        return True
