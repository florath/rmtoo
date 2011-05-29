#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# Burndown diagram
#
# (c) 2011 by flonatel
#
# For licencing details see COPYING
#

import datetime
from rmtoo.lib.ParamMap import ParamMap
from rmtoo.lib.DateUtils import parse_date

class StdParams:
      
      @staticmethod
      def parse(this, param):
        pmap = {}
        if len(param)>2:
            pmap = param[2]

        today = datetime.date.today()
        yesterday = today - datetime.timedelta(1)
        this.start_date = ParamMap.extract(
            pmap, "start_date", parse_date, yesterday)
        this.end_date = ParamMap.extract(pmap, "end_date", parse_date, today)

