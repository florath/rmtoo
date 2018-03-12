'''rmtoo
   Free and Open Source Requirements Management Tool

 Print the traceability matrix for all requirements

 (c) 2018 Kristoffer Nordstroem

 For licensing details see COPYING
'''
from __future__ import unicode_literals

import io
from six import iteritems

from rmtoo.lib.Constraints import Constraints
from rmtoo.lib.TestCases import collect
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.StdOutputParams import StdOutputParams
from rmtoo.lib.ExecutorTopicContinuum import ExecutorTopicContinuum
from rmtoo.lib.logging import tracer
from rmtoo.lib.CreateMakeDependencies import CreateMakeDependencies


class TraceMatrix(StdOutputParams, ExecutorTopicContinuum, CreateMakeDependencies):
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


    def topic_set_post(self, topic_set):
        '''Print out the constraints and clean up file.'''
        tracer.debug("Called; output constraints.")
        if topic_set is None:
            assert False
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
        self.__fd.write(u"%s\n" % name)

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

        self.__fd.write(u"\n\\par\n{\small \\begin{center}"
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
            else:
                pass
                # This only happens when a wrong configuration is supllied.
                # raise RMTException(85, "Wrong latex2 output configuration "
                #                    "supplied: unknown tag [%s]" % rattr)


    def cmad_topic_continuum_pre(self, _):
        '''Write out the one and only dependency to all the requirements.'''
        tracer.debug("Called.")
        CreateMakeDependencies.write_reqs_dep(self._cmad_file,
                                              self._output_filename)
        self._cmad_file.write(u"REQS_LATEX2=%s\n" % self._output_filename)
