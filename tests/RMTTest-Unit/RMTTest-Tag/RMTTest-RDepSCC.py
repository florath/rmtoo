'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for RDepNo Directed Digraph
  (which finds strongly connected components)

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals


from RDep import create_parameters
from rmtoo.inputs.RDepNoDirectedCircles import RDepNoDirectedCircles


class RMTTestRDepSCC(object):

    def rmttest_positive_01(self):
        "Two node one edge digraph B -> A"
        config, reqset = create_parameters({"B": ["A"], "A": []})
        reqset.graph_master_node = reqset.find("A")

        rdep = RDepNoDirectedCircles(config)
        result = rdep.rewrite(reqset)

        assert result

    def rmttest_positive_02(self):
        "small digraph D -> B -> A and D -> C -> A"
        config, reqset = create_parameters(
            {"D": ["B", "C"], "C": ["A"], "B": ["A"], "A": []})
        reqset.graph_master_node = reqset.find("A")

        rdep = RDepNoDirectedCircles(config)
        result = rdep.rewrite(reqset)

        assert result

    def rmttest_negative_01(self):
        "small digraph D -> B -> A and A -> C -> D"
        config, reqset = create_parameters(
            {"D": ["B"], "C": ["D"], "B": ["A"], "A": ["C"]})
        reqset.graph_master_node = reqset.find("A")

        rdep = RDepNoDirectedCircles(config)
        result = rdep.rewrite(reqset)

        assert not result
