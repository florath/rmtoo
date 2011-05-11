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

class stats_sprint_burndown1:

    def __init__(self, param):
        self.topic_name = param[0]
        self.output_filename = param[1]
        self.start_date = parse_date("stats burndown init", param[2])

    def set_topics(self, topics):
        self.topic_set = topics.get(self.topic_name)

    # Create Makefile Dependencies
    def cmad(self, reqscont, ofile):
        ofile.write("%s: ${REQS}\n\t${CALL_RMTOO}\n" % (self.output_filename))

    def output(self, reqscont):
        rv = Statistics.get_units_sprint(self.topic_set.reqset, self.start_date)
        Statistics.output_stat_files(self.output_filename, self.start_date, rv)
