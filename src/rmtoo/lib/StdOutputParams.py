'''
 rmtoo
   Free and Open Source Requirements Management Tool

 Handling of standard parameters for output parameter handling.

 (c) 2011,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals

import datetime

from rmtoo.lib.DateUtils import parse_date
from rmtoo.lib.configuration.Cfg import Cfg
from rmtoo.lib.logging import tracer


# This is a base class - so no public methods
# pylint: disable=too-few-public-methods
class StdOutputParams(object):
    '''Handles the standard output parameters and sets the values
       in the self object provided.'''

    def __init__(self, config):
        '''Constructs the standard output parameters based on the
           provided config.'''
        self._output_filename = None
        self._start_date = None
        self._end_date = None
        self._config = Cfg(config)
        self.__parse()

    def __parse_output_filename(self):
        '''Sets the output filename.'''
        self._output_filename = self._config.get_rvalue('output_filename')

    @staticmethod
    def __parse_date(cfg, name, default_value):
        '''If name is in params, the value is converted to a date
           and returned.  If name is not in params, the default_value
           is returned.'''
        pname = cfg.get_value_wo_throw(name)
        if pname is None:
            return default_value
        return parse_date(name, pname)

    def __parse_start_and_end_date(self):
        '''Extracts the start and the end date from the params.'''
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(1)
        self._start_date = self.__parse_date(
            self._config, 'start_date', yesterday)
        tracer.debug("Start date [%s]", self._start_date)
        self._end_date = self.__parse_date(self._config, 'end_date', today)
        tracer.debug("End date [%s]", self._end_date)

    def __parse(self):
        '''Parses the standard parameters.'''
        self.__parse_output_filename()
        self.__parse_start_and_end_date()
