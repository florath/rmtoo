'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Unit tests for connected components
   
 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import unittest

from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.digraph.ConnectedComponents \
    import connected_components, CC_Components

class CCTest(unittest.TestCase):

    def test_cc_001(self):
        "Connected digraph"
        dg = Digraph({"A": ["B"], "B": ["C"], "C": [] })
        ccs = connected_components(dg)
        assert(ccs.len() == 1)

    def test_cc_002(self):
        "Not connected digraph"
        dg = Digraph({"A": ["B"], "B": ["C"], "C": [],
                       "D": ["E"], "E": [] })
        ccs = connected_components(dg)
        assert(ccs.len() > 1)

    def test_cc_003(self):
        "digraph connected_component: check for not found node exception"

        ccc = CC_Components()
        try:
            ccc.find(None)
            assert(False)
        except RMTException, rmte:
            assert(rmte.id() == 68)


