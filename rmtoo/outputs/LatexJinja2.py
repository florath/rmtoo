'''
 rmtoo
   Free and Open Source Requirements Management Tool

 LaTeX output with jinja templating engine.

 (c) 2017,2025 Kristoffer Nordstrom / Andreas Florath

 For licensing details see COPYING
'''

import io
import jinja2

from rmtoo.lib.Constraints import Constraints
from rmtoo.lib.TestCases import collect
from rmtoo.lib.StdOutputParams import StdOutputParams
from rmtoo.lib.ExecutorTopicContinuum import ExecutorTopicContinuum
from rmtoo.lib.logging import tracer
from rmtoo.lib.CreateMakeDependencies import CreateMakeDependencies
from rmtoo.outputs.latex_base import LatexOutputBase


class LatexJinja2(StdOutputParams, ExecutorTopicContinuum,
                  CreateMakeDependencies, LatexOutputBase):
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
        LatexOutputBase.__init__(self)
        self.__ce3set = None
        self.__fd = None
        self.__testcases = None

        # Jinja2 initialisation
        template_loader = jinja2.FileSystemLoader(
                searchpath=oconfig['template_path'])
        template_env_unmodded = jinja2.Environment(
            loader=template_loader,
            autoescape=False)
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

    def topic_set_pre(self, _topics_set):
        '''Prepare the output file.'''
        self.__fd = io.open(self._output_filename, "w", encoding="utf-8")

    def topic_set_post(self, topic_set):
        '''Print out the constraints and clean up file.'''
        tracer.debug("Called; output constraints.")
        assert topic_set is not None
        constraints = Constraints.collect(topic_set)
        self._output_latex_constraints(self.__fd, constraints)
        testcases = collect(topic_set)
        self._output_latex_testcases(self.__fd, testcases,
                                     include_hypertarget=True)
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

    def requirement(self, req):
        self.__fd.write(self._get_requirement(req))

    def _get_requirement(self, req):
        '''Write out one requirement.'''
        req_template = self._template_env.get_template("singleReq.tex")
        template_vars = (
            {'req_id': self._strescape(req.get_id()),
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
            inc = [self._strescape(testcase)
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
