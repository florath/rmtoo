#
# LaTeX2 output class
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#
class latex2:

    def __init__(self, param):
        self.directory = param[0]

    # Create MAkefile Dependencies
    def cmad(self, reqscont, ofile):
        pass
    
    def output(self, reqscont):
        # Currently just pass this to the RequirementSet
        pass
