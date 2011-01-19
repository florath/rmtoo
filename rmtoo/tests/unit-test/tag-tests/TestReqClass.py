#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# Unit test for ReqClass
#
# (c) 2010-2011 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.modules.ReqClass import ReqClass
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RMTException import RMTException
from rmtoo.tests.lib.ReqTag import create_parameters
from rmtoo.lib.storagebackend.RecordEntry import RecordEntry

class TestReqClass:

    def test_positive_01(self):
        "Requirement Tag Class - no Class tag given"
        opts, config, req = create_parameters()

        rt = ReqClass(opts, config)
        name, value = rt.rewrite("Class-test", req)
        assert(name=="Class")
        assert(value==Requirement.ct_detailable)

    def test_positive_02(self):
        "Requirement Tag Class - Class set to 'detailable'"
        opts, config, req = create_parameters()
        req = {"Class": RecordEntry("Class", "detailable")}

        rt = ReqClass(opts, config)
        name, value = rt.rewrite("Class-test", req)
        assert(name=="Class")
        assert(value==Requirement.ct_detailable)

    def test_positive_03(self):
        "Requirement Tag Class - no Class implementable"
        opts, config, req = create_parameters()
        req = {"Class": RecordEntry("Class", "implementable")}

        rt = ReqClass(opts, config)
        name, value = rt.rewrite("Class-test", req)
        assert(name=="Class")
        assert(value==Requirement.ct_implementable)

    def test_negative_01(self):
        "Requirement Tag Class - unsupported Class value"
        opts, config, req = create_parameters()
        req = {"Class": RecordEntry("Class", "something_completly_different")}

        rt = ReqClass(opts, config)
        try:
            name, value = rt.rewrite("Class-test", req)
            assert(False)
        except RMTException, rmte:
            assert(rmte.id()==1)
