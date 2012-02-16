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

# TODO: Cleanup 'indent'
class graph2(StdOutputParams, ExecutorTopicContinuum):

    def __init__(self, oconfig):
        '''Create a graph output object.'''
        tracer.debug("Called.")
        StdOutputParams.__init__(self, oconfig)
        self.__output_file = None

    def topics_continuum_pre(self, topics_continuum):
        '''This is the first thing which is called.'''
        tracer.debug("Called.")
        self.__output_file = file(self._output_filename, "w")
        self.__output_file.write(
                "digraph reqdeps {\nrankdir=BT;\nmclimit=10.0;\n"
                "nslimit=10.0;ranksep=1;\n")
        self.__level = 0
        tracer.debug("Finished.")

    def topics_continuum_post(self, topics_continuum):
        '''Finish major entry and close file.'''
        tracer.debug("Called.")
        self.__output_file.write("}")
        self.__output_file.close()
        tracer.debug("Finished.")

    def topics_set_pre(self, topic):
        '''This writes out all the subgraphs and nodes.'''
        ident = "          "[0:self.__level]
        self.__level += 1
        # The _GRAPH_ is there to differentiate between topics and
        # possible equally named requirements. 
        self.__output_file.write('%ssubgraph cluster_GRAPH_%s {\n'
            ' label="Topic: %s";\n' % (ident, topic.name, topic.name))

        # Write out the sub-sub-graphs
#        for t in sorted(topic.outgoing, key=lambda t: t.name):
#            self.output_topic(dotfile, t)
#        for req in sorted(topic.reqs, key=lambda r: r.id):
#            dotfile.write('%s"%s" [%s];\n'
#                          % (ident, req.name, graph.node_attributes(req)))

    def topics_set_post(self, topic):
        '''Write header to file.'''
        ident = "          "[0:self.__level]
        self.__output_file.write('%s}\n' % ident)
        self.__level -= 1

    def requirement(self, requirement):
        '''Output one node.'''
        ident = "          "[0:self.__level]
        self.__output_file.write('%s"%s" [%s];\n'
                      % (ident, requirement.name,
                         graph.node_attributes(requirement)))



#    def requirement_set_pre(self, requirement_set):
#        # Edges
#        for r in sorted(requirement_set.nodes, key=lambda r: r.id):
#            self.output_req(r, self.__output_file)
#
#    # This writes out the edges
#    def output_req(self, req, dotfile):
#        for d in sorted(req.outgoing, key=lambda r: r.id):
#            dotfile.write('"%s" -> "%s";\n' % (req.id, d.id))

### Deprecated
    def set_topics(self, topics):
        self.topic_set = topics.get(self.topic_name)

    # Create Makefile Dependencies
    def cmad(self, reqscont, ofile):
        ofile.write("%s: ${REQS}\n\t${CALL_RMTOO}\n" % (self.output_filename))
