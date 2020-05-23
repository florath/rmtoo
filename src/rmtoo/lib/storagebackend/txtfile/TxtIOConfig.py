'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Text IO Configuration
  This holds the configuration for the TxtIO class.

 (c) 2011-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals

from rmtoo.lib.RMTException import RMTException


# pylint: disable=too-few-public-methods
class TxtIOConfig(object):
    """Hold configuration for TextIO class"""

    def __init__(self, config=None, type_str=""):
        self.__max_line_length = 80
        if config is not None:
            self.__init_overwrite(config, type_str)

    def get_max_line_length(self):
        """Return the max line length"""
        return self.__max_line_length

    def __init_overwrite(self, config, type_str):
        '''Overwrite the existing default parameters with parameters
        from the configuration.
        '''
        self.__max_line_length = config.get_integer(
            'max_input_line_length', 80)
        if self.__max_line_length < 0:
            raise RMTException(
                72, "max_input_line_length for type [%s] is "
                "negative [%s]" % (type_str, self.__max_line_length))
