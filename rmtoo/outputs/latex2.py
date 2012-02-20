'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
 LaTeX output class version 2.
  
 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import os
import time

from rmtoo.lib.TopicSet import TopicSet
from rmtoo.lib.Constraints import Constraints
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.StdOutputParams import StdOutputParams
from rmtoo.lib.ExecutorTopicContinuum import ExecutorTopicContinuum
from rmtoo.lib.logging.EventLogging import tracer

class latex2(StdOutputParams, ExecutorTopicContinuum):
    default_config = { "req_attributes":
                       ["Id", "Priority", "Owner", "Invented on",
                        "Invented by", "Status", "Class"] }

    level_names = [
        "chapter",
        "section",
        "subsection",
        "subsubsection",
        "paragraph",
        "subparagraph" ]

    def __init__(self, oconfig):
        '''Create a graph output object.'''
        tracer.debug("Called.")
        StdOutputParams.__init__(self, oconfig)

        if not self._config.is_available('req_attributes'):
            self._config.set_value('req_attributes',
                ["Id", "Priority", "Owner", "Invented on",
                        "Invented by", "Status", "Class"])
        self.__level = -1

    def topics_set_pre(self, topics_set):
        '''Prepare the output file.'''
        self.__fd = file(self._output_filename, "w")

        # The TopicSet itself needs no output.
        # TODO:
#        self.output_latex_topic(fd, topic_set.get_master(), ce3set)
#        constraints = Constraints.collect(topic_set)
#        self.output_latex_constraints(fd, topic_set, constraints)

    def topics_set_post(self, topics_set):
        '''Clean up file.'''
        self.__fd.close()

    def topic_pre(self, topic):
        '''Output one topic.'''
        self.__level += 1
        self.__fd.write("%% Output topic '%s'\n" % topic.name)

    def topic_post(self, topic):
        '''Cleanup things for topic.'''
        self.__level -= 1

    def topic_name(self, name):
        '''Output the topic name.'''
        self.__fd.write("\\%s{%s}\n" % (self.level_names[self.__level], name))
        
    def topic_text(self, text):
        '''Write out the given text.'''
        self.__fd.write("%s\n" % text)
        
    def requirement_set_pre(self, rset):
        '''Prepare the requirements set output.'''
        self.__ce3set = rset.get_ce3set()
        
    def requirement(self, req):
        self.__fd.write("%% REQ '%s'\n" % req.id)

        self.__fd.write("\%s{%s}\label{%s}\n\\textbf{Description:} %s\n"
                 % (self.level_names[self.__level+1],
                    req.get_value("Name").get_content(),
                    latex2.strescape(req.id),
                    req.get_value("Description").get_content()))

        if req.is_val_av_and_not_null("Rationale"):
            self.__fd.write("\n\\textbf{Rationale:} %s\n"
                     % req.get_value("Rationale").get_content())

        if req.is_val_av_and_not_null("Note"):
            self.__fd.write("\n\\textbf{Note:} %s\n"
                     % req.get_value("Note").get_content())

        # Only output the depends on when there are fields for output.
        if len(req.outgoing) > 0:
            # Create links to the corresponding labels.
            self.__fd.write("\n\\textbf{Depends on:} ")
            self.__fd.write(", ".join(["\\ref{%s} \\nameref{%s}" %
                                (latex2.strescape(d.id),
                                 latex2.strescape(d.id))
                                for d in sorted(req.outgoing,
                                                key=lambda r: r.id)]))
            self.__fd.write("\n")

        if len(req.incoming) > 0:
            # Create links to the corresponding dependency nodes.
            self.__fd.write("\n\\textbf{Solved by:} ")
            # No comma at the end.
            self.__fd.write(", ".join(["\\ref{%s} \\nameref{%s}" %
                                (latex2.strescape(d.id),
                                 latex2.strescape(d.id))
                                for d in sorted(req.incoming,
                                                key=lambda r: r.id)]))
            self.__fd.write("\n")

        if self.__ce3set != None:
            cnstrt = self.__ce3set.get(req.get_id())
            if cnstrt != None and cnstrt.len() > 0:
                self.__fd.write("\n\\textbf{Constraints:} ")
    
                #cl = req.get_value("Constraints") # .split()
    
                cs = []
                for k, v in sorted(cnstrt.get_values().iteritems()):
                    #name = v.get_value("Name").get_content()
                    refid = latex2.strescape(k)
                    rs = "\\ref{CONSTRAINT%s} \\nameref{CONSTRAINT%s}" \
                           % (refid, refid)
                    description = v.description()
                    if description != None:
                        rs += " [" + description + "] "
                    cs.append(rs)
    
                self.__fd.write(", ".join(cs))
                self.__fd.write("\n")

        status = req.get_value("Status").get_output_string()
        clstr = req.get_value("Class").get_output_string()

        self.__fd.write("\n\\par\n{\small \\begin{center}\\begin{tabular}{rlrlrl}\n")

        # Put mostly three things in a line.
        i = 0
        for rattr in self._config.get_value("req_attributes"):
            if rattr == "Id":
                self.__fd.write("\\textbf{Id:} & %s " % req.id)
            elif rattr == "Priority":
                self.__fd.write("\\textbf{Priority:} & %4.2f "
                         % (req.get_value("Priority") * 10))
            elif rattr == "Owner":
                self.__fd.write("\\textbf{Owner:} & %s" % req.get_value("Owner"))
            elif rattr == "Invented on":
                self.__fd.write("\\textbf{Invented on:} & %s "
                         % req.get_value("Invented on").strftime("%Y-%m-%d"))
            elif rattr == "Invented by":
                self.__fd.write("\\textbf{Invented by:} & %s "
                         % req.get_value("Invented by"))
            elif rattr == "Status":
                self.__fd.write("\\textbf{Status:} & %s " % status)
            elif rattr == "Class":
                self.__fd.write("\\textbf{Class:} & %s " % clstr)
            else:
                # This only happens when a wrong configuration is supllied.
                raise RMTException(85, "Wrong latex2 output configuration "
                                   "supplied: unknown tag [%s]" % rattr)
            i += 1
            if i == 3:
                i = 0
                self.__fd.write("\\\ \n")
            else:
                self.__fd.write(" & ")
        while i < 2:
            self.__fd.write("& & ")
            i += 1

        self.__fd.write("\end{tabular}\end{center} }\n\n")



