'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for RequirementSet

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
import unittest

from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.inputs.RDepOneComponent import RDepOneComponent
from rmtoo.lib.RMTException import RMTException


class RMTTestOutputOneComponent(unittest.TestCase):

    def rmttest_neg_01(self):
        "RDepOneComponent: check rewrite error case"

        oc = RDepOneComponent(None)

        dr = Digraph()
        with self.assertRaises(RMTException) as rmte:
            oc.rewrite(dr)
            self.assertEqual(69, rmte.id())
