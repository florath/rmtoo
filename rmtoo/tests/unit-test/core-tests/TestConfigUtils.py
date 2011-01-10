#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# The test class for ConfigUtils.
#
# (c) 2011 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.ConfigUtils import ConfigUtils
from rmtoo.tests.lib.TestConfig import TestConfig

class TestConfigUtils:

    def test_neg_01(self):
        "Wrong value in dependency_notation"

        tc = TestConfig()
        tc.reqs_spec["dependency_notation"] = set(["Das gibbt es nich",])
        try:
            ConfigUtils.check(tc)
            assert(False)
        except RMTException, rmte:
            assert(rmte.id()==70)

    def test_neg_02(self):
        "Wrong type in requirements max_line_length"

        tc = TestConfig()
        tc.parser = {}
        tc.parser["requirements"] = {}
        tc.parser["requirements"]["max_line_length"] = \
            set(["Das gibbt es nich",])
        try:
            ConfigUtils.set_defaults_parser(tc)
            ConfigUtils.check(tc)
            assert(False)
        except RMTException, rmte:
            assert(rmte.id()==71)

    def test_neg_03(self):
        "Wrong value in requirements max_line_length"

        tc = TestConfig()
        tc.parser = {}
        tc.parser["requirements"] = {}
        tc.parser["requirements"]["max_line_length"] = -112
        try:
            ConfigUtils.set_defaults_parser(tc)
            ConfigUtils.check(tc)
            assert(False)
        except RMTException, rmte:
            assert(rmte.id()==72)
