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

class RMTTest_Digraph:

    def rmttest_constructor_001(self):
        "Test conversion from dictionary to graph and back (two nodes)"
        d = {"A": ["B"], "B": []}
        dg = Digraph(d)
        e = dg.output_to_dict()
        assert(d==e)

    def rmttest_constructor_002(self):
        "Test conversion from dictionary to graph and back (zero nodes)"
        d = {}
        dg = Digraph(d)
        e = dg.output_to_dict()
        assert(d==e)

    def rmttest_constructor_003(self):
        "Test conversion from dictionary to graph and back (one node)"
        d = {"A": [] }
        dg = Digraph(d)
        e = dg.output_to_dict()
        assert(d==e)

    def rmttest_constructor_004(self):
        "Test conversion from dictionary to graph and back (one node to itself)"
        d = {"A": ["A"] }
        dg = Digraph(d)
        e = dg.output_to_dict()
        assert(d==e)

    def rmttest_constructor_005(self):
        "Test conversion: error: pointed node does not exists"
        d = {"A": ["B"] }
        try:
            d = Digraph(d)
            assert(False)
        except RMTException as rmte:
            assert(rmte.id()==24)

    def rmttest_constructor_006(self):
        "Test conversion from dictionary: two node circle"
        d = {"A": ["B"], "B": ["A"] }
        dg = Digraph(d)
        e = dg.output_to_dict()
        assert(d==e)

    def rmttest_constructor_007(self):
        "Test conversion from dictionary: more complex graph"
        d = {"A": ["B"], "B": ["A", "C", "D"], "C": ["A", "D"],
             "D": ["D"] }
        dg = Digraph(d)
        e = dg.output_to_dict()
        assert(d==e)

    def rmttest_find_01(self):
        "Digraph find with element available"
        d = {"A": ["B"], "B": ["A", "C", "D"], "C": ["A", "D"],
             "D": ["D"] }
        dg = Digraph(d)
        n = dg.find("A")
        assert(n.name=="A")

    def rmttest_find_02(self):
        "Digraph find with element not available"
        d = {"A": ["B"], "B": ["A", "C", "D"], "C": ["A", "D"],
             "D": ["D"] }
        dg = Digraph(d)
        n = dg.find("Z")
        assert(n==None)

    def rmttest_build_named_nodes_01(self):
        "Digraph build named nodes with node without name"
        d = {"A": ["B"], "B": ["A", "C", "D"], "C": ["A", "D"],
             "D": ["D"] }
        dg = Digraph(d)
        n = dg.find("A")
        n.name=None
        try:
            dg.build_named_nodes()
            assert(False)
        except RMTException as rmte:
            assert(rmte.id()==20)

    def rmttest_build_named_nodes_02(self):
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
        except RMTException as rmte:
            assert(rmte.id()==21)

    def rmttest_get_named_node_01(self):
        "Digraph get named node with map available"
        d = {"A": ["B"], "B": ["A", "C", "D"], "C": ["A", "D"],
             "D": ["D"] }
        dg = Digraph(d)
        dg.build_named_nodes()
        n = dg.get_named_node("A")
        assert(n.name=="A")

    def rmttest_get_named_node_02(self):
        "Digraph get named node with map available but invalid node name"
        d = {"A": ["B"], "B": ["A", "C", "D"], "C": ["A", "D"],
             "D": ["D"] }
        dg = Digraph(d)
        dg.build_named_nodes()
        try:
            n = dg.get_named_node("NotThere")
            assert(False)
        except RMTException as rmte:
            assert(rmte.id()==23)

    def rmttest_get_named_node_03(self):
        "Digraph get named node with map not available"
        d = {"A": ["B"], "B": ["A", "C", "D"], "C": ["A", "D"],
             "D": ["D"] }
        dg = Digraph(d)
        try:
            n = dg.get_named_node("NotThere")
            assert(False)
        except RMTException as rmte:
            assert(rmte.id()==22)

    def rmttest_add_node_01(self):
        "Digraph add node with two times same name"
        dg = Digraph()
        n1 = Digraph.Node("myname")
        n2 = Digraph.Node("myname")
        dg.add_node(n1)
        try:
            dg.add_node(n2)
            assert(False)
        except RMTException as rmte:
            assert(rmte.id()==39)

