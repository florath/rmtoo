#
# LaTeX output class version 2
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

import os
import time

from rmtoo.lib.TopicSet import TopicSet
from rmtoo.lib.RMTException import RMTException

class latex2:
    default_config = { "req_attributes": ["Id", "Priority", "Owner", "Invented on",
                                          "Invented by", "Status", "Class"] }

    level_names = [
        "chapter",
        "section",
        "subsection",
        "subsubsection" ]

    def __init__(self, params):
        self.topic_name = params[0]
        self.filename = params[1]
        self.config = latex2.default_config
        if len(params)>2:
            self.config = params[2]

    def set_topics(self, topics):
        self.topic_set = topics.get(self.topic_name)

    # Create Makefile Dependencies
    def cmad(self, reqscont, ofile):
        ofile.write("REQS_LATEX2=%s\n" % self.filename)
        reqset = reqscont.continuum_latest()
        # For each requirement get the dependency correct
        ofile.write("%s: " % self.filename)
        for r in reqset.reqs:
            ofile.write("%s/%s.req "
                        % (reqscont.config.reqs_spec["directory"],
                           reqset.reqs[r].id))
        ofile.write("\n\t${CALL_RMTOO}\n")

    # The real output
    # Note that currently the 'reqscont' is not used in case of topics
    # based output.
    def output(self, reqscont):
        # Currently just pass this to the RequirementSet
        self.output_reqset(reqscont.continuum_latest())

    def output_reqset(self, reqset):
        # Call the topic to write out everything
        self.output_latex_topic_set(self.topic_set)

    def output_latex_topic_set(self, topic_set):
        fd = file(self.filename, "w")
        # The TopicSet itself needs no output.
        self.output_latex_topic(fd, topic_set.get_master())
        fd.close()

    def output_latex_topic(self, fd, topic):
        fd.write("%% Output topic '%s'\n" % topic.name)
        for t in topic.t:

            tag = t.get_tag()
            val = t.get_content()

            if tag == "Name":
                # The name itself is dependent on the level
                fd.write("\\%s{%s}\n" % (self.level_names[topic.level], val))
                continue

            if tag == "SubTopic":
                rtopic = topic.find_outgoing(val)
                self.output_latex_topic(fd, rtopic)
                continue

            if tag == "Text":
                fd.write("%s\n" % val)
                continue

            if tag == "IncludeRequirements":
                self.output_requirements(fd, topic)
                continue

            print("+++ ERROR: Ignoring unknown tag '%s' in "
                  "topic file" % tag)

    def output_requirements(self, fd, topic):
        for req in sorted(topic.reqs, key = lambda r: r.id):
            self.output_requirement(fd, req, topic.level + 1)

    def output_requirement(self, fd, req, level):
        fd.write("%% REQ '%s'\n" % req.id)

        fd.write("\%s{%s}\label{%s}\n\\textbf{Description:} %s\n" 
                 % (self.level_names[level], 
                    req.get_value("Name").get_content(),
                    req.id, req.get_value("Description").get_content()))

        if req.is_value_available("Rationale") \
                and req.get_value("Rationale")!=None:
            fd.write("\n\\textbf{Rationale:} %s\n"
                     % req.get_value["Rationale"])

        if req.is_value_available("Note") and req.get_value("Note")!=None:
            fd.write("\n\\textbf{Note:} %s\n" % req.get_value("Note"))

        # Only output the depends on when there are fields for output.
        if len(req.outgoing)>0:
            # Create links to the corresponding labels.
            fd.write("\n\\textbf{Depends on:} ")
            fd.write(", ".join(["\\ref{%s} \\nameref{%s}" % (d.id, d.id) 
                                for d in req.outgoing]))
            fd.write("\n")

        if len(req.incoming)>0:
            # Create links to the corresponding dependency nodes.
            fd.write("\n\\textbf{Solved by:} ")
            # No comma at the end.
            fd.write(", ".join(["\\ref{%s} \\nameref{%s}" % (d.id, d.id) 
                                for d in sorted(req.incoming,
                                                key=lambda r: r.id)]))
            fd.write("\n")

        if req.get_value("Status")==req.st_finished:
            status = "completed"
        else:
            status = "open"

        if req.get_value("Class")==req.ct_implementable:
            clstr="implementable"
        else:
            clstr="detailable"

        fd.write("\n\\par\n{\small \\begin{center}\\begin{tabular}{rlrlrl}\n")

        # Put mostly three things in a line.
        i=0
        for rattr in self.config["req_attributes"]:
            if rattr=="Id":
                fd.write("\\textbf{Id:} & %s " % req.id)
            elif rattr=="Priority":
                fd.write("\\textbf{Priority:} & %4.2f " 
                         % (req.get_value("Priority")*10))
            elif rattr=="Owner":
                fd.write("\\textbf{Owner:} & %s" % req.get_value("Owner"))
            elif rattr=="Invented on":
                fd.write("\\textbf{Invented on:} & %s " 
                         % time.strftime("%Y-%m-%d", 
                                         req.get_value("Invented on")))
            elif rattr=="Invented by":
                fd.write("\\textbf{Invented by:} & %s " 
                         % req.get_value("Invented by"))
            elif rattr=="Status":
                fd.write("\\textbf{Status:} & %s " % status)
            elif rattr=="Class":
                fd.write("\\textbf{Class:} & %s " % clstr)
            else:
                # This can never happen
                assert(False)
            i+=1
            if i==3:
                i=0
                fd.write("\\\ \n")
            else:
                fd.write(" & ")
        while i<2:
            fd.write("& & ")
            i+=1

        fd.write("\end{tabular}\end{center} }\n")
