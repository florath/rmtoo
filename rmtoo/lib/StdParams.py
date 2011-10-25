'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
 Handling of standard parameters for output parameter handling.
   
 (c) 2011 by flonatel GmhH & Co. KG

 For licensing details see COPYING
'''

import datetime
from rmtoo.lib.DateUtils import parse_date

class StdParams:
    '''Handles the standard output parameters and sets the values
       in the self object provided.'''

    @staticmethod
    def internal_parse_output_filename(this, params):
        '''Sets the output filename.'''
        this.output_filename = params['output_filename']

    @staticmethod
    def internal_parse_date(params, name, default_value):
        '''If name is in params, the value is converted to a date
           and returned.  If name is not in params, the default_value
           is returned.'''
        if name in params:
            return parse_date(name, params[name])
        return default_value

    @staticmethod
    def internal_parse_start_and_end_date(this, params):
        '''Extracts the start and the end date from the params.'''
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(1)
        this.start_date = StdParams.internal_parse_date(
                    params, 'start_date', yesterday)
        this.end_date = StdParams.internal_parse_date(
                    params, 'end_date', today)

    @staticmethod
    def parse(this, params):
        '''Parses the standard parameters.'''
        StdParams.internal_parse_output_filename(this, params)
        StdParams.internal_parse_start_and_end_date(this, params)
