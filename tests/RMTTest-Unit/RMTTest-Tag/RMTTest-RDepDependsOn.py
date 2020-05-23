'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for RDepDependsOn

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals


from rmtoo.inputs.RDepDependsOn import RDepDependsOn
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RequirementSet import RequirementSet
from TestConfig import TestConfig
from rmtoo.lib.InputModules import InputModules


class RMTTestRDepDependsOn(object):

    def rmttest_positive_01(self):
        "Two node one edge digraph B -> A"
        config = TestConfig()

        imod = InputModules(config)

        reqset = RequirementSet(config)
        req1 = Requirement('''Name: A
Type: master requirement''', 'A', None, imod, config)
        reqset.add_requirement(req1)
        req2 = Requirement('''Name: B
Type: requirement
Depends on: A''', 'B', None, imod, config)
        reqset.add_requirement(req2)
        config.set_depends_on()

        rdep = RDepDependsOn(config)
        rdep.rewrite(reqset)

        assert [] == reqset.get_requirement("A").incoming_as_named_list()
        assert ["B"] == reqset.get_requirement("A").outgoing_as_named_list()
        assert ["A"] == reqset.get_requirement("B").incoming_as_named_list()
        assert [] == reqset.get_requirement("B").outgoing_as_named_list()

    def rmttest_positive_02(self):
        "Three node one edge digraph B -> A, C -> A and C -> B"
        config = TestConfig()

        imod = InputModules(config)

        reqset = RequirementSet(config)
        req1 = Requirement('''Name: A
Type: master requirement''', 'A', None, imod, config)
        reqset.add_requirement(req1)
        req2 = Requirement('''Name: B
Type: requirement
Depends on: A''', 'B', None, imod, config)
        reqset.add_requirement(req2)
        config.set_depends_on()
        req3 = Requirement('''Name: C
Type: requirement
Depends on: A B''', 'C', None, imod, config)
        reqset.add_requirement(req3)
        config.set_depends_on()

        rdep = RDepDependsOn(config)
        rdep.rewrite(reqset)

        assert [] == reqset.get_requirement("A").incoming_as_named_list()
        # There are two possible valid results
        assert reqset.get_requirement("A").outgoing_as_named_list() \
            in [["C", "B"], ["B", "C"]]
        assert ["A"] == reqset.get_requirement("B").incoming_as_named_list()
        assert ["C"] == reqset.get_requirement("B").outgoing_as_named_list()
        assert ["A", "B"] == reqset.get_requirement(
            "C").incoming_as_named_list()
        assert [] == reqset.get_requirement("C").outgoing_as_named_list()

    def rmttest_negative_01(self):
        "Master requirement with Depends on field"
        config = TestConfig()

        imod = InputModules(config)

        reqset = RequirementSet(config)
        req1 = Requirement('''Name: A
Type: master requirement
Depends on: A''', 'A', None, imod, config)
        reqset.add_requirement(req1)
        config.set_depends_on()

        rdep = RDepDependsOn(config)
        status = rdep.rewrite(reqset)

        assert not status

    def rmttest_negative_03(self):
        "Normal requirement has no 'Depends on'"
        config = TestConfig()

        imod = InputModules(config)

        reqset = RequirementSet(config)
        req1 = Requirement('''Name: A
Type: master requirement''', 'A', None, imod, config)
        reqset.add_requirement(req1)
        req2 = Requirement('''Name: B
Type: requirement''', 'B', None, imod, config)
        reqset.add_requirement(req2)
        config.set_depends_on()

        rdep = RDepDependsOn(config)
        status = rdep.rewrite(reqset)

        assert not status

    def rmttest_negative_04(self):
        "Normal requirement has empty 'Depends on'"
        config = TestConfig()

        imod = InputModules(config)

        reqset = RequirementSet(config)
        req1 = Requirement('''Name: A
Type: master requirement''', 'A', None, imod, config)
        reqset.add_requirement(req1)
        req2 = Requirement('''Name: B
Type: requirement
Depends on:''', 'B', None, imod, config)
        reqset.add_requirement(req2)
        config.set_depends_on()

        rdep = RDepDependsOn(config)
        status = rdep.rewrite(reqset)

        assert not status

    def rmttest_negative_05(self):
        "'Depends on' points to a non existing requirement"
        config = TestConfig()

        imod = InputModules(config)

        reqset = RequirementSet(config)
        req1 = Requirement('''Name: A
Type: master requirement''', 'A', None, imod, config)
        reqset.add_requirement(req1)
        req2 = Requirement('''Name: B
Type: requirement
Depends on: C''', 'B', None, imod, config)
        reqset.add_requirement(req2)
        config.set_depends_on()

        rdep = RDepDependsOn(config)
        status = rdep.rewrite(reqset)

        assert not status

    def rmttest_negative_07(self):
        "'Depends on' points to same requirement"
        config = TestConfig()

        imod = InputModules(config)

        reqset = RequirementSet(config)
        req1 = Requirement('''Name: A
Type: master requirement''', 'A', None, imod, config)
        reqset.add_requirement(req1)
        req2 = Requirement('''Name: B
Type: requirement
Depends on: B''', 'B', None, imod, config)
        reqset.add_requirement(req2)
        config.set_depends_on()

        rdep = RDepDependsOn(config)
        status = rdep.rewrite(reqset)

        assert not status
