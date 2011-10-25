'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
 Logging Levels used in rmtoo.
   
 (c) 2011 by flonatel GmhH & Co. KG

 For licensing details see COPYING
'''

from types import StringType
from rmtoo.lib.RMTException import RMTException

class LogLevel:
    '''Contains all the available log levels and respective
       input / output handling.'''

    # Log-levels symbolic constants
    ll_cstnt_trace = 10
    ll_cstnt_debug = 20
    ll_cstnt_info = 30
    ll_cstnt_warning = 40
    ll_cstnt_error = 50
    ll_cstnt_fatal = 60

    levels = set([ll_cstnt_trace, ll_cstnt_debug, ll_cstnt_info,
                  ll_cstnt_warning, ll_cstnt_error, ll_cstnt_fatal])

    level_names = {ll_cstnt_trace: 'trace', ll_cstnt_debug: "debug",
                   ll_cstnt_info: "info", ll_cstnt_warning: "warning",
                   ll_cstnt_error: "error", ll_cstnt_fatal: 'fatal' }
    names_level = {'trace': ll_cstnt_trace, "debug": ll_cstnt_debug,
                   "info": ll_cstnt_info, "warning": ll_cstnt_warning,
                   "error": ll_cstnt_error, 'fatal': ll_cstnt_fatal }

    level_output = {ll_cstnt_trace: 'Trace', ll_cstnt_debug: "Debug",
                    ll_cstnt_info: "Info", ll_cstnt_warning: "Warning",
                    ll_cstnt_error: "Error", ll_cstnt_fatal: 'Fatal' }

    @staticmethod
    def check_level(level):
        '''Checks the level: only the defined levels are allowed.'''
        if level not in LogLevel.levels:
            raise RMTException(52, "Invalid level [%s] in log message"
                               % level)

    def __init__(self, level):
        '''Private constructor.
           If there is the need to construct a LogLevel, please use
           one of the factory methods.'''
        LogLevel.check_level(level)
        self.level = level

    def get_output_str(self):
        '''Returns the string which can be used for logging of this
           level.'''
        return LogLevel.level_output[self.level]

    def get_symbolic_str(self):
        '''Returns the string which can be used for symbolic processing
           level.'''
        return LogLevel.level_names[self.level]

    @staticmethod
    def trace():
        '''Creates a trace log level.'''
        return LogLevel(LogLevel.ll_cstnt_trace)

    @staticmethod
    def debug():
        '''Creates a debug log level.'''
        return LogLevel(LogLevel.ll_cstnt_debug)

    @staticmethod
    def info():
        '''Creates a info log level.'''
        return LogLevel(LogLevel.ll_cstnt_info)

    @staticmethod
    def warning():
        '''Creates a warning log level.'''
        return LogLevel(LogLevel.ll_cstnt_warning)

    @staticmethod
    def error():
        '''Creates a error log level.'''
        return LogLevel(LogLevel.ll_cstnt_error)

    def __eq__(self, other):
        '''Compared this log level with the other.
           True is returned iff both level are the same.'''
        if type(other) == StringType:
            # Convert this to a value
            return self.level == LogLevel.names_level[other]
        return self.level == other.level
