'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for RDepSolvedBy

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals


try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from rmtoo.inputs.RDepSolvedBy import RDepSolvedBy
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RequirementSet import RequirementSet
from TestConfig import TestConfig
from rmtoo.lib.logging import init_logger, tear_down_log_handler
from Utils import hide_volatile


class RMTTestRDepSolvedBy(object):

    def rmttest_neg_empty_solved_by(self):
        "Normal requirement has empty 'Solved by'"
        mstderr = StringIO()
        init_logger(mstderr)

        config = TestConfig()
        reqset = RequirementSet(config)
        req1 = Requirement('''Name: A
Type: master requirement''', 'A', None, None, None)
        reqset.add_requirement(req1)
        req2 = Requirement('''Name: B
Type: requirement
Solved by:''', 'B', None, None, None)
        reqset.add_requirement(req2)
        config.set_solved_by()
        rdep = RDepSolvedBy(config)
        status = rdep.rewrite(reqset)

        assert not status
        lstderr = hide_volatile(mstderr.getvalue())
        tear_down_log_handler()
        result_expected \
            = "===DATETIMESTAMP===;rmtoo;ERROR;RequirementSet;" \
            "__resolve_solved_by_one_req_deps;===LINENO===; " \
            "77:B:'Solved by' field has length 0\n"
        assert result_expected == lstderr

    def rmttest_neg_solved_by_to_nonex_req(self):
        "'Solved by' points to a non existing requirement"
        mstderr = StringIO()
        init_logger(mstderr)

        config = TestConfig()
        reqset = RequirementSet(config)
        req1 = Requirement('''Name: A
Type: master requirement''', 'A', None, None, None)
        reqset.add_requirement(req1)
        req2 = Requirement('''Name: B
Type: requirement
Solved by: C''', 'B', None, None, None)
        reqset.add_requirement(req2)

        config.set_solved_by()
        rdep = RDepSolvedBy(config)
        status = rdep.rewrite(reqset)

        assert not status
        lstderr = hide_volatile(mstderr.getvalue())
        tear_down_log_handler()
        result_expected \
            = "===DATETIMESTAMP===;rmtoo;ERROR;RequirementSet;" \
            "__resolve_solved_by_one_req_deps;===LINENO===; " \
            "74:B:'Solved by' points to a non-existing requirement 'C'\n"
        assert result_expected == lstderr

    def rmttest_neg_point_to_self(self):
        "'Solved by' points to same requirement"
        mstderr = StringIO()
        init_logger(mstderr)

        config = TestConfig()
        reqset = RequirementSet(config)
        req1 = Requirement('''Name: A
Type: master requirement''', 'A', None, None, None)
        reqset.add_requirement(req1)
        req2 = Requirement('''Name: B
Type: requirement
Solved by: B''', 'B', None, None, None)
        reqset.add_requirement(req2)
        config.set_solved_by()
        rdep = RDepSolvedBy(config)
        status = rdep.rewrite(reqset)

        assert not status
        lstderr = hide_volatile(mstderr.getvalue())
        tear_down_log_handler()
        result_expected \
            = "===DATETIMESTAMP===;rmtoo;ERROR;RequirementSet;" \
            "__resolve_solved_by_one_req_deps;===LINENO===; " \
            "75:B:'Solved by' points to the requirement itself\n"
        assert result_expected == lstderr
