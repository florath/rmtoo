'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
 The correct way to define dependencies.
 
 (c) 2010-2011 by flonatel GmhH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.digraph.Digraph import Digraph

class RDepDependsOn(Digraph.Node):
    '''This class handles the creation of the full directed 
       graphs: one 'Depends on' and one 'Dependent'.  
       Both graphs are digraphs.'''

    depends_on = []
    tag = "Depends on"

    def __init__(self, config):
        Digraph.Node.__init__(self, "RDepDependsOn")
        self.config = config

    def type(self):
        return set(["reqdeps", ])

    def set_modules(self, mods):
        self.mods = mods

    def rewrite(self, reqset):
        conf_dependency_notation = \
            self.config.get_value('requirements.input.dependency_notation')
        if self.tag not in conf_dependency_notation:
            return True

        # Check if the "Solved by" is also available in the config
        also_solved_by = "Solved by" in conf_dependency_notation

        return reqset.resolve_depends_on(also_solved_by)
