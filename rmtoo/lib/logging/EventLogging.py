'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Event Logging.
   This is used to get information about the events / tasks
   done in the rmtoo itself.
   
 (c) 2010-2011 by flonatel GmhH & Co. KG

 For licensing details see COPYING
'''

import logging

tracer = None

def init_logging():

    global tracer

    tracer = logging.getLogger("rmtoo-trace")
    tracer.setLevel(logging.DEBUG)
    tracer.propagate = False

    # Create a file handle
    tracer_fh = logging.FileHandler('/tmp/rmtoo.log')
    tracer_fh.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    tracer_ch = logging.StreamHandler()
    tracer_ch.setLevel(logging.INFO)

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

    tracer.debug("rmtoo tracer system enabled")
