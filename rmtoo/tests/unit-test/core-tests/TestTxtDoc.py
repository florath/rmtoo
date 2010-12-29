#
# rmtoo 
#  Txt Document Test Class
#
# (c) 2010-2011 by flonatel
#
# For licencing details see COPYING
#
import StringIO
from rmtoo.lib.TxtDoc import TxtDocAsMap
from rmtoo.tests.lib.TestConfig import TestConfig

class TestTxtDoc:

    def test_pos_01(self):
        "Check top level get_as_map() method"

        doc = """# Comment for Name
Name: meiner
# Comment for Rationale 1
# Comment for Rationale 2
Rationale: Its because.
# Comment for Note 1 (before empty line)

# Comment for Note 2 (after empty line)
Note: This is my Note.
"""

        sfd = StringIO.StringIO(doc)

        txt_doc = TxtDocAsMap("myid", sfd, TestConfig())

        print("Tag name: %s" % txt_doc["Name"])
        print("Tag Note: %s" % txt_doc["Note"])
