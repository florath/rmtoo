#
# Requirement Management Toolset
#
# Unit test for Effort Estimation
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.modules.ReqEffortEst import ReqEffortEst
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RMTException import RMTException
from rmtoo.tests.lib.ReqTag import create_parameters

class TestReqClass:

    def test_positive_01(self):
        "Requirement Tag Effort Estimation - no tag given"
        opts, config, req = create_parameters()

        rt = ReqEffortEst(opts, config)
        name, value = rt.rewrite("EffortEstimation-test", req)
        assert(name=="Effort estimation")
        assert(value==None)

    def test_positive_02(self):
        "Requirement Tag Effort Estimation - tag given with all valid numbers"
        opts, config, req = create_parameters()

        for i in ReqEffortEst.valid_values:
            req["Effort estimation"] = str(i)
            rt = ReqEffortEst(opts, config)
            name, value = rt.rewrite("EffortEstimation-test", req)
            assert(name=="Effort estimation")
            assert(value==i)

    def test_negative_01(self):
        "Requirement Tag Effort Estimation - tag given with invalid numbers"
        opts, config, req = create_parameters()

        for i in [4, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 22,
                  23, 24, 25, 26, 27, 28, 29, 30, 31, 32]:
            req["Effort estimation"] = str(i)
            rt = ReqEffortEst(opts, config)
            try:
                name, value = rt.rewrite("EffortEstimation-test", req)
                assert(False)
            except RMTException, rmte:
                assert(rmte.eid==4)
