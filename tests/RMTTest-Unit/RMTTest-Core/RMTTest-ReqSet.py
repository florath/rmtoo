'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for RequirementSet

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals

import re
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


from rmtoo.lib.RequirementSet import RequirementSet
from rmtoo.lib.InputModules import InputModules
from rmtoo.lib.Requirement import Requirement
from TestConfig import TestConfig
from rmtoo.lib.logging import init_logger, tear_down_log_handler
from Utils import hide_volatile


class RMTTestReqSet(object):
    """Test cases for Requirment Set"""

    def rmttest_positive_01(self):
        """Requirement contains a tag where no handler exists"""
        mstderr = StringIO()
        init_logger(mstderr)

        test_config = TestConfig()
        test_config.set_solved_by()
        mods = InputModules(test_config)

        reqs = RequirementSet(None)
        req = Requirement("Hubbel: bubbel", "hubbel",
                          reqs, mods, test_config)
        reqs.add_requirement(req)
        reqs._handle_modules(mods)

        lstderr = hide_volatile(mstderr.getvalue())
        tear_down_log_handler()
        result_expected \
            = ["===DATETIMESTAMP===;rmtoo;ERROR;RequirementSet;"
               "__all_tags_handled;===LINENO===; 57:hubbel:No tag handler "
               "found for "
               "tag(s) '[\"Hubbel\"]' - Hint: typo in tag(s)?",
               "===DATETIMESTAMP===;rmtoo;ERROR;"
               "RequirementSet;_handle_modules;"
               "===LINENO===; 56:There were errors encountered during parsing "
               "and checking - can't continue."]

        lstderr_last_two_lines = lstderr.split("\n")[-3:-1]

        assert result_expected == lstderr_last_two_lines

    def rmttest_positive_02(self):
        "Requirement contains a tag where no handler exists - multiple tags"
        mstderr = StringIO()
        init_logger(mstderr)

        tc = TestConfig()
        tc.set_solved_by()
        mods = InputModules(tc)

        reqs = RequirementSet(None)
        req = Requirement("Hubbel: bubbel\nSiebel: do", "InvalidTagReq",
                          reqs, mods, tc)
        reqs.add_requirement(req)
        reqs._handle_modules(mods)

        lstderr = hide_volatile(mstderr.getvalue())
        tear_down_log_handler()

        lstderr_last_two_lines = lstderr.split("\n")[-3:-1]

        result0 \
            = re.match(
                r"^===DATETIMESTAMP===;rmtoo;ERROR;RequirementSet;"
                r"__all_tags_handled;===LINENO===; 57:InvalidTagReq:"
                r"No tag handler found "
                r"for tag\(s\) '\[.*\]' - Hint: typo in tag\(s\)\?$",
                lstderr_last_two_lines[0])
        result1 \
            = re.match(
                r"^===DATETIMESTAMP===;rmtoo;ERROR;RequirementSet;"
                "_handle_modules;"
                "===LINENO===; 56:There were errors encountered "
                "during parsing "
                "and checking - can't continue.$",
                lstderr_last_two_lines[1])

        assert result0
        assert result1
