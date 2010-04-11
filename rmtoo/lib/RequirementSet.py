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
import StringIO

from Requirement import Requirement
from PyGitCompat import PyGitCompat
from rmtoo.lib.digraph.Digraph import Digraph

# This class handles a whole set of requirments.
# These set must be enclosed, i.e. all references must be resolvable.

class RequirementSet(Digraph):

    er_fine = 0
    er_error = 1

    def __init__(self, mods, opts, config):
        Digraph.__init__(self)

        self.reqs = {}
        self.mods = mods
        self.opts = opts
        self.state = self.er_fine
        self.config = config

    def handle_modules(self):
        # Dependencies can be done, if all requirements are successfully
        # read in.
        self.handle_modules_reqdeps()
        # If there was an error, the state flag is set:
        if self.state != self.er_fine:
            print("+++ ERROR: there was a problem handling the "
                  "requirement set modules")
            return False

        # The must no be left
        if not self.check_left_tags():
            print("+++ ERROR there were errors encountered during parsing "
                  "and checking - can't continue")
            return False

        return True

    def read_from_filesystem(self, directory):
        everythings_fine = self.read(directory)
        if not everythings_fine:
            print("+++ ERROR: There were errors in the requirments")
            return False

        return self.handle_modules()

    def read(self, directory):
        everythings_fine = True
        files = os.listdir(directory)
        for f in files:
            m = re.match("^.*\.req$", f)
            if m==None:
                continue
            rid = f[:-4]
            fd = file(os.path.join(directory, f))
            req = Requirement(fd, rid, self.mods, self.opts, self.config)
            if req.ok():
                # Store in the map, so that it is easy to access the
                # node by id.
                self.reqs[req.id] = req
                # Also store it in the digraph's node list for simple
                # access to the digraph algorithms.
                self.nodes.append(req)
            else:
                print("+++ ERROR %s: could not be parsed" % req.id)
                everythings_fine = False
        return everythings_fine

    def read_from_git_tree(self, tree):
        everythings_fine = True
        files = PyGitCompat.Tree.items(tree)
        for f in files:
            m = re.match("^.*\.req$", PyGitCompat.Tree.iter_name(f))
            if m==None:
                continue
            rid = PyGitCompat.Tree.iter_name(f)[:-4]
            req = Requirement(StringIO.StringIO(PyGitCompat.Tree.iter_data(f)), 
                              rid, self.mods, self.opts, self.config)
            if req.ok():
                # Store in the map, so that it is easy to access the
                # node by id.
                self.reqs[req.id] = req
                # Also store it in the digraph's node list for simple
                # access to the digraph algorithms.
                self.nodes.append(req)
            else:
                print("+++ ERROR %s: could not be parsed" % req.id)
                everythings_fine = False

        if not everythings_fine:
            return False
        return self.handle_modules()


    # This is mostly the same functionallaty of similar method of the
    # class Requirement.
    # ToDo: Unify this!
    def handle_modules_reqdeps(self):
        for module in self.mods.reqdeps_sorted:
            state = module.rewrite(self)
            if state==False:
                # Some sematic error occured.
                self.state = self.er_error
                # Do not continue - return immediately, because some
                # algorithms rely on the correct run from others.
                return

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

    # This is the corresponding makefile dependency outputter.
    def cmad_latex(self, ofile, req_subdir, directory):
        reqs_latex_dir = os.path.join(directory, "reqs")
        # Print out the REQS_TEX variable
        ofile.write("REQS_TEX=")
        for r in self.reqs:
            ofile.write("%s/%s.tex " % (reqs_latex_dir, self.reqs[r].id))
        ofile.write("\n")
        # For each requirement get the dependency correct
        for r in self.reqs:
            ofile.write("%s/%s.tex: %s/%s.req\n\t${CALL_RMTOO}\n"
                        % (reqs_latex_dir, self.reqs[r].id,
                           req_subdir, self.reqs[r].id))

    def output_graph(self, dot_output_file):
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

        # Local function which outputs one set of requirments.
        def output_prio_table(name, l):
            f.write("\subsection{%s}\n" % name)
            f.write("\\begin{longtable}{|r|c|p{7cm}||r|r|} \hline\n")
            f.write("\\textbf{Prio} & \\textbf{Chap} & "
                    "\\textbf{Requirement Id} & \\textbf{EfE} & "
                    "\\textbf{Sum} \\\ \hline\endhead\n")
            s=0
            for p in l:
                if self.reqs[p[1]].tags["Effort estimation"]!=None:
                    efest=self.reqs[p[1]].tags["Effort estimation"]
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

    def stats_reqs_cnt(self, outputfilename):
        statfile = file(outputfilename, "w")
