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
from rmtoo.lib.Parser import Parser

class TestRequirementParser:

    def test_positive_01a(self):
        "Parser Test 01a: empty lines"
        sf = StringIO.StringIO("\n\n\n")
        req = Parser.read_as_map("Parser-Test", sf)
        assert(req=={})

    def test_positive_01b(self):
        "Parser Test 01b: empty lines"
        sf = StringIO.StringIO("\n\n\n")
        req = Parser.read_as_list("Parser-Test", sf)
        assert(req==[])

    def test_positive_02a(self):
        "Parser Test 02a: comment lines"
        sf = StringIO.StringIO("# Hallo\n# A small text\n# \n")
        req = Parser.read_as_map("Parser-Test", sf)
        assert(req=={})

    def test_positive_02b(self):
        "Parser Test 02b: comment lines"
        sf = StringIO.StringIO("# Hallo\n# A small text\n# \n")
        req = Parser.read_as_list("Parser-Test", sf)
        assert(req==[])

    def test_positive_03a(self):
        "Parser Test 03a: continue line"
        sf = StringIO.StringIO("Test: long long\n long value\n")
        req = Parser.read_as_map("Parser-Test", sf)
        assert(req=={'Test': 'long long long value'})

    def test_positive_03b(self):
        "Parser Test 03b: continue line"
        sf = StringIO.StringIO("Test: long long\n long value\n")
        req = Parser.read_as_list("Parser-Test", sf)
        assert(req==[['Test', 'long long long value']])

    def test_positive_04b(self):
        "Parser Test: two times the same tag"
        sf = StringIO.StringIO("AlreadyThere: something\n"
                               "AlreadyThere: something else\n")
        req = Parser.read_as_list("Parser-Test", sf)

        assert(req==[['AlreadyThere', 'something'], 
                     ['AlreadyThere', 'something else']])

    # This is the same as the last one - except that the tailing newline
    # is not there.
    def test_positive_05b(self):
        "Parser Test: two times the same tag"
        sf = StringIO.StringIO("AlreadyThere: something\n"
                               "AlreadyThere: something else")
        req = Parser.read_as_list("Parser-Test", sf)

        assert(req==[['AlreadyThere', 'something'], 
                     ['AlreadyThere', 'something else']])

    def test_negative_01a(self):
        "Parser Test n01a: line too long"
        sf = StringIO.StringIO("Test: long long long long long"
                               "long long long long long long long long"
                               "long long long long long long long long"
                               "long long long long long long long long"
                               "line\n")
        req = Parser.read_as_map("Parser-Test", sf)
        assert(req==None)

    def test_negative_01b(self):
        "Parser Test n01b: line too long"
        sf = StringIO.StringIO("Test: long long long long long"
                               "long long long long long long long long"
                               "long long long long long long long long"
                               "long long long long long long long long"
                               "line\n")
        req = Parser.read_as_list("Parser-Test", sf)
        assert(req==None)
        
    def test_negative_02a(self):
        "Parser Test n02a: no colon in line"
        sf = StringIO.StringIO("Test; something\n")
        req = Parser.read_as_map("Parser-Test", sf)
        assert(req==None)

    def test_negative_02b(self):
        "Parser Test n02b: no colon in line"
        sf = StringIO.StringIO("Test; something\n")
        req = Parser.read_as_list("Parser-Test", sf)
        assert(req==None)

    def test_negative_03a(self):
        "Parser Test: colon in first column"
        sf = StringIO.StringIO(": something\n")
        req = Parser.read_as_map("Parser-Test", sf)
        assert(req==None)

    def test_negative_03b(self):
        "Parser Test: colon in first column"
        sf = StringIO.StringIO(": something\n")
        req = Parser.read_as_list("Parser-Test", sf)
        assert(req==None)

    def test_negative_04a(self):
        "Parser Test: continue line without initial tag line"
        sf = StringIO.StringIO(" something\n")
        req = Parser.read_as_map("Parser-Test", sf)
        assert(req==None)

    def test_negative_04b(self):
        "Parser Test: continue line without initial tag line"
        sf = StringIO.StringIO(" something\n")
        req = Parser.read_as_list("Parser-Test", sf)
        assert(req==None)

    def test_negative_05a(self):
        "Parser Test: two times the same tag"
        sf = StringIO.StringIO("AlreadyThere: something\n"
                               "AlreadyThere: something else\n")
        req = Parser.read_as_map("Parser-Test", sf)
        assert(req==None)

        
