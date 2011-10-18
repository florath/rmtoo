#
# Requirement Management Toolset
#
#  Unit test for RequirementSet
#
# (c) 2010 on flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.modules.RDepOneComponent import RDepOneComponent
from rmtoo.lib.RMTException import RMTException

class TestOutputOneComponent:

    def test_neg_01(self):
        "RDepOneComponent: check rewrite error case"

        oc = RDepOneComponent(None)

        dr = Digraph()
        try:
            oc.rewrite(dr)
            assert(False)
        except RMTException, rmte:
            assert(rmte.id() == 69)

