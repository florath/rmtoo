'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
 Handling of standard parameters for output parameter handling.
   
 (c) 2011 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import datetime
from rmtoo.lib.DateUtils import parse_date

class StdOutputParams:
    '''Handles the standard output parameters and sets the values
       in the self object provided.'''

    def __init__(self, config):
        '''Constructs the standard output parameters based on the
           provided config.'''
        self.__config = config
        self.__parse()

    def __parse_output_filename(self):
        '''Sets the output filename.'''
        self._output_filename = self.__config['output_filename']

    @staticmethod
    def __parse_date(params, name, default_value):
        '''If name is in params, the value is converted to a date
           and returned.  If name is not in params, the default_value
           is returned.'''
        if name in params:
            return parse_date(name, params[name])
        return default_value

    def __parse_start_and_end_date(self):
        '''Extracts the start and the end date from the params.'''
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(1)
        self._start_date = self.__parse_date(
                                self.__config, 'start_date', yesterday)
        self._end_date = self.__parse_date(self.__config, 'end_date', today)

    def __parse(self):
        '''Parses the standard parameters.'''
        self.__parse_output_filename()
        self.__parse_start_and_end_date()
