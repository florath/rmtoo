#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# Detect if the graph is connected or not
#
# (c) 2010-2011 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.digraph.ConnectedComponents \
    import connected_components
from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.RMTException import RMTException

class RDepOneComponent(Digraph.Node):
    depends_on = ["RDepDependsOn", "RDepSolvedBy"]

    def __init__(self, opts, config):
        Digraph.Node.__init__(self, "RDepOneComponent")
        self.opts = opts
        self.config = config
    
    def type(self):
        return set(["reqdeps", ])
    
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

        raise RMTException(
            69, "Requirements graph has two or more connected "
            "components. Please fix the edges between the nodes."
            "Found components: %s" % components.as_string())
