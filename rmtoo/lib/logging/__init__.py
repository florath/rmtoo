'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Logging.
   This is used to get information about the events / tasks
   done in the rmtoo itself.

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals

import sys
import logging


LOGGING_CONFIG = {
    "stdout": {
        "loglevel": logging.WARN,
    },
    "tracer": {
        "loglevel": logging.DEBUG,
        "filename": "/tmp/rmtoo.log"
    },
    "handler": [],
    "log_handler": []
}


def tear_down_trace_handler():
    """Remove the (possible) old handlers"""
    for handler in LOGGING_CONFIG["handler"]:
        tracer.removeHandler(handler)
        handler.close()
    LOGGING_CONFIG["handler"] = []


def __setup_trace_handler(ltracer):
    '''Based on the configuration, establish a new set of log handlers.'''

    tear_down_trace_handler()

    # Create a file handle
    ltracer_fh = logging.FileHandler(LOGGING_CONFIG["tracer"]["filename"])
    ltracer_fh.setLevel(LOGGING_CONFIG["tracer"]["loglevel"])

    # create console handler and set level to debug
    ltracer_ch = logging.StreamHandler()
    ltracer_ch.setLevel(LOGGING_CONFIG["stdout"]["loglevel"])

    # create formatter
    formatter = logging.Formatter(
        '%(asctime)s;%(name)s;%(levelname)s;%(module)s;'
        '%(funcName)s;%(lineno)d;%(message)s')

    # add formatter to ch
    ltracer_ch.setFormatter(formatter)
    ltracer_fh.setFormatter(formatter)

    # add ch to logger
    ltracer.addHandler(ltracer_fh)
    ltracer.addHandler(ltracer_ch)

    LOGGING_CONFIG["handler"].append(ltracer_fh)
    LOGGING_CONFIG["handler"].append(ltracer_ch)


def __setup_log_handler(mstderr=sys.stderr):
    '''Set up logger.'''
    # create console handler and set level to debug
    logger_ch = logging.StreamHandler(mstderr)
    logger_ch.setLevel(logging.INFO)
    # create formatter
    formatter = logging.Formatter(
        '%(asctime)s;%(name)s;%(levelname)s;%(module)s;'
        '%(funcName)s;%(lineno)d;%(message)s')
    # add formatter to ch
    logger_ch.setFormatter(formatter)
    # add ch to logger
    logger.addHandler(logger_ch)
    LOGGING_CONFIG["log_handler"].append(logger_ch)


def tear_down_log_handler():
    """Remove the (possible) old handlers"""
    for handler in LOGGING_CONFIG["log_handler"]:
        logger.removeHandler(handler)
        handler.close()
    LOGGING_CONFIG["log_handler"] = []


def __init_logger_object():
    '''This function sets up the global logger variable.'''
    tracer.debug("rmtoo init logger.")
    llogger = logging.getLogger("rmtoo")
    llogger.setLevel(logging.INFO)
    llogger.propagate = False
    return llogger


def init_logger(mstderr):
    '''This only setups the logger stream.
       The logger object must be already initialized -
       which is typically done in the module's init phase.'''
    __setup_log_handler(mstderr)
    tracer.debug("rmtoo logger enabled.")
    tracer.debug("logger [%s]", logger)


def init_tracer():
    '''This sets up the whole logging that it is available directly
    after process startup.
    The logging can be configured by the help of the 'configure_logging()'
    function.'''

    ltracer = logging.getLogger("rmtoo-trace")
    ltracer.setLevel(logging.DEBUG)
    ltracer.propagate = False
    __setup_trace_handler(ltracer)
    ltracer.debug("rmtoo tracer system enabled.")
    return ltracer


def configure_logging(cfg, mstderr):
    '''Configure the logging based on the configuration.'''
    llmap = {"debug": logging.DEBUG,
             "info": logging.INFO,
             "warn": logging.WARN,
             "error": logging.ERROR,
             "critical": logging.CRITICAL}

    if not cfg.is_available("global.logging"):
        tracer.debug("No logging configuration found - continue with default.")
    if cfg.is_available("global.logging.stdout.loglevel"):
        LOGGING_CONFIG["stdout"]["loglevel"] = \
            llmap[cfg.get_value("global.logging.stdout.loglevel")]
    if cfg.is_available("global.logging.tracer.loglevel"):
        LOGGING_CONFIG["tracer"]["loglevel"] = \
            llmap[cfg.get_value("global.logging.tracer.loglevel")]
    if cfg.is_available("global.logging.tracer.filename"):
        LOGGING_CONFIG["tracer"]["filename"] = \
            cfg.get_value("global.logging.tracer.filename")

    init_logger(mstderr)

    tracer.debug("rmtoo logging system configured.")


# The following names are uses as logging instances and therefore
# should be lower case.
# pylint: disable=invalid-name
tracer = init_tracer()
# Only the logger object must be created here:
# Looks that this is in another global space when calling this from this
# init or from somewhere else.
logger = __init_logger_object()
