#
# Requirement Management Toolset
#  Test Module
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

import os
import copy
from rmtoo.lib.Modules import Modules
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.digraph.Helper import node_list_to_node_name_list

mod_base_dir = "rmtoo/tests/unit-test/core-tests/testdata"
mods_name = mod_base_dir.split("/")

def mods_list(lm):
    #print("MODSNAME '%s'" % mods_name)
    ml=copy.deepcopy(mods_name)
    ml.append(lm)
    return ml

class TestModule:

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
            assert(rmte.eid==27)

    def test_simple_04(self):
        "Module test with cyclic dependency "
        try:
            mods = Modules(os.path.join(mod_base_dir, "modules04"),
                           {}, {}, [], mods_list("modules04"))
            assert(False)
        except RMTException, rmte:
            assert(rmte.eid==26)

