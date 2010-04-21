#
# prios output class
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

import operator

class prios:

    def __init__(self, param):
        self.output_filename = param[0]

    # Create MAkefile Dependencies
    def cmad(self, reqscont, ofile):
        ofile.write("%s: ${REQS}\n\t${CALL_RMTOO}\n" % (self.output_filename))

    def output(self, reqscont):
        # Currently just pass this to the RequirementSet
        self.output_reqset(reqscont.base_requirement_set)

    def output_reqset(self, reqset):
        # This is mostly done at this level - because they must be
        # sorted.
        prios_impl = []
        prios_detail = []
        for r in reqset.reqs:
            # Only open requirmentes are interesting
            if reqset.reqs[r].is_open():
                if reqset.reqs[r].is_implementable():
                    prios_impl.append([reqset.reqs[r].get_prio(),
                                       reqset.reqs[r].id])
                else:
                    prios_detail.append([reqset.reqs[r].get_prio(),
                                         reqset.reqs[r].id])

        # Sort them after prio
        sprios_impl = sorted(prios_impl, key=operator.itemgetter(0),
                             reverse=True)
        sprios_detail = sorted(prios_detail, key=operator.itemgetter(0),
                               reverse=True)

        # Write everything to a file.
        f = file(self.output_filename, "w")

        # Local function which outputs one set of requirments.
        def output_prio_table(name, l):
            f.write("\subsection{%s}\n" % name)
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
