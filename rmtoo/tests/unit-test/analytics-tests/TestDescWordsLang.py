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

class TestConfig:

    reqs_spec = []

class TestDescWords:

    def test_pos_01(self):
        "DescWords: check language handling"

        tc = TestConfig()
        lwords = DescWords.get_lang(tc)
        level, log = DescWords.analyse(lwords, "Me and You, You and Me")
        assert(level==-30)
        assert(log==[" -20:2*-10: Usage of the word 'and'"])


