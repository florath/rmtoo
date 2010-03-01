#
# Detect if the graph has directed circles
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.digraph.StronglyConnectedComponents \
    import strongly_connected_components
from rmtoo.lib.digraph.StronglyConnectedComponents \
    import check_for_strongly_connected_components
from rmtoo.lib.digraph.Helper import remove_single_element_lists_name_rest

class RDepNoDirectedCircles:
    depends_on = ["RDepDependsOn"]
    
    def __init__(self, opts, config):
        self.opts = opts
        self.config = config

    def type(self):
        return "reqdeps"
    
    def set_modules(self, mods):
        self.mods = mods

    # The rewrite function here does mostly a search for strongly
    # connected components.  It uses the algorithm from Trajan for
    # this - which is implemented in the digraph library.
    def rewrite(self, reqset):
        scc = strongly_connected_components(reqset)
        result = check_for_strongly_connected_components(scc)
        if result==True:
            print("+++ ERROR: There is at least one circular "
                  "dependency component: '%s'" % 
                  remove_single_element_lists_name_rest(scc))
            return False
        return True
