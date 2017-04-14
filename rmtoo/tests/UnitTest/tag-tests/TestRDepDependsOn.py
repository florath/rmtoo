'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Unit test for RDepDependsOn
   
 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.tests.lib.RDep import create_parameters
from rmtoo.tests.lib.RDep import TestReq
from rmtoo.inputs.RDepDependsOn import RDepDependsOn
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RequirementDNode import RequirementDNode
from rmtoo.lib.storagebackend.RecordEntry import RecordEntry
from rmtoo.lib.RequirementSet import RequirementSet
from rmtoo.tests.lib.TestConfig import TestConfig
from rmtoo.lib.InputModules import InputModules

class TestRDepDependsOn:

    def test_positive_01(self):
        "Two node one edge digraph B -> A"
        config = TestConfig()

        imod = InputModules("..", config)

        reqset = RequirementSet(config)
        req1 = Requirement('''Name: A
Type: master requirement''', 'A', None, imod, config)
        reqset.add_node(RequirementDNode(req1))
        req2 = Requirement('''Name: B
Type: requirement
Depends on: A''', 'B', None, imod, config)
        reqset.add_node(RequirementDNode(req2))
        config.set_depends_on()

        rdep = RDepDependsOn(config)
        rdep.rewrite(reqset)

        assert(reqset.get_requirement("A").get_incoming_as_named_list() == [])
        assert(reqset.get_requirement("A").get_outgoing_as_named_list() == ["B"])
        assert(reqset.get_requirement("B").get_incoming_as_named_list() == ["A"])
        assert(reqset.get_requirement("B").get_outgoing_as_named_list() == [])

    def test_positive_02(self):
        "Three node one edge digraph B -> A, C -> A and C -> B"
        config = TestConfig()

        imod = InputModules("..", config)

        reqset = RequirementSet(config)
        req1 = Requirement('''Name: A
Type: master requirement''', 'A', None, imod, config)
        reqset.add_node(RequirementDNode(req1))
        req2 = Requirement('''Name: B
Type: requirement
Depends on: A''', 'B', None, imod, config)
        reqset.add_node(RequirementDNode(req2))
        config.set_depends_on()
        req3 = Requirement('''Name: C
Type: requirement
Depends on: A B''', 'C', None, imod, config)
        reqset.add_node(RequirementDNode(req3))
        config.set_depends_on()

        rdep = RDepDependsOn(config)
        rdep.rewrite(reqset)

        assert(reqset.get_requirement("A").get_incoming_as_named_list() == [])
        assert(reqset.get_requirement("A").get_outgoing_as_named_list() == ["C", "B"])
        assert(reqset.get_requirement("B").get_incoming_as_named_list() == ["A"])
        assert(reqset.get_requirement("B").get_outgoing_as_named_list() == ["C"])
        assert(reqset.get_requirement("C").get_incoming_as_named_list() == ["A", "B"])
        assert(reqset.get_requirement("C").get_outgoing_as_named_list() == [])

    def test_negative_01(self):
        "Master requirement with Depends on field"
        config = TestConfig()

        imod = InputModules("..", config)

        reqset = RequirementSet(config)
        req1 = Requirement('''Name: A
Type: master requirement
Depends on: A''', 'A', None, imod, config)
        reqset.add_node(RequirementDNode(req1))
        config.set_depends_on()

        rdep = RDepDependsOn(config)
        status = rdep.rewrite(reqset)

        assert(status == False)

    def test_negative_03(self):
        "Normal requirement has no 'Depends on'"
        config = TestConfig()

        imod = InputModules("..", config)

        reqset = RequirementSet(config)
        req1 = Requirement('''Name: A
Type: master requirement''', 'A', None, imod, config)
        reqset.add_node(RequirementDNode(req1))
        req2 = Requirement('''Name: B
Type: requirement''', 'B', None, imod, config)
        reqset.add_node(RequirementDNode(req2))
        config.set_depends_on()

        rdep = RDepDependsOn(config)
        status = rdep.rewrite(reqset)

        assert(status == False)

    def test_negative_04(self):
        "Normal requirement has empty 'Depends on'"
        config = TestConfig()

        imod = InputModules("..", config)

        reqset = RequirementSet(config)
        req1 = Requirement('''Name: A
Type: master requirement''', 'A', None, imod, config)
        reqset.add_node(RequirementDNode(req1))
        req2 = Requirement('''Name: B
Type: requirement
Depends on:''', 'B', None, imod, config)
        reqset.add_node(RequirementDNode(req2))
        config.set_depends_on()

        rdep = RDepDependsOn(config)
        status = rdep.rewrite(reqset)

        assert(status == False)

    def test_negative_05(self):
        "'Depends on' points to a non existing requirement"
        config = TestConfig()

        imod = InputModules("..", config)

        reqset = RequirementSet(config)
        req1 = Requirement('''Name: A
Type: master requirement''', 'A', None, imod, config)
        reqset.add_node(RequirementDNode(req1))
        req2 = Requirement('''Name: B
Type: requirement
Depends on: C''', 'B', None, imod, config)
        reqset.add_node(RequirementDNode(req2))
        config.set_depends_on()

        rdep = RDepDependsOn(config)
        status = rdep.rewrite(reqset)

        assert(status == False)

    def test_negative_07(self):
        "'Depends on' points to same requirement"
        config = TestConfig()

        imod = InputModules("..", config)

        reqset = RequirementSet(config)
        req1 = Requirement('''Name: A
Type: master requirement''', 'A', None, imod, config)
        reqset.add_node(RequirementDNode(req1))
        req2 = Requirement('''Name: B
Type: requirement
Depends on: B''', 'B', None, imod, config)
        reqset.add_node(RequirementDNode(req2))
        config.set_depends_on()

        rdep = RDepDependsOn(config)
        status = rdep.rewrite(reqset)

        assert(status == False)
