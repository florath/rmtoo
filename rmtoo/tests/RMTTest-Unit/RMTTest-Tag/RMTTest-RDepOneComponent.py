'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Unit test for RequirementSet
   
 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.inputs.RDepOneComponent import RDepOneComponent
from rmtoo.lib.RMTException import RMTException

class RMTTest_OutputOneComponent:

    def rmttest_neg_01(self):
        "RDepOneComponent: check rewrite error case"

        oc = RDepOneComponent(None)

        dr = Digraph()
        try:
            oc.rewrite(dr)
            assert(False)
        except RMTException as rmte:
            assert(rmte.id() == 69)

