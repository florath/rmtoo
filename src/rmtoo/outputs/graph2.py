'''
 rmtoo
   Free and Open Source Requirements Management Tool

 Output handler graph2.

 This is the graph output class using topics as base for a clustered
 subgraph.

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.outputs.graph import graph
from rmtoo.lib.logging import tracer
from rmtoo.lib.StdOutputParams import StdOutputParams
from rmtoo.lib.ExecutorTopicContinuum import ExecutorTopicContinuum
from rmtoo.lib.CreateMakeDependencies import CreateMakeDependencies


class graph2(StdOutputParams, ExecutorTopicContinuum, CreateMakeDependencies):
    '''The output class handling graph2.
       graph2 is a requirements dependency graph which has additional
       clusters for each topic.'''

    def __init__(self, oconfig):
        '''Create a graph output object.'''
        tracer.debug("Called.")
        StdOutputParams.__init__(self, oconfig)
        CreateMakeDependencies.__init__(self)
        self.__output_file = None
        self.__ident = ""
        self.__level = 0
        self.__req_dep_graph = ""

    def __set_indent(self):
        '''Set the ident.'''
        self.__ident = "             "[0:self.__level]

    def __inc_indent_level(self):
        '''Increases the indent level by one.'''
        self.__level += 1
        self.__set_indent()

    def __dec_indent_level(self):
        '''Decreases the indent level by one.'''
        self.__level -= 1
        self.__set_indent()

    def topic_continuum_sort(self, vcs_commit_ids, topic_sets):
        '''Because graph2 can only one topic continuum,
           the latest (newest) is used.'''
        return [topic_sets[vcs_commit_ids[-1].get_commit()]]

    def topic_set_pre(self, _):
        '''This is the first thing which is called.'''
        tracer.debug("Called.")
        self.__output_file = open(self._output_filename, "w")
        self.__output_file.write(
                "digraph reqdeps {\nrankdir=BT;\nmclimit=10.0;\n"
                "nslimit=10.0;ranksep=1;\n")
        tracer.debug("Finished.")

    def topic_set_post(self, _):
        '''Finish major entry and close file.'''
        tracer.debug("Called.")
        self.__output_file.write(self.__req_dep_graph)
        self.__output_file.write("}\n")
        self.__output_file.close()
        tracer.debug("Finished.")

    def topic_pre(self, topic):
        '''This writes out all the subgraphs and nodes.'''
        # The _GRAPH_ is there to differentiate between topics and
        # possible equally named requirements.
        self.__output_file.write(
            '%ssubgraph cluster_GRAPH_%s {\n'
            '%s label="Topic: %s";\n'
            % (self.__ident, topic.name, self.__ident, topic.name))
        self.__inc_indent_level()

    def topic_post(self, _):
        '''Write header to file.'''
        self.__output_file.write('%s}\n' % self.__ident)
        self.__dec_indent_level()

    def requirement_set_sort(self, list_to_sort):
        '''Set the order of the requirements.'''
        return sorted(list_to_sort, key=lambda t: t.name)

    def requirement(self, requirement):
        '''Output one requirement - and collect information about the
           requirement's coherence.'''
        ident = "          "[0:self.__level]
        self.__output_file.write('%s"%s" [%s];\n'
                                 % (ident, requirement.name,
                                    graph.node_attributes(requirement)))

        for d in sorted(requirement.incoming, key=lambda r: r.get_id()):
            self.__req_dep_graph += '"%s" -> "%s";\n' \
                                    % (requirement.get_id(), d.get_id())

    def cmad_topic_continuum_pre(self, _):
        '''Write out the one and only dependency to all the requirements.'''
        tracer.debug("Called.")
        CreateMakeDependencies.write_reqs_dep(self._cmad_file,
                                              self._output_filename)
