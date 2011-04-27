#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
#  prios output class
#
# (c) 2010-2011 by flonatel
#
# For licencing details see COPYING
#

###
### ToDo:
###  Store the whole requirements instead of some other date in
###  the different lists.
###

import datetime
import operator
import time
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.RequirementStatus import RequirementStatusNotDone, \
    RequirementStatusAssigned, RequirementStatusFinished
from rmtoo.lib.DateUtils import parse_date, format_date

class prios:

    def __init__(self, param):
        self.topic_name = param[0]
        self.output_filename = param[1]
        if len(param)>2:
            self.start_date = parse_date("prios config", param[2])
        else:
            self.start_date = time.localtime()

    def set_topics(self, topics):
        self.topic_set = topics.get(self.topic_name)

    # Create MAkefile Dependencies
    def cmad(self, reqscont, ofile):
        ofile.write("%s: ${REQS}\n\t${CALL_RMTOO}\n" % (self.output_filename))

    def output(self, reqscont):
        # Currently just pass this to the RequirementSet
        self.output_reqset(reqscont.continuum_latest())

    def get_reqs_impl_detail(self):
        # This is mostly done at this level - because they must be
        # sorted.
        prios_impl = []
        prios_detail = []
        prios_assigned = []
        prios_finished = []

        for tr in self.topic_set.reqset.nodes:
            try:
                status = tr.get_status() 
                if isinstance(status, RequirementStatusNotDone):
                    if tr.is_implementable():
                        prios_impl.append([tr.get_prio(), tr.id])
                    else:
                        prios_detail.append([tr.get_prio(), tr.id])
                elif isinstance(status, RequirementStatusAssigned):
                    prios_assigned.append(tr)
                elif isinstance(status, RequirementStatusFinished):
                    prios_finished.append(tr)
            except KeyError, ke:
                raise RMTException(35, "%s: KeyError: %s" % (tr.id, ke))

        return prios_impl, prios_detail, prios_assigned, prios_finished

    def output_reqset(self, reqset):
        prios_impl, prios_detail, prios_assigned, prios_finished  \
            = self.get_reqs_impl_detail()

        # Sort them after prio
        sprios_impl = sorted(prios_impl, key=operator.itemgetter(0, 1),
                             reverse=True)
        sprios_detail = sorted(prios_detail, key=operator.itemgetter(0, 1),
                               reverse=True)
        sprios_assigned = sorted(
            prios_assigned, key=lambda x: x.get_value("Status").get_date_str(),
            reverse=False)
        sprios_finished = sorted(
            prios_finished, key=lambda x: x.get_value("Status").get_date_str(),
            reverse=False)

        # Write everything to a file.
        f = file(self.output_filename, "w")

        def get_efe(tr):
            if tr.get_value("Effort estimation")!=None:
                return str(tr.get_value("Effort estimation"))
            else:
                return " "

        # Local function which outputs one set of requirments.
        def output_prio_table(name, l):
            # XXX This must be configurable
            f.write("\section{%s}\n" % name)
            f.write("\\begin{longtable}{|r|c|p{7cm}||r|r|} \hline\n")
            f.write("\\textbf{Prio} & \\textbf{Chap} & "
                    "\\textbf{Requirement Id} & \\textbf{EfE} & "
                    "\\textbf{Sum} \\\ \hline\endhead\n")
            s=0
            for p in l:
                if reqset.reqs[p[1]].get_value("Effort estimation")!=None:
                    efest=reqset.reqs[p[1]].get_value("Effort estimation")
                    s+=efest
                    efest_str=str(efest)
                else:
                    efest_str=" "

                f.write("%4.2f & \\ref{%s} & \\nameref{%s} & %s & %s "
                        "\\\ \hline\n"
                        % (p[0]*10, p[1], p[1], efest_str, s))
            f.write("\end{longtable}")

        def output_assigned_table(name, l):
            f.write("\section{%s}\n" % name)
            f.write("\\begin{longtable}{|r|c|p{6.5cm}||r|l|l|} \hline\n")
            f.write("\\textbf{Prio} & \\textbf{Chap} & "
                    "\\textbf{Requirement Id} & \\textbf{EfE} & "
                    "\\textbf{Person} & \\textbf{Date} \\\ \hline\endhead\n")
            for tr in l:
                status = tr.get_status()
                f.write("%4.2f & \\ref{%s} & \\nameref{%s} & %s & %s & %s "
                        "\\\ \hline\n"
                        % (tr.get_prio()*10, tr.get_id(), tr.get_id(),
                           get_efe(tr), status.get_person(),
                           status.get_date_str()))
            f.write("\end{longtable}")

        def output_finished_table(name, l):
            f.write("\section{%s}\n" % name)
            f.write("{\small ")
            f.write("\\begin{longtable}{|c|p{5.5cm}||r|l|l|r|r|} \hline\n")
            f.write("\\textbf{Chap} & "
                    "\\textbf{Requirement Id} & \\textbf{EfE} & "
                    "\\textbf{Person} & \\textbf{Date} & "
                    "\\textbf{Time} & \\textbf{Rel} "
                    "\\\ \hline\endhead\n")
            for tr in l:
                status = tr.get_status()
                rel = "\\ "
                dur = status.get_duration()
                if dur==None:
                    durs = "\\ "
                else:
                    durs = str(dur)
                if tr.get_value("Effort estimation")!=None:
                    efe = tr.get_value("Effort estimation")
                    if dur!=None:
                        rel = "%4.2f" % (efe / float(dur))
                person = status.get_person()
                if person==None:
                    person = "\\ "
                
                f.write("\\ref{%s} & \\nameref{%s} & %s & %s & %s & "
                        "%s & %s \\\ \hline\n"
                        % (tr.get_id(), tr.get_id(),
                           get_efe(tr), person,
                           status.get_date_str(), durs, rel))
            f.write("\end{longtable}")
            f.write("}")

        def output_statistics(name, simpl, sdetail, sassigned, sfinished):
            f.write("\section{%s}\n" % name)
            f.write("\\begin{longtable}{rrl}\n")
            f.write("Start date & %s & \\\ \n" % format_date(self.start_date))
            
            # Compute the opens
            sum_open=0
            for p in simpl:
                sum_open += reqset.reqs[p[1]].get_efe_or_0()
            f.write("Not done & %d & EfE units \\\ \n" % sum_open)

            # Compute the assigned
            sum_assigned=0
            for tr in sassigned:
                sum_assigned += tr.get_efe_or_0()
            f.write("Assigned & %d & EfE units \\\ \n" % sum_assigned)

            # Compute the finished
            sum_finished=0
            for tr in sfinished:
                sum_finished += tr.get_efe_or_0()
            f.write("Finished & %d & EfE units \\\ \n" % sum_finished)

            # Compute the finished where a time is given
            sum_finished_with_duration=0
            for tr in sfinished:
                if tr.get_status().get_duration()!=None:
                    sum_finished_with_duration += tr.get_efe_or_0()
            f.write("Finished (duration given) & %d & EfE units \\\ \n" % 
                    sum_finished_with_duration)

            # Compute the finished where a time is given
            sum_duration=0
            for tr in sfinished:
                dur = tr.get_status().get_duration()
                if dur!=None:
                    sum_duration += dur
            f.write(" & %d & hours \\\ \n" % sum_duration)

            # The Relation and the Estimated End Date can only be computed
            # When the duration is not 0.
            if sum_duration!=0:
                # Relation
                rel = sum_finished_with_duration / float(sum_duration)
                f.write("Relation & %4.2f & EfE units / hour \\\ \n" % rel)
            
                hours_to_do = sum_open / rel
                f.write("Estimated Not done & %4.2f & hours \\\ \n" 
                        % (hours_to_do))

                # Estimated End Date
                dt = datetime.date(self.start_date.tm_year,
                                   self.start_date.tm_mon,
                                   self.start_date.tm_mday)
                dtdiff = datetime.timedelta(
                    days = hours_to_do / (8  * 5 / 7) + 1)
                f.write("Estimated End date & %s & \\\ \n" %
                        (dt + dtdiff))

            f.write("\end{longtable}")

        # Really output the priority tables.
        output_prio_table("Backlog", sprios_impl)
        output_prio_table("Requirements Elaboration List", sprios_detail)
        output_assigned_table("Assigned", sprios_assigned)
        output_finished_table("Finished", sprios_finished)
        output_statistics("Statistics", sprios_impl, sprios_detail, 
                          sprios_assigned, sprios_finished) 


        f.close()
