#
# Digraph Pyhton library
#
# Unit tests for connected components
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

import unittest

from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.digraph.ConnectedComponents \
    import connected_components

class CCTest(unittest.TestCase):

    def test_cc_001(self):
        "Connected digraph"
        dg = Digraph( {"A": ["B"], "B": ["C"], "C": [] } )
        ccs = connected_components(dg)
        assert(ccs.len()==1)

    def test_cc_002(self):
        "Not connected digraph"
        dg = Digraph( {"A": ["B"], "B": ["C"], "C": [],
                       "D": ["E"], "E": [] } )
        ccs = connected_components(dg)
        assert(ccs.len()>1)
        
