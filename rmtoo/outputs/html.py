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
from rmtoo.lib.LaTeXMarkup import LaTeXMarkup

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
                fd.write('<p><span class="fltext">%s</span></p>\n'
                         % LaTeXMarkup.replace_html(val))
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
        fd.write("\n<!- REQ '%s' -->\n" % req.id)
        fd.write('<h%d><a name="%s">%s</a></h%d>\n' % 
                 (level+1, req.id, req.tags["Name"], level+1))
        fd.write("<dl>")

        fd.write('<dt><span class="dlt_description">Description</span>'
                 '</dt><dd><span class="dlv_description">%s</span></dd>' % 
                  LaTeXMarkup.replace_html(req.tags["Description"]))

        if "Rationale" in req.tags and req.tags["Rationale"]!=None:
            fd.write('<dt><span class="dlt_rationale">Rationale</span>'
                     '</dt><dd><span class="dlv_rationale">%s</span></dd>' %
                     LaTeXMarkup.replace_html_par(req.tags["Rationale"]))

        if "Note" in req.tags and req.tags["Note"]!=None:
            fd.write('<dt><span class="dlt_note">Note</span></dt>'
                     '<dd><span class="dlv_note">%s</span></dd>' 
                     % req.tags["Note"])

        # Only output the depends on when there are fields for output.
        if len(req.outgoing)>0:
            # Create links to the corresponding labels.
            fd.write('<dt><span class="dlt_depends_on">Depends on:'
                     '</span></dt><dd><span class="dlv_depends_on"')
            is_first = True
            for d in req.outgoing:
                if not is_first:
                    fd.write(", ")
                is_first=False
                fd.write('<a href="%s.html#%s">%s</a>' % 
                         (d.tags["Topic"], d.id, d.id))
            fd.write("</span></dd>")

        if len(req.incoming)>0:
            # Create links to the corresponding dependency nodes.
            fd.write('<dt><span class="dlt_dependent">Dependent'
                     '</span></dt><dd><span class="dlv_dependent">')
            is_first = True
            for d in req.incoming:
                if not is_first:
                    fd.write(", ")
                is_first=False
                fd.write('<a href="%s.html#%s">%s</a>' % 
                         (d.tags["Topic"], d.id, d.id))
            fd.write("</span></dd>")

        if req.tags["Status"]==req.st_finished:
            status = "completed"
        else:
            status = "open"

        if req.tags["Class"]==req.ct_implementable:
            clstr="implementable"
        else:
            clstr="detailable"

        fd.write('<dt><span class="dlt_id">Id</span></dt>'
                 '<dd><span class="dlv_id">%s</span></dd>'
                 '<dt><span class="dlt_priority">Priority</span></dt>'
                 '<dd><span class="dlv_priority">%4.2f</span></dd>'
                 '<dt><span class="dlt_owner">Owner</span></dt>'
                 '<dd><span class="dlv_owner">%s</span></dd>'
                 '<dt><span class="dlt_invented_on">Invented on</span></dt>'
                 '<dd><span class="dlv_invented_on">%s</span></dd>'
                 '<dt><span class="dlt_invented_by">Invented by</span></dt>'
                 '<dd><span class="dlv_invented_by">%s</span></dd>'
                 '<dt><span class="dlt_status">Status</span></dt>'
                 '<dd><span class="dlv_status">%s</span></dd>'
                 '<dt><span class="dlt_class">Class</span></dt>'
                 '<dd><span class="dlv_class">%s</span></dd>'
                 % (req.id, req.tags["Priority"]*10, req.tags["Owner"],
                    time.strftime("%Y-%m-%d", req.tags["Invented on"]),
                    req.tags["Invented by"], status, clstr))
        fd.write("</dl>")

        # Mark the end of the requirment - then it is possible to add
        # some ruler here
        fd.write('<div class="requirment_end"> </div>')
