#
# Command Line Parser Test Class
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.RmtooMain import parse_cmd_line_opts
from rmtoo.lib.RMTException import RMTException

class TestCmdLineParser:

    def test_neg_01(self):
        "Command Line Parser: check default -m"

        args = ["-f", "SomeFile" ]
        options = parse_cmd_line_opts(args)
        assert(options.modules_directory == "/usr/share/pyshared")

    def test_neg_02(self):
        "Command Line Parser: no config file given"

        args = [ ]
        try:
            options = parse_cmd_line_opts(args)
            assert(False)
        except RMTException, rmte:
            assert(rmte.id()==60)

    def test_neg_03(self):
        "Command Line Parser: too many args"

        args = ["-f", "SomeFile", "das", "ist", "was"]
        try:
            options = parse_cmd_line_opts(args)
            assert(False)
        except RMTException, rmte:
            assert(rmte.id()==61)

