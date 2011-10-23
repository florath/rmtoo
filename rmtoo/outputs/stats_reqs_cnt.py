#
# stats_reqs_cnt output class
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

import re
import time

class stats_reqs_cnt:

    def __init__(self, topic_set, params):
        self.topic_set = topic_set
        self.output_filename = params['output_filename']

    # Create Makefile Dependencies
    def cmad(self, reqscont, ofile):
        ofile.write("%s: ${REQS}\n\t${CALL_RMTOO}\n" % (self.output_filename))

    def output(self, reqscont):
        # Depending on the number of elements in the continuum, this
        # might be a list or, if only FILES should be used, exactly
        # one value (the current time).
        ofile = file(self.output_filename, "w")

        for cid in reqscont.continuum_order:
            rs = reqscont.continuum[cid]
            ofile.write("%s %d\n" %
                        (time.strftime("%Y-%m-%d_%H:%M:%S",
                                       time.localtime(rs.timestamp())),
                         rs.reqs_count()))

        # Clean up the file.
        ofile.close()

