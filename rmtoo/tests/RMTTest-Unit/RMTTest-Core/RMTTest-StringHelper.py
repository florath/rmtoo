#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
#  Unit test for StringHelper
#
# (c) 2011,2017 on flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.StringHelper import StringHelper


class RMTTest_StringHelper:

    def rmttest_pos_01(self):
        "StringHelper.join_ate with elements"

        s = StringHelper.join_ate("-", ["a", "b", "c", "d"])
        assert s == "a-b-c-d-"

    def rmttest_pos_02(self):
        "StringHelper.join_ate empty list"

        s = StringHelper.join_ate("-", [])
        assert s == ""
