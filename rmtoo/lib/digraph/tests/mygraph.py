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

from Digraph import Digraph
from TopologicalSort import topological_sort
from Helper import node_list_to_node_name_list

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
    n1.outgoing.append(n2)
    n1.outgoing.append(n3)
    n2.outgoing.append(n3)
    mg.nodes.append(n1)
    mg.nodes.append(n2)
    mg.nodes.append(n3)
    return mg

class InheritanceTest(unittest.TestCase):

    def test_inherit_001(self):
        "Test creation syntax check"
        mg = create_test_graph_01()

    def test_inherit_002(self):
        "Output check"
        mg = create_test_graph_01()
        d = mg.output_to_dict()
        self.assertEqual(d, {'A': ['B', 'C'], 'C': [], 'B': ['C']},
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

        
