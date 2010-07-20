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

    def __init__(self, param):
        self.topic_name = param[0]
        self.output_dir = param[1]
        self.html_header_filename = param[2]
        self.html_footer_filename = param[3]
        self.read_html_arts()

    def set_topics(self, topics):
        self.topic_set = topics.get(self.topic_name)

    # Create Makefile Dependencies
    # Basic idea: each HTML file is dependend of the approriate topic
    # file plus the header and the footer.
    # Each html file depends on it's topic file
    def cmad(self, reqscont, ofile):
        # Emit the dependencies for the topic
        self.topic_set.cmad(reqscont, ofile)

        reqset = reqscont.base_requirement_set

        # Dependencies of every single topic html page
        for topic in self.topic_set.nodes:
            ofile.write("%s.html: %s %s ${%s}\n\t${CALL_RMTOO}\n" %
                        (os.path.join(self.output_dir, topic.name),
                         self.html_header_filename,
                         self.html_footer_filename,
                         self.topic_set.create_makefile_name(topic.name)))

        # All HTML files
        ofile.write("OUTPUT_HTML=")
        for topic in self.topic_set.nodes:
            ofile.write("%s.html " % os.path.join(self.output_dir, topic.name))
        ofile.write("\n")

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
        self.output_html_topic(self.topic_set.get_master())

    def output_html_topic(self, topic):
        # If not already there, create the directory.

        try:
            os.makedirs(self.output_dir)
        except OSError, ose:
            # It's ok if already there
            pass

        # Each Topic will be stored in an seperate html file.
        fd = file(os.path.join(self.output_dir, topic.name + ".html"),
                  "w")
        fd.write(self.html_header)

        # Subtopics go in a ul
        ul_open = False
        for t in topic.t:
            assert(len(t)>=2)

            tag = t[0]
            val = t[1]

            if tag != "SubTopic" and ul_open:
                fd.write("</ul></span>")
                ul_open = False

            if tag == "Name":
                # The Name itself depends on the level.
                fd.write("<h%d>%s</h%d>\n" % (topic.level+1, val,
                                              topic.level+1))
                continue

            if tag == "SubTopic":
                if not ul_open:
                    fd.write('<span class="subtopiclist"><ul>')
                    ul_open = True

                rtopic = topic.find_outgoing(val)
                # A link to the other file.
                fd.write('<li><a href="%s.html">%s</a></li>\n' % 
                         (val, rtopic.get_name()))
                self.output_html_topic(rtopic)
                continue

            if tag == "Text":
                fd.write("%s\n" % val)
                continue

            if tag == "IncludeRequirements":
                self.output_requirements(fd, topic)
                continue

        if ul_open:
            fd.write("</ul></span>")

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
