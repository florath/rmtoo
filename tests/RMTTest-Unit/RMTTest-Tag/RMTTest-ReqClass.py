'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for ReqClass

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals


from rmtoo.inputs.ReqClass import ReqClass
from rmtoo.lib.RMTException import RMTException
from ReqTag import create_parameters
from rmtoo.lib.storagebackend.RecordEntry import RecordEntry
from rmtoo.lib.ClassType import ClassTypeDetailable, ClassTypeImplementable


class RMTTestReqClass(object):

    def rmttest_positive_01(self):
        "Requirement Tag Class - no Class tag given"
        config, req = create_parameters()

        rt = ReqClass(config)
        name, value = rt.rewrite("Class-test", req)
        assert "Class" == name
        assert isinstance(value, ClassTypeDetailable)

    def rmttest_positive_02(self):
        "Requirement Tag Class - Class set to 'detailable'"
        config, req = create_parameters()
        req = {"Class": RecordEntry("Class", "detailable")}

        rt = ReqClass(config)
        name, value = rt.rewrite("Class-test", req)
        assert "Class" == name
        assert isinstance(value, ClassTypeDetailable)

    def rmttest_positive_03(self):
        "Requirement Tag Class - no Class implementable"
        config, req = create_parameters()
        req = {"Class": RecordEntry("Class", "implementable")}

        rt = ReqClass(config)
        name, value = rt.rewrite("Class-test", req)
        assert "Class" == name
        assert isinstance(value, ClassTypeImplementable)

    def rmttest_negative_01(self):
        "Requirement Tag Class - unsupported Class value"
        config, req = create_parameters()
        req = {"Class": RecordEntry("Class", "something_completly_different")}

        rt = ReqClass(config)
        try:
            name, value = rt.rewrite("Class-test", req)
            assert False
        except RMTException as rmte:
            assert 95 == rmte.get_id()
