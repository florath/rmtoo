'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for RDepPriority

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals


from rmtoo.inputs.RDepPriority import RDepPriority
from TestConfig import TestConfig
from rmtoo.lib.RequirementSet import RequirementSet
from rmtoo.lib.Requirement import Requirement


class RMTTestRDepPriority(object):

    def rmttest_positive_01(self):
        "Two node one edge digraph B -> A"
        config = TestConfig()
        reqset = RequirementSet(config)
        req1 = Requirement('''Name: A
Type: master requirement
Solved by: B''', 'A', None, None, None)
        reqset.add_requirement(req1)
        req2 = Requirement('''Name: B
Type: requirement''', 'B', None, None, None)
        reqset.add_requirement(req2)
        reqset.resolve_solved_by()
        reqset.find_master_nodes()
        reqset.build_named_nodes()
        reqset.graph_master_node = reqset.get_named_node("A")
        reqset.get_named_node("A").set_value("Factor", 1.0)
        reqset.get_named_node("B").set_value("Factor", 0.8)

        rdep = RDepPriority(config)
        rdep.rewrite(reqset)

        assert 1.0 == reqset.get_named_node("A").get_value("Priority")
        assert 0.8 == reqset.get_named_node("B").get_value("Priority")

    def rmttest_positive_02(self):
        "Three node digraph C -> B -> A"
        config = TestConfig()
        reqset = RequirementSet(config)
        req1 = Requirement('''Name: A
Type: master requirement
Solved by: B''', 'A', None, None, None)
        reqset.add_requirement(req1)
        req2 = Requirement('''Name: B
Type: requirement
Solved by: C''', 'B', None, None, None)
        reqset.add_requirement(req2)
        req3 = Requirement('''Name: C
Type: requirement''', 'C', None, None, None)
        reqset.add_requirement(req3)
        reqset.resolve_solved_by()
        reqset.find_master_nodes()
        reqset.build_named_nodes()

        reqset.graph_master_node = reqset.get_named_node("A")
        reqset.get_named_node("A").set_value("Factor", 1.0)
        reqset.get_named_node("B").set_value("Factor", 0.8)
        reqset.get_named_node("C").set_value("Factor", 0.5)

        rdep = RDepPriority(config)
        rdep.rewrite(reqset)

        assert 1.0 == reqset.get_named_node("A").get_value("Priority")
        assert 0.8 == reqset.get_named_node("B").get_value("Priority")
        assert 0.4 == reqset.get_named_node("C").get_value("Priority")

    def rmttest_positive_03(self):
        "Four node digraph D -> B -> A and D -> C -> A"
        config = TestConfig()
        reqset = RequirementSet(config)
        req1 = Requirement('''Name: A
Type: master requirement
Solved by: B C''', 'A', None, None, None)
        reqset.add_requirement(req1)
        req2 = Requirement('''Name: B
Type: requirement
Solved by: D''', 'B', None, None, None)
        reqset.add_requirement(req2)
        req3 = Requirement('''Name: C
Type: requirement
Solved by: D''', 'C', None, None, None)
        reqset.add_requirement(req3)
        req4 = Requirement('''Name: D
Type: requirement''', 'D', None, None, None)
        reqset.add_requirement(req4)
        reqset.resolve_solved_by()
        reqset.find_master_nodes()
        reqset.build_named_nodes()

        reqset.graph_master_node = reqset.get_named_node("A")
        reqset.get_named_node("A").set_value("Factor", 1.0)
        reqset.get_named_node("B").set_value("Factor", 0.2)
        reqset.get_named_node("C").set_value("Factor", 0.4)
        reqset.get_named_node("D").set_value("Factor", 0.5)

        rdep = RDepPriority(config)
        rdep.rewrite(reqset)

        assert 1.0 == reqset.get_named_node("A").get_value("Priority")
        assert 0.2 == reqset.get_named_node("B").get_value("Priority")
        assert 0.4 == reqset.get_named_node("C").get_value("Priority")
        assert 0.2 == reqset.get_named_node("D").get_value("Priority")
