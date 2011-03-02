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

from rmtoo.lib.digraph.Digraph import Digraph

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

    # Set up the initial constraints
    def set_initial_constraints(self, reqset):
        for k, v in reqset.reqs.items():
            cstrnts = v.get_value("Constraints")
            if cstrnts!=None:
                sval = cstrnts.get_content().split()
                cs = {}
                for s in sval:
                    cs[s] = reqset.constraints[s]
                v.set_value("Constraints", cs)
                v.set_value("CE3Local", CE3(cs))
        return

    def distribute_constraints(self, reqset):
        
        def distribute_constraints_req(req):
            for n in req.outgoing:
                pass

        distribute_constraints_req(reqset.graph_master_node)

    # The constrains value gets a dictionary from the name of the
    # constraints to the object.
    def rewrite(self, reqset):
        print("TTTTTTTTTTTTTTTTTT %s" % reqset.graph_master_node)
        self.set_initial_constraints(reqset)
        self.distribute_constraints(reqset)

        return True
