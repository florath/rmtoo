'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Detect if the graph has directed circles

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.digraph.StronglyConnectedComponents \
    import strongly_connected_components
from rmtoo.lib.digraph.StronglyConnectedComponents \
    import check_for_strongly_connected_components
from rmtoo.lib.digraph.Helper import remove_single_element_lists_name_rest
from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.InputModuleTypes import InputModuleTypes


class RDepNoDirectedCircles(Digraph.Node):
    depends_on = ["RDepDependsOn", "RDepSolvedBy"]

    def __init__(self, config):
        Digraph.Node.__init__(self, "RDepNoDirectedCircles")
        self.config = config

    def get_type_set(self):
        return set([InputModuleTypes.reqdeps, ])

    # The rewrite function here does mostly a search for strongly
    # connected components.  It uses the algorithm from Trajan for
    # this - which is implemented in the digraph library.
    def rewrite(self, reqset):
        scc = strongly_connected_components(reqset)
        result = check_for_strongly_connected_components(scc)
        if result:
            print("+++ ERROR: There is at least one circular "
                  "dependency component: '%s'" %
                  remove_single_element_lists_name_rest(scc))
            return False
        return True
