#
# Requirement Management Toolset
#
# Unit test for RequirementParser
#
# (c) 2010 on flonatel
#
# For licencing details see COPYING
#

import StringIO
from rmtoo.lib.RequirementParser import RequirementParser

class TestRequirementParser:

    def test_positive_01(self):
        "Parser Test: empty lines"
        sf = StringIO.StringIO("\n\n\n")
        req = RequirementParser.read("Parser-Test", sf)
        assert(req=={})

    def test_positive_02(self):
        "Parser Test: comment lines"
        sf = StringIO.StringIO("# Hallo\n# A small text\n# \n")
        req = RequirementParser.read("Parser-Test", sf)
        assert(req=={})

    def test_positive_03(self):
        "Parser Test: continue line"
        sf = StringIO.StringIO("Test: long long\n long value\n")
        req = RequirementParser.read("Parser-Test", sf)
        assert(req=={'Test': 'long long long value'})

    def test_negative_01(self):
        "Parser Test: line too long"
        sf = StringIO.StringIO("Test: long long long long long"
                               "long long long long long long long long"
                               "long long long long long long long long"
                               "long long long long long long long long"
                               "line\n")
        req = RequirementParser.read("Parser-Test", sf)
        assert(req==None)
        
    def test_negative_02(self):
        "Parser Test: no colon in line"
        sf = StringIO.StringIO("Test; something\n")
        req = RequirementParser.read("Parser-Test", sf)
        assert(req==None)

    def test_negative_03(self):
        "Parser Test: colon in first column"
        sf = StringIO.StringIO(": something\n")
        req = RequirementParser.read("Parser-Test", sf)
        assert(req==None)

    def test_negative_04(self):
        "Parser Test: continue line without initial tag line"
        sf = StringIO.StringIO(" something\n")
        req = RequirementParser.read("Parser-Test", sf)
        assert(req==None)

    def test_negative_05(self):
        "Parser Test: two times the same tag"
        sf = StringIO.StringIO("AlreadyThere: something\nAlreadyThere: something else\n")
        req = RequirementParser.read("Parser-Test", sf)
        assert(req==None)
        
