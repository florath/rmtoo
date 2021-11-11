'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit tests for the digraph

 (c) 2010,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''


from rmtoo.lib.digraph.Digraph import Digraph


class RMTTestNode(object):

    def rmttest_neg_01(self):
        "Node test: not find outgoing node which is not there"

        n = Digraph.Node()
        r = n.find_outgoing("nixdamit")
        assert r is None

    def rmttest_neg_02(self):
        "Node test: check if is_self_of_ancient is correct"

        n = Digraph.Node()
        r = n.is_self_of_ancient(None)
        assert not r
