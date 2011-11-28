'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Caches objects.
   This class caches objects.  The ID is the unique VCS id.
   
 (c) 2010-2011 by flonatel GmhH & Co. KG

 For licensing details see COPYING
'''

class ObjectCache:

    def __init__(self, object_type):
        '''Creates a cache for the given object_type.'''
        self.__object_type = object_type
        self.__objects = {}

    def get(self, oid):
        '''Tries to receive an object with the given id.
           If found, the object is returned, if not found
           None is returned.'''
        if self.__objects.has_key(oid):
            return self.__objects[oid]
        return None
