#
# Requirement Management Toolset
#
# Unit test for RDepPriority
#
# (c) 2010 on flonatel
#
# For licencing details see COPYING
#

from rmtoo.tests.lib.RDep import create_parameters
from rmtoo.modules.RDepPriority import RDepPriority

class TestRDepPriority:

    def test_positive_01(self):
        "Two node one edge digraph B -> A"
        opts, config, reqset = create_parameters({"B": ["A"], "A": [] })
        reqset.build_named_nodes()
        reqset.graph_master_node = reqset.get_named_node("A")
        reqset.get_named_node("A").tags = {"Factor": 1.0}
        reqset.get_named_node("B").tags = {"Factor": 0.8}

        rdep = RDepPriority(opts, config)
        rdep.rewrite(reqset)

        assert(reqset.get_named_node("A").tags["Priority"]==1.0)
        assert(reqset.get_named_node("B").tags["Priority"]==0.8)

    def test_positive_02(self):
        "Three node digraph C -> B -> A"
        opts, config, reqset = create_parameters(
            {"C": ["B"], "B": ["A"], "A": [] })
        reqset.build_named_nodes()
        reqset.graph_master_node = reqset.get_named_node("A")
        reqset.get_named_node("A").tags = {"Factor": 1.0}
        reqset.get_named_node("B").tags = {"Factor": 0.8}
        reqset.get_named_node("C").tags = {"Factor": 0.5}

        rdep = RDepPriority(opts, config)
        rdep.rewrite(reqset)

        assert(reqset.get_named_node("A").tags["Priority"]==1.0)
        assert(reqset.get_named_node("B").tags["Priority"]==0.8)
        assert(reqset.get_named_node("C").tags["Priority"]==0.4)

    def test_positive_03(self):
        "Four node digraph D -> B -> A and D -> C -> A"
        opts, config, reqset = create_parameters(
            {"D": ["B", "C"], "C": ["A"], "B": ["A"], "A": [] })
        reqset.build_named_nodes()
        reqset.graph_master_node = reqset.get_named_node("A")
        reqset.get_named_node("A").tags = {"Factor": 1.0}
        reqset.get_named_node("B").tags = {"Factor": 0.2}
        reqset.get_named_node("C").tags = {"Factor": 0.4}
        reqset.get_named_node("D").tags = {"Factor": 0.5}

        rdep = RDepPriority(opts, config)
        rdep.rewrite(reqset)

        assert(reqset.get_named_node("A").tags["Priority"]==1.0)
        assert(reqset.get_named_node("B").tags["Priority"]==0.2)
        assert(reqset.get_named_node("C").tags["Priority"]==0.4)
        assert(reqset.get_named_node("D").tags["Priority"]==0.2)
