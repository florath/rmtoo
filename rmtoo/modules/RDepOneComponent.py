#
# Detect if the graph is connected or not
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.digraph.ConnectedComponents \
    import connected_components
from rmtoo.lib.digraph.Digraph import Digraph

class RDepOneComponent(Digraph.Node):
    depends_on = ["RDepDependsOn"]

    def __init__(self, opts, config):
        Digraph.Node.__init__(self, "RDepOneComponent")
        self.opts = opts
        self.config = config
    
    def type(self):
        return "reqdeps"
    
    def set_modules(self, mods):
        self.mods = mods

    # The rewrite method checks if there is only one connected
    # component.  If not an error is printed including all the found
    # components.
    def rewrite(self, reqset):
        components = connected_components(reqset)
        if components.len()==1:
            # Everything is ok: graph is connected
            return True

        print("+++ ERROR: requirements graph has two or more "
              "connected components.")
        print("+++        Please fix the edges between the nodes.")
        print("+++        Found components: %s" % components.as_string())
        return False
