'''
 rmtoo
   Free and Open Source Requirements Management Tool

 The straight forward way to define dependencies.

 (c) 2010-2011,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals

from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.InputModuleTypes import InputModuleTypes


class RDepSolvedBy(Digraph.Node):
    """Tag handling the solved by"""

    depends_on = []
    tag = "Solved by"

    def __init__(self, config):
        Digraph.Node.__init__(self, "RDepSolvedBy")
        self.config = config

    @staticmethod
    def get_type_set():
        """Get the type"""
        return set([InputModuleTypes.reqdeps, ])

    def rewrite(self, reqset):
        """Solved by: is (historically) seen the default."""
        if self.tag not in \
           self.config.get_value_default(
                   'requirements.input.dependency_notation',
                   set(["Solved by", ])):
            return True
        return reqset.resolve_solved_by()
