'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Base class for Analytics.

  This class provides some basic functionality and the interface
  for the analytics classes.

 (c) 2010-2011,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from rmtoo.lib.Executor import Executor


class Base(Executor):
    '''Base class for all analytics checks.
       This class provides the basic methods and infrastructure
       to handle the analytics.'''

    def __init__(self):
        '''Constructs an Analytics Base.'''
        self.__success = True
        self.__results = []

    def get_success(self):
        '''Returns if the analytics were successful.'''
        return self.__success

    def set_failed(self):
        '''Set the state to not successful.'''
        self.__success = False

    def add_result(self, result):
        '''Add the given result to the result container.'''
        self.__results.append(result)

    def write_result(self, mfd):
        '''Write the result to the given file descriptor.'''
        for result in self.__results:
            result.write_error(mfd)
