#
# rmtoo 
#  Record Text Test Class
#
# (c) 2010-2011 by flonatel
#
# For licencing details see COPYING
#
import StringIO
from rmtoo.lib.storagebackend.Record import RecordAsDict
from rmtoo.lib.storagebackend.txtfile.TxtParser import TxtParser
from rmtoo.tests.lib.TestConfig import TestConfig

class NOTestRecordTxt:

    def test_pos_01(self):
        "Check top level RecordAsMap"

        doc = """# Comment for whole record

# ... with empty lines.
Name: meiner
# Comment for Name
Rationale: Its because.
# Comment for Rationale 1
# Comment for Rationale 2
Note: This is my Note.
# Comment for Note 1 (before empty line)

# Comment for Note 2 (after empty line)
"""

        txt_doc = RecordAsDict(TxtParser.from_string(doc))

        print("Tag name: %s" % txt_doc["Name"])
        print("Tag Note: %s" % txt_doc["Note"])
