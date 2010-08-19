#
# RMTException Test Class
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.RMTException import RMTException

class TestRMTException:

    def test_positive_01(self):
        "Checks the __str__ method"
    
        rmte = RMTException(77, "ExceptMsg")
        s = rmte.__str__()
        assert(s==' 77: ExceptMsg')
