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
from rmtoo.lib.MemLogStore import MemLogStore
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.digraph.Helper import node_list_to_node_name_list

mod_base_dir = "tests/unit-test/core-tests/testdata"
mods_name = mod_base_dir.split("/")

def mods_list(lm):
    #print("MODSNAME '%s'" % mods_name)
    ml=["rmtoo"]
    ml.extend(mods_name)
    ml.append(lm)
    return ml

class TestModules:

    def test_positive_01(self):
        "Modules.split_directory with '.'"

        d = Modules.split_directory(".")
        assert(d==[])

    def test_positive_02(self):
        "Modules.split_directory with absolute path"

        d = Modules.split_directory("/tmp/this/is/a/path")
        assert(d==['/', 'tmp', 'this', 'is', 'a', 'path'])


    def test_simple_01(self):
        "Simple module test"
        mods = Modules(os.path.join(mod_base_dir, "modules01"),
                       {}, {}, [], mods_list("modules01"))

    def test_simple_02(self):
        "Module test with dependend modules"
        mods = Modules(os.path.join(mod_base_dir, "modules02"),
                       {}, {}, [], mods_list("modules02"))
        mods_name = node_list_to_node_name_list(mods.reqdeps_sorted)
        assert(mods_name==['Module01', 'Module02'])
        
    def test_simple_03(self):
        "Module test with invalid dependency "
        try:
            mods = Modules(os.path.join(mod_base_dir, "modules03"),
                           {}, {}, [], mods_list("modules03"))
            assert(False)
        except RMTException, rmte:
            assert(rmte.id()==27)

    def test_simple_04(self):
        "Module test with cyclic dependency "
        try:
            mods = Modules(os.path.join(mod_base_dir, "modules04"),
                           {}, {}, [], mods_list("modules04"))
            assert(False)
        except RMTException, rmte:
            assert(rmte.id()==26)

    def test_simple_05(self):
        "Module test with dependend modules"
        mods = Modules(os.path.join(mod_base_dir, "modules05"),
                       {}, {}, [], mods_list("modules05"))
        sio = StringIO.StringIO("Name: t\n")
        mls = MemLogStore()
        req = Requirement(sio, 77, mls, mods, None, None)

        sout = StringIO.StringIO()
        mls.write_log(sout)
        assert(req.state==Requirement.er_error)
        assert(sout.getvalue()==
               "+++ Error: 54:77:tag 'SameTag' already defined\n")
