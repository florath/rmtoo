'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for RequirementSet

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals

import os
import re
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
import unittest

from rmtoo.lib.RequirementSet import RequirementSet
from rmtoo.lib.InputModules import InputModules
from rmtoo.lib.Requirement import Requirement
from rmtoo.tests.lib.ModuleHelper import mods_list
from rmtoo.tests.lib.TestConfig import TestConfig
from rmtoo.lib.logging import init_logger, tear_down_log_handler
from rmtoo.tests.lib.Utils import hide_volatile


mod_base_dir = "tests/RMTTest-Unit/RMTTest-Core/testdata"


class RMTTestReqSet(unittest.TestCase):

    def rmttest_positive_01(self):
        "Requirement contains a tag where no handler exists"
        self.maxDiff = 1000
        mstderr = StringIO()
        init_logger(mstderr)

        mods = InputModules(os.path.join(mod_base_dir, "modules08"),
                            {}, [], mods_list("modules08", mod_base_dir))

        reqs = RequirementSet(None)
        req = Requirement("Hubbel: bubbel", "hubbel",
                          reqs, mods, TestConfig())
        reqs._add_requirement(req)
        reqs.nodes.append(req)
        reqs._handle_modules(mods)

        lstderr = hide_volatile(mstderr.getvalue())
        tear_down_log_handler()
        result_expected \
            = "===DATETIMESTAMP===;rmtoo;ERROR;RequirementSet;" \
            "__all_tags_handled;===LINENO===; 57:hubbel:No tag handler " \
            "found for " \
            "tag(s) '[\"Hubbel\"]' - Hint: typo in tag(s)?\n" \
            "===DATETIMESTAMP===;rmtoo;ERROR;RequirementSet;_handle_modules;" \
            "===LINENO===; 56:There were errors encountered during parsing " \
            "and checking - can't continue.\n"

        self.assertEquals(result_expected, lstderr)

    def rmttest_positive_02(self):
        "Requirement contains a tag where no handler exists - multiple tags"
        mstderr = StringIO()
        init_logger(mstderr)

        mods = InputModules(os.path.join(mod_base_dir, "modules08"),
                            {}, [], mods_list("modules08", mod_base_dir))

        reqs = RequirementSet(None)
        req = Requirement("Hubbel: bubbel\nSiebel: do", "InvalidTagReq",
                          reqs, mods, TestConfig())
        reqs._add_requirement(req)
        reqs.nodes.append(req)
        reqs._handle_modules(mods)

        lstderr = hide_volatile(mstderr.getvalue())
        tear_down_log_handler()
        result \
            = re.match(
                "^===DATETIMESTAMP===;rmtoo;ERROR;RequirementSet;"
                "__all_tags_handled;===LINENO===; 57:InvalidTagReq:"
                "No tag handler found "
                "for tag\(s\) '\[.*\]' - Hint: typo in tag\(s\)\?\n"
                "===DATETIMESTAMP===;rmtoo;ERROR;RequirementSet;"
                "_handle_modules;"
                "===LINENO===; 56:There were errors encountered "
                "during parsing "
                "and checking - can't continue.\n$", lstderr)

        self.assertTrue(result)
