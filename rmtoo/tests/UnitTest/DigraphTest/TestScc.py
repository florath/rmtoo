'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Digraph library - tests for strongly connected graph.
    
 (c) 2010,2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import unittest

from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.digraph.StronglyConnectedComponents \
    import strongly_connected_components
from rmtoo.lib.digraph.StronglyConnectedComponents \
    import check_for_strongly_connected_components
from rmtoo.lib.digraph.Helper import node_sl_to_node_name_sl, \
    digraph_create_from_dict

class SCCTests(unittest.TestCase):

    def test_scc_001(self):
        "Simple two node digraph with one scc"
        dg = digraph_create_from_dict({"A": ["B"], "B": ["A"] })
        sccs = strongly_connected_components(dg)
        sccsnames = node_sl_to_node_name_sl(sccs)
        self.assertEqual(sccsnames, [set(['A', 'B'])], "incorrect")

    def test_scc_002(self):
        "Simple two node digraph with no scc"
        dg = digraph_create_from_dict({"A": ["B"], "B": [] })
        sccs = strongly_connected_components(dg)
        sccsnames = node_sl_to_node_name_sl(sccs)
        self.assertEqual(sccsnames, [set(['B']), set(['A'])], "incorrect")

    def test_scc_003(self):
        "Simple three node digraph with one scc and an extra node"
        dg = digraph_create_from_dict({"A": ["B", "C"], "B": ["A"], "C": [] })
        sccs = strongly_connected_components(dg)
        sccsnames = node_sl_to_node_name_sl(sccs)
        self.assertEqual(sccsnames, [set(['C']), set(['A', 'B'])], "incorrect")

    def test_scc_004(self):
        "Simple three node digraph with one scc I"
        dg = digraph_create_from_dict({"A": ["B", "C"], "B": ["A"], "C": ["A"] })
        sccs = strongly_connected_components(dg)
        sccsnames = node_sl_to_node_name_sl(sccs)
        self.assertEqual(sccsnames, [set(['A', 'C', 'B'])], "incorrect")

    def test_scc_005(self):
        "Simple three node digraph with one scc II"
        dg = digraph_create_from_dict({"A": ["B", "C"], "B": ["A"], "C": ["B"] })
        sccs = strongly_connected_components(dg)
        sccsnames = node_sl_to_node_name_sl(sccs)
        self.assertEqual(sccsnames, [set(['A', 'C', 'B'])], "incorrect")

    def test_scc_006(self):
        "Check for scc in a three node digraph with scc"
        dg = digraph_create_from_dict({"A": ["B", "C"], "B": ["A"], "C": ["B"] })
        sccs = strongly_connected_components(dg)
        scc_exists = check_for_strongly_connected_components(sccs)
        self.assertEqual(scc_exists, True, "incorrect")

    def test_scc_007(self):
        "Check for scc in a three node digraph without scc"
        dg = digraph_create_from_dict({"A": ["B"], "B": ["C"], "C": [] })
        sccs = strongly_connected_components(dg)
        scc_exists = check_for_strongly_connected_components(sccs)
        self.assertEqual(scc_exists, False, "incorrect")

    def test_scc_008(self):
        "Check for scc in a three node digraph with a two node scc"
        dg = digraph_create_from_dict({"A": ["B"], "B": ["A"], "C": [] })
        sccs = strongly_connected_components(dg)
        scc_exists = check_for_strongly_connected_components(sccs)
        self.assertEqual(scc_exists, True, "incorrect")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SCCTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
