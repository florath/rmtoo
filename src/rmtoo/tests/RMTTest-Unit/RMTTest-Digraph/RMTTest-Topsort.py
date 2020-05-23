'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for Toposort

 (c) 2010,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''


from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.digraph.TopologicalSort import topological_sort
from rmtoo.lib.digraph.Helper import node_list_to_node_name_list


class RMTTestTopologicalSearchTests(object):

    def rmttest_tsort_001(self):
        "Simple three node digraph"
        dg = Digraph({"A": ["B", "C"], "B": ["C"], "C": []})
        tsort = topological_sort(dg)
        tnames = node_list_to_node_name_list(tsort)
        assert tnames == ['C', 'B', 'A'], "incorrect"

    def rmttest_tsort_002(self):
        "Zero node digraph"
        dg = Digraph({})
        tsort = topological_sort(dg)
        tnames = node_list_to_node_name_list(tsort)
        assert tnames == [], "incorrect"

    def rmttest_tsort_003(self):
        "One node digraph"
        dg = Digraph({"A": []})
        tsort = topological_sort(dg)
        tnames = node_list_to_node_name_list(tsort)
        assert tnames == ["A"], "incorrect"

    def rmttest_tsort_004(self):
        "More complex digraph"
        dg = Digraph({"A": ["B", "C"], "B": ["C", "E"], "C": ["D", "E"],
                      "D": [], "E": []})
        tsort = topological_sort(dg)
        tnames = node_list_to_node_name_list(tsort)
        # There is no 'fixed' result - depending on the python
        # implementation different correct values are computed.
        assert self.__list_order(tnames, "D", "C")
        assert self.__list_order(tnames, "E", "C")
        assert self.__list_order(tnames, "E", "B")
        assert self.__list_order(tnames, "C", "B")
        assert self.__list_order(tnames, "C", "A")
        assert self.__list_order(tnames, "B", "A")

    @staticmethod
    def __list_order(lst, x, y):
        return lst.index(x) < lst.index(y)

    def rmttest_tsort_005(self):
        "Digraph with two components"
        dg = Digraph({"A": ["B", "C"], "B": ["C"], "C": [],
                      "D": ["E"], "E": []})
        tsort = topological_sort(dg)
        tnames = node_list_to_node_name_list(tsort)

        # There is no 'fixed' result - depending on the python
        # implementation different correct values are computed.
        assert self.__list_order(tnames, "B", "A")
        assert self.__list_order(tnames, "C", "A")
        assert self.__list_order(tnames, "E", "D")
