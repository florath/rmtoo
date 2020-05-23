'''
 rmtoo
   Free and Open Source Requirements Management Tool

 LaTeX output with jinja templating engine.

 (c) 2017 Kristoffer Nordstrom

 For licensing details see COPYING
'''
from __future__ import unicode_literals

import io
import jinja2
from six import iteritems

from rmtoo.lib.Constraints import Constraints
from rmtoo.lib.TestCases import collect
from rmtoo.lib.StdOutputParams import StdOutputParams
from rmtoo.lib.ExecutorTopicContinuum import ExecutorTopicContinuum
from rmtoo.lib.logging import tracer
from rmtoo.lib.CreateMakeDependencies import CreateMakeDependencies


class LatexJinja2(StdOutputParams, ExecutorTopicContinuum,
                  CreateMakeDependencies):
    default_config = {"req_attributes":
                      ["Id", "Priority", "Owner", "Invented on",
                       "Invented by", "Status", "Class"]}

    level_names = [
        "chapter",
        "section",
        "subsection",
        "subsubsection",
        "subsubsubsection",
    ]

    def __init__(self, oconfig):
        '''Create a graph output object.'''
        tracer.info("Called.")
        StdOutputParams.__init__(self, oconfig)
        CreateMakeDependencies.__init__(self)
        self.__ce3set = None
        self.__fd = None
        self.__constraints_reqs_ref = {}
        self.__testcases = None

        # Jinja2 initialisation
        template_loader = jinja2.FileSystemLoader(
                searchpath=oconfig['template_path'])
        template_env_unmodded = jinja2.Environment(loader=template_loader)
        self._template_env = template_env_unmodded.overlay(
            block_start_string='((*',
            block_end_string='*))',
            variable_start_string='(((',
            variable_end_string=')))',
            comment_start_string='((=',
            comment_end_string='=))')

        if not self._config.is_available('req_attributes'):
            self._config.set_value(
                'req_attributes',
                ["Id", "Priority", "Owner", "Invented on",
                 "Invented by", "Status", "Class"])
        self.__level = -1

    @staticmethod
    def __strescape(string):
        '''Escapes a string: hexifies it.'''
        result = ""
        for fchar in string:
            if ord(fchar) >= 32 and ord(fchar) < 127:
                result += fchar
            else:
                result += "%02x" % ord(fchar)
        return result

    def topic_set_pre(self, _topics_set):
        '''Prepare the output file.'''
        self.__fd = io.open(self._output_filename, "w", encoding="utf-8")

    def __output_latex_one_constraint(self, cname, cnstrt):
        '''Output one constraint.'''
        cname = LatexJinja2.__strescape(cname)
        tracer.debug("Output constraint [%s]." % cname)
        self.__fd.write(u"%% CONSTRAINT '%s'\n" % cname)

        self.__fd.write(u"\\%s{%s}\\label{CONSTRAINT%s}\n"
                        "\\textbf{Description:} %s\n"
                        % (self.level_names[1],
                           cnstrt.get_value("Name").get_content(),
                           cname, cnstrt.get_value(
                               "Description").get_content()))

        if cnstrt.is_val_av_and_not_null("Rationale"):
            self.__fd.write(u"\n\\textbf{Rationale:} %s\n"
                            % cnstrt.get_value("Rationale").get_content())

        if cnstrt.is_val_av_and_not_null("Note"):
            self.__fd.write(u"\n\\textbf{Note:} %s\n"
                            % cnstrt.get_value("Note").get_content())

        # Write out the references to the requirements

        reqs_refs = []
        for req in self.__constraints_reqs_ref[cname]:
            refid = LatexJinja2.__strescape(req)
            refctr = "\\ref{%s} \\nameref{%s}" \
                     % (refid, refid)
            reqs_refs.append(refctr)
        self.__fd.write(u"\n\\textbf{Requirements:} %s\n" %
                        ", ".join(reqs_refs))

        tracer.debug("Finished.")

    def __output_latex_constraints(self, constraints):
        '''Write out all constraints for the topic set.'''
        if len(constraints) == 0:
            tracer.debug("No constraints to output.")
            return

        self.__fd.write(u"\\%s{Constraints}\n" % self.level_names[0])
        for cname, cnstrt in sorted(iteritems(constraints)):
            self.__output_latex_one_constraint(cname, cnstrt)

    # TODO: Code duplication from constraints
    def __output_latex_one_testcase(self, cname, cnstrt):
        '''Output one testcase.'''
        cname = LatexJinja2.__strescape(cname)
        tracer.debug("Output testcase [%s]." % cname)
        self.__fd.write(u"%% TEST-CASE '%s'\n" % cname)

        self.__fd.write(u"\\%s{%s}\\label{TESTCASE%s}\n"
                        "\\hypertarget{TESTCASE%s}{}"
                        "\\textbf{Description:} %s\n"
                        % (self.level_names[1],
                           cnstrt.get_value("Name").get_content(),
                           cnstrt.get_value("Name").get_content(),
                           cname, cnstrt.get_value(
                               "Description").get_content()))

        if cnstrt.is_val_av_and_not_null("Expected Result"):
            self.__fd.write(u"\n\\textbf{Expected Result:} %s\n"
                            % cnstrt.get_value(
                                "Expected Result").get_content())

        if cnstrt.is_val_av_and_not_null("Rationale"):
            self.__fd.write(u"\n\\textbf{Rationale:} %s\n"
                            % cnstrt.get_value("Rationale").get_content())

        if cnstrt.is_val_av_and_not_null("Note"):
            self.__fd.write(u"\n\\textbf{Note:} %s\n"
                            % cnstrt.get_value("Note").get_content())
        tracer.debug("Finished.")

    def __output_latex_testcases(self, testcases):
        '''Write out all testcases for the topic set.'''
        if not len(testcases):
            tracer.debug("No testcases to output.")
            return

        self.__fd.write(u"\\%s{Test Cases}\n" % self.level_names[0])
        for cname, cnstrt in sorted(iteritems(testcases)):
            self.__output_latex_one_testcase(cname, cnstrt)

    def topic_set_post(self, topic_set):
        '''Print out the constraints and clean up file.'''
        tracer.debug("Called; output constraints.")
        assert topic_set is not None
        constraints = Constraints.collect(topic_set)
        self.__output_latex_constraints(constraints)
        testcases = collect(topic_set)
        self.__output_latex_testcases(testcases)
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
        req_template = self._template_env.get_template("topicName.tex")
        template_vars = {'level': self.__level, 'name': name}
        self.__fd.write(req_template.render(template_vars))

    def topic_text(self, text):
        '''Write out the given text.'''
        req_template = self._template_env.get_template("topicText.tex")
        template_vars = {'text': text}
        self.__fd.write(req_template.render(template_vars))

    def requirement_set_pre(self, rset):
        '''Prepare the requirements set output.'''
        self.__ce3set = rset.get_ce3set()
        self.__testcases = rset.get_testcases()

    def requirement_set_sort(self, list_to_sort):
        '''Sort by id.'''
        return sorted(list_to_sort, key=lambda r: r.get_id())

    def __add_constraint_req_ref(self, constraint, requirement):
        if constraint not in self.__constraints_reqs_ref:
            self.__constraints_reqs_ref[constraint] = []
        self.__constraints_reqs_ref[constraint].append(requirement)

    def requirement(self, req):
        self.__fd.write(self._get_requirement(req))

    def _get_requirement(self, req):
        '''Write out one requirement.'''
        req_template = self._template_env.get_template("singleReq.tex")
        template_vars = (
            {'req_id': self.__strescape(req.get_id()),
             'name':  req.get_value("Name").get_content(),
             'description':  req.get_value("Description").get_content(),
             'req_status': req.get_value("Status").get_output_string()}
        )

        if req.is_val_av_and_not_null("Rationale"):
            template_vars['rationale'] = (
                req.get_value("Rationale").get_content()
            )
        if req.is_val_av_and_not_null("Note"):
            template_vars['note'] = (
                req.get_value("Note").get_content()
            )

        if len(req.outgoing) > 0:
            # Create links to the corresponding dependency nodes.
            inc = [d.get_id() for d in
                   sorted(req.outgoing, key=lambda r: r.get_id())]
            template_vars['solvedby'] = inc

        if len(req.incoming) > 0:
            # Only output the depends on when there are fields for output.
            inc = [d.get_id() for d in
                   sorted(req.incoming, key=lambda r: r.get_id())]
            template_vars['dependson'] = inc

        try:
            template_vars['status'] = (
                    req.get_value("Status").get_output_string())
        except KeyError:
            pass
        try:
            template_vars['clstr'] = (
                    req.get_value("Class").get_output_string())
        except KeyError:
            pass
        try:
            template_vars['rtype'] = req.get_value("Type").as_string()
        except KeyError:
            pass
        try:
            template_vars['prio'] = req.get_value("Priority") * 10
        except KeyError:
            pass
        try:
            template_vars['owner'] = req.get_value("Owner")
        except KeyError:
            pass
        try:
            template_vars['inventedon'] = (
                    req.get_value("Invented on").strftime("%Y-%m-%d"))
        except KeyError:
            pass
        try:
            template_vars['inventedby'] = req.get_value("Invented by")
        except KeyError:
            pass

        # The following has not been ported yet (TODO)
        if self.__ce3set is not None:
            cnstrt = self.__ce3set.get(req.get_id())
            if cnstrt is not None and len(cnstrt) > 0:
                raise NotImplementedError(
                        'Not yet defined, use latex2 output instead!')
                self.__fd.write(u"\n\\textbf{Constraints:} ")
                cstrs = []
                for key, val in sorted(iteritems(cnstrt)):
                    refid = LatexJinja2.__strescape(key)
                    refctr = "\\ref{CONSTRAINT%s} \\nameref{CONSTRAINT%s}" \
                             % (refid, refid)
                    description = val.description()
                    if description is not None:
                        refctr += " [" + description + "] "
                    cstrs.append(refctr)
                    # Also put a reference (for later use) in the
                    # constraints to requirements ref.
                    self.__add_constraint_req_ref(refid, req.get_id())

                self.__fd.write(u", ".join(cstrs))
                self.__fd.write(u"\n")

        testcases = req.get_value_default("Test Cases")
        if testcases is not None:
            inc = [LatexJinja2.__strescape(testcase)
                   for testcase in testcases]
            template_vars['testcases'] = inc

        return req_template.render(template_vars)

    def cmad_topic_continuum_pre(self, _):
        '''Write out the one and only dependency to all the requirements.'''
        tracer.debug("Called.")
        CreateMakeDependencies.write_reqs_dep(self._cmad_file,
                                              self._output_filename)
        self._cmad_file.write(u"REQS_LATEX2=%s\n" %
                              self._output_filename)
