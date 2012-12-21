'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Requirement Digraph Node class
   
 (c) 2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.digraph.Digraph import Digraph

class RequirementDNode(Digraph.Node):
    '''Indirection class between a digraph and a requirement.
       In some cases a requirement must be held in some digraphs.
       This class can be stored into one digraph and the internal
       reference points to the appropriate requirement.'''

    def __init__(self, requirement):
        '''Sets up the class hirarchy and stores the requirement.'''
        Digraph.Node.__init__(self, requirement.get_id())
        self.__requirement = requirement

    def get_requirement(self):
        '''Returns the requirement from inside.'''
        return self.__requirement
