'''
 rmtoo
   Free and Open Source Requirements Management Tool

 LaTeX output class version 2.

 (c) 2010-2012,2017,2025 by flonatel GmbH & Co. KG / Andreas Florath

 For licensing details see COPYING
'''

import io

from rmtoo.lib.Constraints import Constraints
from rmtoo.lib.TestCases import collect
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.StdOutputParams import StdOutputParams
from rmtoo.lib.ExecutorTopicContinuum import ExecutorTopicContinuum
from rmtoo.lib.logging import tracer
from rmtoo.lib.CreateMakeDependencies import CreateMakeDependencies
from rmtoo.outputs.latex_base import LatexOutputBase


class latex2(StdOutputParams, ExecutorTopicContinuum,
             CreateMakeDependencies, LatexOutputBase):
    default_config = {"req_attributes":
                      ["Id", "Priority", "Owner", "Invented on",
                       "Invented by", "Status", "Class"]}

    level_names = [
        "chapter",
        "section",
        "subsection",
        "subsubsection",
        "paragraph",
        "subparagraph"
    ]

    def __init__(self, oconfig):
        '''Create a graph output object.'''
        tracer.info("Called.")
        StdOutputParams.__init__(self, oconfig)
        CreateMakeDependencies.__init__(self)
        LatexOutputBase.__init__(self)
        self.__ce3set = None
        self.__fd = None

        if not self._config.is_available('req_attributes'):
            self._config.set_value(
                'req_attributes',
                ["Id", "Priority", "Owner", "Invented on",
                 "Invented by", "Status", "Class"])
        self.__level = -1

    def topic_set_pre(self, _topics_set):
        '''Prepare the output file.'''
        self.__fd = io.open(self._output_filename, "w", encoding="utf-8")

    def topic_set_post(self, topic_set):
        '''Print out the constraints and clean up file.'''
        tracer.debug("Called; output constraints.")
        if topic_set is None:
            assert False
        constraints = Constraints.collect(topic_set)
        self._output_latex_constraints(self.__fd, constraints)
        testcases = collect(topic_set)
        self._output_latex_testcases(self.__fd, testcases)
        tracer.debug("Clean up file.")
        self.__fd.close()
        tracer.debug("Finished.")

    def topic_pre(self, topic):
        '''Output one topic.'''
        self.__level += 1
        self.__fd.write(u"%% Output topic '%s'\n" % topic.name)

    def topic_post(self, _topic):
        '''Cleanup things for topic.'''
        self.__level -= 1

    def topic_name(self, name):
        '''Output the topic name.'''
        self.__fd.write(u"\\%s{%s}\n" % (self.level_names[self.__level], name))

    def topic_text(self, text):
        '''Write out the given text.'''
        self.__fd.write(u"%s\n" % text)

    def requirement_set_pre(self, rset):
        '''Prepare the requirements set output.'''
        self.__ce3set = rset.get_ce3set()
        self.__testcases = rset.get_testcases()

    def requirement_set_sort(self, list_to_sort):
        '''Sort by id.'''
        return sorted(list_to_sort, key=lambda r: r.get_id())

    def requirement(self, req):
        '''Write out one requirement.'''
        self.__fd.write(u"%% REQ '%s'\n" % req.get_id())

        self.__fd.write(u"\\%s{%s}\\label{%s}\n\\textbf{Description:} %s\n"
                        % (self.level_names[self.__level + 1],
                           req.get_value("Name").get_content(),
                           self._strescape(req.get_id()),
                           req.get_value("Description").get_content()))

        if req.is_val_av_and_not_null("Rationale"):
            self.__fd.write(u"\n\\textbf{Rationale:} %s\n"
                            % req.get_value("Rationale").get_content())

        if req.is_val_av_and_not_null("Note"):
            self.__fd.write(u"\n\\textbf{Note:} %s\n"
                            % req.get_value("Note").get_content())

        # Only output the depends on when there are fields for output.
        if len(req.incoming) > 0:
            # Create links to the corresponding labels.
            self.__fd.write(u"\n\\textbf{Depends on:} ")
            self.__fd.write(u", ".join(
                ["\\ref{%s} \\nameref{%s}" %
                 (self._strescape(d.get_id()),
                  self._strescape(d.get_id()))
                 for d in sorted(req.incoming,
                                 key=lambda r: r.get_id())]))
            self.__fd.write(u"\n")

        if len(req.outgoing) > 0:
            # Create links to the corresponding dependency nodes.
            self.__fd.write(u"\n\\textbf{Solved by:} ")
            # No comma at the end.
            self.__fd.write(u", ".join(
                ["\\ref{%s} \\nameref{%s}" %
                 (self._strescape(d.get_id()),
                  self._strescape(d.get_id()))
                 for d in sorted(req.outgoing,
                                 key=lambda r: r.get_id())]))
            self.__fd.write(u"\n")

        if self.__ce3set is not None:
            cnstrt = self.__ce3set.get(req.get_id())
            if cnstrt is not None and len(cnstrt) > 0:
                self.__fd.write(u"\n\\textbf{Constraints:} ")
                cstrs = []
                for key, val in sorted(cnstrt.items()):
                    refid = self._strescape(key)
                    refctr = "\\ref{CONSTRAINT%s} \\nameref{CONSTRAINT%s}" \
                             % (refid, refid)
                    description = val.description()
                    if description is not None:
                        refctr += " [" + description + "] "
                    cstrs.append(refctr)
                    # Also put a reference (for later use) in the
                    # constraints to requirements ref.
                    self._add_constraint_req_ref(refid, req.get_id())

                self.__fd.write(u", ".join(cstrs))
                self.__fd.write(u"\n")

        testcases = req.get_value_default("Test Cases")
        if testcases is not None:
            self.__fd.write(u"\n\\textbf{Test Cases:} ")
            tcout = []
            for testcase in testcases:
                refid = self._strescape(testcase)
                refctr = "\\ref{TESTCASE%s} \\nameref{TESTCASE%s}" \
                         % (refid, refid)
                tcout.append(refctr)

            self.__fd.write(u", ".join(tcout))
            self.__fd.write(u"\n")

        status = req.get_value("Status").get_output_string()
        clstr = req.get_value("Class").get_output_string()
        rtype = req.get_value("Type").as_string()

        self.__fd.write(u"\n\\par\n{\\small \\begin{center}"
                        "\\begin{tabular}{rlrlrl}\n")

        # Put mostly three things in a line.
        i = 0
        for rattr in self._config.get_value("req_attributes"):
            if rattr == "Id":
                self.__fd.write(u"\\textbf{Id:} & %s " % req.get_id())
            elif rattr == "Priority":
                self.__fd.write(u"\\textbf{Priority:} & %4.2f "
                                % (req.get_value("Priority") * 10))
            elif rattr == "Owner":
                self.__fd.write(u"\\textbf{Owner:} & %s" %
                                req.get_value("Owner"))
            elif rattr == "Invented on":
                self.__fd.write(u"\\textbf{Invented on:} & %s "
                                % req.get_value("Invented on")
                                .strftime("%Y-%m-%d"))
            elif rattr == "Invented by":
                self.__fd.write(u"\\textbf{Invented by:} & %s "
                                % req.get_value("Invented by"))
            elif rattr == "Status":
                self.__fd.write(u"\\textbf{Status:} & %s " % status)
            elif rattr == "Class":
                self.__fd.write(u"\\textbf{Class:} & %s " % clstr)
            elif rattr == "Type":
                self.__fd.write(u"\\textbf{Type:} & %s " % rtype)
            else:
                # This only happens when a wrong configuration is supllied.
                raise RMTException(85, "Wrong latex2 output configuration "
                                   "supplied: unknown tag [%s]" % rattr)
            i += 1
            if i == 3:
                i = 0
                self.__fd.write(u"\\\\ \n")
            else:
                self.__fd.write(u" & ")
        while i < 2:
            self.__fd.write(u"& & ")
            i += 1

        self.__fd.write(u"\\end{tabular}\\end{center} }\n\n")

    def cmad_topic_continuum_pre(self, _):
        '''Write out the one and only dependency to all the requirements.'''
        tracer.debug("Called.")
        CreateMakeDependencies.write_reqs_dep(self._cmad_file,
                                              self._output_filename)
        self._cmad_file.write(u"REQS_LATEX2=%s\n" % self._output_filename)
