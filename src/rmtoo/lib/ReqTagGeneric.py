'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Generic Tag Class

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from rmtoo.lib.RMTException import RMTException


class ReqTagGeneric(object):
    '''This class is the base class of mostly all tags.
       It handles basic setup as well as handling of common cases.'''

    def __init__(self, config, tag, ltypes):
        '''Store the appropriate values in the tag.'''
        self.__config = config
        self.__tag = tag
        self.__ltypes = ltypes

    def get_type_set(self):
        '''Return all types where this tag is valid for.'''
        return self.__ltypes

    def get_tag(self):
        '''Returns the current tag.'''
        return self.__tag

    def get_config(self):
        '''Return the configuration.'''
        return self.__config

    def get_and_remove(self, req):
        '''Remove the deleted tag from the req.'''
        tval = req[self.__tag]
        del req[self.__tag]
        return self.__tag, tval

    def check_mandatory_tag(self, rid, req, eid):
        '''Call this from the 'rewrite()' method, if the tag is mandatory.
           Note: this function only checks the availability of the tag but
           does not perform any other check.
           Returns 'True' if the tag is available and 'False' if the tag is
           not available.'''
        # The given tag is mandatory
        if self.__tag not in req:
            raise RMTException(eid, "Does not contain the "
                               "tag '%s'" % self.__tag, rid)

    def handle_optional_tag(self, req):
        '''The method 'handle_optional_tag()' handles optional tags in the
           sense, that it copies over the content to the class object
           itself and removes it from the input req queue.  It does not
           perform any other check.
           Note: if the tag is not available, the appropriate value is set
           to None.
           Note: It is possible to use the return values directly from the
           rewrite() method.'''
        if self.__tag in req:
            return self.get_and_remove(req)

        return self.__tag, None
