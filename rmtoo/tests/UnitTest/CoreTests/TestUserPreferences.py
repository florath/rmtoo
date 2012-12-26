'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Unit test for User Preferences

 (c) 2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import unittest

from rmtoo.lib.UserPreferences import UserPreferences

class TestUserPreferences(unittest.TestCase):
    
    def test_set_rmtoo_home_dir(self):
        '''UserPreferences: check if the rmtoo home dir is set correctly.'''
        up = UserPreferences("/tmp/my/path")
        assert(up.get_rmtoo_home_dir() == "/tmp/my/path")
