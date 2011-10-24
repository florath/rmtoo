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
from rmtoo.lib.storagebackend.txtfile.TxtParser import TxtParser
from rmtoo.lib.storagebackend.txtfile.TxtIOConfig import TxtIOConfig
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.MemLogStore import MemLogStore, MemLog

class TestRecordTxt2:

    def test_pos_01(self):
        "TestRecordTxt2: empty input"

        txt_doc = TxtRecord.from_string("", "Nothing", TxtIOConfig())

        assert(len(txt_doc) == 0)
        assert(txt_doc.get_comment() == "")

    def test_neg_01(self):
        "TestRecordTxt2: rubbish in input"

        txt_doc = TxtRecord.from_string("rubbish", "Rubbish",
                                        TxtIOConfig())

        assert(txt_doc.is_usable() == False)
        assert(txt_doc.to_list() ==
               [[79, MemLog.error,
                 'Expected tag line not found', 'Rubbish', 1]])

    def test_neg_02(self):
        "TestRecordTxt2: only ':'"

        txt_doc = TxtRecord.from_string(":", "Rubbish", TxtIOConfig())
        assert(txt_doc.is_usable() == False)
        assert(txt_doc.to_list() ==
               [[79, MemLog.error,
                 'Expected tag line not found', 'Rubbish', 1]])

    def test_neg_03(self):
        "TestRecordTxt2: no chars before ':'"

        txt_doc = TxtRecord.from_string(": something", "Rubbish",
                                        TxtIOConfig())
        assert(txt_doc.is_usable() == False)
        assert(txt_doc.to_list() ==
               [[79, MemLog.error,
                 'Expected tag line not found', 'Rubbish', 1]])

    def test_neg_04(self):
        "TestRecordTxt2: long long line"

        tioconfig = TxtIOConfig()
        tioconfig.max_line_length = 7
        txt_doc = TxtRecord.from_string("good: but too long",
                                        "TooLong", tioconfig)

        assert(txt_doc.is_usable() == False)
        assert(txt_doc.to_list() ==
               [[80, MemLog.error, 'line too long: is [18], max allowed [7]',
                 'TooLong', 1]])

    def test_neg_05(self):
        "TestRecordTxt2: long long line - check for lineno"

        tioconfig = TxtIOConfig()
        tioconfig.max_line_length = 7
        txt_doc = TxtRecord.from_string("""# com
ok: yes
 no
# cs
# dds
good: but too long
# dds

""",
                                        "TooLong", tioconfig)

        assert(txt_doc.is_usable() == False)
        assert([[80, MemLog.error, 'line too long: is [18], max allowed [7]',
                  'TooLong', 6]] == txt_doc.to_list())

    def test_neg_06(self):
        "TestRecordTxt2: long long line - check for multiple errors"

        tioconfig = TxtIOConfig()
        tioconfig.max_line_length = 7
        txt_doc = TxtRecord.from_string("""#1 com
ok: yes
 no
#4 cs
#5 dds
good: but too long
#7 dds
#8 hi
also good: but too long
#10 gsst
 dhd
#12 dhdh 
d:
#14
""",
                                        "TooLong", tioconfig)

        assert(txt_doc.is_usable() == False)
        assert(txt_doc.to_list() ==
               [[80, MemLog.error, 'line too long: is [18], max allowed [7]',
                 'TooLong', 6],
                [80, MemLog.error, 'line too long: is [23], max allowed [7]',
                 'TooLong', 9],
                [80, MemLog.error, 'line too long: is [8], max allowed [7]',
                 'TooLong', 10],
                [80, MemLog.error, 'line too long: is [9], max allowed [7]',
                 'TooLong', 12],
                [80, MemLog.info, TxtParser.comment_in_req, 'TooLong', 11]])


    def test_neg_07(self):
        "TestRecordTxt2: test comments between content lines"

        tioconfig = TxtIOConfig()
        txt_doc = TxtRecord.from_string("""#1 com
t1: uuuu
#3 Comment not allowed here.
#4 Should emitt a warning
 vvvv
t2: uuuu
 vvvv
#8 Here a comment is also not allowed
 wwww
t3: uuuu
#11 Same as t1 but with additional 
#12 comment at the end of the requirement
 vvvv
#14 End comment for t3
t4: uuuu
 vvvv
#17 Same as t2 but with additional 
#18 comment at the end of the requirement
 wwww
#20 End comment for t4
""",
                                        "CommentsEverywhere", tioconfig)

        assert(txt_doc.is_usable() == True)

        assert(txt_doc.to_list() ==
               [[80, MemLog.info, TxtParser.comment_in_req,
                 'CommentsEverywhere', 5],
                [80, MemLog.info, TxtParser.comment_in_req,
                 'CommentsEverywhere', 9],
                [80, MemLog.info, TxtParser.comment_in_req,
                 'CommentsEverywhere', 13],
                [80, MemLog.info, TxtParser.comment_in_req,
                 'CommentsEverywhere', 19]])

    def test_neg_08(self):
        "TestRecordTxt2: only intro content line"

        tioconfig = TxtIOConfig()
        txt_doc = TxtRecord.from_string("#1 com",
                                        "OnlyEntryComment", tioconfig)

        assert(txt_doc.is_usable() == True)
        assert(txt_doc.to_list() == [])
        assert(txt_doc.get_comment() == "1 com\n")
