#
# Digraph Pyhton library
#
# Unit tests for strongly connected components
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

import unittest

from Digraph import Digraph
from StronglyConnectedComponents import strongly_connected_components
from Helper import node_sl_to_node_name_sl

class SCCTests(unittest.TestCase):

    def test_scc_001(self):
        "Simple two node digraph with one scc"
        dg = Digraph( {"A": ["B"], "B": ["A"] } )
        sccs = strongly_connected_components(dg)
        sccsnames = node_sl_to_node_name_sl(sccs)
        self.assertEqual(sccsnames, [set(['A', 'B'])], "incorrect")

    def test_tsort_002(self):
        "Simple two node digraph with no scc"
        dg = Digraph( {"A": ["B"], "B": [] } )
        sccs = strongly_connected_components(dg)
        sccsnames = node_sl_to_node_name_sl(sccs)
        self.assertEqual(sccsnames, [set(['B']), set(['A'])], "incorrect")

    def test_tsort_003(self):
        "Simple three node digraph with one scc and an extra node"
        dg = Digraph( {"A": ["B", "C"], "B": ["A"], "C": [] } )
        sccs = strongly_connected_components(dg)
        sccsnames = node_sl_to_node_name_sl(sccs)
        self.assertEqual(sccsnames, [set(['C']), set(['A', 'B'])], "incorrect")

    def test_tsort_004(self):
        "Simple three node digraph with one scc I"
        dg = Digraph( {"A": ["B", "C"], "B": ["A"], "C": ["A"] } )
        sccs = strongly_connected_components(dg)
        sccsnames = node_sl_to_node_name_sl(sccs)
        self.assertEqual(sccsnames, [set(['A', 'C', 'B'])], "incorrect")

    def test_tsort_005(self):
        "Simple three node digraph with one scc II"
        dg = Digraph( {"A": ["B", "C"], "B": ["A"], "C": ["B"] } )
        sccs = strongly_connected_components(dg)
        sccsnames = node_sl_to_node_name_sl(sccs)
        self.assertEqual(sccsnames, [set(['A', 'C', 'B'])], "incorrect")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SCCTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
