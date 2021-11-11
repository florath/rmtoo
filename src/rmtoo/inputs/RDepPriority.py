'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Hirachical Priority computation

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.logging import tracer
from rmtoo.lib.InputModuleTypes import InputModuleTypes


class RDepPriority(Digraph.Node):
    '''This class computes the priority.
    If one node has priority 0, the whole subtree has also priority 0.
    A node has always the maximum of possible priorities.
    '''

    depends_on = ["RDepDependsOn", "RDepNoDirectedCircles",
                  "RDepOneComponent", "RDepSolvedBy", "RDepMasterNodes"]

    def __init__(self, config):
        Digraph.Node.__init__(self, "RDepPriority")
        self.config = config

    @staticmethod
    def get_type_set():
        """Get the type set"""
        return set([InputModuleTypes.reqdeps, ])

    @staticmethod
    def rewrite(reqset):
        """Do a DFS and compute the priority during that way.
        If there is a node which was already visited, only recompute the
        subtree, if the new priority is higher.
        """
        tracer.debug("Called.")

        def handle_priorization(node, inc_weight):
            """The second argument (the number) is the weight of the
            outgoing edge.
            """
            tracer.debug("Node [%s] inc_weight [%4.3f]",
                         node.get_id(), inc_weight)
            # This is the weight which is inherited
            weight = inc_weight * node.get_value("Factor")

            # If there is none, or if the current priority is lower
            # that the newly computed, recompute this node and
            # everything beneath.
            if not node.is_value_available("Priority") \
                    or node.get_value("Priority") < weight:
                tracer.debug("Node [%s] set priority to [%4.3f]",
                             node.get_id(), weight)
                node.set_value("Priority", weight)
                for out_node in node.outgoing:
                    tracer.debug(
                        "Recursive call to node [%s] with weight [%4.3f]",
                        out_node.get_id(), weight)
                    handle_priorization(out_node, weight)

        # Start at the root (master) node and evaluate all nodes
        # there.
        for req in reqset.get_master_nodes():
            handle_priorization(req, 1.0)
