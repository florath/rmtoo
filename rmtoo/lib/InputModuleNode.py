'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Wrapper to handle modules as digraph nodes.
   
 (c) 2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.digraph.Digraph import Digraph

class InputModuleNode(Digraph.Node):
    '''Class to implement an Node interface and to hold a reference to
       a python module.'''

    def __init__(self, name, module):
        '''Constructs an object with the help of the provided information.'''
        Digraph.Node.__init__(self, name)
        self.__module = module
        
    def get_module(self):
        '''Returns the module.'''
        return self.__module
    
    def __deepcopy__(self, a):
        assert False
