#
# Digraph Pyhton library
#
# Unit tests for the digraph
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.digraph.Digraph import Digraph

class RMTTest_Node:

    def rmttest_neg_01(self):
        "Node test: not find outgoing node which is not there"

        n = Digraph.Node()
        r = n.find_outgoing("nixdamit")
        assert(r==None)

    def rmttest_neg_02(self):
        "Node test: check if is_self_of_ancient is correct when the other is not an ancient"

        n = Digraph.Node()
        r = n.is_self_of_ancient(None)
        assert(r==False)
