'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit tests for the digraph.

 (c) 2010,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''


from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.digraph.Digraph import Digraph
import pytest


class RMTTestDigraph(object):

    def rmttest_constructor_001(self):
        "Test conversion from dictionary to graph and back (two nodes)"
        d = {"A": ["B"], "B": []}
        dg = Digraph(d)
        e = dg.output_to_dict()
        assert d == e

    def rmttest_constructor_002(self):
        "Test conversion from dictionary to graph and back (zero nodes)"
        d = {}
        dg = Digraph(d)
        e = dg.output_to_dict()
        assert d == e

    def rmttest_constructor_003(self):
        "Test conversion from dictionary to graph and back (one node)"
        d = {"A": []}
        dg = Digraph(d)
        e = dg.output_to_dict()
        assert d == e

    def rmttest_constructor_004(self):
        "Test conversion from dict to graph and back (one node to itself)"
        d = {"A": ["A"]}
        dg = Digraph(d)
        e = dg.output_to_dict()
        assert d == e

    def rmttest_constructor_005(self):
        "Test conversion: error: pointed node does not exists"
        d = {"A": ["B"]}
        with pytest.raises(RMTException) as rmte:
            Digraph(d)
            assert 24 == rmte.id()

    def rmttest_constructor_006(self):
        "Test conversion from dictionary: two node circle"
        d = {"A": ["B"], "B": ["A"]}
        dg = Digraph(d)
        e = dg.output_to_dict()
        assert d == e

    def rmttest_constructor_007(self):
        "Test conversion from dictionary: more complex graph"
        d = {"A": ["B"], "B": ["A", "C", "D"], "C": ["A", "D"],
             "D": ["D"]}
        dg = Digraph(d)
        e = dg.output_to_dict()
        assert d == e

    def rmttest_find_01(self):
        "Digraph find with element available"
        d = {"A": ["B"], "B": ["A", "C", "D"], "C": ["A", "D"],
             "D": ["D"]}
        dg = Digraph(d)
        n = dg.find("A")
        assert "A" == n.name

    def rmttest_find_02(self):
        "Digraph find with element not available"
        d = {"A": ["B"], "B": ["A", "C", "D"], "C": ["A", "D"],
             "D": ["D"]}
        dg = Digraph(d)
        n = dg.find("Z")
        assert n is None

    def rmttest_build_named_nodes_01(self):
        "Digraph build named nodes with node without name"
        d = {"A": ["B"], "B": ["A", "C", "D"], "C": ["A", "D"],
             "D": ["D"]}
        dg = Digraph(d)
        n = dg.find("A")
        n.name = None
        with pytest.raises(RMTException) as rmte:
            dg.build_named_nodes()
            assert 20 == rmte.id()

    def rmttest_build_named_nodes_02(self):
        "Digraph build named nodes with two nodes with same name"
        d = {"A": ["B"], "B": ["A", "C", "D"], "C": ["A", "D"],
             "D": ["D"]}
        dg = Digraph(d)
        n = dg.find("A")
        n.name = "Twice"
        n = dg.find("B")
        n.name = "Twice"

        with pytest.raises(RMTException) as rmte:
            dg.build_named_nodes()
            assert 21 == rmte.id()

    def rmttest_get_named_node_01(self):
        "Digraph get named node with map available"
        d = {"A": ["B"], "B": ["A", "C", "D"], "C": ["A", "D"],
             "D": ["D"]}
        dg = Digraph(d)
        dg.build_named_nodes()
        n = dg.get_named_node("A")
        assert "A" == n.name

    def rmttest_get_named_node_02(self):
        "Digraph get named node with map available but invalid node name"
        d = {"A": ["B"], "B": ["A", "C", "D"], "C": ["A", "D"],
             "D": ["D"]}
        dg = Digraph(d)
        dg.build_named_nodes()
        with pytest.raises(RMTException) as rmte:
            dg.get_named_node("NotThere")
            assert 23 == rmte.id()

    def rmttest_get_named_node_03(self):
        "Digraph get named node with map not available"
        d = {"A": ["B"], "B": ["A", "C", "D"], "C": ["A", "D"],
             "D": ["D"]}
        dg = Digraph(d)
        with pytest.raises(RMTException) as rmte:
            dg.get_named_node("NotThere")
            assert 22 == rmte.id()

    def rmttest_add_node_01(self):
        "Digraph add node with two times same name"
        dg = Digraph()
        n1 = Digraph.Node("myname")
        n2 = Digraph.Node("myname")
        dg.add_node(n1)
        with pytest.raises(RMTException) as rmte:
            dg.add_node(n2)
            assert 39 == rmte.id()
