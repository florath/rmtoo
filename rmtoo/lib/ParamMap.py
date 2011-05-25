#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
#  prios output class
#
# (c) 2011 by flonatel
#
# For licencing details see COPYING
#

# This class handles the extraction of parameters from the parameter map.

class ParamMap:

    @staticmethod
    def extract(pmap, name, conv_func, valdefault):
        if name in pmap:
            return conv_func(name, pmap[name])
        return valdefault
