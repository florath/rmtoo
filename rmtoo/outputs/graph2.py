'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
 Output handler graph2.
 
 This is the graph output class using topics as base for a clustered
 subgraph.
  
 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.outputs.graph import graph
from rmtoo.lib.logging.EventLogging import tracer
from rmtoo.lib.StdOutputParams import StdOutputParams
from rmtoo.lib.ExecutorTopicContinuum import ExecutorTopicContinuum

class graph2(StdOutputParams, ExecutorTopicContinuum):

    def __init__(self, oconfig):
        '''Create a graph output object.'''
        tracer.debug("Called.")
        StdOutputParams.__init__(self, oconfig)
        self.__output_file = None

    def topics_continuum_pre(self, topics_continuum):
        '''This is the first thing which is called.'''
        self.__output_file = file(self._output_filename, "w")
        self.__output_file.write(
                "digraph reqdeps {\nrankdir=BT;\nmclimit=10.0;\n"
                "nslimit=10.0;ranksep=1;\n")

    def topic_set_pre(self, topic_set):
        '''This is call in the Topic pre-phase.'''
        # Subgraphs
        self.output_topic(self.__output_file, topic_set.get_master())

    def requirement_set_pre(self, requirement_set):
        # Edges
        for r in sorted(requirement_set.nodes, key=lambda r: r.id):
            self.output_req(r, self.__output_file)
        self.__output_file.write("}")
        self.__output_file.close()

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

### Deprecated
    def set_topics(self, topics):
        self.topic_set = topics.get(self.topic_name)

    # Create Makefile Dependencies
    def cmad(self, reqscont, ofile):
        ofile.write("%s: ${REQS}\n\t${CALL_RMTOO}\n" % (self.output_filename))
