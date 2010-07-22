#
# graph output class
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

class graph:

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
        # Only output the nodes which are connected to the chosen topic. 
        for r in self.topic_set.all_reqs:
            self.output_req(r, g)
        g.write("}")
        g.close()

    @staticmethod
    def node_attributes(req):
        # Colorize the current requirement depending on type
        nodeparam = []
        if req.tags["Type"] == req.rt_initial_requirement:
            nodeparam.append("color=orange")
        if req.tags["Type"] == req.rt_design_decision:
            nodeparam.append("color=green")

        if req.tags["Status"] == req.st_not_done:
            nodeparam.append("fontcolor=red")
            nodeparam.append('label="%s\\n[%4.2f]"' %
                             (req.id, req.tags["Priority"]*10))

        if req.tags["Class"] == req.ct_implementable:
            nodeparam.append("shape=octagon")

        if req.tags["Topic"] == "internal":
            nodeparam.append("fillcolor=lightblue")
            nodeparam.append("style=filled")

        return ",".join(nodeparam)

    def output_req(self, req, dotfile):
        dotfile.write("%s [%s];\n" %
                      (req.id, self.node_attributes(req)))

        for d in req.outgoing:
            dotfile.write("%s -> %s;\n" % (req.id, d.id))
