'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Stores user preferences in the ~/.rmtoo directory. 
   
 (c) 2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import os

class UserPreferences:
    '''Global User Preferences handling.
       There are some global user preferences which must be stored
       system wide.  This class with handle these things.'''
    
    __default_rmtoo_home_dir = "~/.rmtoo"
    '''This is the default location of the rmtoo home dir.'''
    
    @staticmethod
    def __eval_rmtoo_home_dir(rmtoo_home_dir):
        '''Evaluates the rmtoo home dir.
           If given (and nor None), the provided directory is used.
           If not given, the default is used.'''
        if rmtoo_home_dir == None:
            return os.path.expanduser("~/.rmtoo")
        else:
            return rmtoo_home_dir

    def __init__(self, rmtoo_home_dir=None):
        '''Constructs a User Preferences object which can hold
           and store configuration values.'''
        self.__rmtoo_home_dir = self.__eval_rmtoo_home_dir(rmtoo_home_dir)
        
    def get_rmtoo_home_dir(self):
        '''Returns the used home directory.'''
        return self.__rmtoo_home_dir