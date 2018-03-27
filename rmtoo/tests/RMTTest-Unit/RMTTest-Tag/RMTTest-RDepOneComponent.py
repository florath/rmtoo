'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for RequirementSet

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''


from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.inputs.RDepOneComponent import RDepOneComponent
from rmtoo.lib.RMTException import RMTException
import pytest


class RMTTestOutputOneComponent(object):

    def rmttest_neg_01(self):
        "RDepOneComponent: check rewrite error case"

        oc = RDepOneComponent(None)

        dr = Digraph()
        with pytest.raises(RMTException) as rmte:
            oc.rewrite(dr)
            assert 69 == rmte.id()
