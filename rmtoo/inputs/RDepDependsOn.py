'''
 rmtoo
   Free and Open Source Requirements Management Tool

 The correct way to define dependencies.

 (c) 2010-2011,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals

from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.InputModuleTypes import InputModuleTypes


class RDepDependsOn(Digraph.Node):
    '''This class handles the creation of the full directed
    graphs: one 'Depends on' and one 'Dependent'.
    Both graphs are digraphs.
    '''

    depends_on = []
    tag = "Depends on"

    def __init__(self, config):
        Digraph.Node.__init__(self, "RDepDependsOn")
        self.config = config

    @staticmethod
    def get_type_set():
        """Return the requirement's types"""
        return set([InputModuleTypes.reqdeps, ])

    def rewrite(self, reqset):
        """Change the requirement set based on 'Depends on'"""
        conf_dependency_notation = \
            self.config.get_value('requirements.input.dependency_notation')
        if self.tag not in conf_dependency_notation:
            return True

        # Check if the "Solved by" is also available in the config
        also_solved_by = "Solved by" in conf_dependency_notation

        return reqset.resolve_depends_on(also_solved_by)
