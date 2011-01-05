#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# Unit Test cases for MemLogStore
#
# (c) 2010-2011 by flonatel
#
# For licencing details see COPYING
#

import StringIO

from rmtoo.lib.MemLogStore import MemLogStore, MemLog
from rmtoo.lib.RMTException import RMTException

class TestMemLogStore:

    def test_positive_01(self):
        "MemLogStore: Check error msg - only message"

        mls = MemLogStore()
        mls.error(77, "ErrMsg")
        sio = StringIO.StringIO()
        mls.write_log(sio)
        assert(sio.getvalue()=="+++ Error: 77:ErrMsg\n")

    def test_positive_02(self):
        "MemLogStore: Check error msg - file"

        mls = MemLogStore()
        mls.error(77, "ErrMsg", "EFile")
        sio = StringIO.StringIO()
        mls.write_log(sio)
        assert(sio.getvalue()=="+++ Error: 77:EFile:ErrMsg\n")

    def test_positive_03(self):
        "MemLogStore: Check error msg - line"

        mls = MemLogStore()
        mls.error(77, "ErrMsg", None, "ELine")
        sio = StringIO.StringIO()
        mls.write_log(sio)
        assert(sio.getvalue()=="+++ Error: 77:ELine:ErrMsg\n")

    def test_positive_04(self):
        "MemLogStore: Check error msg - file and line"

        mls = MemLogStore()
        mls.error(77, "ErrMsg", "EFile", "ELine")
        sio = StringIO.StringIO()
        mls.write_log(sio)
        assert(sio.getvalue()=="+++ Error: 77:EFile:ELine:ErrMsg\n")

    def test_positive_05(self):
        "MemLogStore: Check error msg - only message - easy cmp"

        mls = MemLogStore()
        mls.error(77, "ErrMsg")
        assert(mls==MemLogStore.create_mls(
                [ [77, MemLog.error, "ErrMsg"] ]))

    def test_positive_06(self):
        "MemLogStore: Check error msg - file - easy cmp"

        mls = MemLogStore()
        mls.error(77, "ErrMsg", "EFile")
        assert(mls==MemLogStore.create_mls(
                [ [77, MemLog.error, "ErrMsg", "EFile"] ]))

    def test_positive_07(self):
        "MemLogStore: Check error msg - line - easy cmp"

        mls = MemLogStore()
        mls.error(77, "ErrMsg", None, "ELine")
        assert(mls==MemLogStore.create_mls(
                [ [77, MemLog.error, "ErrMsg", None, "ELine"] ]))

    def test_positive_08(self):
        "MemLogStore: Check error msg - file and line"

        mls = MemLogStore()
        mls.error(77, "ErrMsg", "EFile", "ELine")
        assert(mls==MemLogStore.create_mls(
                [ [77, MemLog.error, "ErrMsg", "EFile", "ELine"] ]))

    def test_positive_09(self):
        "MemLogStore: Check debug msg"

        mls = MemLogStore()
        mls.debug(77, "DebugMsg", "EFile", "ELine")
        assert(mls==MemLogStore.create_mls(
                [ [77, MemLog.debug, "DebugMsg", "EFile", "ELine"] ]))

    def test_positive_10(self):
        "MemLogStore: Check info msg"

        mls = MemLogStore()
        mls.info(77, "InfoMsg", "EFile", "ELine")
        assert(mls==MemLogStore.create_mls(
                [ [77, MemLog.info, "InfoMsg", "EFile", "ELine"] ]))

    def test_positive_11(self):
        "MemLogStore: Check to_list - without file and line"

        mls = MemLogStore()
        mls.info(77, "InfoMsg")
        l = mls.to_list()
        assert(mls==MemLogStore.create_mls(l))

    def test_positive_12(self):
        "MemLogStore: Check to_list - without line"

        mls = MemLogStore()
        mls.info(77, "InfoMsg", "EFile")
        l = mls.to_list()
        assert(mls==MemLogStore.create_mls(l))

    def test_positive_13(self):
        "MemLogStore: Check to_list - without file"

        mls = MemLogStore()
        mls.info(77, "InfoMsg", None, "ELine")
        l = mls.to_list()
        assert(mls==MemLogStore.create_mls(l))

    def test_positive_14(self):
        "MemLogStore: Check to_list - with file and line"

        mls = MemLogStore()
        mls.info(77, "InfoMsg", "EFile", "ELine")
        l = mls.to_list()
        assert(mls==MemLogStore.create_mls(l))

    def test_negative_01(self):
        "Check if the exception for invalid log level works"

        try:
            ml = MemLog(77, 77771, "ErrMsg")
            assert(False)
        except RMTException, rmte:
            assert(rmte.id()==52)
