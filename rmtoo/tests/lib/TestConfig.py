#
# rmtoo
#    Requirement Management Toolset
#
# Common methods for handling test config
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#
from rmtoo.lib.ConfigUtils import ConfigUtils

class TestConfig:

    def __init__(self):
        ConfigUtils.set_defaults(self)

    def set_solved_by(self):
        self.reqs_spec["dependency_notation"] = "Solved by"
