#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# Constraint class
#
# (c) 2011 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.BaseRMObject import BaseRMObject

class Constraint(BaseRMObject):

    def __init__(self, fd, rid, mls, mods, config):
        BaseRMObject.__init__(self, "ctstag", fd, rid, mls, mods,
                              config, "constraints")

