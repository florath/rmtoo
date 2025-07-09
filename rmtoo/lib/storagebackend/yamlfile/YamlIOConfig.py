'''
 rmtoo
   Free and Open Source Requirements Management Tool

  YAML IO Configuration
  This holds the configuration for the YAML IO class.

 (c) 2025 by flonatel GmbH & Co. KG / Andreas Florath

 SPDX-License-Identifier: GPL-3.0-or-later

 For licensing details see COPYING
'''

from rmtoo.lib.RMTException import RMTException


# pylint: disable=too-few-public-methods
class YamlIOConfig(object):
    """Hold configuration for YAML IO class"""

    def __init__(self, config=None, type_str=""):
        self.__max_line_length = 80
        self.__preserve_order = True
        self.__indent_spaces = 2
        if config is not None:
            self.__init_overwrite(config, type_str)

    def get_max_line_length(self):
        """Return the max line length (for compatibility with TxtIOConfig)"""
        return self.__max_line_length

    def get_preserve_order(self):
        """Return whether to preserve key order in YAML output"""
        return self.__preserve_order

    def get_indent_spaces(self):
        """Return number of spaces for YAML indentation"""
        return self.__indent_spaces

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

        self.__preserve_order = config.get_bool(
            'yaml_preserve_order', True)

        self.__indent_spaces = config.get_integer(
            'yaml_indent_spaces', 2)
        if self.__indent_spaces < 1:
            raise RMTException(
                72, "yaml_indent_spaces for type [%s] is "
                "invalid [%s]" % (type_str, self.__indent_spaces))
