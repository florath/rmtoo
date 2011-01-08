#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# Record Text Test Class: try to run through all the possible states
# and error scenarios.
#
# (c) 2011 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.storagebackend.txtfile.TxtRecord import TxtRecord
from rmtoo.lib.storagebackend.txtfile.TxtIOConfig import TxtIOConfig
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.MemLogStore import MemLogStore

class TestRecordTxt2:

    def test_pos_01(self):
        "TestRecordTxt2: empty input"

        txt_doc = TxtRecord.from_string("", "Nothing", TxtIOConfig())

        assert(len(txt_doc)==0)
        assert(txt_doc.get_comment()=="")

    def test_neg_04(self):
        "TestRecordTxt2: long long line"

        tioconfig = TxtIOConfig()
        tioconfig.set_max_line_length(7)
        txt_doc = TxtRecord.from_string("good: but too long", 
                                        "TooLong", tioconfig)
        assert([['TooLong', 40, 'line too long: is [18], max allowed [7]',
                  None, 1]] == txt_doc.to_list())

    def test_neg_01(self):
        "TestRecordTxt2: rubbish in input"

        try:
            txt_doc = TxtRecord.from_string("rubbish", "Rubbish", 
                                            TxtIOConfig())
            assert(False)
        except RMTException, rmte:
            assert(rmte.id()==79)

    def test_neg_02(self):
        "TestRecordTxt2: only ':'"

        try:
            txt_doc = TxtRecord.from_string(":", "Rubbish", TxtIOConfig())
            assert(False)
        except RMTException, rmte:
            assert(rmte.id()==79)

    def test_neg_03(self):
        "TestRecordTxt2: no chars before ':'"

        try:
            txt_doc = TxtRecord.from_string(": something", "Rubbish", 
                                            TxtIOConfig())
            assert(False)
        except RMTException, rmte:
            assert(rmte.id()==79)

