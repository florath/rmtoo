'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit Test cases for Requirement

 (c) 2010,2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals

from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RMTException import RMTException
from rmtoo.tests.lib.TestConfig import TestConfig


class RMTTestRequirement:

    def rmttest_positive_01(self):
        "Requirement: parser returns error"

        try:
            Requirement("DTag: content1\n"
                        "DTag: content2\n", "1", None,
                        None, TestConfig())
            assert(False)
        except RMTException as rmte:
            assert(rmte.get_id() == 81)
