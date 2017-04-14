'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Unit tests for the digraph
  
 (c) 2010, 2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
import copy

from rmtoo.lib.digraph.Digraph import Digraph

class TestNode:

    def test_neg_01(self):
        "Node test: not find outgoing node which is not there"

        n = Digraph.Node("MyName")
        r = n.find_outgoing("nixdamit")
        assert(r==None)

    def test_neg_02(self):
        "Node test: check if is_self_of_ancient is correct when the other is not an ancient"

        n = Digraph.Node("MyName")
        r = n.is_self_of_ancient(None)
        assert(r==False)

    def test_copy_node(self):
        "Node test: deep copy node"
        n = Digraph.Node("MyName")
        nc = copy.deepcopy(n)