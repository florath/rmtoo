'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
 Unit tests for the digraph
 
 (c) 2010,2012 by flonatel

 For licensing details see COPYING
'''

from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.digraph.DigraphUtils import digraph_create_from_dict

class TestDigraph:

    def test_constructor_001(self):
        "Test conversion from dictionary to graph and back (two nodes)"
        d = {"A": ["B"], "B": []}
        dg = digraph_create_from_dict(d)
        e = dg.as_dict()
        assert(d == e)

    def test_constructor_002(self):
        "Test conversion from dictionary to graph and back (zero nodes)"
        d = {}
        dg = digraph_create_from_dict(d)
        e = dg.as_dict()
        assert(d == e)

    def test_constructor_003(self):
        "Test conversion from dictionary to graph and back (one node)"
        d = {"A": [] }
        dg = digraph_create_from_dict(d)
        e = dg.as_dict()
        assert(d == e)

    def test_constructor_004(self):
        "Test conversion from dictionary to graph and back (one node to itself)"
        d = {"A": ["A"] }
        dg = digraph_create_from_dict(d)
        e = dg.as_dict()
        assert(d == e)

    def test_constructor_005(self):
        "Test conversion: error: pointed node does not exists"
        d = {"A": ["B"] }
        try:
            d = digraph_create_from_dict(d)
            assert(False)
        except RMTException, rmte:
            assert(rmte.id() == 24)

    def test_constructor_006(self):
        "Test conversion from dictionary: two node circle"
        d = {"A": ["B"], "B": ["A"] }
        dg = digraph_create_from_dict(d)
        e = dg.as_dict()
        assert(d == e)

    def test_constructor_007(self):
        "Test conversion from dictionary: more complex graph"
        d = {"A": ["B"], "B": ["A", "C", "D"], "C": ["A", "D"],
             "D": ["D"] }
        dg = digraph_create_from_dict(d)
        e = dg.as_dict()
        assert(d == e)

    def test_find_01(self):
        "Digraph find with element available"
        d = {"A": ["B"], "B": ["A", "C", "D"], "C": ["A", "D"],
             "D": ["D"] }
        dg = digraph_create_from_dict(d)
        n = dg.find("A")
        assert(n.get_name() == "A")

    def test_find_02(self):
        "Digraph find with element not available"
        d = {"A": ["B"], "B": ["A", "C", "D"], "C": ["A", "D"],
             "D": ["D"] }
        dg = digraph_create_from_dict(d)
        n = dg.find("Z")
        assert(n == None)

    def test_get_named_node_01(self):
        "Digraph get named node with map available"
        d = {"A": ["B"], "B": ["A", "C", "D"], "C": ["A", "D"],
             "D": ["D"] }
        dg = digraph_create_from_dict(d)
        n = dg.find("A")
        assert(n.get_name() == "A")

    def test_get_named_node_02(self):
        "Digraph get named node with map available but invalid node name"
        d = {"A": ["B"], "B": ["A", "C", "D"], "C": ["A", "D"],
             "D": ["D"] }
        dg = digraph_create_from_dict(d)
        try:
            n = dg.find_wt("NotThere")
            assert(False)
        except RMTException, rmte:
            assert(rmte.id() == 23)

    def test_add_node_01(self):
        "Digraph add node with two times same name"
        dg = Digraph()
        n1 = Digraph.Node("myname")
        n2 = Digraph.Node("myname")
        dg.add_node(n1)
        try:
            dg.add_node(n2)
            assert(False)
        except RMTException, rmte:
            assert(rmte.id() == 39)

