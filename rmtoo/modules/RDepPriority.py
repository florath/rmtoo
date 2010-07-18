#
# Hirachical Priority computation
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.digraph.Digraph import Digraph

#
# This class computes the priority.
#
# If one node has priority 0, the whole subtree has also priority 0.
# A node has always the maximum of possible priorities.
#
class RDepPriority(Digraph.Node):
    depends_on = ["RDepDependsOn", "RDepNoDirectedCircles",
                  "RDepOneComponent"]

    def __init__(self, opts, config):
        Digraph.Node.__init__(self, "RDepPriority")
        self.opts = opts
        self.config = config

    def type(self):
        return "reqdeps"
    
    def set_modules(self, mods):
        self.mods = mods

    # Do a DFS and compute the priority during that way.
    # If there is a node which was already visited, only recompute the
    # subtree, if the new priority is higher.
    def rewrite(self, reqset):

        # The second argument (the number) is the weight of the
        # incoming edge.
        def handle_priorization(node, inc_weight):
            # This is the weight which is inherited
            weight = inc_weight * node.tags["Factor"]

            # If there is none, or if the current priority is lower
            # that the newly computed, recompute this node and
            # everything beneath.
            if "Priority" not in node.tags \
                    or node.tags["Priority"] < weight:
                node.tags["Priority"] = weight
                for n in node.incoming:
                    handle_priorization(n, weight)

        # Start at the root (master) node and evaluate all nodes
        # there. 
        handle_priorization(reqset.graph_master_node, 1.0)
