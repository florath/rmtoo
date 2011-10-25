#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# Test case for handling BaseRMObjects
#
# (c) 2011 by flonatel
#
# For licencing details see COPYING
#

import StringIO
from rmtoo.lib.logging.MemLogStore import MemLogStore
from rmtoo.lib.BaseRMObject import BaseRMObject
from rmtoo.lib.storagebackend.txtfile.TxtIOConfig import TxtIOConfig
from rmtoo.tests.lib.TestConfig import TestConfig

class TMods:

    def type(self):
        return [1, 2, 3]

class TBRMObj(BaseRMObject):

    def __init__(self):
        sfd = StringIO.StringIO()
        tc = TestConfig()
        tc.set_value('input.txtfile.whatsoever.max_line_length', 80)
        tm = TMods()
        tm.tagtypes = {"mytag": {"keyA": TMods()}}
        self.mls = MemLogStore()
        BaseRMObject.__init__(self, "mytag", sfd, "MRid", self.mls, tm,
                              tc, "tobjs")

class TestBaseRMObject:

    def test_neg_01(self):
        "BaseRMObject: check for module which has wrong type"

        tbrmo = TBRMObj()

        print("U!U!U!U [%s]" % tbrmo.mls.to_list())

        assert(tbrmo.mls.to_list() ==
               [[90, 'error', 'Wrong module type [mytag] not in [[1, 2, 3]]']])
