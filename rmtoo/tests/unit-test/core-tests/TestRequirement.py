#
# Unit Test cases for Requirement
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

import StringIO

from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.MemLogStore import MemLogStore
from rmtoo.tests.lib.TestConfig import TestConfig

class TestRequirement:

    def test_positive_01(self):
        "Requirement: parser returns error"

        sio = StringIO.StringIO("DTag: content1\n"
                                "DTag: content2\n")
        try:
            req = Requirement(sio, 1, MemLogStore(), None, TestConfig())
            assert(False)
        except RMTException, rmte:
            assert(rmte.get_id() == 81)
