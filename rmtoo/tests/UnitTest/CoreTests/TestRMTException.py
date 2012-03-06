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
        "Checks the __str__ method: no file, no line"
    
        rmte = RMTException(77, "ExceptMsg")

        assert(rmte.get_id()==77)
        assert(rmte.get_msg()=="ExceptMsg")
        assert(rmte.get_efile()==None)
        assert(rmte.get_eline()==None)
        assert(rmte.__str__()=='[  77]: ExceptMsg')

    def test_positive_02(self):
        "Checks the __str__ method: with file, no line"
    
        rmte = RMTException(77, "ExceptMsg", "MyFile")

        assert(rmte.get_id()==77)
        assert(rmte.get_msg()=="ExceptMsg")
        assert(rmte.get_efile()=="MyFile")
        assert(rmte.get_eline()==None)
        assert(rmte.__str__()=='[  77]:MyFile: ExceptMsg')

    def test_positive_03(self):
        "Checks the __str__ method: with file, with line"
    
        rmte = RMTException(77, "ExceptMsg", "MyFile", 678)

        assert(rmte.get_id()==77)
        assert(rmte.get_msg()=="ExceptMsg")
        assert(rmte.get_efile()=="MyFile")
        assert(rmte.get_eline()==678)
        assert(rmte.__str__()=='[  77]:MyFile:678: ExceptMsg')
