'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Unit test for Library for comparing XML documents
   
 (c) 2011-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import unittest
import re
from rmtoo.lib.xmlutils.xmlcmp import xmlcmp_strings
from rmtoo.lib.logging import init_logger, tear_down_log_handler
from rmtoo.tests.lib.Utils import hide_timestamp

class RMTTest_XMLCmp(unittest.TestCase):

    def rmttest_pos01(self):
        "xmlcmp: small xml document"
        r, s = xmlcmp_strings('<hu/>', '<hu/>')
        assert(r == True)

    def rmttest_pos02(self):
        "xmlcmp: same tags with different arrtibutes"
        r, s = xmlcmp_strings(
            '<hu><t a="1"/><t b="2"/></hu>',
            '<hu><t b="2"/><t a="1"/></hu>')
        assert(r == True)

    def rmttest_neg01(self):
        "xmlcmp: top level node names differ"
        r, s = xmlcmp_strings('<hu/>', '<hi/>')
        assert(r == False)
        assert(s == "Tag names differ [hu] != [hi] at []")

    def rmttest_neg02(self):
        "xmlcmp: types of subnode differ"
        r, s = xmlcmp_strings('<hu>Mein Text</hu>', '<hu><uj></uj></hu>')
        assert(r == False)
        assert(s == """Child node [<DOM Text node "u'Mein Text'">] not found at [] - last error was [Node types differ [3] != [1] at [/hu]]""")

    def rmttest_neg03(self):
        "xmlcmp: text data differs"
        r, s = xmlcmp_strings('<hu>Was</hu>', '<hu>Ist</hu>')
        assert(r == False)
        assert(s == """Child node [<DOM Text node "u'Was'">] not found at [] - last error was [Text Node data differs [Was] != [Ist] at [/hu]]""")

    def rmttest_neg04(self):
        "xmlcmp: number of child nodes differ"
        r, s = xmlcmp_strings('<hu><h1></h1></hu>',
                              '<hu><h2></h2><h1></h1></hu>')
        assert(r == False)
        assert(s == "Number of child nodes differs [1] != [2] at []")

    def rmttest_neg05(self):
        "xmlcmp: Text node in sub node differs"
        r, s = xmlcmp_strings('<hu><hi>Was</hi></hu>', '<hu><hi>Ist</hi></hu>')
        assert(r == False)
        assert(re.match("""Child node \[<DOM Element: hi at 0x[0-9a-f]*>\] not found at \[\] - last error was \[Child node \[<DOM Text node "u'Was'">\] not found at \[/hu\] - last error was \[Text Node data differs \[Was\] != \[Ist\] at \[/hu/hi\]\]\]""", s))
