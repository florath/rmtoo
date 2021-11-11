'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for Effort Estimation

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals


from rmtoo.lib.Encoding import Encoding
from rmtoo.inputs.ReqEffortEst import ReqEffortEst
from rmtoo.lib.RMTException import RMTException
from ReqTag import create_parameters
from rmtoo.lib.storagebackend.RecordEntry import RecordEntry
import pytest


class RMTTestReqClass(object):

    def rmttest_positive_01(self):
        "Requirement Tag Effort Estimation - no tag given"
        config, req = create_parameters()

        rt = ReqEffortEst(config)
        name, value = rt.rewrite("EffortEstimation-test", req)
        assert "Effort estimation" == name
        assert value is None

    def rmttest_positive_02(self):
        "Requirement Tag Effort Estimation - tag given with all valid numbers"
        config, req = create_parameters()

        for i in ReqEffortEst.valid_values:
            req["Effort estimation"] = RecordEntry("Effort estimation",
                                                   Encoding.to_unicode(i))
            rt = ReqEffortEst(config)
            name, value = rt.rewrite("EffortEstimation-test", req)
            assert "Effort estimation" == name
            assert i == value

    def rmttest_negative_01(self):
        "Requirement Tag Effort Estimation - tag given with invalid numbers"
        config, req = create_parameters()

        for i in [4, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 22,
                  23, 24, 25, 26, 27, 28, 29, 30, 31, 32]:
            req["Effort estimation"] = RecordEntry("Effort estimation",
                                                   Encoding.to_unicode(i))
            rt = ReqEffortEst(config)

            with pytest.raises(RMTException) as rmte:
                rt.rewrite("EffortEstimation-test", req)
                assert 4 == rmte.id()
