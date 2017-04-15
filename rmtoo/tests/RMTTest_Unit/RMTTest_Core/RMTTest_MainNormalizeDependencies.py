#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
#  Unit test for calling main of Normalize Dependencies
#
# (c) 2011 on flonatel
#
# For licencing details see COPYING
#
import sys

from rmtoo.lib.main.NormalizeDependencies import main
from rmtoo.lib.RMTException import RMTException

class RMTTest_MainNormalizeDependencies:

    def rmttest_neg_01(self):
        "NormalizeDependencies: check if result is correctly handled: Exception"
        global myexit_called
        myexit_called = False
        global myexit_val
        myexit_val = None

        def myexit(n):
            global myexit_called
            myexit_called = True
            global myexit_val
            myexit_val = n

        def mymain(args, mstdout, mstderr):
            raise RMTException(63, "test thingy")

        main(None, None, sys.stderr, mymain, myexit)
        assert(myexit_called == True)
        assert(myexit_val == 1)

