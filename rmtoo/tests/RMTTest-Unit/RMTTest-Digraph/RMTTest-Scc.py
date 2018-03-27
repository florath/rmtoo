'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit tests for strongly connected components

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''


from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.digraph.StronglyConnectedComponents \
    import strongly_connected_components
from rmtoo.lib.digraph.StronglyConnectedComponents \
    import check_for_strongly_connected_components
from rmtoo.lib.digraph.Helper import node_sl_to_node_name_sl


class RMTTestSCCTests(object):

    def rmttest_scc_001(self):
        "Simple two node digraph with one scc"
        dg = Digraph({"A": ["B"], "B": ["A"]})
        sccs = strongly_connected_components(dg)
        sccsnames = node_sl_to_node_name_sl(sccs)
        assert sccsnames == [set(['A', 'B'])], "incorrect"

    def rmttest_scc_002(self):
        "Simple two node digraph with no scc"
        dg = Digraph({"A": ["B"], "B": []})
        sccs = strongly_connected_components(dg)
        sccsnames = node_sl_to_node_name_sl(sccs)
        assert sccsnames == [set(['B']), set(['A'])], "incorrect"

    def rmttest_scc_003(self):
        "Simple three node digraph with one scc and an extra node"
        dg = Digraph({"A": ["B", "C"], "B": ["A"], "C": []})
        sccs = strongly_connected_components(dg)
        sccsnames = node_sl_to_node_name_sl(sccs)
        assert sccsnames == [set(['C']), set(['A', 'B'])], "incorrect"

    def rmttest_scc_004(self):
        "Simple three node digraph with one scc I"
        dg = Digraph({"A": ["B", "C"], "B": ["A"], "C": ["A"]})
        sccs = strongly_connected_components(dg)
        sccsnames = node_sl_to_node_name_sl(sccs)
        assert sccsnames == [set(['A', 'C', 'B'])], "incorrect"

    def rmttest_scc_005(self):
        "Simple three node digraph with one scc II"
        dg = Digraph({"A": ["B", "C"], "B": ["A"], "C": ["B"]})
        sccs = strongly_connected_components(dg)
        sccsnames = node_sl_to_node_name_sl(sccs)
        assert sccsnames == [set(['A', 'C', 'B'])], "incorrect"

    def rmttest_scc_006(self):
        "Check for scc in a three node digraph with scc"
        dg = Digraph({"A": ["B", "C"], "B": ["A"], "C": ["B"]})
        sccs = strongly_connected_components(dg)
        scc_exists = check_for_strongly_connected_components(sccs)
        assert scc_exists is True, "incorrect"

    def rmttest_scc_007(self):
        "Check for scc in a three node digraph without scc"
        dg = Digraph({"A": ["B"], "B": ["C"], "C": []})
        sccs = strongly_connected_components(dg)
        scc_exists = check_for_strongly_connected_components(sccs)
        assert scc_exists is False, "incorrect"

    def rmttest_scc_008(self):
        "Check for scc in a three node digraph with a two node scc"
        dg = Digraph({"A": ["B"], "B": ["A"], "C": []})
        sccs = strongly_connected_components(dg)
        scc_exists = check_for_strongly_connected_components(sccs)
        assert scc_exists is True, "incorrect"
