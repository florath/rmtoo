#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
#  Unit test for Topic
#
# (c) 2011,2017 on flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.storagebackend.txtfile.TxtRecord import TxtRecord


class RMTTestTxtRecord:

    def rmttest_pos_01(self):
        "Check maybe_remove_last_empty_line with len=0"
        config = {}
        tr = TxtRecord(config)
        sl = []
        tr.maybe_remove_last_empty_line(sl)

        assert len(sl) == 0
