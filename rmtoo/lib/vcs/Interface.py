'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Abstract Base Class (ABC) to handle different version control systems.
  This includes also reading in the latest version from the file system.
   
 (c) 2011 by flonatel GmhH & Co. KG

 For licensing details see COPYING
'''

import abc

class Interface:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def read(self):
        '''Reads in the complete history. The appropriate
           information was given in the constructor.
           Returns a list of pairs (list with two entries):
           Each pair must contain a unique version id and appropriate 
           TopicSetCollection object.
           The list must be ordered in the way that the newest one
           is in the front of the list.'''
        assert False
