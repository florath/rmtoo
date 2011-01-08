#
# rmtoo 
#   Free and Open Source Requirements Management Tool
#
# Text IO Configuration
#  This holds the configuration for the TxtIO class
#
# (c) 2011 by flonatel
#
# For licencing details see COPYING
#

class TxtIOConfig:

    def __init__(self, config=None):
        self.init_default()
        if config!=None:
            self.init_overwrite(config)

    def init_default(self):
        self.max_line_length = 80

    def set_max_line_length(self, n):
        self.max_line_length = n

    def get_max_line_length(self):
        return self.max_line_length
        
