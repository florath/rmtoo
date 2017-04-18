'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for input modules

 (c) 2010,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
import unittest

from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.ReqTagGeneric import ReqTagGeneric
from rmtoo.lib.InputModuleTypes import InputModuleTypes


class MyTag(ReqTagGeneric):

    def __init__(self, config):
        ReqTagGeneric.__init__(self, config, "mytag",
                               set([InputModuleTypes.reqtag, ]))


class RMTTest_GenericTag(unittest.TestCase):

    def rmttest_positive_01(self):
        "Generic Tag: construction"
        MyTag(None)

    def rmttest_positive_02(self):
        "Generic Tag: type()"
        mt = MyTag(None)
        t = mt.get_type_set()
        assert(t == set([InputModuleTypes.reqtag, ]))

    def rmttest_positive_03(self):
        "Generic Tag: mandatory tag"
        mt = MyTag(None)

        rid = "Generic-Test-Id"
        r = {"mytag": "some value"}
        eid = None
        mt.check_mandatory_tag(rid, r, eid)

    def rmttest_positive_04(self):
        "Generic Tag: optional tag (available)"
        mt = MyTag(None)

        r = {"mytag": "some value"}
        tag, v = mt.handle_optional_tag(r)

        assert(tag == "mytag")
        assert(v == "some value")

    def rmttest_positive_05(self):
        "Generic Tag: optional tag (not available)"
        mt = MyTag(None)

        r = {"notmytag": "some value"}
        tag, v = mt.handle_optional_tag(r)

        assert(tag == "mytag")
        self.assertIsNone(v)

    def rmttest_negative_01(self):
        "Generic Tag: mandatory tag not available"
        mt = MyTag(None)

        rid = "Generic-Test-Id"
        r = {"notmytag": "some value"}
        eid = 112
        try:
            mt.check_mandatory_tag(rid, r, eid)
            assert(False)
        except RMTException as rmte:
            assert(rmte.id() == 112)
