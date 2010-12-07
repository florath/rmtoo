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

class TestNode:

    def test_neg_01(self):
        "Node test: not find outgoing node which is not there"

        n = Digraph.Node()
        r = n.find_outgoing("nixdamit")
        assert(r==None)
