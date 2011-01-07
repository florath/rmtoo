#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
#  Record Text Test Class
#
# (c) 2010-2011 by flonatel
#
# For licencing details see COPYING
#
import StringIO
from rmtoo.lib.storagebackend.txtfile.TxtRecord import TxtRecord
from rmtoo.lib.storagebackend.RecordEntry import RecordEntry
from rmtoo.tests.lib.TestConfig import TestConfig

dp1 = """# Comment for whole record

# ... with empty lines.
"""

dp2 = """Name: meiner
# Comment for Name
"""

dp3 = """Rationale: It's because.
 And another reason.
 And maybe a third one.
# Comment for Rationale 1
# Comment for Rationale 2
"""

dp4 = """Note: This is my Note.
# Comment for Note 1 (before empty line)

# Comment for Note 2 (after empty line)
"""

dpA = """Hinzu: This is quite new.
"""

doc1 = dp1 + dp2 + dp3 + dp4
doc2 = dp1 + dp2 + dp3 + dpA + dp4
doc3 = dp1 + dp2 + dp3

dpC1 = """ Comment for whole record

 ... with empty lines.
"""

class TestRecordTxt:

    def test_pos_01(self):
        "Check top level RecordAsDict (string)"

        txt_doc = TxtRecord.from_string(doc1)
        txt_doc_dict = txt_doc.get_dict()

        assert(txt_doc.get_comment() == dpC1)
        assert(txt_doc_dict["Name"].get_content() == "meiner")
        assert(txt_doc_dict["Note"].get_content() == "This is my Note.")
        assert(txt_doc.to_string()==doc1)

    def test_pos_02(self):
        "Check top level RecordAsDict (fd)"

        fd = StringIO.StringIO(doc1)
        txt_doc = TxtRecord.from_fd(fd)
        txt_doc_dict = txt_doc.get_dict()

        assert(txt_doc.get_comment() == dpC1)
        assert(txt_doc_dict["Name"].get_content() == "meiner")
        assert(txt_doc_dict["Note"].get_content() == "This is my Note.")
        assert(txt_doc.to_string()==doc1)

    def test_pos_03(self):
        "Check top level Record: add entry"

        txt_doc = TxtRecord.from_string(doc1)
        txt_doc.insert(2, RecordEntry("Hinzu", "This is quite new."))
        txt_doc_dict = txt_doc.get_dict()

        assert(txt_doc.get_comment() == dpC1)
        assert(txt_doc_dict["Name"].get_content() == "meiner")
        assert(txt_doc_dict["Note"].get_content() == "This is my Note.")
        assert(txt_doc.to_string()==doc2)

    def test_pos_04(self):
        "Check top level Record: remove entry"

        txt_doc = TxtRecord.from_string(doc1)
        del(txt_doc[2])
        txt_doc_dict = txt_doc.get_dict()

        #print("ALL '%s'" % txt_doc.to_string())

        assert(txt_doc.get_comment() == dpC1)
        assert(txt_doc_dict["Name"].get_content() == "meiner")
        # 'Note' is not available - it was deleted.
        try:
            txt_doc_dict["Note"].get_content()
            assert(False)
        except KeyError, ke:
            pass
        assert(txt_doc.to_string()==doc3)
