'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Computes all the different master nodes.

 (c) 2011,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.InputModuleTypes import InputModuleTypes


class RDepMasterNodes(Digraph.Node):
    """Handling master nodes: nodes without parents"""
    depends_on = ["RDepDependsOn", "RDepNoDirectedCircles",
                  "RDepOneComponent", "RDepSolvedBy"]

    def __init__(self, config):
        Digraph.Node.__init__(self, "RDepMasterNodes")
        self.config = config

    @staticmethod
    def get_type_set():
        """Return the requirement's types"""
        return set([InputModuleTypes.reqdeps, ])

    @staticmethod
    def rewrite(reqset):
        """Rewrite the type"""
        return reqset.find_master_nodes()
