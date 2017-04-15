'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Unit test for desc words.
  
 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import StringIO

from rmtoo.lib.analytics.DescWords import DescWords
from rmtoo.lib.configuration.Cfg import Cfg

class TestConfig1(Cfg):

    def __init__(self):
        Cfg.__init__(self)

class TestConfig2(Cfg):

    def __init__(self):
        Cfg.__init__(self)
        self.set_value('requirements.input.default_language', 'kl_EL')

class RMTTest_DescWords:

    def rmttest_check_language_handling(self):
        "DescWords: check language handling."

        tc = TestConfig1()
        lwords = DescWords.get_lang(tc)
        res = DescWords.analyse("lname", lwords, "Me and You, You and Me")
        assert(res.get_value() == -30)

        fd = StringIO.StringIO()
        res.write_error(fd)
        assert(fd.getvalue() == '''+++ Error:Analytics:DescWords:lname:result is '-30'
+++ Error:Analytics:DescWords:lname: -20:2*-10: Usage of the word 'and'
''')

    def rmttest_neg_01(self):
        "DescWords: get non existing language spec (empty config)."

        tc = TestConfig2()
        lang = DescWords.get_lang(tc)
        assert(lang == DescWords.words_en_GB)

    def rmttest_neg_02(self):
        "DescWords: get non existing language spec (wrong config)."

        tc = TestConfig2()
        lang = DescWords.get_lang(tc)
        assert(lang == DescWords.words_en_GB)
