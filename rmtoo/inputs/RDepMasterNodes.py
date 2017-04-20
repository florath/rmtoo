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
    depends_on = ["RDepDependsOn", "RDepNoDirectedCircles",
                  "RDepOneComponent", "RDepSolvedBy"]

    def __init__(self, config):
        Digraph.Node.__init__(self, "RDepMasterNodes")
        self.config = config

    def get_type_set(self):
        return set([InputModuleTypes.reqdeps, ])

    def rewrite(self, reqset):
        return reqset.find_master_nodes()
