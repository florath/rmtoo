#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# Utils handling dates
#
# (c) 2010-2011 by flonatel
#
# For licencing details see COPYING
#

import time

from rmtoo.lib.RMTException import RMTException

def parse_date(rid, ds):
    try:
        return time.strptime(ds, "%Y-%m-%d")
    except ValueError, ve:
        raise RMTException(8, "%s: invalid date specified (must be "
                           "YYYY-MM-DD) was '%s'" % (rid, ds))

def format_date(tm):
    return "%04d-%02d-%02d" % (tm.tm_year, tm.tm_mon, tm.tm_mday)    
