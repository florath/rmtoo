#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# Record Text Test Class: try to run through all the possible states
# and error scenarios.
# Extended version
#
# (c) 2011 by flonatel
#
# For licencing details see COPYING
#

import StringIO

from rmtoo.lib.storagebackend.txtfile.TxtRecord import TxtRecord
from rmtoo.lib.storagebackend.txtfile.TxtParser import TxtParser
from rmtoo.lib.storagebackend.txtfile.TxtIOConfig import TxtIOConfig
from rmtoo.lib.RMTException import RMTException

tc1i = """Name: rmtoo
Type: master requirement
Invented on: 2010-02-06
Invented by: flonatel
Owner: development
Description: \textsl{rmtoo} \textbf{must} exists.
Rationale: The world needs a good, usable and free Requirements
 Management Tool.\par
 It looks that there are no such programs out.\par
 But: it's complex! 
Status: not done
Priority: development:10
Effort estimation: 5
Topic: ReqsDocument
"""

class TestRecordTxt3:

    def test_pos_01(self):
        "TestRecordTxt3: long long complicated input"

        txt_doc = TxtRecord.from_string(tc1i, "rmtoo", TxtIOConfig())
        d = txt_doc.get_dict()

        o = StringIO.StringIO()
        txt_doc.write_log(o)

        assert(d["Rationale"].get_content() ==
               "The world needs a good, usable and free "
               "Requirements Management Tool.\par It looks "
               "that there are no such programs out.\par But: it's complex! ")

        assert(len(txt_doc) == 11)
        assert(txt_doc.get_comment() == "")


