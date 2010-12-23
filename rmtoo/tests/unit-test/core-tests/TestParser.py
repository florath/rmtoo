#
# Parser Test Class
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

import StringIO

from rmtoo.lib.Parser import Parser, ParserHelper
from rmtoo.lib.RMTException import RMTException
from rmtoo.tests.lib.TestConfig import TestConfig

def tparsefunc_invalid(rid, line, lineno, pconfig):
    return 77, None, None

class tst_container:
    pass


class TestParser:

    def test_positive_01(self):
        "Check erase_tailing_newline: text without newline"
        
        r = ParserHelper.erase_tailing_newline("Hi")
        assert(r=="Hi")

    def test_positive_02(self):
        "Check erase_tailing_newline: text with newline"
        
        r = ParserHelper.erase_tailing_newline("Hi\n")
        assert(r=="Hi")

    def test_positive_03(self):
        "Check erase_tailing_newline: empty with newline"
        
        r = ParserHelper.erase_tailing_newline("\n")
        assert(r=="")

    def test_positive_04(self):
        "Check erase_tailing_newline: empty without newline"
        
        r = ParserHelper.erase_tailing_newline("")
        assert(r=="")

    def test_positive_05(self):
        "Check impossible state handling in parse function"

        try:
            sio = StringIO.StringIO("Hi\n")
            tstcntr = tst_container()
            a, b, c = Parser.read_as_container(1, sio, tstcntr, TestConfig(),
                                               tparsefunc_invalid)
            assert(False)
        except RMTException, rmte:
            assert(rmte.id()==53)

                                           
