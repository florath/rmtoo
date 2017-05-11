'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit tests for connected components

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
import unittest

from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.digraph.ConnectedComponents \
    import connected_components, ConnectedComponents


class CCTest(unittest.TestCase):
    """Tests for Connected Component"""

    def rmttest_cc_001(self):
        "Connected digraph"
        digraph = Digraph({"A": ["B"], "B": ["C"], "C": []})
        ccs = connected_components(digraph)
        self.assertEqual(1, ccs.get_length())

    def rmttest_cc_002(self):
        "Not connected digraph"
        digraph = Digraph({"A": ["B"], "B": ["C"], "C": [],
                           "D": ["E"], "E": []})
        ccs = connected_components(digraph)
        self.assertTrue(ccs.get_length() > 1)

    def rmttest_cc_003(self):
        "digraph connected_component: check for not found node exception"

        ccc = ConnectedComponents()

        with self.assertRaises(RMTException) as rmte:
            ccc.find(None)
            self.assertEqual(68, rmte.get_id())
