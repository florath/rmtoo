'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Test case for handling BaseRMObjects
   
 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import unittest
import StringIO
from rmtoo.lib.BaseRMObject import BaseRMObject
from rmtoo.tests.lib.TestConfig import TestConfig
from rmtoo.lib.logging import init_logger, tear_down_log_handler
from rmtoo.tests.lib.Utils import hide_timestamp, hide_lineno


class TMods:

    def get_type_set(self):
        return set([1, 2, 3])

    def get_tagtype(self, ttype):
        return {"heinzelmann": self}

class TBRMObj(BaseRMObject):

    def __init__(self):
        tc = TestConfig()
        tc.set_value('input.txtfile.whatsoever.max_line_length', 80)
        tm = TMods()
        tm.tagtypes = {"mytag": {"keyA": TMods()}}
        BaseRMObject.__init__(self, "mytag", "", "MRid", tm,
                              tc, "tobjs", None)

expected_result = \
    "===DATETIMESTAMP===;rmtoo;ERROR;BaseRMObject;handle_modules_tag;"\
    "===SOURCELINENO===; " \
    "90:Wrong module type [mytag] not in [set([1, 2, 3])]\n"

class TestBaseRMObject(unittest.TestCase):

    def test_neg_01(self):
        "BaseRMObject: check for module which has wrong type"

        mstderr = StringIO.StringIO()
        init_logger(mstderr)

        tbrmo = TBRMObj()

        result = hide_lineno(hide_timestamp(mstderr.getvalue()))
        tear_down_log_handler()

        self.assertEqual(result, expected_result)
