#
# Requirement Management Toolset
#
#  Unit test for RequirementSet
#
# (c) 2010 on flonatel
#
# For licencing details see COPYING
#

import os
import sys
import StringIO
from rmtoo.lib.RequirementSet import RequirementSet
from rmtoo.lib.Modules import Modules
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.MemLogStore import MemLogStore, MemLog
from rmtoo.tests.lib.ModuleHelper import mods_list
from rmtoo.tests.lib.TestConfig import TestConfig

mod_base_dir = "tests/unit-test/core-tests/testdata"

class TestReqSet:

    def test_positive_01(self):
        "Requirement contains a tag where no handler exists"

        mods = Modules(os.path.join(mod_base_dir, "modules08"),
                       {}, {}, [], mods_list("modules08", mod_base_dir))

        sio = StringIO.StringIO("Hubbel: bubbel")
        req = Requirement(sio, "hubbel", None, mods, None, TestConfig())

        reqs = RequirementSet(mods, None, None)
        reqs.add_req(req)
        reqs.handle_modules()

        assert(reqs.mls()==MemLogStore.create_mls(
                [ [57, MemLog.error, "req not empty. Missing tag handers "
                   "for '{'Hubbel': 'bubbel'}'", "hubbel"],
                  [56, MemLog.error, "There were errors encountered during "
                   "parsing and checking - can't continue"] ] ))
