'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Constrains implementation

 (c) 2011-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.logging import tracer
from rmtoo.lib.InputModuleTypes import InputModuleTypes


class RDepConstraints(Digraph.Node):
    """Holding Constraints"""

    depends_on = ["RDepDependsOn", "RDepSolvedBy"]

    def __init__(self, config):
        Digraph.Node.__init__(self, "RDepConstraints")
        self.config = config

    @staticmethod
    def get_type_set():
        """Return the requirement's types"""
        return set([InputModuleTypes.reqdeps, ])

    @staticmethod
    def rewrite(reqset):
        """The constrains value gets a dictionary from the name of the
        constraints to the object.
        """
        tracer.debug("Called.")
        reqset.resolve_ce3()
        tracer.debug("Finished.")
        return True
