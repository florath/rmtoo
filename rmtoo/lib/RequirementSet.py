#
# Requirement Management Toolset
#
#   RequirementSet
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

import os
import re
import sys
import operator

from Requirement import Requirement

# This class handles a whole set of requirments.
# These set must be enclosed, i.e. all references must be resolvable.

class RequirementSet:

    def __init__(self, directory, mods, opts, config):
        self.reqs = {}
        self.mods = mods
        self.opts = opts
        self.config = config
        self.read(directory)

        # Dependencies can be done, if all requirements are successfully
        # read in.
        self.handle_modules_reqdeps()

        # The must no be left
        if not self.check_left_tags():
            print("+++ ERROR there were errors encountered during parsing "
                  "and checking - can't continue")
            sys.exit(1)

    def read(self, directory):
        files = os.listdir(directory)
        for f in files:
            m = re.match("^.*\.req$", f)
            if m==None:
                continue
            rid = f[:-4]
            fd = file(os.path.join(directory, f))
            req = Requirement(fd, rid, self.mods, self.opts, self.config)
            self.reqs[req.id] = req

    def handle_modules_reqdeps(self):
        for module in self.mods.reqdeps:
            self.mods.reqdeps[module].rewrite(self)

    def check_left_tags(self):
        alls_fine = True
        for r in self.reqs:
            rr = self.reqs[r]
            if len(rr.req)>0:
                print("+++ ERROR %s: req not empty. Missing tag handers "
                      "for '%s'" % (rr.id, rr.req)) 
                alls_fine = False
        return alls_fine

    # This is a major heuristic
    # ToDo: have a very, very close look, because it might work (or
    # not) 
    def output_latex_check_master(self, directory):
        f = file(os.path.join(directory, "requirements.tex"), "r")

        included = set()
        for line in f:
            if len(line)>0 and line[-1]=='\n':
                line = line[:-1]
            m=re.match("^\\\input\{reqs/(.*)\.tex\}$", line)
            if m!=None:
                included.add(m.group(1))

        ks = set(self.reqs.keys())

        not_included = ks - included
        must_included = included - ks

        too_much_or_less = False
        if len(not_included)>0:
            print("+++ ERROR: missing reqs in document: '%s'" 
                  % not_included)
            too_much_or_less = True

        if len(must_included)>0:
            print("+++ ERROR: additional reqs in document: '%s'" 
                  % must_included)
            too_much_or_less = True

        return not too_much_or_less
                
    def output_latex(self, directory):
        if not self.output_latex_check_master(directory):
            print("+++ ERROR: please fix errors first")
            return
        reqs_dir = os.path.join(directory, "reqs")
        try:
            os.makedirs(reqs_dir)
        except OSError:
            # This is not a problem: the directory already exists.
            pass
        # Call all requirments to write their files.
        for r in self.reqs:
            self.reqs[r].output_latex(reqs_dir)

    def output_dot(self, dot_output_file):
        # Initialize the graph output
        g = file(dot_output_file, "w")
        g.write("digraph reqdeps {\nrankdir=BT;\nmclimit=10.0;\n"
                "nslimit=10.0;ranksep=1;\n")
        for r in self.reqs:
            self.reqs[r].output_dot(g)
        g.write("}")
        g.close()

    def output_prios(self, prio_output_file):
        # This is mostly done at this level - because they must be
        # sorted.
        prios_impl = []
        prios_detail = []
        for r in self.reqs:
            # Only open requirmentes are interesting
            if self.reqs[r].is_open():
                if self.reqs[r].is_implementable():
                    prios_impl.append([self.reqs[r].get_prio(),
                                       self.reqs[r].id])
                else:
                    prios_detail.append([self.reqs[r].get_prio(),
                                         self.reqs[r].id])

        # Sort them after prio
        sprios_impl = sorted(prios_impl, key=operator.itemgetter(0),
                             reverse=True)
        sprios_detail = sorted(prios_detail, key=operator.itemgetter(0),
                               reverse=True)

        # Write everything to a file.
        f = file(prio_output_file, "w")

        # Backlog
        f.write("\subsection{Backlog}\n")
        f.write("\\begin{longtable}{|r|p{7cm}|} \hline\endhead\n")
        f.write("\\textbf{Priority} & \\textbf{Requirement Id}\\\ \hline\n")
        for p in sprios_impl:
            f.write("%4.0f & \\ref{%s} \\nameref{%s} \\\ \hline\n"
                    % (p[0], p[1], p[1]))
        f.write("\hline\n")
        f.write("\end{longtable}")

        # Requirments Elaboration
        f.write("\subsection{Requirments Elaboration}\n")
        f.write("\\begin{longtable}{|r|p{7cm}|} \hline\endhead \n")
        f.write("\\textbf{Priority} & \\textbf{Requirement Id}\\\\ \hline\n")
        for p in sprios_detail:
            f.write("%4.0f & \\ref{%s} \\nameref{%s} \\\\\n"
                    % (p[0], p[1], p[1]))
        f.write("\hline\n")
        f.write("\end{longtable}")


        f.close()

        
