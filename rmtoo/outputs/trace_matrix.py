'''rmtoo
   Free and Open Source Requirements Management Tool

 Print the traceability matrix for all requirements

 (c) 2018 Kristoffer Nordstroem

 For licensing details see COPYING
'''
from __future__ import unicode_literals

import io
import jinja2

from rmtoo.lib.StdOutputParams import StdOutputParams
from rmtoo.lib.ExecutorTopicContinuum import ExecutorTopicContinuum
from rmtoo.lib.logging import tracer
from rmtoo.lib.CreateMakeDependencies import CreateMakeDependencies


class TraceMatrix(StdOutputParams, ExecutorTopicContinuum,
                  CreateMakeDependencies):
    default_config = {"req_attributes":
                      ["Id", "Priority", "Owner", "Invented on",
                       "Invented by", "Status", "Class"]}

    def __init__(self, oconfig):
        '''Create a graph output object.'''
        tracer.info("Called.")
        StdOutputParams.__init__(self, oconfig)
        CreateMakeDependencies.__init__(self)
        self.__ce3set = None
        self.__fd = None
        self.__constraints_reqs_ref = {}
        self.__testcases = None
        self.__level = -1

        self._ifiles = oconfig['input_files']
        self._num_files = len(self._ifiles)
        self._print_static = True

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

        req_template = self._template_env.get_template("trmat_topicName.tex")
        template_vars = {}
        self.__fd.write(u"%% Traceability Matrix\n\n")
        self.__fd.write(req_template.render(template_vars))

        req_template = self._template_env.get_template("trmat_tblStart.tex")
        template_vars = {'printstatic': self._print_static,
                         'numfiles': self._num_files,
                         'ifiles': self._ifiles}
        self.__fd.write(req_template.render(template_vars))

    def topic_set_post(self, topic_set):
        '''Print out the end and clean up file.'''
        req_template = self._template_env.get_template("trmat_tblEnd.tex")
        template_vars = {}
        self.__fd.write(req_template.render(template_vars))

        tracer.debug("Called; output constraints.")
        self.__fd.close()
        assert(topic_set is not None)
        tracer.debug("Clean up file.")
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
        self.__fd.write(u"%% %s\n" % name)

    def topic_text(self, text):
        '''Write out the given text.'''
        pass

    def requirement_set_pre(self, rset):
        '''Prepare the requirements set output.'''
        self.__ce3set = rset.get_ce3set()
        self.__testcases = rset.get_testcases()

    def requirement_set_sort(self, list_to_sort):
        '''Sort by id.'''
        return sorted(list_to_sort, key=lambda r: r.get_id())

    def requirement(self, req):
        '''Write out one requirement.'''
        # Get status information from requirement
        file_status = []
        for fname in self._ifiles:
            try:
                i = (req.get_status().verification_status.
                     get_file_status_string_short(fname))
            except (KeyError, AttributeError):
                file_status.append("")
            else:
                file_status.append(i)

        req_template = self._template_env.get_template("trmat_tblReq.tex")
        template_vars = (
            {
                'printstatic': self._print_static,
                'numfiles': self._num_files,
                'req_id': self.__strescape(req.get_id()),
                'name': req.get_value("Name").get_content(),
                'description': req.get_value("Description").get_content(),
                'req_status':
                req.get_status().get_output_string_short(),
                'file_statuses': file_status,
                'hash': req.get_hash()
            }
        )
        self.__fd.write(req_template.render(template_vars))

        ''' Create a grep'able output for every requirement '''
        try:
            rid_status_failed = (req.get_status().verification_status.
                                 get_status_failed())
        except AttributeError:
            ''' Not a failure if status doesn't support this method '''
            rid_status_failed = False
        if rid_status_failed:
            self.__fd.write("%%% TRACEMAT_RID_FAILED : " +
                            self.__strescape(req.get_id()) + "\n")
        else:
            self.__fd.write("%%% TRACEMAT_RID_FINE : " +
                            self.__strescape(req.get_id()) + "\n")

    def cmad_topic_continuum_pre(self, _):
        '''Write out the one and only dependency to all the requirements.'''
        tracer.debug("Called.")
        CreateMakeDependencies.write_reqs_dep(self._cmad_file,
                                              self._output_filename)
        self._cmad_file.write(u"REQS_LATEX2=%s\n" % self._output_filename)
