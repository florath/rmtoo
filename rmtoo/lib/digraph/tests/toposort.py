#
# Digraph Pyhton library
#
# Unit tests for tolological search
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

import unittest

from Digraph import Digraph
from TopologicalSort import topological_sort
from Helper import node_list_to_node_name_list

class TopologicalSearchTests(unittest.TestCase):

    def test_tsort_001(self):
        "Simple three node digraph"
        dg = Digraph( {"A": ["B", "C"], "B": ["C"], "C": [] } )
        tsort = topological_sort(dg)
        tnames = node_list_to_node_name_list(tsort)
        self.assertEqual(tnames, ['C', 'B', 'A'], "incorrect")

    def test_tsort_002(self):
        "Zero node digraph"
        dg = Digraph( {} )
        tsort = topological_sort(dg)
        tnames = node_list_to_node_name_list(tsort)
        self.assertEqual(tnames, [], "incorrect")

    def test_tsort_003(self):
        "One node digraph"
        dg = Digraph( {"A": [] } )
        tsort = topological_sort(dg)
        tnames = node_list_to_node_name_list(tsort)
        self.assertEqual(tnames, ["A"], "incorrect")

    def test_tsort_004(self):
        "More complex digraph"
        dg = Digraph( {"A": ["B", "C"], "B": ["C", "E"], "C": ["D", "E"],
                       "D": [], "E": [] } )
        tsort = topological_sort(dg)
        tnames = node_list_to_node_name_list(tsort)
        self.assertEqual(tnames, ['D', 'E', 'C', 'B', 'A'], "incorrect")

    def test_tsort_005(self):
        "Digraph with two components"
        dg = Digraph( {"A": ["B", "C"], "B": ["C"], "C": [],
                       "D": ["E"], "E": [] } )
        tsort = topological_sort(dg)
        tnames = node_list_to_node_name_list(tsort)
        self.assertEqual(tnames, ['C', 'B', 'A', 'E', 'D'], "incorrect")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TopologicalSearchTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
