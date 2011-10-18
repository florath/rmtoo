#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# Unit test for RDepSolvedBy
#
# (c) 2011 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.tests.lib.RDep import create_parameters
from rmtoo.tests.lib.RDep import TestReq
from rmtoo.modules.RDepSolvedBy import RDepSolvedBy
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.MemLogStore import MemLogStore, MemLog
from rmtoo.lib.storagebackend.RecordEntry import RecordEntry

class TestRDepSolvedBy:

    def test_negative_01(self):
        "Two nodes as master requirement"
        config, reqset = create_parameters()
        reqset.reqs = {
            "A": TestReq("A",
                         {"Type": Requirement.rt_master_requirement},
                         {}),
            "B": TestReq("B",
                         {"Type": Requirement.rt_master_requirement},
                         {})}

        config.set_solved_by()
        rdep = RDepSolvedBy(config)
        status = rdep.rewrite(reqset)
        assert(status == False)
        assert(reqset.mls() == MemLogStore.create_mls(
                [ [76, MemLog.error, "Another master is already there. "
                   "There can only be one.", "B"] ]))

    def test_negative_02(self):
        "Normal requirement has empty 'Solved by'"
        config, reqset = create_parameters()
        reqset.reqs = {
            "A": TestReq("A",
                         {"Type": Requirement.rt_master_requirement},
                         {}),
            "B": TestReq("B",
                         {"Type": Requirement.rt_requirement},
                         {"Solved by": RecordEntry("Solved by", "")})}

        config.set_solved_by()
        rdep = RDepSolvedBy(config)
        status = rdep.rewrite(reqset)

        assert(status == False)
        assert(reqset.mls() == MemLogStore.create_mls(
                [ [77, MemLog.error, "'Solved by' field has len 0", "B"] ]))

    def test_negative_03(self):
        "'Solved by' points to a non existing requirement"
        config, reqset = create_parameters()
        reqset.reqs = {
            "A": TestReq("A",
                         {"Type": Requirement.rt_master_requirement},
                         {}),
            "B": TestReq("B",
                         {"Type": Requirement.rt_requirement},
                         {"Solved by": RecordEntry("Solved by", "C")})}

        config.set_solved_by()
        rdep = RDepSolvedBy(config)
        status = rdep.rewrite(reqset)

        assert(status == False)
        assert(reqset.mls() == MemLogStore.create_mls(
                [[74, MemLog.error, "'Solved by' points to a non-existing "
                  "requirement 'C'", "B" ], ]))

    def test_negative_04(self):
        "'Solved by' points to same requirement"
        config, reqset = create_parameters()
        reqset.reqs = {
            "A": TestReq("A",
                         {"Type": Requirement.rt_master_requirement},
                         {}),
            "B": TestReq("B",
                         {"Type": Requirement.rt_requirement},
                         {"Solved by": RecordEntry("Solved by", "B")})}

        config.set_solved_by()
        rdep = RDepSolvedBy(config)
        status = rdep.rewrite(reqset)

        assert(status == False)
        assert(reqset.mls() == MemLogStore.create_mls(
                [[75, MemLog.error, "'Solved by' points to the requirement "
                  "itself", "B" ], ]))

    def test_negative_05(self):
        "Set without any master requirement"
        config, reqset = create_parameters()
        reqset.reqs = {
            "A": TestReq("A",
                         {"Type": Requirement.rt_requirement},
                         {"Solved by": RecordEntry("Solved by", "B")}),
            "B": TestReq("B",
                         {"Type": Requirement.rt_requirement},
                         {"Solved by": RecordEntry("Solved by", "A")})}

        config.set_solved_by()
        rdep = RDepSolvedBy(config)
        status = rdep.rewrite(reqset)

        assert(status == False)
        assert(reqset.mls() == MemLogStore.create_mls(
                [[78, MemLog.error, "no master requirement found"], ]))
