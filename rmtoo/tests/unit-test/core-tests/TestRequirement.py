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

class TestRequirement:

    def test_positive_01(self):
        "Requirement: parser returns error"

        sio = StringIO.StringIO("DTag: content1\n"
                                "DTag: content2\n")
        req = Requirement(sio, 1, MemLogStore(), None, None, None)
        assert(req.state==Requirement.er_error)
