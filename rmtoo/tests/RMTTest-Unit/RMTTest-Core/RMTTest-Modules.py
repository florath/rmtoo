'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for input modules

 (c) 2010,2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
import os
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
import unittest

from rmtoo.lib.InputModules import InputModules
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RequirementSet import RequirementSet
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.digraph.Helper import node_list_to_node_name_list
from rmtoo.tests.lib.ModuleHelper import mods_list
from rmtoo.tests.lib.TestConfig import TestConfig
from rmtoo.lib.logging import init_logger, tear_down_log_handler
from rmtoo.tests.lib.Utils import hide_volatile

mod_base_dir = "tests/RMTTest-Unit/RMTTest-Core/testdata"


class RMTTestModules(unittest.TestCase):

    def rmttest_positive_01(self):
        "InputModules._split_directory with '.'"

        d = InputModules._split_directory(".")
        self.assertEqual([], d)

    def rmttest_positive_02(self):
        "InputModules._split_directory with absolute path"

        d = InputModules._split_directory("/tmp/this/is/a/path")
        self.assertEqual(['/', 'tmp', 'this', 'is', 'a', 'path'], d)

    def rmttest_simple_01(self):
        "Simple module test"
        InputModules(os.path.join(mod_base_dir, "modules01"),
                     {}, [], mods_list("modules01", mod_base_dir))

    def rmttest_simple_02(self):
        "Module test with dependend modules"
        mods = InputModules(os.path.join(mod_base_dir, "modules02"),
                            {}, [], mods_list("modules02", mod_base_dir))
        mods_name = node_list_to_node_name_list(mods.get_reqdeps_sorted())
        assert(mods_name == ['Module01', 'Module02'])

    def rmttest_simple_03(self):
        "Module test with invalid dependency "
        with self.assertRaises(RMTException) as rmte:
            InputModules(os.path.join(mod_base_dir, "modules03"),
                         {}, [], mods_list("modules03", mod_base_dir))
            self.assertEqual(27, rmte.id())

    def rmttest_simple_04(self):
        "Module test with cyclic dependency "
        with self.assertRaises(RMTException) as rmte:
            InputModules(os.path.join(mod_base_dir, "modules04"),
                         {}, [], mods_list("modules04", mod_base_dir))
            self.assertEqual(26, rmte.get_id())

    def rmttest_simple_05(self):
        "Module test with dependent modules"
        mstderr = StringIO()
        init_logger(mstderr)

        mods = InputModules(os.path.join(mod_base_dir, "modules05"),
                            {}, [], mods_list("modules05", mod_base_dir))
        req = Requirement(u"Name: t\n", u"77", None, mods, TestConfig())

        lstderr = hide_volatile(mstderr.getvalue())
        tear_down_log_handler()
        self.assertEqual(req.is_usable(), False)
        expected_result \
            = "===DATETIMESTAMP===;rmtoo;ERROR;BaseRMObject;" \
            "handle_modules_tag;===LINENO===; 54:77:tag [SameTag] " \
            "already defined\n"
        self.assertEqual(lstderr, expected_result)

    def rmttest_simple_06(self):
        "Requirement: Module test with exception thrown"
        mstderr = StringIO()
        init_logger(mstderr)

        mods = InputModules(os.path.join(mod_base_dir, "modules06"),
                            {}, [], mods_list("modules06", mod_base_dir))
        req = Requirement(u"Name: t\n", u"77", None, mods, TestConfig())

        lstderr = hide_volatile(mstderr.getvalue())
        tear_down_log_handler()
        self.assertEqual(req.is_usable(), False)
        expected_result \
            = "===DATETIMESTAMP===;rmtoo;ERROR;BaseRMObject;" \
            "handle_modules_tag;===LINENO===; 55:TCExcept\n" \
            "===DATETIMESTAMP===;rmtoo;ERROR;BaseRMObject;" \
            "handle_modules_tag;" \
            "===LINENO===; 41:77:semantic error occurred " \
            "in module [Module01]\n"
        self.assertEqual(lstderr, expected_result)

    def rmttest_simple_07(self):
        "RequirementSet: Module which renders set as errornous"
        mstderr = StringIO()
        init_logger(mstderr)

        mods = InputModules(os.path.join(mod_base_dir, "modules07"),
                            {}, [], mods_list("modules07", mod_base_dir))
        reqs = RequirementSet(None)
        reqs._handle_modules(mods)
        self.assertEqual(reqs.is_usable(), False)

        lstderr = hide_volatile(mstderr.getvalue())
        tear_down_log_handler()

        expected_result \
            = "===DATETIMESTAMP===;rmtoo;ERROR;RequirementSet;" \
            "_handle_modules;===LINENO===; 43:there was a problem " \
            "handling the requirement set modules\n"
        self.assertEqual(lstderr, expected_result)
