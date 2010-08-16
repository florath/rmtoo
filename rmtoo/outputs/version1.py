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
    def __init__(self, param):
        self.topic_name = param[0]
        self.filename = param[1]

    def set_topics(self, topics):
        self.topic_set = topics.get(self.topic_name)

    # Create Makefile Dependencies
    def cmad(self, reqscont, ofile):
        ofile.write("%s: ${REQS}\n\t${CALL_RMTOO}\n" % (self.filename))

    # The 'real' output.
    # (The requirements are not needed at all, only the version number.)
    def output(self, reqscont):
        f = file(self.filename, "w")
        f.write("%s\n" % reqscont.continnum_latest_id())
        f.close()


