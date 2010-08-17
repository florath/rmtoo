#
# graph output class
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

class graph:
    default_config = { "node_attributes": ["Type", "Status", "Class", "Topic"] }

    def __init__(self, params):
        self.topic_name = params[0]
        self.output_filename = params[1]
        self.config = graph.default_config
        if len(params)>2:
            self.config = params[2]

    def set_topics(self, topics):
        self.topic_set = topics.get(self.topic_name)
  
    # Create MAkefile Dependencies
    def cmad(self, reqscont, ofile):
        ofile.write("%s: ${REQS}\n\t${CALL_RMTOO}\n" % (self.output_filename))
        
    # Note that currently the 'reqscont' is not used in case of topics
    # based output.
    def output(self, reqscont):
        # Currently just pass this to the RequirementSet
        self.output_reqset(reqscont.continnum_latest(), reqscont)

    def output_reqset(self, reqset, reqscont):
        # Initialize the graph output
        g = file(self.output_filename, "w")
        g.write("digraph reqdeps {\nrankdir=BT;\nmclimit=10.0;\n"
                "nslimit=10.0;ranksep=1;\n")
        # Only output the nodes which are connected to the chosen topic. 
        for r in sorted(self.topic_set.reqset.nodes, key = lambda r: r.id):
            self.output_req(r, g)
            
        # Print out a node with the version number:
        g.write('ReqVersion [shape=plaintext label="ReqVersion\\n%s"]\n'
                % (reqscont.continnum_latest_id()))
            
        g.write("}")
        g.close()

    @staticmethod
    def node_attributes(req, config = default_config):

        def get_conf_attr(attr):
            return "node_attributes" in config \
                and attr in config["node_attributes"]

        # Colorize the current requirement depending on type
        nodeparam = []
        if get_conf_attr("Type") \
                and req.tags["Type"] == req.rt_initial_requirement:
            nodeparam.append("color=orange")
        if get_conf_attr("Type") \
                and req.tags["Type"] == req.rt_design_decision:
            nodeparam.append("color=green")

        if get_conf_attr("Status") \
                and req.tags["Status"] == req.st_not_done:
            nodeparam.append("fontcolor=red")
            nodeparam.append('label="%s\\n[%4.2f]"' %
                             (req.id, req.tags["Priority"]*10))

        if get_conf_attr("Class") \
                and req.tags["Class"] == req.ct_implementable:
            nodeparam.append("shape=octagon")

        if get_conf_attr("Topic") \
                and req.tags["Topic"] == "internal":
            nodeparam.append("fillcolor=lightblue")
            nodeparam.append("style=filled")

        return ",".join(nodeparam)

    def output_req(self, req, dotfile):
        dotfile.write("%s [%s];\n" %
                      (req.id, self.node_attributes(req, self.config)))

        for d in req.outgoing:
            dotfile.write("%s -> %s;\n" % (req.id, d.id))
