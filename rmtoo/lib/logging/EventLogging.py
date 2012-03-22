'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Event Logging.
   This is used to get information about the events / tasks
   done in the rmtoo itself.
   
 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import logging

tracer = None
logger = None

logging_config = {
    "stdout": {
        "loglevel": logging.WARN,
    },
    "tracer": {
        "loglevel": logging.DEBUG,
        "filename": "/tmp/rmtoo.log"
    },
    "handler": []
}

def __setup_trace_handler():
    '''Based on the configuration, establish a new set of log handlers.'''

    # Remove the (possible) old handlers
    for handler in logging_config["handler"]:
        tracer.removeHandler(handler)
    logging_config["handler"] = []

    # Create a file handle
    tracer_fh = logging.FileHandler(logging_config["tracer"]["filename"])
    tracer_fh.setLevel(logging_config["tracer"]["loglevel"])

    # create console handler and set level to debug
    tracer_ch = logging.StreamHandler()
    tracer_ch.setLevel(logging_config["stdout"]["loglevel"])

    # create formatter
    formatter = logging.Formatter(
                '%(asctime)s;%(name)s;%(levelname)s;%(module)s;'
                '%(funcName)s;%(lineno)d;%(message)s')

    # add formatter to ch
    tracer_ch.setFormatter(formatter)
    tracer_fh.setFormatter(formatter)

    # add ch to logger
    tracer.addHandler(tracer_fh)
    tracer.addHandler(tracer_ch)
    
    logging_config["handler"].append(tracer_fh)
    logging_config["handler"].append(tracer_ch)

def __setup_log_handler():
    '''Set up logger.'''
    # create console handler and set level to debug
    logger_ch = logging.StreamHandler()
    logger_ch.setLevel(logging.INFO)
    # create formatter
    formatter = logging.Formatter(
                '%(asctime)s;%(name)s;%(levelname)s;%(module)s;'
                '%(funcName)s;%(lineno)d;%(message)s')
    # add formatter to ch
    logger_ch.setFormatter(formatter)
    # add ch to logger
    logger.addHandler(logger_ch)
    

def init_logging():
    '''This sets up the whole logging that it is available directly 
       after process startup.
       The logging can be configured by the help of the 'configure_logging()'
       function.'''

    # pylint: disable=W0603
    global tracer
    global logger

    tracer = logging.getLogger("rmtoo-trace")
    tracer.setLevel(logging.DEBUG)
    tracer.propagate = False
    __setup_trace_handler()
    
    logger = logging.getLogger("rmtoo")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    __setup_log_handler()

    tracer.debug("rmtoo tracer system enabled.")

def configure_logging(cfg):
    '''Configure the logging based on the configuration.'''
    llmap= {"debug": logging.DEBUG,
            "info": logging.INFO,
            "warn": logging.WARN,
            "error": logging.ERROR,
            "critical": logging.CRITICAL }
    
    if not cfg.is_available("global.logging"):
        tracer.debug("No logging configuration found - continue with default.")
    if cfg.is_available("global.logging.stdout.loglevel"):
        logging_config["stdout"]["loglevel"] = \
            llmap[cfg.get_value("global.logging.stdout.loglevel")]
    if cfg.is_available("global.logging.tracer.loglevel"):
        logging_config["tracer"]["loglevel"] = \
            llmap[cfg.get_value("global.logging.tracer.loglevel")]
    if cfg.is_available("global.logging.tracer.filename"):
        logging_config["tracer"]["filename"] = \
            cfg.get_value("global.logging.tracer.filename")

    __setup_trace_handler()
    
    tracer.debug("rmtoo logging system configured.")
    