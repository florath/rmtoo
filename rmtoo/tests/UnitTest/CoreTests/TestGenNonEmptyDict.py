'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Tests for Generic non-empty dictionary.
   
 (c) 2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import unittest

from rmtoo.lib.GenNonEmptyDict import GenNonEmptyDict

class TestGenNonEmptyDict(unittest.TestCase):
    
    def test_int_only_existing(self):
        '''GenNonEmtpyDict:  (int): Only exisiting values.'''
        gned = GenNonEmptyDict(int)
        gned.insert(1, "one")
        gned.insert(2, "two")
        gned.insert(3, "three")
        gned.insert(77, "seventyseven")
        self.assertEqual("one", gned[1])
        self.assertEqual("seventyseven", gned[77])
        
        