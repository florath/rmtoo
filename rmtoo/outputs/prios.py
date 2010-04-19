#
# prios output class
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

class prios:

    ## XXX How to handle the parameters?
    def output(self, reqscont):
        # Currently just pass this to the RequirementSet
        reqscont.base_requirement_set.output_prios(ofilename)
        
