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

from rmtoo.lib.main.NormalizeDependencies import parse_cmd_line_opts, main
from rmtoo.lib.RMTException import RMTException

class TestMainNormalizeDependencies:

    def test_pos_01(self):
        "NormalizeDependencies: check command line parameters: standard module"

        opt = parse_cmd_line_opts(["-f", "somewhere", "hubbel"])
        assert(opt.modules_directory=="/usr/share/pyshared")

    def test_pos_02(self):
        "NormalizeDependencies: check command line parameters: no config"

        try:
            opt = parse_cmd_line_opts(["hubbel"])
            assert(False)
        except RMTException, rmte:
            assert(rmte.get_id()==82)

    def test_pos_03(self):
        "NormalizeDependencies: check command line parameters: no dir"

        try:
            opt = parse_cmd_line_opts(["-f", "somewhere"])
            assert(False)
        except RMTException, rmte:
            assert(rmte.get_id()==83)

    def test_neg_01(self):
        "NormalizeDependencies: check if result is correctly handled: Exception"
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

        main(None, None, sys.stderr, mymain, myexit)
        assert(myexit_called==True)
        assert(myexit_val==1)

