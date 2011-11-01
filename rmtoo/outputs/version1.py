#
# version output class
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

# Outputs the version number of the version control system to a given
# file. 

class version1:
    def __init__(self, topic_set, params):
        self.topic_set = topic_set
        self.filename = params['output_filename']

    # Create Makefile Dependencies
    def cmad(self, reqscont, ofile):
        ofile.write("%s: ${REQS}\n\t${CALL_RMTOO}\n" % (self.filename))

    # The 'real' output.
    # (The requirements are not needed at all, only the version number.)
    def output(self, reqscont):
        f = file(self.filename, "w")
        f.write("%s\n" % reqscont.continuum_latest_id())
        f.close()

