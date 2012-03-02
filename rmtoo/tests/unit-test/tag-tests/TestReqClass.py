'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Unit test for ReqClass
   
 (c) 2010-2012 by flonatel GmhH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.inputs.ReqClass import ReqClass
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RMTException import RMTException
from rmtoo.tests.lib.ReqTag import create_parameters
from rmtoo.lib.storagebackend.RecordEntry import RecordEntry
from rmtoo.lib.ClassType import ClassTypeImplementable, \
    ClassTypeDetailable, ClassTypeSelected

class TestReqClass:

    def test_positive_01(self):
        "Requirement Tag Class - no Class tag given"
        config, req = create_parameters()

        rt = ReqClass(config)
        name, value = rt.rewrite("Class-test", req)
        assert(name == "Class")
        assert(isinstance(value, ClassTypeDetailable))

    def test_positive_02(self):
        "Requirement Tag Class - Class set to 'detailable'"
        config, req = create_parameters()
        req = {"Class": RecordEntry("Class", "detailable")}

        rt = ReqClass(config)
        name, value = rt.rewrite("Class-test", req)
        assert(name == "Class")
        assert(isinstance(value, ClassTypeDetailable))

    def test_positive_03(self):
        "Requirement Tag Class - no Class implementable"
        config, req = create_parameters()
        req = {"Class": RecordEntry("Class", "implementable")}

        rt = ReqClass(config)
        name, value = rt.rewrite("Class-test", req)
        assert(name == "Class")
        assert(isinstance(value, ClassTypeImplementable))

    def test_negative_01(self):
        "Requirement Tag Class - unsupported Class value"
        config, req = create_parameters()
        req = {"Class": RecordEntry("Class", "something_completly_different")}

        rt = ReqClass(config)
        try:
            name, value = rt.rewrite("Class-test", req)
            assert(False)
        except RMTException, rmte:
            assert(rmte.get_id() == 95)
