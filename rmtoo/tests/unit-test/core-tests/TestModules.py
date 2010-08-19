#
# Unit Test cases for Modules
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.Modules import Modules

class TestModules:

    def test_positive_01(self):
        "Modules.split_directory with '.'"

        d = Modules.split_directory(".")
        assert(d==[])

    def test_positive_02(self):
        "Modules.split_directory with absolute path"

        d = Modules.split_directory("/tmp/this/is/a/path")
        assert(d==['/', 'tmp', 'this', 'is', 'a', 'path'])

