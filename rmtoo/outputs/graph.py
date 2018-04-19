'''
 rmtoo
   Free and Open Source Requirements Management Tool

 Output handler graph.

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals

from rmtoo.lib.RequirementStatus import RequirementStatusNotDone, \
    RequirementStatusAssigned
from rmtoo.lib.ClassType import ClassTypeImplementable, \
    ClassTypeSelected
from rmtoo.lib.StdOutputParams import StdOutputParams
from rmtoo.lib.Requirement import RequirementType
from rmtoo.lib.ExecutorTopicContinuum import ExecutorTopicContinuum
from rmtoo.lib.logging import tracer
from rmtoo.lib.configuration.Cfg import Cfg
from rmtoo.lib.CreateMakeDependencies import CreateMakeDependencies


class graph(StdOutputParams, ExecutorTopicContinuum, CreateMakeDependencies):
    default_config = Cfg.new_by_json_str(
            """json:{"node_attributes":
               ["Type", "Status", "Class", "Topic", "Priority" ] }""")

    def __init__(self, oconfig):
        '''Create a graph output object.'''
        tracer.info("Called.")
        StdOutputParams.__init__(self, oconfig)
        CreateMakeDependencies.__init__(self)
        self.__used_vcs_id = None
        self.__output_file = None

        if not self._config.is_available('node_attributes'):
            self._config.set_value(
                'node_attributes',
                ["Type", "Status", "Class", "Topic", "Priority", ])

    def topic_continuum_sort(self, vcs_commit_ids, topic_sets):
        '''Because graph2 can only one topic continuum,
           the latest (newest) is used.'''
        self.__used_vcs_id = vcs_commit_ids[-1]
        return [topic_sets[vcs_commit_ids[-1].get_commit()]]

    def topic_set_pre(self, _requirement_set):
        '''This is call in the RequirementSet pre-phase.'''
        tracer.debug("Called")
        # Initialize the graph output
        self.__output_file = open(self._output_filename, "w")
        self.__output_file.write(
                "digraph reqdeps {\nrankdir=BT;\nmclimit=10.0;\n"
                "nslimit=10.0;ranksep=1;\n")

    def requirement_set_sort(self, list_to_sort):
        '''Sort by id.'''
        return sorted(list_to_sort, key=lambda r: r.get_id())

    def topic_set_post(self, _requirement_set):
        '''Write footer - close file.'''
        # Print out a node with the version number:
        self.__output_file.write(
                'ReqVersion [shape=plaintext label="ReqVersion\\n%s"]\n'
                % self.__used_vcs_id)
        self.__output_file.write("}\n")
        self.__output_file.close()

    def requirement(self, requirement):
        '''Output the given requirement.'''
        self.__output_file.write(
            '"%s" [%s];\n' %
            (requirement.get_id(),
             self.node_attributes(requirement, self._config)))

        for d in requirement.incoming:
            self.__output_file.write('"%s" -> "%s";\n' %
                                     (requirement.get_id(), d.get_id()))

# TODO: currently the =default_config is needed for graph2
    @staticmethod
    def node_attributes(req, config=default_config):

        def get_conf_attr(attr):
            return config.is_available("node_attributes") \
                and attr in config.get_value("node_attributes")

        # Colorize the current requirement depending on type
        nodeparam = []
        if get_conf_attr("Type") \
                and req.get_value("Type") \
                == RequirementType.initial_requirement:
            nodeparam.append("color=orange")
        if get_conf_attr("Type") \
                and req.get_value("Type") == RequirementType.design_decision:
            nodeparam.append("color=green")

        if get_conf_attr("Status"):
            req_status = req.get_status()

            if isinstance(req_status, RequirementStatusNotDone):
                nodeparam.append("fontcolor=red")
            elif isinstance(req_status, RequirementStatusAssigned):
                nodeparam.append("fontcolor=blue")

            label = 'label="%s' % req.get_id().replace("/", "\\n/")

            if get_conf_attr("Priority"):
                label += "\\n[%4.2f]" % (req.get_value("Priority") * 10)

            if get_conf_attr("EffortEstimation"):
                est_effort = req.get_value("Effort estimation")
                if est_effort is not None:
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

    def cmad_topic_continuum_pre(self, _):
        '''Write out the one and only dependency to all the requirements.'''
        tracer.debug("Called.")
        CreateMakeDependencies.write_reqs_dep(self._cmad_file,
                                              self._output_filename)
