#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# graph2 output class
#
#  This is the graph output class using topics as base for a clustered
#  subgraph. 
#
# (c) 2011 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.outputs.graph import graph

class graph2:

    def __init__(self, params):
        self.output_filename = params['output_filename']

    def set_topics(self, topics):
        self.topic_set = topics.get(self.topic_name)

    # Create Makefile Dependencies
    def cmad(self, reqscont, ofile):
        ofile.write("%s: ${REQS}\n\t${CALL_RMTOO}\n" % (self.output_filename))

    # Note that currently the 'reqscont' is not used in case of topics
    # based output.
    def output(self, reqscont):
        # Currently just pass this to the RequirementSet
        self.output_reqset(reqscont.continuum_latest())

    def output_reqset(self, reqset):
        # Initialize the graph output
        g = file(self.output_filename, "w")
        g.write("digraph reqdeps {\nrankdir=BT;\nmclimit=10.0;\n"
                "nslimit=10.0;ranksep=1;\n")
        # Subgraphs
        self.output_topic(g, self.topic_set.get_master())
        # Edges
        for r in sorted(self.topic_set.reqset.nodes, key=lambda r: r.id):
            self.output_req(r, g)
        g.write("}")
        g.close()

    # This writes out all the subgraphs and nodes
    def output_topic(self, dotfile, topic):
        ident = "          "[0:topic.level]
        # The _GRAPH_ is there to differentiate between topics and
        # possible equally named requiremnts. 
        dotfile.write('%ssubgraph cluster_GRAPH_%s {\n'
                      ' label="Topic: %s";\n' % (ident, topic.name, topic.name))

        # Write out the sub-sub-graphs
        for t in sorted(topic.outgoing, key=lambda t: t.name):
            self.output_topic(dotfile, t)
        for req in sorted(topic.reqs, key=lambda r: r.id):
            dotfile.write('%s"%s" [%s];\n'
                          % (ident, req.name, graph.node_attributes(req)))
        dotfile.write('%s}\n' % ident)

    # This writes out the edges
    def output_req(self, req, dotfile):
        for d in sorted(req.outgoing, key=lambda r: r.id):
            dotfile.write('"%s" -> "%s";\n' % (req.id, d.id))
