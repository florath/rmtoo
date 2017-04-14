'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
 Unit tests for tolological search
 
 (c) 2010,2012 by flonatel

 For licensing details see COPYING
'''

import unittest

from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.digraph.TopologicalSort import topological_sort
from rmtoo.lib.digraph.Helper import node_list_to_node_name_list, \
    digraph_create_from_dict

class TopologicalSearchTests(unittest.TestCase):

    def test_tsort_001(self):
        "Simple three node digraph"
        dg = digraph_create_from_dict( {"A": ["B", "C"], "B": ["C"], "C": [] } )
        tsort = topological_sort(dg)
        tnames = node_list_to_node_name_list(tsort)
        self.assertEqual(tnames, ['C', 'B', 'A'], "incorrect")

    def test_tsort_002(self):
        "Zero node digraph"
        dg = digraph_create_from_dict( {} )
        tsort = topological_sort(dg)
        tnames = node_list_to_node_name_list(tsort)
        self.assertEqual(tnames, [], "incorrect")

    def test_tsort_003(self):
        "One node digraph"
        dg = digraph_create_from_dict( {"A": [] } )
        tsort = topological_sort(dg)
        tnames = node_list_to_node_name_list(tsort)
        self.assertEqual(tnames, ["A"], "incorrect")

    def test_tsort_004(self):
        "More complex digraph"
        dg = digraph_create_from_dict( 
                {"A": ["B", "C"], "B": ["C", "E"], "C": ["D", "E"],
                 "D": ["E"], "E": [] } )
        tsort = topological_sort(dg)
        tnames = node_list_to_node_name_list(tsort)        
        self.assertEqual(tnames, ['E', 'D', 'C', 'B', 'A'], "incorrect")

    def test_tsort_005(self):
        "Digraph with two components"
        dg = digraph_create_from_dict( {"A": ["B", "C"], "B": ["C"], "C": [],
                       "D": ["E"], "E": [] } )
        tsort = topological_sort(dg)
        tnames = node_list_to_node_name_list(tsort)
        self.assertEqual(tnames, ['C', 'B', 'A', 'E', 'D'], "incorrect")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TopologicalSearchTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
