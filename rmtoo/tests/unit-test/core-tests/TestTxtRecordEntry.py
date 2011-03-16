#
# rmtoo 
#   Free and Open Source Requirements Management Tool
#
#  Unit test for TxtRecordEntry
#
# (c) 2011 on flonatel
#
# For licencing details see COPYING
#

import StringIO

from rmtoo.lib.storagebackend.txtfile.TxtRecordEntry import TxtRecordEntry

class TestTxtRecordEntry:

    def test_pos_01(self):
        "Check format entry with existing comment"
        tre = TxtRecordEntry(["mtag:", [" iline"], ["# Comment"] ])

        r = TxtRecordEntry.format_entry(tre)
        expres = "mtag: iline\n#  Comment\n"
        assert(r==expres)

    def test_pos_02(self):
        "Check fd output with no raw comment"

        tre = TxtRecordEntry(["mtag:", [" iline"], ["# Comment"] ])
        tre.set_comment("A new comment")
        fd = StringIO.StringIO()
        tre.write_fd(fd)

        expres = "mtag: iline\n# A new comment\n"
        assert(fd.getvalue()==expres)
