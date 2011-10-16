'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
 Test class for the Configuration.
 
 (c) 2011 by flonatel GmhH & Co. KG

 For licensing details see COPYING
'''

import unittest
import json
import os

from rmtoo.lib.configuration.Cfg import Cfg
from rmtoo.lib.configuration.CfgEx import CfgEx
from rmtoo.tests.lib.Utils import create_tmp_dir, delete_tmp_dir

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

    def test_json_init_add_old_cmd_line_params(self):
        '''Init Cfg with JSON and add parameters with command line options'''
        config = Cfg.new_by_json_str('{"k": 1, "l": [2, 3], "m": {"n": 4}}');
        config.merge_cmd_line_params(['-m', '/tmp/something',
                                      '-c', '/tmp/cmad'])

        self.failUnlessEqual(1, config.get_value("k"), "k is not 1")
        self.failUnlessEqual({'create_makefile_dependencies': '/tmp/cmad'},
                             config.get_value("actions"))

    def test_json_init_add_new_cmd_line_params(self):
        '''Init Cfg with JSON and adds parameters with command line options'''
        # Create two JSON files.
        tmpdir = create_tmp_dir()
        jsonfile1 = os.path.join(tmpdir, "config1.json")
        jsonfd1 = file(jsonfile1, "w")
        jsonfd1.write(json.dumps({'k': 2 , 'm': {'n': 5}, 'o': 7}))
        jsonfd1.close()
        jsonfile2 = os.path.join(tmpdir, "config2.json")
        jsonfd2 = file(jsonfile2, "w")
        jsonfd2.write(json.dumps({'k': 3 , 'm': {'w': 11}, 'p': 9}))
        jsonfd2.close()

        config = Cfg.new_by_json_str('{"k": 1, "l": [2, 3], "m": {"n": 4}}');
        config.merge_cmd_line_params(['-j', '{"m": {"p": 99}}',
                                      '-j', 'file://' + jsonfile1,
                                      '-j', '{"m": {"q": 100}}',
                                      '-j', 'file://' + jsonfile2])
        self.failUnlessEqual(1, config.get_value("k"), "k is not 1")
        print("j [%s]" % config.config)
        assert(False)
