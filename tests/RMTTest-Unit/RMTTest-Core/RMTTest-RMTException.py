'''
 rmtoo
   Free and Open Source Requirements Management Tool

 RMTException Test Class

 (c) 2010,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''


from rmtoo.lib.RMTException import RMTException


class RMTTestRMTException(object):

    def rmttest_positive_01(self):
        "Checks the __str__ method: no file, no line"

        rmte = RMTException(77, "ExceptMsg")

        assert 77 == rmte.get_id()
        assert "ExceptMsg" == rmte.get_msg()
        assert rmte.get_efile() is None
        assert rmte.get_eline() is None
        assert '[  77]: ExceptMsg' == rmte.__str__()

    def rmttest_positive_02(self):
        "Checks the __str__ method: with file, no line"

        rmte = RMTException(77, "ExceptMsg", "MyFile")

        assert 77 == rmte.get_id()
        assert "ExceptMsg" == rmte.get_msg()
        assert "MyFile" == rmte.get_efile()
        assert rmte.get_eline() is None
        assert '[  77]:MyFile: ExceptMsg' == rmte.__str__()

    def rmttest_positive_03(self):
        "Checks the __str__ method: with file, with line"

        rmte = RMTException(77, "ExceptMsg", "MyFile", 678)

        assert 77 == rmte.get_id()
        assert "ExceptMsg" == rmte.get_msg()
        assert "MyFile" == rmte.get_efile()
        assert 678 == rmte.get_eline()
        assert '[  77]:MyFile:678: ExceptMsg' == rmte.__str__()
