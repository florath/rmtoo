'''
 rmtoo
   Free and Open Source Requirements Management Tool

 Output handler prios.

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
#
# TODO:
#  Store the whole requirements instead of some other date in
#  the different lists.
#

from rmtoo.lib.logging import tracer
from rmtoo.lib.ExecutorTopicContinuum import ExecutorTopicContinuum

import datetime
import operator
from scipy import stats
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.RequirementStatus import RequirementStatusNotDone, \
    RequirementStatusAssigned, RequirementStatusFinished
from rmtoo.lib.ClassType import ClassTypeImplementable, \
    ClassTypeSelected
from rmtoo.lib.DateUtils import format_date
from rmtoo.lib.Statistics import Statistics
from rmtoo.lib.StdOutputParams import StdOutputParams
from rmtoo.lib.CreateMakeDependencies import CreateMakeDependencies


class prios(StdOutputParams, ExecutorTopicContinuum, CreateMakeDependencies):

    def __init__(self, oconfig):
        '''Create a prios output object.'''
        tracer.info("Called.")
        StdOutputParams.__init__(self, oconfig)
        CreateMakeDependencies.__init__(self)

    def topic_continuum_sort(self, vcs_commit_ids, topic_sets):
        '''Because graph2 can only one topic continuum,
           the latest (newest) is used.'''
        self.__used_vcs_id = vcs_commit_ids[-1]
        return [topic_sets[vcs_commit_ids[-1].get_commit()]]

    def __get_reqs_impl_detail(self, topic_set):
        '''Return the implementation details of the requirements.'''
        prios_impl = []
        prios_detail = []
        prios_selected = []
        prios_assigned = []
        prios_finished = []

        req_set = topic_set.get_requirement_set()
        for reqid in req_set.get_all_requirement_ids():
            tr = req_set.get_requirement(reqid)
            try:
                status = tr.get_status()
                if isinstance(status, RequirementStatusNotDone):
                    rclass = tr.values["Class"]
                    if isinstance(rclass, ClassTypeImplementable):
                        prios_impl.append([tr.get_prio(), tr.get_id()])
                    elif isinstance(rclass, ClassTypeSelected):
                        prios_selected.append([tr.get_prio(), tr.get_id()])
                    else:
                        prios_detail.append([tr.get_prio(), tr.get_id()])
                elif isinstance(status, RequirementStatusAssigned):
                    prios_assigned.append(tr)
                elif isinstance(status, RequirementStatusFinished):
                    prios_finished.append(tr)
            except KeyError as ke:
                raise RMTException(35, "%s: KeyError: %s" % (tr.get_id(), ke))

        return prios_impl, prios_detail, prios_selected, \
            prios_assigned, prios_finished

    def topic_set_pre(self, topic_set):
        '''This is call in the TopicSet pre-phase.'''
        prios_impl, prios_detail, prios_selected, \
            prios_assigned, prios_finished = \
            self.__get_reqs_impl_detail(topic_set)

        # Sort them after prio
        sprios_impl = sorted(prios_impl, key=operator.itemgetter(0, 1),
                             reverse=True)
        sprios_detail = sorted(prios_detail, key=operator.itemgetter(0, 1),
                               reverse=True)
        sprios_selected = sorted(prios_selected, key=operator.itemgetter(0, 1),
                                 reverse=True)
        sprios_assigned = sorted(
            prios_assigned, key=lambda x: x.get_value("Status").get_date_str(),
            reverse=False)
        sprios_finished = sorted(
            prios_finished, key=lambda x: x.get_value("Status").get_date_str(),
            reverse=False)

        # Write everything to a file.
        f = open(self._output_filename, "w")

        def get_efe(tr):
            if tr.get_value("Effort estimation") is not None:
                return str(tr.get_value("Effort estimation"))
            else:
                return " "

        # Local function which outputs one set of requirements.
        def output_prio_table(name, reqlist):
            # XXX This must be configurable
            f.write("\\section{%s}\n" % name)
            f.write("\\begin{longtable}{|r|c|p{7cm}||r|r|} \\hline\n")
            f.write("\\textbf{Prio} & \\textbf{Chap} & "
                    "\\textbf{Requirement Id} & \\textbf{EfE} & "
                    "\\textbf{Sum} \\\\ \\hline\\endhead\n")

            s = 0
            for p in reqlist:
                if topic_set.get_requirement_set().get_requirement(
                        p[1]).get_value("Effort estimation") is not None:
                    efest = topic_set.get_requirement_set().\
                            get_requirement(p[1]).\
                            get_value("Effort estimation")
                    s += efest
                    efest_str = str(efest)
                else:
                    efest_str = " "

                f.write("%4.2f & \\ref{%s} & \\nameref{%s} & %s & %s "
                        "\\\\ \\hline\n"
                        % (p[0] * 10, p[1], p[1], efest_str, s))
            f.write("\\end{longtable}")

        def output_assigned_table(name, trr):
            f.write("\\section{%s}\n" % name)
            f.write("\\begin{longtable}{|r|c|p{6.5cm}||r|l|l|} \\hline\n")
            f.write("\\textbf{Prio} & \\textbf{Chap} & "
                    "\\textbf{Requirement Id} & \\textbf{EfE} & "
                    "\\textbf{Person} & \\textbf{Date} \\\\ "
                    "\\hline\\endhead\n")
            for tr in trr:
                status = tr.get_status()
                f.write("%4.2f & \\ref{%s} & \\nameref{%s} & %s & %s & %s "
                        "\\\\ \\hline\n"
                        % (tr.get_prio() * 10, tr.get_id(), tr.get_id(),
                           get_efe(tr), status.get_person(),
                           status.get_date_str()))
            f.write("\\end{longtable}")

        def output_finished_table(name, trr):
            f.write("\\section{%s}\n" % name)
            f.write("{\\small ")
            f.write("\\begin{longtable}{|c|p{5.5cm}||r|l|l|r|r|} \\hline\n")
            f.write("\\textbf{Chap} & "
                    "\\textbf{Requirement Id} & \\textbf{EfE} & "
                    "\\textbf{Person} & \\textbf{Date} & "
                    "\\textbf{Time} & \\textbf{Rel} "
                    "\\\\ \\hline\\endhead\n")
            for tr in trr:
                status = tr.get_status()
                rel = "\\ "
                dur = status.get_duration()
                if dur is None:
                    durs = "\\ "
                else:
                    durs = str(dur)
                if tr.get_value("Effort estimation") is not None:
                    efe = tr.get_value("Effort estimation")
                    if dur is not None and dur != 0.0:
                        rel = "%4.2f" % (efe / float(dur))
                person = status.get_person()
                if person is None:
                    person = "\\ "

                f.write("\\ref{%s} & \\nameref{%s} & %s & %s & %s & "
                        "%s & %s \\\\ \\hline\n"
                        % (tr.get_id(), tr.get_id(),
                           get_efe(tr), person,
                           status.get_date_str(), durs, rel))
            f.write("\\end{longtable}")
            f.write("}")

        def output_statistics(name, simpl, sselected, sdetail,
                              sassigned, sfinished):
            f.write("\\section{%s}\n" % name)
            f.write("\\begin{longtable}{rrl}\n")
            f.write("Start date & %s & \\\\ \n" % format_date(
                self._start_date))

            # Compute the opens
            sum_open = 0
            for sp in [simpl, sselected]:
                for p in sp:
                    sum_open += topic_set.get_requirement_set().\
                                get_requirement(p[1]).\
                                get_efe_or_0()
            f.write("Not done & %d & EfE units \\\\ \n" % sum_open)

            # Compute the assigned
            sum_assigned = 0
            for tr in sassigned:
                sum_assigned += tr.get_efe_or_0()
            f.write("Assigned & %d & EfE units \\\\ \n" % sum_assigned)

            # Compute the finished
            sum_finished = 0
            for tr in sfinished:
                sum_finished += tr.get_efe_or_0()
            f.write("Finished & %d & EfE units \\\\ \n" % sum_finished)

            # Compute the finished where a time is given
            sum_finished_with_duration = 0
            for tr in sfinished:
                if tr.get_status().get_duration() is not None:
                    sum_finished_with_duration += tr.get_efe_or_0()
            f.write("Finished (duration given) & %d & EfE units \\\\ \n" %
                    sum_finished_with_duration)

            # Compute the finished where a time is given
            sum_duration = 0
            for tr in sfinished:
                dur = tr.get_status().get_duration()
                if dur is not None:
                    sum_duration += dur
            f.write(" & %d & hours \\\\ \n" % sum_duration)

            # The Relation and the Estimated End Date can only be computed
            # When the duration is not 0.
            if sum_duration != 0:
                # Relation
                rel = sum_finished_with_duration / float(sum_duration)
                f.write("Relation & %4.2f & EfE units / hour \\\\ \n" % rel)

                hours_to_do = sum_open / rel
                f.write("Estimated Not done & %4.2f & hours \\\\ \n"
                        % (hours_to_do))

                # Estimated End Date

                rv = Statistics.get_units(topic_set.get_requirement_set(),
                                          self._start_date, self._end_date)
                x = list(i for i in range(0, len(rv)))
                y = list(x[0] + x[1] for x in rv)

                gradient, intercept, r_value, p_value, std_err \
                    = stats.linregress(x, y)

                if gradient >= 0.0:
                    f.write("Estimated End date & unpredictable & \\\\ \n")
                else:
                    d = intercept / -gradient
                    end_date = self._start_date + datetime.timedelta(d)
                    f.write("Estimated End date & %s & \\\\ \n" % end_date)

            f.write("\\end{longtable}")

        # Really output the priority tables.
        output_prio_table("Selected for Sprint", sprios_selected)
        output_assigned_table("Assigned", sprios_assigned)
        output_prio_table("Backlog", sprios_impl)
        output_prio_table("Requirements Elaboration List", sprios_detail)
        output_finished_table("Finished", sprios_finished)
        output_statistics("Statistics", sprios_impl, sprios_selected,
                          sprios_detail, sprios_assigned, sprios_finished)
        f.close()

    def cmad_topic_continuum_pre(self, _):
        '''Write out the one and only dependency to all the requirements.'''
        tracer.debug("Called.")
        CreateMakeDependencies.write_reqs_dep(self._cmad_file,
                                              self._output_filename)
