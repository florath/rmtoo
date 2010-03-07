#
# Requirement Management Toolset
#
# Unit test for RDepDependsOn
#
# (c) 2010 on flonatel
#
# For licencing details see COPYING
#

from rmtoo.tests.lib.RDep import create_parameters
from rmtoo.tests.lib.RDep import TestReq
from rmtoo.modules.RDepDependsOn import RDepDependsOn
from rmtoo.lib.Requirement import Requirement

class TestRDepDependsOn:

    def test_positive_01(self):
        "Two node one edge digraph B -> A"
        opts, config, reqset = create_parameters()
        reqset.reqs = {
            "A": TestReq("A",
                         {"Type": Requirement.rt_master_requirement},
                         {}),
            "B": TestReq("B",
                         {"Type": Requirement.rt_initial_requirement},
                         {"Depends on": "A"})}

        rdep = RDepDependsOn(opts, config)
        rdep.rewrite(reqset)
        
        assert(reqset.reqs["A"].outgoing_as_named_list()==[])
        assert(reqset.reqs["A"].incoming_as_named_list()==["B"])
        assert(reqset.reqs["B"].outgoing_as_named_list()==["A"])
        assert(reqset.reqs["B"].incoming_as_named_list()==[])

    def test_positive_02(self):
        "Three node one edge digraph B -> A, C -> A and C -> B"
        opts, config, reqset = create_parameters()
        reqset.reqs = {
            "A": TestReq("A",
                         {"Type": Requirement.rt_master_requirement},
                         {}),
            "B": TestReq("B",
                         {"Type": Requirement.rt_initial_requirement},
                         {"Depends on": "A"}),
            "C": TestReq("C",
                         {"Type": Requirement.rt_requirement},
                         {"Depends on": "A B"}),
            }

        rdep = RDepDependsOn(opts, config)
        rdep.rewrite(reqset)
        
        assert(reqset.reqs["A"].outgoing_as_named_list()==[])
        assert(reqset.reqs["A"].incoming_as_named_list()==["C", "B"])
        assert(reqset.reqs["B"].outgoing_as_named_list()==["A"])
        assert(reqset.reqs["B"].incoming_as_named_list()==["C"])
        assert(reqset.reqs["C"].outgoing_as_named_list()==["A", "B"])
        assert(reqset.reqs["C"].incoming_as_named_list()==[])
