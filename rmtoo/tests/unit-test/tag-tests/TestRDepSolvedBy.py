'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Unit test for RDepSolvedBy
   
 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.tests.lib.RDep import create_parameters
from rmtoo.tests.lib.RDep import TestReq
from rmtoo.inputs.RDepSolvedBy import RDepSolvedBy
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RequirementSet import RequirementSet
from rmtoo.lib.storagebackend.RecordEntry import RecordEntry
from rmtoo.lib.logging.MemLogStore import MemLogStore
from rmtoo.lib.logging.MemLog import MemLog
from rmtoo.lib.logging.LogLevel import LogLevel
from rmtoo.tests.lib.TestConfig import TestConfig

class TestRDepSolvedBy:

    def test_neg_empty_solved_by(self):
        "Normal requirement has empty 'Solved by'"
        config = TestConfig()
        reqset = RequirementSet(config)
        req1 = Requirement('''Name: A
Type: master requirement''', 'A', None, None, None, None)
        reqset._add_requirement(req1)
        req2 = Requirement('''Name: B
Type: requirement
Solved by:''', 'B', None, None, None, None)
        reqset._add_requirement(req2)
        config.set_solved_by()
        rdep = RDepSolvedBy(config)
        status = rdep.rewrite(reqset)

        assert(status == False)
        assert(reqset.to_list() ==
                [ [77, LogLevel.error(), "'Solved by' field has length 0", "B"] ])

    def test_neg_solved_by_to_nonex_req(self):
        "'Solved by' points to a non existing requirement"
        config = TestConfig()
        reqset = RequirementSet(config)
        req1 = Requirement('''Name: A
Type: master requirement''', 'A', None, None, None, None)
        reqset._add_requirement(req1)
        req2 = Requirement('''Name: B
Type: requirement
Solved by: C''', 'B', None, None, None, None)
        reqset._add_requirement(req2)

        config.set_solved_by()
        rdep = RDepSolvedBy(config)
        status = rdep.rewrite(reqset)

        assert(status == False)
        assert(reqset.to_list() ==
                [[74, LogLevel.error(), "'Solved by' points to a non-existing "
                  "requirement 'C'", "B" ], ])

    def test_neg_point_to_self(self):
        "'Solved by' points to same requirement"
        config = TestConfig()
        reqset = RequirementSet(config)
        req1 = Requirement('''Name: A
Type: master requirement''', 'A', None, None, None, None)
        reqset._add_requirement(req1)
        req2 = Requirement('''Name: B
Type: requirement
Solved by: B''', 'B', None, None, None, None)
        reqset._add_requirement(req2)
        config.set_solved_by()
        rdep = RDepSolvedBy(config)
        status = rdep.rewrite(reqset)

        assert(status == False)
        assert(reqset.to_list() ==
                [[75, LogLevel.error(), "'Solved by' points to the requirement "
                  "itself", "B" ], ])
