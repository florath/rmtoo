#
# graph2 output class
#
#  This is the graph output class using topics as base for a clustered
#  subgraph. 
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.outputs.graph import graph

class graph2:

    def __init__(self, param):
        self.topic_name = param[0]
        self.output_filename = param[1]

    def set_topics(self, topics):
        self.topic_set = topics.get(self.topic_name)
  
    # Create MAkefile Dependencies
    def cmad(self, reqscont, ofile):
        ofile.write("%s: ${REQS}\n\t${CALL_RMTOO}\n" % (self.output_filename))
        
    def output(self, reqscont):
        # Currently just pass this to the RequirementSet
        self.output_reqset(reqscont.base_requirement_set)

    def output_reqset(self, reqset):
        # Initialize the graph output
        g = file(self.output_filename, "w")
        g.write("digraph reqdeps {\nrankdir=BT;\nmclimit=10.0;\n"
                "nslimit=10.0;ranksep=1;\n")
        # Subgraphs
        self.output_topic(g, self.topic_set.get_master())
        # Edges
        for r in self.topic_set.all_reqs:
            self.output_req(r, g)
        g.write("}")
        g.close()

    # This writes out all the subgraphs and nodes
    def output_topic(self, dotfile, topic):
        ident = "          "[0:topic.level]
        dotfile.write('%ssubgraph cluster_%s {\n'
                      ' label="%s";\n' % (ident, topic.name, topic.name))

        # Write out the sub-sub-graphs
        for t in topic.outgoing:
            self.output_topic(dotfile, t)

        for req in topic.reqs:
            dotfile.write('%snode [%s] %s;\n'
                          % (ident, graph.node_attributes(req),
                             req.name))
        dotfile.write('%s}\n' % ident)

    # This writes out the edges
    def output_req(self, req, dotfile):
        for d in req.outgoing:
            dotfile.write("%s -> %s;\n" % (req.id, d.id))
