#
# Digraph Pyhton library
#
# Unit tests for inheritance
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

import unittest

from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.digraph.TopologicalSort import topological_sort
from rmtoo.lib.digraph.Helper import node_list_to_node_name_list

class MyGraph(Digraph):

    def __init__(self):
        Digraph.__init__(self)

    class MyNode(Digraph.Node):

        def __init__(self, name):
            Digraph.Node.__init__(self, name)
            self.something_more = 1

def create_test_graph_01():
    mg = MyGraph()
    n1 = MyGraph.MyNode("A")
    n2 = MyGraph.MyNode("B")
    n3 = MyGraph.MyNode("C")
    n1.add_outgoing(n2)
    n1.add_outgoing(n3)
    n2.add_outgoing(n3)
    mg.add_node(n1)
    mg.add_node(n2)
    mg.add_node(n3)
    return mg

class InheritanceTest(unittest.TestCase):

    def test_inherit_001(self):
        "Test creation syntax check"
        mg = create_test_graph_01()

    def test_inherit_002(self):
        "Output check"
        mg = create_test_graph_01()
        d = mg.as_dict()
        self.assertEqual(d, {'A': ['C', 'B'], 'C': [], 'B': ['C']},
                         "incorrect dictionary output")

    def test_inherit_003(self):
        "Topological sort check"
        mg = create_test_graph_01()
        tsort = topological_sort(mg)
        tnames = node_list_to_node_name_list(tsort)
        self.assertEqual(tnames, ['C', 'B', 'A'],
                         "incorrect topological sort")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(InheritanceTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

        
