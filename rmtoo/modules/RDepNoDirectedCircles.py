#
# Detect if the graph has directed circles
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

class RDepNoDirectedCircles:
    depends_on = ["RDepDependsOn"]
    
    def __init__(self, opts, config):
        self.opts = opts
        self.config = config

    def type(self):
        return "reqdeps"
    
    def set_modules(self, mods):
        self.mods = mods

    # The main entry point for Trajans algorithm
    def algo_trajan(self, reqset):
        
        # Here is a set of variables that is also accessed from the
        # inner algorithm method.

        # Counter for the Deepth First Search
        # ToDo: plain int does not work - Why?
        md = [0]
        # Set of not yet visited nodes
        U = []
        for u in reqset.reqs:
            U.append(u)
        # Stack where nodes of strongly connected components are
        # stored. 
        S = []

        # The algorithm in recursive.  This is the method that is
        # called from itself.
        def trajan_inner(v_name):
            print("TI %s" % v_name)
            # This node is visited - mark it.
            U.remove(v_name)
            v = reqset.reqs[v_name]
            # Mark the node that we have visited it
            print("TI dfs=%d" % md[0])
            v.graph_algo_trajan_dfs = md[0]
            v.graph_algo_trajan_lowlink = md[0]
            # Increment the counter
            md[0] += 1
            # Push the current node to the stack
            S.append(v_name)

            # Step though all adjacent edges of the current node.
            for vl in v.depends_on:
                # Only for the not-yet discovered
                if vl.id in U:
                    # recursive call the algorithm
                    trajan_inner(vl.id)
                    v.graph_algo_trajan_lowlink = \
                        min(v.graph_algo_trajan_lowlink,
                            vl.graph_algo_trajan_lowlink)
                elif vl.id in S:
                    v.graph_algo_trajan_lowlink = \
                        min(v.graph_algo_trajan_lowlink,
                            vl.graph_algo_trajan_lowlink)

            if v.graph_algo_trajan_lowlink == v.graph_algo_trajan_dfs:
                print("SZK found: %s" % S)

        # While there are unvisited nodes, call the inner Trajan
        # algorithm. 
        while len(U)>0:
            # Get one from the unvisited nodes
            v_name = U[0]
            trajan_inner(v_name)

    # The rewrite function here does mostly a search for strongly
    # connected components.  It uses the algorithm from trajan for
    # this. 
    def rewrite(self, reqset):
        res= self.algo_trajan(reqset)
        if res!=None:
            print("+++ ERROR: There is at least one circular "
                  "dependency component: '%s'" % res)
            return False
        return True