### TODO: Ueberlegen

    def set_topics(self, topics):
        self.topic_set = topics.get(self.topic_name)

    @staticmethod
    def strescape(string):
        r = ""
        for s in string:
            if ord(s) >= 32 and ord(s) < 127:
                r += s
            else:
                r += "%02x" % ord(s)
        return r

    # Create Makefile Dependencies
    def cmad(self, reqscont, ofile):
        ofile.write("REQS_LATEX2=%s\n" % self.filename)
        reqset = reqscont.continuum_latest()
        # For each requirement get the dependency correct
        reqs_directory = reqscont.config.get_value('requirements.input.directory')
        ofile.write("%s: " % self.filename)
        for r in reqset.reqs:
            ofile.write("%s/%s.req "
                        % (reqs_directory, reqset.reqs[r].id))
        ofile.write("\n\t${CALL_RMTOO}\n")

    # The real output
    # Note that currently the 'reqscont' is not used in case of topics
    # based output.
    def output(self, reqscont):
        # Currently just pass this to the RequirementSet
        self.output_reqset(reqscont.continuum_latest())

    def output_reqset(self, reqset):
        # Call the topic to write out everything
        self.output_latex_topic_set(self.topic_set, reqset.ce3set)

    def output_requirements(self, fd, topic, ce3set):
        for req in sorted(topic.reqs, key=lambda r: r.id):
            self.output_requirement(fd, req, topic.level + 1, ce3set)

    def output_latex_constraints(self, fd, topic_set, constraints):

        #print("AC %s" % self.constraints)

        if len(constraints) > 0:
            fd.write("\\%s{Constraints}\n" % self.level_names[0])
            for cname, cnstrt in sorted(constraints.iteritems()):
                self.output_latex_one_constraint(fd, cname, cnstrt)

    def output_latex_one_constraint(self, fd, cname, cnstrt):
        cname = latex2.strescape(cname)
        fd.write("%% CONSTRAINT '%s'\n" % cname)

        fd.write("\%s{%s}\label{CONSTRAINT%s}\n\\textbf{Description:} %s\n"
                 % (self.level_names[1],
                    cnstrt.get_value("Name").get_content(),
                    cname, cnstrt.get_value("Description").get_content()))

        if cnstrt.is_val_av_and_not_null("Rationale"):
            fd.write("\n\\textbf{Rationale:} %s\n"
                     % cnstrt.get_value("Rationale").get_content())

        if cnstrt.is_val_av_and_not_null("Note"):
            fd.write("\n\\textbf{Note:} %s\n"
                     % cnstrt.get_value("Note").get_content())



