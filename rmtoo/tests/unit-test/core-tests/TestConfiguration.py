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
import sys

from rmtoo.lib.configuration.Cfg import Cfg
from rmtoo.lib.RMTException import RMTException
from rmtoo.tests.lib.Utils import create_tmp_dir, delete_tmp_dir
from rmtoo.lib.logging.MemLogStore import MemLogStore
from rmtoo.lib.logging.LogLevel import LogLevel

class TestConfiguration(unittest.TestCase):

    def test_empty_configuration(self):
        '''Checks the empty configuration with different types of parameters'''
        config = Cfg()

        self.failUnlessRaises(RMTException, config.get_value, "k")
        self.failUnlessRaises(RMTException, config.get_value, "k.i")
        self.failUnlessRaises(RMTException, config.get_value, "k.i.j")
        self.failUnlessRaises(RMTException, config.get_value, ['k'])
        self.failUnlessRaises(RMTException, config.get_value, ['k', 'i'])
        self.failUnlessRaises(RMTException, config.get_value, ['k', 'i', 'j'])

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
        log_store = MemLogStore()

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
        config.evaluate(log_store)
        self.failUnlessEqual(3, config.get_value("k"), "k is not 3")
        self.failUnlessEqual(11, config.get_value("m.w"))
        self.failUnlessEqual(MemLogStore.create_mls([]), log_store)

    def test_json_init_add_old_cmd_line_params(self):
        '''Init Cfg with old config and adds parameters with command line options'''
        log_store = MemLogStore()

        config = Cfg.new_by_json_str('{"k": 1, "l": [2, 3], "m": {"n": 4}}');
        config.merge_cmd_line_params(['-f', 'tests/unit-test/core-tests/'
                                      'testdata/Config3.py'])

        self.failUnlessEqual(1, config.get_value("k"), "k is not 1")
        config.evaluate(log_store)
        self.failUnlessEqual(['development', 'management', 'users', 'customers'],
                             config.get_value("requirements.stakeholders"))
        print("UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU")
        log_store.write_log(sys.stdout)

## TODO:+ + +Warning:100:Old Configuration: Not converted attributes: [['output_specs2']]

        print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
        self.failUnlessEqual(MemLogStore.create_mls([[
            100, LogLevel.warning(),
            "Old Configuration: Not converted attributes: [['output_specs2']]"]]),
                             log_store)

    def test_dollar_replacement_environment_variables(self):
        '''Check if the $ replacement works with environment variables.'''
        log_store = MemLogStore()
        os.environ["huho"] = "ThereIsSomeVal"
        config = Cfg.new_by_json_str('{"k": "${ENV:huho}"}')
        val = config.get_rvalue("k")
        os.environ["huho"] = ""
        self.failUnlessEqual("ThereIsSomeVal", val,
                             "k is not ThereIsSomeVal")

    def test_dollar_replacement_configuration_variables(self):
        '''Check if the $ replacement works with configuration variables.'''
        log_store = MemLogStore()
        config = Cfg.new_by_json_str(
            '{"k": "${huho}", "huho": "ThereIsSomeVal"}')
        self.failUnlessEqual("ThereIsSomeVal", config.get_rvalue("k"),
                             "k is not ThereIsSomeVal")



