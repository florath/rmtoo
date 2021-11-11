'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Detect if the graph is connected or not

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.digraph.ConnectedComponents \
    import connected_components
from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.logging import tracer
from rmtoo.lib.InputModuleTypes import InputModuleTypes


class RDepOneComponent(Digraph.Node):
    """Dependency: component checker"""
    depends_on = ["RDepDependsOn", "RDepSolvedBy"]

    def __init__(self, config):
        Digraph.Node.__init__(self, "RDepOneComponent")
        self.config = config

    @staticmethod
    def get_type_set():
        """Return the type list"""
        return set([InputModuleTypes.reqdeps, ])

    @staticmethod
    def rewrite(reqset):
        """The rewrite method checks if there is only one connected
        component.  If not an error is printed including all the found
        components.
        """
        tracer.debug("Called.")
        components = connected_components(reqset)

        if components.get_length() == 1:
            # Everything is ok: graph is connected
            tracer.debug("Finished.")
            return True

        raise RMTException(
            69, "Requirements graph has two or more connected "
            "components. Please fix the edges between the nodes."
            "Found components: %s" % components.as_string())
