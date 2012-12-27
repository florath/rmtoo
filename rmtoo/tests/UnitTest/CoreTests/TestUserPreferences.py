'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Unit test for User Preferences

 (c) 2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import os
import unittest
import tempfile
import shutil

from rmtoo.lib.UserPreferences import UserPreferences

class TestUserPreferences(unittest.TestCase):
    
    def test_set_rmtoo_home_dir(self):
        '''UserPreferences: check if the rmtoo home dir is set correctly.'''
        up = UserPreferences("/tmp/my/path")
        self.assertEqual("/tmp/my/path", up.get_rmtoo_home_dir())

    def test_default_rmtoo_home_dir(self):
        '''UserPreferences: check if the default rmtoo home dir works.'''
        up = UserPreferences()
        self.assertEqual(os.path.expanduser("~/.rmtoo"), 
                         up.get_rmtoo_home_dir())

    def test_add_new_value(self):
        '''UserPreferences: add new value to preferences.'''
        mid = "ThisIsMyNotSoAutomatedGeneratedId"
        up = UserPreferences()
        up.set_value("stats", "id", mid)
        self.assertEqual(mid, up.get_value("stats", "id"))
        
    def test_get_nonex_value(self):
        '''UserPreferences: Get a non existing value'''
        up = UserPreferences()
        self.assertRaises(KeyError, up.get_value, "dasIst", "nicht,da")
        
    def test_basic_io(self):
        '''UserPreferences: create prefs, write them, read them'''
        mid = "ThisIsMyNotSoAutomatedGeneratedId"
        tdir = tempfile.mkdtemp()

        up = UserPreferences(tdir)
        up.set_value("stats", "id", mid)
        up.write()
        
        upr = UserPreferences(tdir)
        upr.read()
        val = upr.get_value("stats", "id")
        
        shutil.rmtree(tdir)
        
        self.assertEqual(mid, val)
        