'''
 rmtoo
   Free and Open Source Requirements Management Tool

 UsableFlag
   In some circumstances it makes sense - even if there is
   an error - to continue.
   This objects help flagging the object either usable or unusable.

 (c) 2011-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from rmtoo.lib.logging import tracer


# pylint: disable=too-few-public-methods
class UsableFlag(object):
    '''Holding flag to show if an object is usable or not.'''

    def __init__(self):
        '''Initializes the usable flag - which is initially set
           to true (is usable).'''
        self.__is_usable = True

    def _adapt_usablility(self, ouflag):
        '''If the other usable flag is false, the usability of the self
           is set to false.  If the other usable flag is true, the self
           is not touched.'''
        if not ouflag.is_usable():
            self.__is_usable = False

    def is_usable(self):
        '''Return the current state of the usable flag.'''
        return self.__is_usable

    def _set_not_usable(self):
        '''The object is marked as not usable (any more).'''
        tracer.info("Setting object to unusable.")
        self.__is_usable = False
