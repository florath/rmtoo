#
# rmtoo 
#   Free and Open Source Requirements Management Tool
#
#  Unit test for Topic
#
# (c) 2011 on flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.storagebackend.txtfile.TxtIOConfig import TxtIOConfig

class TestTxtIOConfig:

    def test_pos_01(self):
        "TxtIOConfig: check new max line length setting"
        config = {"max_line_length": 77}
        tic = TxtIOConfig(config)

        assert(tic.get_max_line_length()==77)
