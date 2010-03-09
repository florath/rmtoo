#
# Generic Tag Class
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.ReqTagGeneric import ReqTagGeneric

class MyTag(ReqTagGeneric):
    tag="mytag"

    def __init__(self, opts, config):
        ReqTagGeneric.__init__(self, opts, config)

    
class TestGenericTag:

    def test_positive_01(self):
        "Generic Tag: construction"
        mt = MyTag(None, None)

    def test_positive_02(self):
        "Generic Tag: type()"
        mt = MyTag(None, None)
        t = mt.type()
        assert(t=="reqtag")

    def test_positive_03(self):
        "Generic Tag: mandatory tag"
        mt = MyTag(None, None)

        rid = "Generic-Test-Id"
        r = {"mytag": "some value"}
        eid = None
        mt.check_mandatory_tag(rid, r, eid)

    def test_positive_04(self):
        "Generic Tag: optional tag (available)"
        mt = MyTag(None, None)

        r = {"mytag": "some value"}
        tag, v = mt.handle_optional_tag(r)

        assert(tag=="mytag")
        assert(v=="some value")

    def test_positive_05(self):
        "Generic Tag: optional tag (not available)"
        mt = MyTag(None, None)

        r = {"notmytag": "some value"}
        tag, v = mt.handle_optional_tag(r)

        assert(tag=="mytag")
        assert(v==None)

    def test_negative_01(self):
        "Generic Tag: mandatory tag not available"
        mt = MyTag(None, None)

        rid = "Generic-Test-Id"
        r = {"notmytag": "some value"}
        eid = 112
        try:
            mt.check_mandatory_tag(rid, r, eid)
            assert(False)
        except RMTException, rmte:
            assert(rmte.eid==112)

