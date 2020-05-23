'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Constraint Execution and Evaluation Environment Set

 (c) 2011-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from rmtoo.lib.logging import tracer


class CE3Set(object):
    '''Sets which holds all the constrains execution environments.'''

    def __init__(self):
        '''Init: empty dict.'''
        tracer.debug("CE3Set constructor called.")
        # This holds all the requirements CE3s
        self.__ce3s = {}

    def insert(self, name, ce3):
        '''Add a new ce3.'''
        tracer.debug("Insert ce3 for requirement [%s]", name)
        if ce3 is None:
            return
        if ce3 in self.__ce3s:
            assert False
        self.__ce3s[name] = ce3

    def get(self, name):
        '''Returns a CE3Set.'''
        tracer.debug("Get ce3 for requirement [%s]", name)
        return self.__ce3s[name]

    def length(self):
        '''Return the number of CE3s in the dictionary.'''
        return len(self.__ce3s)
