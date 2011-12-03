'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Caches objects.
   This class caches objects.  The ID is the unique VCS id.
   
 (c) 2010-2011 by flonatel GmhH & Co. KG

 For licensing details see COPYING
'''

from types import ListType
from rmtoo.lib.logging.EventLogging import tracer
from rmtoo.lib.RMTException import RMTException

class ObjectCache:
    '''Stores objects from different types under a unique id.
       Each class has a separate store: it is possible to 
       have the same id for multiple objects of different types.'''

    def __init__(self):
        '''Creates a cache for the given object_type.'''
        self.__objects = {}
        self.__stats_cnt_objects = 0
        self.__stats_cnt_object_types = 0
        self.__stats_cnt_get = 0
        self.__stats_cnt_get_found = 0

    def log_stats(self):
        '''Prints out the usage statistics.'''
        tracer.info("usage statistics: objects [%d] object types [%d] "
                    "called get [%d] called get (found) [%d]"
                    % (self.__stats_cnt_objects, self.__stats_cnt_object_types,
                       self.__stats_cnt_get, self.__stats_cnt_get_found))

    @staticmethod
    def create_hashable(oid):
        '''If the oid is a list, the oid is converted into a string.'''
        tracer.debug("called: oid [%s]" % oid)
        if type(oid) == ListType:
            if len(oid) == 1:
                return oid[0]
            return '-'.join(oid)
        return oid

    def get(self, object_type, oid):
        '''Tries to receive an object with the given id.
           If found, the object is returned, if not found
           None is returned.'''
        tracer.debug("called: object type [%s] oid [%s]" % (object_type, oid))
        self.__stats_cnt_get += 1

        if self.__objects.has_key(object_type) \
            and self.__objects[object_type].has_key(oid):
            self.__stats_cnt_get_found += 1
            return self.__objects[object_type][oid]
        return None

    def add(self, oid, object_type, obj):
        '''Adds the given object to the cache using the given object id.
           Checks of the object is of the correct type and if
           the object is already in the cache.'''
        tracer.debug("adding object with object type [%s] oid [%s]"
                     % (object_type, oid))

        if not self.__objects.has_key(object_type):
            self.__stats_cnt_object_types += 1
            self.__objects[object_type] = {}

        if oid in self.__objects[object_type]:
            assert False
            raise RMTException(106, "object with oid [%s] already in cache."
                               % oid)
        self.__stats_cnt_objects += 1
        self.__objects[object_type][oid] = obj
