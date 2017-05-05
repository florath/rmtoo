'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Utils handling dates

 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
import datetime

from rmtoo.lib.RMTException import RMTException


def parse_date(rid, date_str):
    """Parse the given date as YYYY-MM-DD"""
    try:
        return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        raise RMTException(8, "%s: invalid date specified (must be "
                           "YYYY-MM-DD) was '%s'" % (rid, date_str))


def format_date(date_time):
    """Format the date as YYYY-MM-DD"""
    return date_time.strftime("%Y-%m-%d")
