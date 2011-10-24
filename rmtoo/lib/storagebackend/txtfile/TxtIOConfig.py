#
# rmtoo 
#   Free and Open Source Requirements Management Tool
#
# Text IO Configuration
#  This holds the configuration for the TxtIO class
#
# (c) 2011 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.configuration.CfgEx import CfgEx

class TxtIOConfig:

    def __init__(self, config=None, type_str=""):
        self.init_default()
        if config != None:
            self.init_overwrite(config, type_str)

    def init_default(self):
        self.max_line_length = 80

    def get_max_line_length(self):
        return self.max_line_length

    def init_overwrite(self, config, type_str):
        '''Overwrite the existing default parameters with parameters
           from the configuration.'''
        self.max_line_length = config.get_integer(
            ['input', 'txtfile', type_str, 'max_line_length'], 80)
        if self.max_line_length < 0:
            raise RMTException(72, "input.txtfile.%s.max_line_length is "
                               "negative [%s]" % (type_str, v))


