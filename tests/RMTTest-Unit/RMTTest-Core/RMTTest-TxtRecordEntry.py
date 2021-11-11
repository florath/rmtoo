'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for TxtRecordEntry

 (c) 2011,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


from rmtoo.lib.storagebackend.txtfile.TxtRecordEntry import TxtRecordEntry


class RMTTestTxtRecordEntry(object):

    def rmttest_pos_01(self):
        "Check format entry with existing comment"
        tre = TxtRecordEntry(["mtag:", [" iline"], ["# Comment"]])

        r = TxtRecordEntry.format_entry(tre)
        expres = "mtag: iline\n#  Comment\n"
        assert expres == r

    def rmttest_pos_02(self):
        "Check fd output with no raw comment"

        tre = TxtRecordEntry(["mtag:", [" iline"], ["# Comment"]])
        tre.set_comment("A new comment")
        fd = StringIO()
        tre.write_fd(fd)

        expres = "mtag: iline\n# A new comment\n"
        assert expres == fd.getvalue()
