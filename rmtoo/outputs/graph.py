#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# graph output class
#
# (c) 2010-2011 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.RequirementStatus import RequirementStatusNotDone, \
    RequirementStatusAssigned, RequirementStatusFinished
from rmtoo.lib.ClassType import ClassTypeImplementable, \
    ClassTypeDetailable, ClassTypeSelected

class graph:
    default_config = { "node_attributes":
                       ["Type", "Status", "Class", "Topic", "Priority", ] }

    def __init__(self, topic_set, params):
        self.topic_set = topic_set
        self.output_filename = params['output_filename']
        # TODO Default class handling
#        self.config = graph.default_config
#        if len(params)>2:
#            self.config = params[2]
        self.config = params
        if 'node_attributes' not in self.config:
            self.config['node_attributes'] = \
                ["Type", "Status", "Class", "Topic", "Priority", ]

    # Create MAkefile Dependencies
    def cmad(self, reqscont, ofile):
        ofile.write("%s: ${REQS}\n\t${CALL_RMTOO}\n" % (self.output_filename))

    # Note that currently the 'reqscont' is not used in case of topics
    # based output.
    def output(self, reqscont):
        # Currently just pass this to the RequirementSet
        self.output_reqset(reqscont.continuum_latest(), reqscont)

    def output_reqset(self, reqset, reqscont):
        # Initialize the graph output
        g = file(self.output_filename, "w")
        g.write("digraph reqdeps {\nrankdir=BT;\nmclimit=10.0;\n"
                "nslimit=10.0;ranksep=1;\n")
        # Only output the nodes which are connected to the chosen topic. 
        for r in sorted(self.topic_set.reqset.nodes, key=lambda r: r.id):
            self.output_req(r, g)

        # Print out a node with the version number:
        g.write('ReqVersion [shape=plaintext label="ReqVersion\\n%s"]\n'
                % (reqscont.continuum_latest_id()))

        g.write("}")
        g.close()

    @staticmethod
    def node_attributes(req, config=default_config):

        def get_conf_attr(attr):
            return "node_attributes" in config \
                and attr in config["node_attributes"]

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

    def output_req(self, req, dotfile):
        dotfile.write('"%s" [%s];\n' %
                      (req.id, self.node_attributes(req, self.config)))

        for d in req.outgoing:
            dotfile.write('"%s" -> "%s";\n' % (req.id, d.id))
