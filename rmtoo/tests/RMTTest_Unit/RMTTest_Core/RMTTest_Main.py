'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for calling main

 (c) 2010,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import sys

from rmtoo.lib.RmtooMain import main_impl
from rmtoo.lib.RMTException import RMTException

class RMTTest_Main:

    def rmttest_positive_01(self):
        "main: check if result is correctly handled: True"
        global myexit_called
        myexit_called=False
        global myexit_val
        myexit_val=None

        def myexit(n):
            global myexit_called
            myexit_called=True
            global myexit_val
            myexit_val=n

        def mymain(args, mstdout, mstderr):
            return True

        main_impl(None, None, None, mymain, myexit)
        assert(myexit_called==True)
        assert(myexit_val==0)

    def rmttest_positive_02(self):
        "main: check if result is correctly handled: False"
        global myexit_called
        myexit_called=False
        global myexit_val
        myexit_val=None

        def myexit(n):
            global myexit_called
            myexit_called=True
            global myexit_val
            myexit_val=n

        def mymain(args, mstdout, mstderr):
            return False

        main_impl(None, None, None, mymain, myexit)
        assert(myexit_called==True)
        assert(myexit_val==1)

    def rmttest_neg_01(self):
        "main: check if result is correctly handled: Exception"
        global myexit_called
        myexit_called=False
        global myexit_val
        myexit_val=None

        def myexit(n):
            global myexit_called
            myexit_called=True
            global myexit_val
            myexit_val=n

        def mymain(args, mstdout, mstderr):
            raise RMTException(63, "test thingy")

        main_impl(None, None, sys.stderr, mymain, myexit)
        assert(myexit_called==True)
        assert(myexit_val==1)

