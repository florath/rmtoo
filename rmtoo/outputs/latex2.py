#
# LaTeX2 output class
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

    level_names = [
        "chapter",
        "section",
        "subsection",
        "subsubsection" ]

    def __init__(self, param):
        self.filename = param[0]
        self.topic_set = TopicSet(param[1])

    # Create Makefile Dependencies
    def cmad(self, reqscont, ofile):
        ofile.write("REQS_LATEX2=%s\n" % self.filename)
        reqset = reqscont.base_requirement_set
        # For each requirement get the dependency correct
        ofile.write("%s: " % self.filename)
        for r in reqset.reqs:
            ofile.write("%s/%s.req "
                        % (reqscont.opts.directory,
                           reqset.reqs[r].id))
        ofile.write("\n\t${CALL_RMTOO}\n")

    # The real output
    def output(self, reqscont):
        # Currently just pass this to the RequirementSet
        self.output_reqset(reqscont.base_requirement_set)

    def output_reqset(self, reqset):
        # Fiddle the requirements into the topics
        self.topic_set.depict(reqset)
        # Call the topic to write out everything
        self.output_latex_topic_set(self.topic_set)

    def output_latex_topic_set(self, topic_set):
        fd = file(self.filename, "w")
        # The TopicSet itself needs no output.
        self.output_latex_topic(fd, topic_set.topic)
        fd.close()

    def output_latex_topic(self, fd, topic):
        fd.write("%% Output topic '%s'\n" % topic.id)
        for t in topic.t:
            assert(len(t)>=2)

            tag = t[0]
            val = t[1]

            if tag == "Name":
                # The name itself is dependent on the level
                fd.write("\\%s{%s}\n" % (self.level_names[topic.level], val))
                continue

            if tag == "SubTopic":
                self.output_latex_topic(fd, t[2])
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
        for req in topic.reqs:
            self.output_requirement(fd, req, topic.level + 1)

    def output_requirement(self, fd, req, level):
        fd.write("%% REQ '%s'\n" % req.id)

        fd.write("\%s{%s}\label{%s}\n\\textbf{Description:} %s\n" 
                 % (self.level_names[level], req.tags["Name"],
                    req.id, req.tags["Description"]))

        if "Rationale" in req.tags:
            fd.write("\n\\textbf{Rationale:} %s\n" % req.tags["Rationale"])

        if "Note" in req.tags:
            fd.write("\n\\textbf{Note:} %s\n" % req.tags["Note"])

        # Only output the depends on when there are fields for output.
        if len(req.outgoing)>0:
            # Create links to the corresponding labels.
            fd.write("\n\\textbf{Depends on:} ")
            for d in req.outgoing:
                fd.write("\\ref{%s} \\nameref{%s}, " % (d.id, d.id))
            fd.write("\n")

        if len(req.incoming)>0:
            # Create links to the corresponding dependency nodes.
            fd.write("\n\\textbf{Dependent:} ")
            for d in req.incoming:
                fd.write("\\ref{%s} \\nameref{%s}, " % (d.id, d.id))
            fd.write("\n")

        if req.tags["Status"]==req.st_finished:
            status = "completed"
        else:
            status = "open"

        if req.tags["Class"]==req.ct_implementable:
            clstr="implementable"
        else:
            clstr="detailable"

        fd.write("\n\\par\n{\small \\begin{center}\\begin{tabular}{rlrlrl}\n"
                 "\\textbf{Id:} & %s & "
                 "\\textbf{Priority:} & %4.2f & "
                 "\\textbf{Owner:} & %s \\\ \n"
                 "\\textbf{Invented on:} & %s & "
                 "\\textbf{Invented by:} & %s & "
                 "\\textbf{Status:} & %s \\\ \n"
                 "\\textbf{Class:} & %s & & & & \\\ \n"
                 "\end{tabular}\end{center} }"
                 % (req.id, req.tags["Priority"]*10, req.tags["Owner"],
                    time.strftime("%Y-%m-%d", req.tags["Invented on"]),
                    req.tags["Invented by"], status, clstr))


