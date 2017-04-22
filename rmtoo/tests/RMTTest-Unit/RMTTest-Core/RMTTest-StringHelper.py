'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for StringHelper

 (c) 2011,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
import unittest

from rmtoo.lib.StringHelper import StringHelper


class RMTTestStringHelper(unittest.TestCase):

    def rmttest_pos_01(self):
        "StringHelper.join_ate with elements"

        s = StringHelper.join_ate("-", ["a", "b", "c", "d"])
        self.assertEqual("a-b-c-d-", s)

    def rmttest_pos_02(self):
        "StringHelper.join_ate empty list"

        s = StringHelper.join_ate("-", [])
        self.assertEqual("", s)
