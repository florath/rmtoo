'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Test case for handling BaseRMObjects

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals


try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from rmtoo.lib.BaseRMObject import BaseRMObject
from TestConfig import TestConfig
from rmtoo.lib.logging import init_logger, tear_down_log_handler
from Utils import hide_volatile


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
        BaseRMObject.__init__(self, u"mytag", u"", u"MRid", tm,
                              tc, u"tobjs", None)


expected_result = \
    "===DATETIMESTAMP===;rmtoo;ERROR;BaseRMObject;handle_modules_tag;" \
    "===LINENO===; 90:Wrong module type [mytag] not in [[1, 2, 3]]\n"


class RMTTestBaseRMObject(object):

    def rmttest_neg_01(self):
        "BaseRMObject: check for module which has wrong type"

        mstderr = StringIO()
        init_logger(mstderr)

        TBRMObj()

        result = hide_volatile(mstderr.getvalue())
        tear_down_log_handler()

        assert expected_result == result
