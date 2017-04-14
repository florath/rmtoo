'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
 Common setup for RDep test cases
 
 (c) 2010, 2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.tests.lib.TestConfig import TestConfig
from rmtoo.lib.digraph.Helper import digraph_create_from_dict

        
class ReqSet(Digraph):

    def __init__(self, d=None):
        Digraph.__init__(self)
        if d!=None:
            self.create_from_dict(d)

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

