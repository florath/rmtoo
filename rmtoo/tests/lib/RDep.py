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

class ReqSet(Digraph):

    def __init__(self, d=None):
        Digraph.__init__(self, d)

class TestConfig:
    pass

def create_parameters(d=None):
    return {}, TestConfig(), ReqSet(d)

