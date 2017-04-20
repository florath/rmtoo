'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Utils handling dates

 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
import datetime

from rmtoo.lib.RMTException import RMTException


def parse_date(rid, ds):
    try:
        return datetime.datetime.strptime(ds, "%Y-%m-%d").date()
    except ValueError:
        raise RMTException(8, "%s: invalid date specified (must be "
                           "YYYY-MM-DD) was '%s'" % (rid, ds))


def format_date(dt):
    return dt.strftime("%Y-%m-%d")
