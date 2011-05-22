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

from rmtoo.lib.DateUtils import parse_date
from rmtoo.lib.Statistics import Statistics

class stats_burndown1:

    def __init__(self, param):
        self.topic_name = param[0]
        self.output_filename = param[1]
        self.start_date = \
            parse_date("stats burndown init", param[2]["start_date"])
        if "end_date" in param[2]:
            self.end_date = \
                parse_date("stats burndown init", param[2]["end_date"])
        else:
            self.end_date = datetime.date.today()

    def set_topics(self, topics):
        self.topic_set = topics.get(self.topic_name)

    # Create Makefile Dependencies
    def cmad(self, reqscont, ofile):
        ofile.write("%s: ${REQS}\n\t${CALL_RMTOO}\n" % (self.output_filename))

    def output(self, reqscont):
        rv = Statistics.get_units(self.topic_set.reqset, 
                                  self.start_date, self.end_date)
        Statistics.output_stat_files(self.output_filename, self.start_date, rv)

