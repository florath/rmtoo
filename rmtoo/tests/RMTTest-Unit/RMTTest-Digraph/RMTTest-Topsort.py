'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for Toposort

 (c) 2010,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
import unittest

from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.digraph.TopologicalSort import topological_sort
from rmtoo.lib.digraph.Helper import node_list_to_node_name_list


class RMTTestTopologicalSearchTests(unittest.TestCase):

    def rmttest_tsort_001(self):
        "Simple three node digraph"
        dg = Digraph({"A": ["B", "C"], "B": ["C"], "C": []})
        tsort = topological_sort(dg)
        tnames = node_list_to_node_name_list(tsort)
        self.assertEqual(tnames, ['C', 'B', 'A'], "incorrect")

    def rmttest_tsort_002(self):
        "Zero node digraph"
        dg = Digraph({})
        tsort = topological_sort(dg)
        tnames = node_list_to_node_name_list(tsort)
        self.assertEqual(tnames, [], "incorrect")

    def rmttest_tsort_003(self):
        "One node digraph"
        dg = Digraph({"A": []})
        tsort = topological_sort(dg)
        tnames = node_list_to_node_name_list(tsort)
        self.assertEqual(tnames, ["A"], "incorrect")

    def rmttest_tsort_004(self):
        "More complex digraph"
        dg = Digraph({"A": ["B", "C"], "B": ["C", "E"], "C": ["D", "E"],
                      "D": [], "E": []})
        tsort = topological_sort(dg)
        tnames = node_list_to_node_name_list(tsort)
        # There is no 'fixed' result - depending on the python
        # implementation different correct values are computed.
        self.assertTrue(self.__list_order(tnames, "D", "C"))
        self.assertTrue(self.__list_order(tnames, "E", "C"))
        self.assertTrue(self.__list_order(tnames, "E", "B"))
        self.assertTrue(self.__list_order(tnames, "C", "B"))
        self.assertTrue(self.__list_order(tnames, "C", "A"))
        self.assertTrue(self.__list_order(tnames, "B", "A"))

    @staticmethod
    def __list_order(l, x, y):
        return l.index(x) < l.index(y)

    def rmttest_tsort_005(self):
        "Digraph with two components"
        dg = Digraph({"A": ["B", "C"], "B": ["C"], "C": [],
                      "D": ["E"], "E": []})
        tsort = topological_sort(dg)
        tnames = node_list_to_node_name_list(tsort)

        # There is no 'fixed' result - depending on the python
        # implementation different correct values are computed.
        self.assertTrue(self.__list_order(tnames, "B", "A"))
        self.assertTrue(self.__list_order(tnames, "C", "A"))
        self.assertTrue(self.__list_order(tnames, "E", "D"))
