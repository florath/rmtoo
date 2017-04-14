'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Generic non-empty dictionary.
  If one element is not there it will be automatically created. 
   
 (c) 2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

class GenNonEmptyDict:
    
    def __init__(self, factory):
        '''Generates an empty dictionary: also the constructor to create
           empty objects.'''
        self.__dict = {}
        self.__factory = factory
        
    def insert(self, key, value):
        '''Insert the key / value pair into the dictionary.'''
        self.__dict[key] = value
        
    def __getitem__(self, key):
        '''Returns the key from the dict.'''
        if key not in self.__dict:
            self.__dict[key] = self.__factory(key)
        return self.__dict[key]
    
    def iteritems(self):
        '''Passes the things directly from the dict.'''
        return self.__dict.iteritems()