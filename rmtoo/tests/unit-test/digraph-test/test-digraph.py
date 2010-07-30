#
# Digraph Pyhton library
#
# Unit tests for the digraph
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.digraph.Digraph import Digraph

class TestDigraph:

    def test_constructor_001(self):
        "Test conversion from dictionary to graph and back (two nodes)"
        d = {"A": ["B"], "B": []}
        dg = Digraph(d)
        e = dg.output_to_dict()
        assert(d==e)

    def test_constructor_002(self):
        "Test conversion from dictionary to graph and back (zero nodes)"
        d = {}
        dg = Digraph(d)
        e = dg.output_to_dict()
        assert(d==e)

    def test_constructor_003(self):
        "Test conversion from dictionary to graph and back (one node)"
        d = {"A": [] }
        dg = Digraph(d)
        e = dg.output_to_dict()
        assert(d==e)

    def test_constructor_004(self):
        "Test conversion from dictionary to graph and back (one node to itself)"
        d = {"A": ["A"] }
        dg = Digraph(d)
        e = dg.output_to_dict()
        assert(d==e)

    def test_constructor_005(self):
        "Test conversion: error: pointed node does not exists"
        d = {"A": ["B"] }
        try:
            d = Digraph(d)
            assert(False)
        except RMTException, rmte:
            assert(rmte.id()==24)

    def test_constructor_006(self):
        "Test conversion from dictionary: two node circle"
        d = {"A": ["B"], "B": ["A"] }
        dg = Digraph(d)
        e = dg.output_to_dict()
        assert(d==e)

    def test_constructor_007(self):
        "Test conversion from dictionary: more complex graph"
        d = {"A": ["B"], "B": ["A", "C", "D"], "C": ["A", "D"],
             "D": ["D"] }
        dg = Digraph(d)
        e = dg.output_to_dict()
        assert(d==e)

    def test_find_01(self):
        "Digraph find with element available"
        d = {"A": ["B"], "B": ["A", "C", "D"], "C": ["A", "D"],
             "D": ["D"] }
        dg = Digraph(d)
        n = dg.find("A")
        assert(n.name=="A")

    def test_find_02(self):
        "Digraph find with element not available"
        d = {"A": ["B"], "B": ["A", "C", "D"], "C": ["A", "D"],
             "D": ["D"] }
        dg = Digraph(d)
        n = dg.find("Z")
        assert(n==None)

    def test_build_named_nodes_01(self):
        "Digraph build named nodes with node without name"
        d = {"A": ["B"], "B": ["A", "C", "D"], "C": ["A", "D"],
             "D": ["D"] }
        dg = Digraph(d)
        n = dg.find("A")
        n.name=None
        try:
            dg.build_named_nodes()
            assert(False)
        except RMTException, rmte:
            assert(rmte.id()==20)

    def test_build_named_nodes_02(self):
        "Digraph build named nodes with two nodes with same name"
        d = {"A": ["B"], "B": ["A", "C", "D"], "C": ["A", "D"],
             "D": ["D"] }
        dg = Digraph(d)
        n = dg.find("A")
        n.name = "Twice"
        n = dg.find("B")
        n.name = "Twice"

        try:
            dg.build_named_nodes()
            assert(False)
        except RMTException, rmte:
            assert(rmte.id()==21)

    def test_get_named_node_01(self):
        "Digraph get named node with map available"
        d = {"A": ["B"], "B": ["A", "C", "D"], "C": ["A", "D"],
             "D": ["D"] }
        dg = Digraph(d)
        dg.build_named_nodes()
        n = dg.get_named_node("A")
        assert(n.name=="A")

    def test_get_named_node_02(self):
        "Digraph get named node with map available but invalid node name"
        d = {"A": ["B"], "B": ["A", "C", "D"], "C": ["A", "D"],
             "D": ["D"] }
        dg = Digraph(d)
        dg.build_named_nodes()
        try:
            n = dg.get_named_node("NotThere")
            assert(False)
        except RMTException, rmte:
            assert(rmte.id()==23)

    def test_get_named_node_03(self):
        "Digraph get named node with map not available"
        d = {"A": ["B"], "B": ["A", "C", "D"], "C": ["A", "D"],
             "D": ["D"] }
        dg = Digraph(d)
        try:
            n = dg.get_named_node("NotThere")
            assert(False)
        except RMTException, rmte:
            assert(rmte.id()==22)

