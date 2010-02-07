#
# Requirement Management Toolset
#  class Req_Name
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

#import Modules

class ReqName:

    def __init__(self, opts, config):
        print("--- INIT Req_Name")
        self.opts = opts
        self.config = config

    def type(self):
        return "reqtag"
