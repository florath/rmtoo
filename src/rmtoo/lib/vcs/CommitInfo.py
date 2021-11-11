'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Small helper class for storing commit / vcs id information.

 (c) 2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from rmtoo.lib.logging import tracer


class CommitInfo(object):
    """Class that stores commit / id information"""

    def __init__(self, input_handler, commit, vcs_id):
        '''Store the data in the local object.
        PLEASE: grab all the information which is needed and
        store this in local variables - do NOT hold
        a reference to the input handler.
        '''
        self.__commit = commit
        self.__vcs_id = vcs_id
        self.__timestamp = input_handler.get_timestamp(commit)
        tracer.debug("Finished; commit info timestamp [%s]",
                     self.__timestamp)

    def get_vcs_id(self):
        '''Returns the vcs id of the object.'''
        return self.__vcs_id

    def get_commit(self):
        '''Returns the commit.'''
        return self.__commit

    def get_timestamp(self):
        '''Returns the timestamp of the commit.'''
        return self.__timestamp

    def __str__(self):
        '''Convert to string.
           This is used e.g. when the version of something is
           written into a document.'''
        return "Commit [%s] VCS Id [%s]" % (self.__commit, self.__vcs_id)
