#
# prios output class
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

import operator
from rmtoo.lib.RMTException import RMTException

class prios:

    def __init__(self, param):
        self.topic_name = param[0]
        self.output_filename = param[1]

    def set_topics(self, topics):
        self.topic_set = topics.get(self.topic_name)

    # Create MAkefile Dependencies
    def cmad(self, reqscont, ofile):
        ofile.write("%s: ${REQS}\n\t${CALL_RMTOO}\n" % (self.output_filename))

    def output(self, reqscont):
        # Currently just pass this to the RequirementSet
        self.output_reqset(reqscont.continnum_latest())

    def get_reqs_impl_detail(self):
        # This is mostly done at this level - because they must be
        # sorted.
        prios_impl = []
        prios_detail = []

        for tr in self.topic_set.reqset.nodes:
            try:
                # Only open requirementes are interesting
                if tr.is_open():
                    if tr.is_implementable():
                        prios_impl.append([tr.get_prio(), tr.id])
                    else:
                        prios_detail.append([tr.get_prio(), tr.id])
            except KeyError, ke:
                raise RMTException(35, "%s: KeyError: %s" % (tr.id, ke))

        return prios_impl, prios_detail

    def output_reqset(self, reqset):
        prios_impl, prios_detail = self.get_reqs_impl_detail()

        # Sort them after prio
        sprios_impl = sorted(prios_impl, key=operator.itemgetter(0, 1),
                             reverse=True)
        sprios_detail = sorted(prios_detail, key=operator.itemgetter(0, 1),
                               reverse=True)

        # Write everything to a file.
        f = file(self.output_filename, "w")

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
                if reqset.reqs[p[1]].tags["Effort estimation"]!=None:
                    efest=reqset.reqs[p[1]].tags["Effort estimation"]
                    s+=efest
                    efest_str=str(efest)
                else:
                    efest_str=" "

                f.write("%4.2f & \\ref{%s} & \\nameref{%s} & %s & %s "
                        "\\\ \hline\n"
                        % (p[0]*10, p[1], p[1], efest_str, s))
            f.write("\end{longtable}")

        # Really output the priority tables.
        output_prio_table("Backlog", sprios_impl)
        output_prio_table("Requirements Elaboration List", sprios_detail)

        f.close()
