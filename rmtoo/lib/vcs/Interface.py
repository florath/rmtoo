'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Abstract Base Class (ABC) to handle different version control systems.
   
 (c) 2011 by flonatel GmhH & Co. KG

 For licensing details see COPYING
'''

import abc

class Interface:
    
    @abc.abstractmethod
    def read_history(self, start_vers, end_vers):
        '''Reads in the complete history beginning from start_vers
           up to the end_vers.
           Returns a list of pairs (list with two entries):
           Each pair must contain a unique version id and appropriate 
           TopicSetCollection object.
           The list must be ordered in the way that the newest one
           is in the front of the list.'''
        return
