'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Requirement Digraph Node class
   
 (c) 2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.logging import tracer
from rmtoo.lib.FuncCall import FuncCall

class RequirementDNode(Digraph.Node):
    '''Indirection class between a digraph and a requirement.
       In some cases a requirement must be held in some digraphs.
       This class can be stored into one digraph and the internal
       reference points to the appropriate requirement.'''
       
    def execute(self, executor, func_prefix):
        '''Execute the parts which are needed for Requirement.'''
        tracer.debug("Called: name [%s]." % self.get_name())
        FuncCall.pcall(executor, func_prefix + "requirement", self)
        tracer.debug("Finished: name [%s]." % self.get_name())
   
    def __init__(self, requirement):
        '''Sets up the class hirarchy and stores the requirement.'''
        Digraph.Node.__init__(self, requirement.get_id())
        self.__requirement = requirement

    def get_requirement(self):
        '''Returns the requirement from inside.'''
        return self.__requirement
    
    def __repr__(self):
        '''The representation is the name of the node.'''
        return self.get_name()
