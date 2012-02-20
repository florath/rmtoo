'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
 Output handler graph.
  
 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.RequirementStatus import RequirementStatusNotDone, \
    RequirementStatusAssigned
from rmtoo.lib.ClassType import ClassTypeImplementable, \
    ClassTypeSelected
from rmtoo.lib.StdOutputParams import StdOutputParams
from rmtoo.lib.ExecutorTopicContinuum import ExecutorTopicContinuum
from rmtoo.lib.logging.EventLogging import tracer
from rmtoo.lib.configuration.Cfg import Cfg

class graph(StdOutputParams, ExecutorTopicContinuum):
    default_config = Cfg.new_by_json_str(
            """json:{"node_attributes":
               ["Type", "Status", "Class", "Topic", "Priority" ] }""")

    def __init__(self, oconfig):
        '''Create a graph output object.'''
        tracer.debug("Called.")
        StdOutputParams.__init__(self, oconfig)

        if not self._config.is_available('node_attributes'):
            self._config.set_value('node_attributes',
                ["Type", "Status", "Class", "Topic", "Priority", ])

    def topics_continuum_sort(self, vcs_ids, topic_sets):
        '''Because graph2 can only one topic continuum,
           the latest (newest) is used.'''
        self.__used_vcs_id = vcs_ids[-1]
        return [ topic_sets[vcs_ids[-1]] ]

    def requirement_set_pre(self, requirement_set):
        '''This is call in the RequirementSet pre-phase.'''
        tracer.debug("Called")
        # Initialize the graph output
        self.__output_file = file(self._output_filename, "w")
        self.__output_file.write(
                "digraph reqdeps {\nrankdir=BT;\nmclimit=10.0;\n"
                "nslimit=10.0;ranksep=1;\n")
        # Only output the nodes which are connected to the chosen topic.
        print("**** OUTPUT GRAPH [%s]" % requirement_set.get_all_requirement_ids())
        print("****TODO OUTPUT GRAPH [%s]" % requirement_set.nodes)
        
    def requirement_set_sort(self, list_to_sort):
        '''Sort by id.'''
        return sorted(list_to_sort, key=lambda r: r.id)

    def requirement_set_post(self, requirement_set):
        '''Write footer - close file.'''
        # Print out a node with the version number:
        self.__output_file.write(
                'ReqVersion [shape=plaintext label="ReqVersion\\n%s"]\n'
                % self.__used_vcs_id)
        self.__output_file.write("}")
        self.__output_file.close()
        
    def requirement(self, requirement):
        '''Output the given requirement.'''
        self.__output_file.write('"%s" [%s];\n' %
                      (requirement.get_id(), 
                       self.node_attributes(requirement, self._config)))

        for d in requirement.outgoing:
            self.__output_file.write('"%s" -> "%s";\n' % 
                                     (requirement.get_id(), d.id))

# TODO: currently the =default_config is needed for graph2
    @staticmethod
    def node_attributes(req, config=default_config):

        def get_conf_attr(attr):
            return config.is_available("node_attributes") \
                and attr in config.get_value("node_attributes")

        # Colorize the current requirement depending on type
        nodeparam = []
        if get_conf_attr("Type") \
                and req.get_value("Type") == req.rt_initial_requirement:
            nodeparam.append("color=orange")
        if get_conf_attr("Type") \
                and req.get_value("Type") == req.rt_design_decision:
            nodeparam.append("color=green")

        if get_conf_attr("Status"):
            req_status = req.get_value("Status")

            if isinstance(req_status, RequirementStatusNotDone):
                nodeparam.append("fontcolor=red")
            elif isinstance(req_status, RequirementStatusAssigned):
                nodeparam.append("fontcolor=blue")

            label = 'label="%s' % req.id

            if get_conf_attr("Priority"):
                label += "\\n[%4.2f]" % (req.get_value("Priority") * 10)

            if get_conf_attr("EffortEstimation"):
                est_effort = req.get_value("Effort estimation")
                if est_effort != None:
                    label += "\\n(%d EfEU)" % est_effort

            label += '"'
            nodeparam.append(label)

        if get_conf_attr("Class"):
            rclass = req.get_value("Class")
            if isinstance(rclass, ClassTypeImplementable):
                nodeparam.append("shape=octagon")
            elif isinstance(rclass, ClassTypeSelected):
                nodeparam.append("shape=box")

        return ",".join(nodeparam)

### TODO: below is deprecated

    # Create MAkefile Dependencies
    def cmad(self, reqscont, ofile):
        ofile.write("%s: ${REQS}\n\t${CALL_RMTOO}\n" % (self.output_filename))

    # Note that currently the 'reqscont' is not used in case of topics
    # based output.
    def output(self, reqscont):
        # Currently just pass this to the RequirementSet
        self.output_reqset(reqscont.continuum_latest(), reqscont)
