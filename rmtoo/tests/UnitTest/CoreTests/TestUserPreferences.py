'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Unit test for User Preferences

 (c) 2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import os
import unittest

from rmtoo.lib.UserPreferences import UserPreferences

class TestUserPreferences(unittest.TestCase):
    
    def test_set_rmtoo_home_dir(self):
        '''UserPreferences: check if the rmtoo home dir is set correctly.'''
        up = UserPreferences("/tmp/my/path")
        assert(up.get_rmtoo_home_dir() == "/tmp/my/path")

    def test_default_rmtoo_home_dir(self):
        '''UserPreferences: check if the default rmtoo home dir works.'''
        up = UserPreferences()
        assert(up.get_rmtoo_home_dir() == os.path.expanduser("~/.rmtoo"))

    def test_add_new_value(self):
        '''UserPreferences: add new value to preferences.'''
        mid = "ThisIsMyNotSoAutomatedGeneratedId"
        up = UserPreferences()
        up.add_value("stats", "id", mid)
        assert(up.get_value("stats", "id") == mid)
        