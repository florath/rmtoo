'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Unit test for RDepSolvedBy
   
 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import unittest
import StringIO
from rmtoo.tests.lib.RDep import create_parameters
from rmtoo.tests.lib.RDep import TestReq
from rmtoo.inputs.RDepSolvedBy import RDepSolvedBy
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RequirementDNode import RequirementDNode
from rmtoo.lib.RequirementSet import RequirementSet
from rmtoo.lib.storagebackend.RecordEntry import RecordEntry
from rmtoo.lib.logging.MemLog import MemLog
from rmtoo.tests.lib.TestConfig import TestConfig
from rmtoo.lib.logging import init_logger, tear_down_log_handler
from rmtoo.tests.lib.Utils import hide_timestamp, hide_lineno

class TestRDepSolvedBy(unittest.TestCase):

    def test_neg_empty_solved_by(self):
        "Normal requirement has empty 'Solved by'"
        mstderr = StringIO.StringIO()
        init_logger(mstderr)

        config = TestConfig()
        reqset = RequirementSet(config)
        req1 = Requirement('''Name: A
Type: master requirement''', 'A', None, None, None)
        reqset.add_node(RequirementDNode(req1))
        req2 = Requirement('''Name: B
Type: requirement
Solved by:''', 'B', None, None, None)
        reqset.add_node(RequirementDNode(req2))
        config.set_solved_by()
        rdep = RDepSolvedBy(config)
        status = rdep.rewrite(reqset)

        self.assertFalse(status)
        lstderr = hide_lineno(hide_timestamp(mstderr.getvalue()))
        tear_down_log_handler()
        result_expected = "===DATETIMESTAMP===;rmtoo;ERROR;RequirementSet;" \
        "__resolve_solved_by_one_req;===SOURCELINENO===; 77:B:'Solved by' " \
        "field has length 0\n"
        self.assertEquals(result_expected, lstderr)

    def test_neg_solved_by_to_nonex_req(self):
        "'Solved by' points to a non existing requirement"
        mstderr = StringIO.StringIO()
        init_logger(mstderr)

        config = TestConfig()
        reqset = RequirementSet(config)
        req1 = Requirement('''Name: A
Type: master requirement''', 'A', None, None, None)
        reqset.add_node(RequirementDNode(req1))
        req2 = Requirement('''Name: B
Type: requirement
Solved by: C''', 'B', None, None, None)
        reqset.add_node(RequirementDNode(req2))

        config.set_solved_by()
        rdep = RDepSolvedBy(config)
        status = rdep.rewrite(reqset)

        self.assertFalse(status)
        lstderr = hide_lineno(hide_timestamp(mstderr.getvalue()))
        tear_down_log_handler()
        result_expected = "===DATETIMESTAMP===;rmtoo;ERROR;RequirementSet;" \
        "__resolve_solved_by_one_req;===SOURCELINENO===; 74:B:'Solved by' " \
        "points to a non-existing requirement 'C'\n"
        self.assertEquals(result_expected, lstderr)

    def test_neg_point_to_self(self):
        "'Solved by' points to same requirement"
        mstderr = StringIO.StringIO()
        init_logger(mstderr)

        config = TestConfig()
        reqset = RequirementSet(config)
        req1 = Requirement('''Name: A
Type: master requirement''', 'A', None, None, None)
        reqset.add_node(RequirementDNode(req1))
        req2 = Requirement('''Name: B
Type: requirement
Solved by: B''', 'B', None, None, None)
        reqset.add_node(RequirementDNode(req2))
        config.set_solved_by()
        rdep = RDepSolvedBy(config)
        status = rdep.rewrite(reqset)

        self.assertFalse(status)
        lstderr = hide_lineno(hide_timestamp(mstderr.getvalue()))
        tear_down_log_handler()
        result_expected = "===DATETIMESTAMP===;rmtoo;ERROR;RequirementSet;" \
        "__resolve_solved_by_one_req;===SOURCELINENO===; 75:B:'Solved by' " \
        "points to the requirement itself\n"
        self.assertEquals(result_expected, lstderr)
#        assert(reqset.to_list() ==
#                [[75, LogLevel.error(), "'Solved by' points to the requirement "
#                  "itself", "B" ], ])
