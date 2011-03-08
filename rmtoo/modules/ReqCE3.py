#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# Constraint Evaluation and Execution Environment python code
#
# (c) 2011 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.ReqTagGeneric import ReqTagGeneric

class ReqCE3(ReqTagGeneric):
    tag = "CE3"
    ltype = set(["ctstag", ])

    def __init__(self, opts, config):
        ReqTagGeneric.__init__(self, opts, config)

    def rewrite(self, rid, req):
        print("RRRRRRRRRRRRRRRRRWWWWWWWWWWWWWW calles")
    	# This is optional
        return self.handle_optional_tag(req)

