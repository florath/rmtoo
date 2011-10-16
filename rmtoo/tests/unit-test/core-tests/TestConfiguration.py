'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
 Test class for the Configuration.
 
 (c) 2011 by flonatel GmhH & Co. KG

 For licensing details see COPYING
'''

import unittest
from rmtoo.lib.configuration.Cfg import Cfg
from rmtoo.lib.configuration.CfgEx import CfgEx

class TestConfiguration(unittest.TestCase):

    def test_empty_configuration(self):
        '''Checks the empty configuration with different types of parameters'''
        config = Cfg()

        self.failUnlessRaises(CfgEx, config.get_value, "k")
        self.failUnlessRaises(CfgEx, config.get_value, "k.i")
        self.failUnlessRaises(CfgEx, config.get_value, "k.i.j")
        self.failUnlessRaises(CfgEx, config.get_value, ['k'])
        self.failUnlessRaises(CfgEx, config.get_value, ['k', 'i'])
        self.failUnlessRaises(CfgEx, config.get_value, ['k', 'i', 'j'])

    def test_json_str(self):
        '''Checks JSON string handling of the configuration class'''
        config = Cfg.new_by_json_str('{"k": 1, "l": [2, 3], "m": {"n": 4}}');
        config.merge_json_str('{"k": 2, "m": {"n": 5}, "o": 7}')

        self.failUnlessEqual(2, config.get_value("k"), "k is not 2")
        self.failUnlessEqual([2, 3], config.get_value("l"), "l is not [2, 3]")
        self.failUnlessEqual(5, config.get_value("m.n"), "m.n is not 5")
        self.failUnlessEqual(5, config.get_value(["m", "n"]), "m.n is not 5")
        self.failUnlessEqual(7, config.get_value("o"), "o is not 7")
