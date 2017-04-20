'''
 rmtoo
   Free and Open Source Requirements Management Tool

 RMTException Test Class

 (c) 2010,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import unittest

from rmtoo.lib.RMTException import RMTException


class RMTTestRMTException(unittest.TestCase):

    def rmttest_positive_01(self):
        "Checks the __str__ method: no file, no line"

        rmte = RMTException(77, "ExceptMsg")

        self.assertEqual(77, rmte.get_id())
        self.assertEqual("ExceptMsg", rmte.get_msg())
        self.assertIsNone(rmte.get_efile())
        self.assertIsNone(rmte.get_eline())
        self.assertEqual('[  77]: ExceptMsg', rmte.__str__())

    def rmttest_positive_02(self):
        "Checks the __str__ method: with file, no line"

        rmte = RMTException(77, "ExceptMsg", "MyFile")

        self.assertEqual(77, rmte.get_id())
        self.assertEqual("ExceptMsg", rmte.get_msg())
        self.assertEqual("MyFile", rmte.get_efile())
        self.assertIsNone(rmte.get_eline())
        self.assertEqual('[  77]:MyFile: ExceptMsg', rmte.__str__())

    def rmttest_positive_03(self):
        "Checks the __str__ method: with file, with line"

        rmte = RMTException(77, "ExceptMsg", "MyFile", 678)

        self.assertEqual(77, rmte.get_id())
        self.assertEqual("ExceptMsg", rmte.get_msg())
        self.assertEqual("MyFile", rmte.get_efile())
        self.assertEqual(678, rmte.get_eline())
        self.assertEqual('[  77]:MyFile:678: ExceptMsg', rmte.__str__())
