'''
 rmtoo
   Free and Open Source Requirements Management Tool

 Base class for LaTeX output generators with common constraint
 and testcase handling.

 (c) 2025 by flonatel GmbH & Co. KG / Andreas Florath

 For licensing details see COPYING
'''

from rmtoo.lib.logging import tracer


class LatexOutputBase:
    '''Base class for LaTeX output generators with shared constraint
    and testcase formatting.'''

    level_names = [
        "chapter",
        "section",
        "subsection",
        "subsubsection",
        "subsubsubsection",
    ]

    def __init__(self):
        self.__constraints_reqs_ref = {}

    @staticmethod
    def _strescape(string):
        '''Escapes a string: hexifies it.'''
        result = ""
        for fchar in string:
            if ord(fchar) >= 32 and ord(fchar) < 127:
                result += fchar
            else:
                result += "%02x" % ord(fchar)
        return result

    def _add_constraint_req_ref(self, constraint, requirement):
        '''Add a reference from constraint to requirement.'''
        if constraint not in self.__constraints_reqs_ref:
            self.__constraints_reqs_ref[constraint] = []
        self.__constraints_reqs_ref[constraint].append(requirement)

    def _output_latex_one_constraint(self, fd, cname, cnstrt):
        '''Output one constraint.'''
        cname = self._strescape(cname)
        tracer.debug("Output constraint [%s]." % cname)
        fd.write(u"%% CONSTRAINT '%s'\n" % cname)

        fd.write(u"\\%s{%s}\\label{CONSTRAINT%s}\n"
                 "\\textbf{Description:} %s\n"
                 % (self.level_names[1],
                    cnstrt.get_value("Name").get_content(),
                    cname, cnstrt.get_value(
                        "Description").get_content()))

        if cnstrt.is_val_av_and_not_null("Rationale"):
            fd.write(u"\n\\textbf{Rationale:} %s\n"
                     % cnstrt.get_value("Rationale").get_content())

        if cnstrt.is_val_av_and_not_null("Note"):
            fd.write(u"\n\\textbf{Note:} %s\n"
                     % cnstrt.get_value("Note").get_content())

        # Write out the references to the requirements
        reqs_refs = []
        for req in self.__constraints_reqs_ref[cname]:
            refid = self._strescape(req)
            refctr = "\\ref{%s} \\nameref{%s}" \
                     % (refid, refid)
            reqs_refs.append(refctr)
        fd.write(u"\n\\textbf{Requirements:} %s\n" %
                 ", ".join(reqs_refs))

        tracer.debug("Finished.")

    def _output_latex_constraints(self, fd, constraints):
        '''Write out all constraints for the topic set.'''
        if len(constraints) == 0:
            tracer.debug("No constraints to output.")
            return

        fd.write(u"\\%s{Constraints}\n" % self.level_names[0])
        for cname, cnstrt in sorted(constraints.items()):
            self._output_latex_one_constraint(fd, cname, cnstrt)

    def _output_latex_one_testcase(self, fd, cname, cnstrt,
                                   include_hypertarget=False):
        '''Output one testcase.'''
        cname = self._strescape(cname)
        tracer.debug("Output testcase [%s]." % cname)
        fd.write(u"%% TEST-CASE '%s'\n" % cname)

        if include_hypertarget:
            fd.write(u"\\%s{%s}\\label{TESTCASE%s}\n"
                     "\\hypertarget{TESTCASE%s}{}"
                     "\\textbf{Description:} %s\n"
                     % (self.level_names[1],
                        cnstrt.get_value("Name").get_content(),
                        cnstrt.get_value("Name").get_content(),
                        cname, cnstrt.get_value(
                            "Description").get_content()))
        else:
            fd.write(u"\\%s{%s}\\label{TESTCASE%s}\n"
                     "\\textbf{Description:} %s\n"
                     % (self.level_names[1],
                        cnstrt.get_value("Name").get_content(),
                        cname, cnstrt.get_value(
                            "Description").get_content()))

        if cnstrt.is_val_av_and_not_null("Expected Result"):
            fd.write(u"\n\\textbf{Expected Result:} %s\n"
                     % cnstrt.get_value(
                         "Expected Result").get_content())

        if cnstrt.is_val_av_and_not_null("Rationale"):
            fd.write(u"\n\\textbf{Rationale:} %s\n"
                     % cnstrt.get_value("Rationale").get_content())

        if cnstrt.is_val_av_and_not_null("Note"):
            fd.write(u"\n\\textbf{Note:} %s\n"
                     % cnstrt.get_value("Note").get_content())
        tracer.debug("Finished.")

    def _output_latex_testcases(self, fd, testcases,
                                include_hypertarget=False):
        '''Write out all testcases for the topic set.'''
        if len(testcases) == 0:
            tracer.debug("No testcases to output.")
            return

        fd.write(u"\\%s{Test Cases}\n" % self.level_names[0])
        for cname, cnstrt in sorted(testcases.items()):
            self._output_latex_one_testcase(fd, cname, cnstrt,
                                            include_hypertarget)
