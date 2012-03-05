'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Test case for handling BaseRMObjects
   
 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import StringIO
from rmtoo.lib.logging.MemLogStore import MemLogStore
from rmtoo.lib.BaseRMObject import BaseRMObject
from rmtoo.lib.storagebackend.txtfile.TxtIOConfig import TxtIOConfig
from rmtoo.tests.lib.TestConfig import TestConfig

class TMods:

    def get_type_set(self):
        return [1, 2, 3]

class TBRMObj(BaseRMObject):

    def __init__(self):
        tc = TestConfig()
        tc.set_value('input.txtfile.whatsoever.max_line_length', 80)
        tm = TMods()
        tm.tagtypes = {"mytag": {"keyA": TMods()}}
        self.mls = MemLogStore()
        BaseRMObject.__init__(self, "mytag", "", "MRid", self.mls, tm,
                              tc, "tobjs", None)

class TestBaseRMObject:

    def test_neg_01(self):
        "BaseRMObject: check for module which has wrong type"

        tbrmo = TBRMObj()

        assert(tbrmo.mls.to_list() ==
               [[90, 'error', 'Wrong module type [mytag] not in [[1, 2, 3]]']])
