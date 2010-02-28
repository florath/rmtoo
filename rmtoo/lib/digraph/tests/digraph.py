#
# Digraph Pyhton library
#
# Unit tests for the digraph
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

import unittest
from Digraph import Digraph

class DigraphTests(unittest.TestCase):

    def test_constructor_001(self):
        "Test conversion from dictionary to graph and back (two nodes)"
        d = {"A": ["B"], "B": []}
        dg = Digraph(d)
        e = dg.output_to_dict()
        self.assertEqual(d, e, "Error during converting the graph")

    def test_constructor_002(self):
        "Test conversion from dictionary to graph and back (zero nodes)"
        d = {}
        dg = Digraph(d)
        e = dg.output_to_dict()
        self.assertEqual(d, e, "Error during converting the graph")

    def test_constructor_003(self):
        "Test conversion from dictionary to graph and back (one node)"
        d = {"A": [] }
        dg = Digraph(d)
        e = dg.output_to_dict()
        self.assertEqual(d, e, "Error during converting the graph")

    def test_constructor_004(self):
        "Test conversion from dictionary to graph and back (one node to itself)"
        d = {"A": ["A"] }
        dg = Digraph(d)
        e = dg.output_to_dict()
        self.assertEqual(d, e, "Error during converting the graph")

    def test_constructor_005(self):
        "Test conversion: error: pointed node does not exists"
        d = {"A": ["B"] }
        self.assertRaises(KeyError, Digraph, d)

    def test_constructor_006(self):
        "Test conversion from dictionary: two node circle"
        d = {"A": ["B"], "B": ["A"] }
        dg = Digraph(d)
        e = dg.output_to_dict()
        self.assertEqual(d, e, "Error during converting the graph")

    def test_constructor_007(self):
        "Test conversion from dictionary: more complex graph"
        d = {"A": ["B"], "B": ["A", "C", "D"], "C": ["A", "D"],
             "D": ["D"] }
        dg = Digraph(d)
        e = dg.output_to_dict()
        self.assertEqual(d, e, "Error during converting the graph")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DigraphTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
