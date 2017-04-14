'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
 HTML output class.
 
 (c) 2011-2012 by flonatel

 For licensing details see COPYING
'''

import os

from rmtoo.lib.LaTeXMarkup import LaTeXMarkup
from rmtoo.lib.configuration.Cfg import Cfg
from rmtoo.lib.ExecutorTopicContinuum import ExecutorTopicContinuum
from rmtoo.lib.logging import tracer
from rmtoo.lib.CreateMakeDependencies import CreateMakeDependencies

class html(ExecutorTopicContinuum, CreateMakeDependencies):

    def __init__(self, oconfig):
        '''Create a graph output object.'''
        tracer.debug("Called: html ouput module constructed.")
        self._config = Cfg(oconfig)
        CreateMakeDependencies.__init__(self)
        self.__fd_stack = []
        self.__topic_name_set = []
        # Take care about the openess of the ul.
        self.__ul_open_stack = []
        self.__output_directory = self._config.get_rvalue('output_directory')
        self.html_header_filename = self._config.get_rvalue('header')
        self.html_footer_filename = self._config.get_rvalue('footer')
        self.read_html_arts()

    def __ouput_html_topic_mkdirs(self):
        '''If not already there, create the directory.'''
        try:
            os.makedirs(self.__output_directory)
        except OSError, ose:
            # It's ok if already there
            pass

    def __ouput_html_topic_open_output_file(self, name, mode):
        '''Each Topic will be stored in an separate html file.'''
        fd = file(os.path.join(self.__output_directory, name + ".html"),
                  mode)
        return fd

    def topic_continuum_sort(self, vcs_commit_ids, topic_sets):
        '''Because graph2 can only one topic continuum,
           the latest (newest) is used.'''
        return [ topic_sets[vcs_commit_ids[-1].get_commit()] ]

    def topic_set_pre(self, topics_set):
        '''Do all the file and directory preparation.'''
        self.__ouput_html_topic_mkdirs()

    def __output_html_topic_write_header(self, fd):
        '''Write the html header.'''
        fd.write(self.html_header)

    def topic_pre(self, topic):
        '''Output one topic.
           This method is called once for each topic and subtopic.'''
        tracer.debug("Called: topic name [%s]." % topic.get_name())
        fd = self.__ouput_html_topic_open_output_file(topic.get_name(), "w")
        self.__output_html_topic_write_header(fd)
        self.__fd_stack.append(fd)
        self.__ul_open_stack.append(False)
#        self.output_html_topic_output_content(fd, topic)

    def topic_post(self, topic):
        '''Write out the footer and do clean ups.'''
        fd = self.__fd_stack.pop()
        self.__ul_open_stack.pop()
        self.output_html_topic_write_footer(fd)
        fd.close()
        tracer.debug("Finished: topic name [%s]" % topic.get_name())

    def topic_name(self, name):
        '''Set the name.'''
        fd = self.__fd_stack[-1]
        level = len(self.__fd_stack)
        fd.write("<h%d>%s</h%d>\n" % (level, name, level))

    def topic_text(self, text):
        '''Called when there is text to be outputted.'''
        fd = self.__fd_stack[-1]
        fd.write('<p><span class="fltext">%s</span></p>\n'
                 % LaTeXMarkup.replace_html(text))

    def topic_sub_pre(self, subtopic):
        '''Prepares a new subtopic output.'''
        fd = self.__fd_stack[-1]
        if not self.__ul_open_stack[-1]:
            fd.write('<span class="subtopiclist"><ul>')
            self.__ul_open_stack[-1] = True
        fd.write('<li><a href="%s.html">%s</a></li>\n' %
                 (subtopic.get_topic_name(), subtopic.get_id()))

    def topic_sub_post(self, subtopic):
        '''Write the header for subtopic.'''
        if self.__ul_open_stack[-1]:
            fd = self.__fd_stack[-1]
            fd.write("</ul></span>")
            self.__ul_open_stack[-1] = False

    def requirement_set_sort(self, list_to_sort):
        '''Sort by id.'''
        return sorted(list_to_sort, key=lambda r: r.get_name())

    def requirement(self, req):
        '''Output one requirement.'''
        fd = self.__fd_stack[-1]
        level = len(self.__fd_stack)

        fd.write("\n<!- REQ '%s' -->\n" % req.get_name())
        fd.write('<h%d><a name="%s">%s</a></h%d>\n' %
                 (level + 1, req.get_name(), 
                  req.get_requirement().get_value("Name").get_content(),
                  level + 1))
        fd.write("<dl>")

        fd.write('<dt><span class="dlt_description">Description</span>'
                 '</dt><dd><span class="dlv_description">%s</span></dd>' %
                  LaTeXMarkup.replace_html(req.get_requirement().get_value("Description")
                                           .get_content()))

        if req.get_requirement().is_value_available("Rationale") \
                and req.get_requirement().get_value("Rationale") != None:
            fd.write('<dt><span class="dlt_rationale">Rationale</span>'
                     '</dt><dd><span class="dlv_rationale">%s</span></dd>' %
                     LaTeXMarkup.replace_html_par(req.get_requirement().get_value("Rationale").
                                                  get_content()))

        if req.get_requirement().is_value_available("Note") \
            and req.get_requirement().get_value("Note") != None:
            fd.write('<dt><span class="dlt_note">Note</span></dt>'
                     '<dd><span class="dlv_note">%s</span></dd>'
                     % req.get_requirement().get_value("Note").get_content())

        # Only output the depends on when there are fields for output.
        if req.get_outgoing_cnt() > 0:
            # Create links to the corresponding labels.
            fd.write('<dt><span class="dlt_depends_on">Depends on:'
                     '</span></dt><dd><span class="dlv_depends_on">')
            is_first = True
            for d in sorted(req.get_iter_outgoing(), key=lambda r: r.get_name()):
                if not is_first:
                    fd.write(", ")
                is_first = False
                fd.write('<a href="%s.html#%s">%s</a>' %
                         (d.get_requirement().get_value("Topic"), d.get_name(), d.get_name()))
            fd.write("</span></dd>")

        if req.get_incoming_cnt()> 0:
            # Create links to the corresponding dependency nodes.
            fd.write('<dt><span class="dlt_dependent">Dependent'
                     '</span></dt><dd><span class="dlv_dependent">')
            is_first = True
            for d in sorted(req.get_iter_incoming(), key=lambda r: r.get_name()):
                if not is_first:
                    fd.write(", ")
                is_first = False
                fd.write('<a href="%s.html#%s">%s</a>' %
                         (d.get_requirement().get_value("Topic"), d.get_name(), 
                          d.get_name()))
            fd.write("</span></dd>")

        status = req.get_requirement().get_value("Status").get_output_string()
        clstr = req.get_requirement().get_value("Class").get_output_string()

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
                 % (req.get_name(), req.get_requirement().get_value("Priority") * 10,
                    req.get_requirement().get_value("Owner"),
                    req.get_requirement().get_value("Invented on").strftime("%Y-%m-%d"),
                    req.get_requirement().get_value("Invented by"), status, clstr))
        fd.write("</dl>")

        # Mark the end of the requirment - then it is possible to add
        # some ruler here
        fd.write('<div class="requirment_end"> </div>')

    def cmad_topic_continuum_pre(self, topics_continuum):
        '''Save the name.'''
        self.__tc_name = topics_continuum.get_name()

    def cmad_topic_set_pre(self, topic_set):
        '''Save the name.'''
        self.__topic_set = topic_set

    def cmad_topic_set_post(self, topic_set):
        '''Output symbol with all the HTMLs artifacts inside.'''
        self._cmad_file.write("OUTPUT_HTML=")
        for topic_name in self.__topic_name_set:
            self._cmad_file.write("%s.html " % os.path.join(self.__output_directory, topic_name))
        self._cmad_file.write("\n")

    def cmad_topic_pre(self, topic):
        '''Create makefile dependencies for given topic.'''
        self.__topic_name_set.append(topic.get_name())
        self._cmad_file.write("%s.html: %s %s ${%s}\n%s" %
                              (os.path.join(self.__output_directory, 
                                            topic.get_name()),
                               self.html_header_filename,
                               self.html_footer_filename,
                               self.__topic_set.create_makefile_name
                               (self.__tc_name, topic.get_name()),
                               self._get_call_rmtoo_line()))
        # TODO: more is needed! (see beneath)

    def cmad_requirement(self, requirement):
        '''Called on requirement level.'''
        self._cmad_file.write("REQS+=%s\n" % requirement.get_requirement().get_file_path())

# TODO: Ueberlegen!

    # Create Makefile Dependencies
    # Basic idea: each HTML file is dependend of the approriate topic
    # file plus the header and the footer.
    # Each html file depends on it's topic file
    def cmad(self, reqscont, ofile):
        reqset = reqscont.continuum_latest()

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
        if self.html_header_filename != None:
            fd = file(self.html_header_filename, "r")
            self.html_header = fd.read()
            fd.close()
        if self.html_footer_filename != None:
            fd = file(self.html_footer_filename, "r")
            self.html_footer = fd.read()
            fd.close()

    # The real output
    # Note that currently the 'reqscont' is not used in case of topics
    # based output.
    def output(self, reqscont):
        # Currently just pass this to the RequirementSet
        self.output_reqset(reqscont.continuum_latest())

    def output_reqset(self, reqset):
        # Call the topic to write out everything
        self.output_html_topic(self.topic_set.get_master())

    def output_html_topic_output_content(self, fd, topic):
        # Subtopics go in a ul
        ul_open = False
        for t in topic.get_tags():
            tag = t.get_tag()
            val = t.get_content()

            if tag != "SubTopic" and ul_open:
                fd.write("</ul></span>")
                ul_open = False

            if tag == "Name":
                # The Name itself depends on the level.
                fd.write("<h%d>%s</h%d>\n" % (topic.level + 1, val,
                                              topic.level + 1))
                continue

            if tag == "SubTopic":
                if not ul_open:
                    fd.write('<span class="subtopiclist"><ul>')
                    ul_open = True

                rtopic = topic.find_incoming(val)
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

    def output_html_topic_write_footer(self, fd):
        fd.write(self.html_footer)

    def output_requirements(self, fd, topic):
        # Output must be sorted - to be comparable
        for req in sorted(topic.reqs, key=lambda r: r.id):
            self.output_requirement(fd, req, topic.level + 1)

