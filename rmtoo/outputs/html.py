#
# HTML output class
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

import os
import time

from rmtoo.lib.TopicSet import TopicSet

class html:

    def __init__(self, topics, param):
        self.output_dir = param[0]
        self.topic_set = topics.get(param[1])
        self.html_header_filename = param[2]
        self.html_footer_filename = param[3]
        self.read_html_arts()

    # Create Makefile Dependencies
    def cmad(self, reqscont, ofile):
        # Emit the dependencies for the topic
        self.topic_set.cmad(reqscont, ofile)

        # Each html file depends on it's topic file
        reqset = reqscont.base_requirement_set
        # For each requirement get the dependency correct
        for r in reqset.reqs:
            ofile.write("%s: " % self.filename)
            ofile.write("%s/%s.req "
                        % (reqscont.opts.directory,
                           reqset.reqs[r].id))
        ofile.write("\n\t${CALL_RMTOO}\n")



        ofile.write("REQS_HTML= %s %s" % (self.html_header_filename,
                                          self.html_footer_filename))
        for r in reqset.reqs:
            ofile.write(" %s/%s" %(

    

    def read_html_arts(self):
        fd = file(self.html_header_filename, "r")
        self.html_header = fd.read()
        fd.close()
        fd = file(self.html_footer_filename, "r")
        self.html_footer = fd.read()
        fd.close()

    # The real output
    def output(self, reqscont):
        # Currently just pass this to the RequirementSet
        self.output_reqset(reqscont.base_requirement_set)

    def output_reqset(self, reqset):
        # Fiddle the requirements into the topics
        self.topic_set.depict(reqset)
        # Call the topic to write out everything
        self.output_html_topic(self.topic_set.topic)

    def output_html_topic(self, topic):
        # Each Topic will be stored in an seperate html file.
        fd = file(os.path.join(self.output_dir, topic.id + ".html"),
                  "w")
        fd.write(self.html_header)
        
        for t in topic.t:
            assert(len(t)>=2)

            tag = t[0]
            val = t[1]

            if tag == "Name":
                # The Name itself depends on the level.
                fd.write("<h%d>%s</h%d>\n" % (topic.level+1, val,
                                              topic.level+1))
                continue

            if tag == "SubTopic":
                # A link to the other file.
                fd.write('<a href="%s.html">%s</a>\n' % 
                         (val, t[2].get_name()))
                self.output_html_topic(t[2])
                continue

            if tag == "Text":
                fd.write("%s\n" % val)
                continue

            if tag == "IncludeRequirements":
                self.output_requirements(fd, topic)
                continue

        fd.write(self.html_footer)
        fd.close()

    def output_requirements(self, fd, topic):
        for req in topic.reqs:
            self.output_requirement(fd, req, topic.level + 1)

    def output_requirement(self, fd, req, level):
        fd.write("<!- REQ '%s' -->\n" % req.id)

        fd.write("<h%d> xxxxx {%s}\label{%s}\n\\textbf{Description:} %s\n" 
                 % (level+1, req.tags["Name"],
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
