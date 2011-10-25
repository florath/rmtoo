#
# Unit Test cases for Modules
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

import os
import StringIO
from rmtoo.lib.Modules import Modules
from rmtoo.lib.logging.MemLogStore import MemLogStore
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RequirementSet import RequirementSet
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.digraph.Helper import node_list_to_node_name_list
from rmtoo.tests.lib.ModuleHelper import mods_list
from rmtoo.tests.lib.TestConfig import TestConfig

mod_base_dir = "tests/unit-test/core-tests/testdata"

class TestModules:

    def test_positive_01(self):
        "Modules.split_directory with '.'"

        d = Modules.split_directory(".")
        assert(d == [])

    def test_positive_02(self):
        "Modules.split_directory with absolute path"

        d = Modules.split_directory("/tmp/this/is/a/path")
        assert(d == ['/', 'tmp', 'this', 'is', 'a', 'path'])


    def test_simple_01(self):
        "Simple module test"
        mods = Modules(os.path.join(mod_base_dir, "modules01"),
                       {}, [], mods_list("modules01", mod_base_dir))

    def test_simple_02(self):
        "Module test with dependend modules"
        mods = Modules(os.path.join(mod_base_dir, "modules02"),
                       {}, [], mods_list("modules02", mod_base_dir))
        mods_name = node_list_to_node_name_list(mods.reqdeps_sorted)
        assert(mods_name == ['Module01', 'Module02'])

    def test_simple_03(self):
        "Module test with invalid dependency "
        try:
            mods = Modules(os.path.join(mod_base_dir, "modules03"),
                           {}, [], mods_list("modules03", mod_base_dir))
            assert(False)
        except RMTException, rmte:
            assert(rmte.id() == 27)

    def test_simple_04(self):
        "Module test with cyclic dependency "
        try:
            mods = Modules(os.path.join(mod_base_dir, "modules04"),
                           {}, [], mods_list("modules04", mod_base_dir))
            assert(False)
        except RMTException, rmte:
            assert(rmte.id() == 26)

    def test_simple_05(self):
        "Module test with dependend modules"
        mods = Modules(os.path.join(mod_base_dir, "modules05"),
                       {}, [], mods_list("modules05", mod_base_dir))
        sio = StringIO.StringIO("Name: t\n")
        mls = MemLogStore()
        req = Requirement(sio, 77, mls, mods, TestConfig())

        sout = StringIO.StringIO()
        mls.write_log(sout)
        assert(req.state == Requirement.er_error)
        assert(sout.getvalue() ==
               "+++ Error: 54:77:tag 'SameTag' already defined\n")

    def test_simple_06(self):
        "Requirement: Module test with exception thrown"

        mods = Modules(os.path.join(mod_base_dir, "modules06"),
                       {}, [], mods_list("modules06", mod_base_dir))
        sio = StringIO.StringIO("Name: t\n")
        mls = MemLogStore()
        req = Requirement(sio, 77, mls, mods, TestConfig())

        sout = StringIO.StringIO()
        mls.write_log(sout)
        assert(req.state == Requirement.er_error)
        assert(sout.getvalue() ==
               "+++ Error: 55:TCExcept\n"
               "+++ Error: 41:77:semantic error occured in module 'Module01'\n")

    def test_simple_07(self):
        "RequirementSet: Module which renders set as errornous"

        mods = Modules(os.path.join(mod_base_dir, "modules07"),
                       {}, [], mods_list("modules07", mod_base_dir))
        reqs = RequirementSet(mods, None)
        reqs.handle_modules()
        assert(reqs.state == RequirementSet.er_error)

        sout = StringIO.StringIO()
        reqs.write_log(sout)
        assert(sout.getvalue() == "+++ Error: 43:there was a problem handling the requirement set modules\n")
