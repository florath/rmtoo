#
# Requirement Management Toolset
#
# Common setup for RDep test cases
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.logging.MemLogStore import MemLogStore
from rmtoo.lib.Requirement import Requirement
from rmtoo.tests.lib.TestConfig import TestConfig

class ReqSet(Digraph, MemLogStore):

    def __init__(self, d=None):
        Digraph.__init__(self, d,
                         lambda nname: Requirement(None, nname, None,
                                                   None, None, None))
        MemLogStore.__init__(self)

# Create a set of parameters for the test-cases
def create_parameters(d=None):
    tconfig = TestConfig()
    return tconfig, ReqSet(d)

# This is a test (minimalistic) requirement
class TestReq(Digraph.Node):

    def __init__(self, name, tags, brmo=None):
        Digraph.Node.__init__(self, name)
        self.id = name
        self.otags = tags
        self.brmo = brmo

    def get_value(self, key):
        return self.otags[key]

