'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Caches objects.
   This class caches objects.  The ID is the unique VCS id.
   
 (c) 2010-2011 by flonatel GmhH & Co. KG

 For licensing details see COPYING
'''

from types import ListType

class ObjectCache:

    def __init__(self, object_type):
        '''Creates a cache for the given object_type.'''
        self.__object_type = object_type
        self.__objects = {}

    @staticmethod
    def __create_hashable(oid):
        '''If the oid is a list, the oid is converted into a string.'''
        if type(oid) == ListType:
            print("LIST TYPE")
            if len(oid) == 1:
                return oid[0]
            return '-'.join(oid)
        return oid

    def get(self, oid):
        '''Tries to receive an object with the given id.
           If found, the object is returned, if not found
           None is returned.'''
        loid = self.__create_hashable(oid)
        print("LOID %s" % loid)
        if self.__objects.has_key(loid):
            return self.__objects[loid]
        return None
