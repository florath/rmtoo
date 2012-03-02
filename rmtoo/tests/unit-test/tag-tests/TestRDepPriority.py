'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Unit test for RDepPriority
   
 (c) 2010-2012 by flonatel GmhH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.tests.lib.RDep import create_parameters
from rmtoo.inputs.RDepPriority import RDepPriority

class TestRDepPriority:

    def test_positive_01(self):
        "Two node one edge digraph B -> A"
        config, reqset = create_parameters({"B": ["A"], "A": [] })
        reqset.build_named_nodes()
        reqset.graph_master_node = reqset.get_named_node("A")
        reqset.get_named_node("A").set_value("Factor", 1.0)
        reqset.get_named_node("B").set_value("Factor", 0.8)

        rdep = RDepPriority(config)
        rdep.rewrite(reqset)

        assert(reqset.get_named_node("A").get_value("Priority") == 1.0)
        assert(reqset.get_named_node("B").get_value("Priority") == 0.8)

    def test_positive_02(self):
        "Three node digraph C -> B -> A"
        config, reqset = create_parameters(
            {"C": ["B"], "B": ["A"], "A": [] })
        reqset.build_named_nodes()
        reqset.graph_master_node = reqset.get_named_node("A")
        reqset.get_named_node("A").set_value("Factor", 1.0)
        reqset.get_named_node("B").set_value("Factor", 0.8)
        reqset.get_named_node("C").set_value("Factor", 0.5)

        rdep = RDepPriority(config)
        rdep.rewrite(reqset)

        assert(reqset.get_named_node("A").get_value("Priority") == 1.0)
        assert(reqset.get_named_node("B").get_value("Priority") == 0.8)
        assert(reqset.get_named_node("C").get_value("Priority") == 0.4)

    def test_positive_03(self):
        "Four node digraph D -> B -> A and D -> C -> A"
        config, reqset = create_parameters(
            {"D": ["B", "C"], "C": ["A"], "B": ["A"], "A": [] })
        reqset.build_named_nodes()
        reqset.graph_master_node = reqset.get_named_node("A")
        reqset.get_named_node("A").set_value("Factor", 1.0)
        reqset.get_named_node("B").set_value("Factor", 0.2)
        reqset.get_named_node("C").set_value("Factor", 0.4)
        reqset.get_named_node("D").set_value("Factor", 0.5)

        rdep = RDepPriority(config)
        rdep.rewrite(reqset)

        assert(reqset.get_named_node("A").get_value("Priority") == 1.0)
        assert(reqset.get_named_node("B").get_value("Priority") == 0.2)
        assert(reqset.get_named_node("C").get_value("Priority") == 0.4)
        assert(reqset.get_named_node("D").get_value("Priority") == 0.2)
