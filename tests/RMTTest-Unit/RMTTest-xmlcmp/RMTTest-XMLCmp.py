'''
 rmtoo
   Free and Open Source Requirements Management Tool

 Unit test for Library for comparing XML documents

 (c) 2011-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals


import re

from rmtoo.lib.xmlutils.xmlcmp import xmlcmp_strings


class RMTTestXMLCmp(object):

    def rmttest_pos01(self):
        "xmlcmp: small xml document"
        r, s = xmlcmp_strings('<hu/>', '<hu/>')
        assert r

    def rmttest_pos02(self):
        "xmlcmp: same tags with different arrtibutes"
        r, s = xmlcmp_strings(
            '<hu><t a="1"/><t b="2"/></hu>',
            '<hu><t b="2"/><t a="1"/></hu>')
        assert r

    def rmttest_neg01(self):
        "xmlcmp: top level node names differ"
        r, s = xmlcmp_strings('<hu/>', '<hi/>')
        assert not r
        assert "Tag names differ [hu] != [hi] at []" == s

    def rmttest_neg02(self):
        "xmlcmp: types of subnode differ"
        r, s = xmlcmp_strings('<hu>Mein Text</hu>', '<hu><uj></uj></hu>')
        assert not r
        assert re.match(r"Child node \[<DOM Text node \"u?'Mein Text'\">\] "
                        r"not found at \[\] - last error was "
                        r"\[Node types differ \[3\] != \[1\] at \[/hu\]\]", s)

    def rmttest_neg03(self):
        "xmlcmp: text data differs"
        r, s = xmlcmp_strings('<hu>Was</hu>', '<hu>Ist</hu>')
        assert not r
        assert re.match(r"Child node \[<DOM Text node \"u?'Was'\">\] "
                        r"not found at \[\] - last error was \[Text Node "
                        r"data differs \[Was\] != \[Ist\] at \[/hu\]\]", s)

    def rmttest_neg04(self):
        "xmlcmp: number of child nodes differ"
        r, s = xmlcmp_strings('<hu><h1></h1></hu>',
                              '<hu><h2></h2><h1></h1></hu>')
        assert not r
        assert "Number of child nodes differs [1] != [2] at []" == s

    def rmttest_neg05(self):
        "xmlcmp: Text node in sub node differs"
        r, s = xmlcmp_strings('<hu><hi>Was</hi></hu>', '<hu><hi>Ist</hi></hu>')
        assert not r
        assert re.match(r"Child node \[<DOM Element: hi at 0x[0-9a-f]*>\] "
                        r"not found at \[\] - last error was \[Child node "
                        r"\[<DOM Text node \"u?'Was'\">\] not found at \[/hu\]"
                        r" - last error was \[Text Node data differs \[Was\] "
                        r"!= \[Ist\] at \[/hu/hi\]\]\]", s)
