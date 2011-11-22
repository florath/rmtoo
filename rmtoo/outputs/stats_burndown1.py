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
from rmtoo.lib.StdParams import StdParams

class stats_burndown1:

    def __init__(self, topic_set, params):
        self.topic_set = topic_set
        self.output_filename = params['output_filename']
        StdParams.parse(self, params)

    # Create Makefile Dependencies
    def cmad(self, reqscont, ofile):
        ofile.write("%s: ${REQS}\n\t${CALL_RMTOO}\n" % (self.output_filename))

    def output(self, reqscont):
        print("***** TODO STATS BURNDOWN OUTPUT")
#        rv = Statistics.get_units(self.topic_set.reqset,
#                                  self.start_date, self.end_date)
#        Statistics.output_stat_files(self.output_filename, self.start_date, rv)

