'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for desc words.

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals


try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from rmtoo.lib.analytics.DescWords import DescWords
from rmtoo.lib.configuration.Cfg import Cfg


class TestConfig1(Cfg):

    def __init__(self):
        Cfg.__init__(self)


class TestConfig2(Cfg):

    def __init__(self):
        Cfg.__init__(self)
        self.set_value('requirements.input.default_language', 'kl_EL')


class RMTTestDescWords(object):

    def rmttest_check_language_handling(self):
        "DescWords: check language handling."

        test_config = TestConfig1()
        desc_words = DescWords(test_config)
        res = desc_words.analyse("lname", "Me and You, You and Me")
        assert -30 == res.get_value()

        fd = StringIO()
        res.write_error(fd)
        assert '''+++ Error:Analytics:DescWords:lname:result is '-30'
+++ Error:Analytics:DescWords:lname: -20:2*-10: Usage of the word 'and'
''' == fd.getvalue()

    def rmttest_neg_01(self):
        "DescWords: get non existing language spec (empty config)."

        tc = TestConfig2()
        lang = DescWords.get_lang(tc)
        assert lang == DescWords.words_en_GB

    def rmttest_neg_02(self):
        "DescWords: get non existing language spec (wrong config)."

        tc = TestConfig2()
        lang = DescWords.get_lang(tc)
        assert lang == DescWords.words_en_GB
