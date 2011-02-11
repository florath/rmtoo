#
# rmtoo 
#   Free and Open Source Requirements Management Tool
#
#  Unit test for RequirementSet
#
# (c) 2010-2011 on flonatel
#
# For licencing details see COPYING
#

from rmtoo.outputs.latex2 import latex2

class TestOutputLaTeX2:

    def test_positive_01(self):
        "LaTeX output: check config"

        mconfig = { "req_attributes": ["Id", "Priority",]}

        l = latex2([None, None, mconfig])
        assert(l.config==mconfig)




