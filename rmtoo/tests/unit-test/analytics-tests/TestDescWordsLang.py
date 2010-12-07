#
# Requirement Management Toolset
#
#  Unit test for calling main
#
# (c) 2010 on flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.analytics.DescWords import DescWords

class TestConfig1:

    reqs_spec = {}

class TestConfig2:

    reqs_spec = { "default_language": "kl_EL"}

class TestDescWords:

    def test_pos_01(self):
        "DescWords: check language handling"

        tc = TestConfig1()
        lwords = DescWords.get_lang(tc)
        level, log = DescWords.analyse(lwords, "Me and You, You and Me")
        assert(level==-30)
        assert(log==[" -20:2*-10: Usage of the word 'and'"])


    def test_neg_01(self):
        "DescWords: get non existing language spec"

        tc = TestConfig2()
        lwords = DescWords.get_lang(tc)
        assert(lwords==None)

    def test_neg_02(self):
        "DescWords: get non existing language spec using run function"

        tc = TestConfig2()
        r = DescWords.run(tc, None, None)
        assert(r==True)
