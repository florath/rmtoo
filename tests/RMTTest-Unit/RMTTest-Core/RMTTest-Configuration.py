'''
 rmtoo
   Free and Open Source Requirements Management Tool

 Test class for the Configuration.

 (c) 2011,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


import json
import os
import shutil

from rmtoo.lib.configuration.Cfg import Cfg
from rmtoo.lib.RMTException import RMTException
from Utils import create_tmp_dir
from rmtoo.lib.logging import init_logger, tear_down_log_handler
from Utils import hide_volatile
import pytest


class RMTTestConfiguration(object):

    def rmttest_empty_configuration(self):
        '''Checks the empty configuration with different types of parameters'''
        config = Cfg()

        with pytest.raises(RMTException):
            config.get_value("k")
        with pytest.raises(RMTException):
            config.get_value("k.i")
        with pytest.raises(RMTException):
            config.get_value("k.i.j")
        with pytest.raises(RMTException):
            config.get_value(['k'])
        with pytest.raises(RMTException):
            config.get_value(['k', 'i'])
        with pytest.raises(RMTException):
            config.get_value(['k', 'i', 'j'])

    def rmttest_json_str(self):
        '''Checks JSON string handling of the configuration class'''
        config = Cfg.new_by_json_str('{"k": 1, "l": [2, 3], "m": {"n": 4}}')
        config.merge_json_str('{"k": 2, "m": {"n": 5}, "o": 7}')

        assert 2 == config.get_value("k"), "k is not 2"
        assert [2, 3] == config.get_value("l"), "l is not [2, 3]"
        assert 5 == config.get_value("m.n"), "m.n is not 5"
        assert 5 == config.get_value(["m", "n"]), "m.n is not 5"
        assert 7 == config.get_value("o"), "o is not 7"

    def rmttest_json_init_add_old_cmd_line_params(self):
        '''Init Cfg with JSON and add parameters with command line options'''
        config = Cfg.new_by_json_str('{"k": 1, "l": [2, 3], "m": {"n": 4}}')
        config.merge_cmd_line_params(['-m', '/tmp/something',
                                      '-c', '/tmp/cmad'])

        assert 1 == config.get_value("k"), "k is not 1"
        assert {'create_makefile_dependencies': '/tmp/cmad'} == \
            config.get_value("actions")

    def rmttest_json_init_add_new_cmd_line_params(self):
        '''Init Cfg with JSON and adds parameters with command line options'''
        mstderr = StringIO()
        init_logger(mstderr)

        # Create two JSON files.
        tmpdir = create_tmp_dir()
        jsonfile1 = os.path.join(tmpdir, "config1.json")
        with open(jsonfile1, "w") as jsonfd1:
            jsonfd1.write(json.dumps({'k': 2, 'm': {'n': 5}, 'o': 7}))

        jsonfile2 = os.path.join(tmpdir, "config2.json")
        with open(jsonfile2, "w") as jsonfd2:
            jsonfd2.write(json.dumps({'k': 3, 'm': {'w': 11}, 'p': 9}))

        config = Cfg.new_by_json_str('{"k": 1, "l": [2, 3], "m": {"n": 4}}')
        config.merge_cmd_line_params(['-j', '{"m": {"p": 99}}',
                                      '-j', 'file://' + jsonfile1,
                                      '-j', '{"m": {"q": 100}}',
                                      '-j', 'file://' + jsonfile2])
        assert 1 == config.get_value("k"), "k is not 1"
        config.evaluate()
        assert 3 == config.get_value("k"), "k is not 3"
        assert 11 == config.get_value("m.w")
        lstderr = hide_volatile(mstderr.getvalue())
        shutil.rmtree(tmpdir)
        tear_down_log_handler()
        assert lstderr == ""

    def rmttest_dollar_replacement_environment_variables(self):
        '''Check if the $ replacement works with environment variables.'''
        os.environ["huho"] = "ThereIsSomeVal"
        config = Cfg.new_by_json_str('{"k": "${ENV:huho}"}')
        val = config.get_rvalue("k")
        os.environ["huho"] = ""
        assert "ThereIsSomeVal" == val, \
            "k is not ThereIsSomeVal"

    def rmttest_dollar_replacement_configuration_variables(self):
        '''Check if the $ replacement works with configuration variables.'''
        config = Cfg.new_by_json_str(
            '{"k": "${huho}", "huho": "ThereIsSomeVal"}')
        assert "ThereIsSomeVal" == config.get_rvalue("k"), \
            "k is not ThereIsSomeVal"
