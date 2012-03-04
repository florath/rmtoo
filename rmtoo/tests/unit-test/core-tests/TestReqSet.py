'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Unit test for RequirementSet

 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''


import os
import sys
import StringIO
from rmtoo.lib.RequirementSet import RequirementSet
from rmtoo.lib.InputModules import InputModules
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.logging.MemLogStore import MemLogStore
from rmtoo.lib.logging.MemLog import MemLog
from rmtoo.lib.logging.LogLevel import LogLevel
from rmtoo.tests.lib.ModuleHelper import mods_list
from rmtoo.tests.lib.TestConfig import TestConfig
from rmtoo.lib.logging.MemLogStore import MemLogStore

mod_base_dir = "tests/unit-test/core-tests/testdata"

class TestReqSet:

    def test_positive_01(self):
        "Requirement contains a tag where no handler exists"

        mods = InputModules(os.path.join(mod_base_dir, "modules08"),
                       {}, [], mods_list("modules08", mod_base_dir))
        mls = MemLogStore()

        reqs = RequirementSet(None)
        req = Requirement("Hubbel: bubbel", "hubbel", None, reqs, mods, TestConfig())
        reqs._add_requirement(req)
        reqs._handle_modules(mods)

        print("REAS [%s]" % reqs.to_list())

        assert(reqs.to_list() ==
                [[57, LogLevel.error(), "No tag handler found for tag(s) "
                  "'['Hubbel']' - Hint: typo in tag(s)?", 'hubbel'],
                 [56, LogLevel.error(), "There were errors encountered during "
                  "parsing and checking - can't continue"] ])

    def test_positive_02(self):
        "Requirement contains a tag where no handler exists - multiple tags"

        mods = InputModules(os.path.join(mod_base_dir, "modules08"),
                       {}, [], mods_list("modules08", mod_base_dir))

        sio = StringIO.StringIO("Hubbel: bubbel\nSiebel: do")
        req = Requirement(sio, "InvalidTagReq", None, mods, TestConfig())

        reqs = RequirementSet(mods, None)
        reqs.add_req(req)
        reqs.handle_modules()

        #o = StringIO.StringIO()
        #reqs.write_log(o)
        #print("HHHHHHHHHHH %s" % o.getvalue())

        assert(reqs.mls() == MemLogStore.create_mls(
                [[57, LogLevel.error(), "No tag handler found for tag(s) "
                  "'['Siebel', 'Hubbel']' - Hint: typo in tag(s)?",
                  'InvalidTagReq'],
                 [56, LogLevel.error(), "There were errors encountered during "
                  "parsing and checking - can't continue"]]))
