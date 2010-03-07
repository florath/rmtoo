#
# Requirement class itself
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

import os
import time

from rmtoo.lib.RequirementParser import RequirementParser
from rmtoo.lib.digraph.Digraph import Digraph

class Requirement(Digraph.Node):

    # Requirment Type
    # Each requirement has exactly one type.
    # The class ReqType sets this from the contents of the file.
    # Note: There can only be one (master requirement)
    rt_master_requirement = 1
    rt_initial_requirement = 2
    rt_design_decision = 3
    rt_requirement = 4

    # Status Type
    # Each requirement has a Status.
    # It will be read in and set by the ReqStatus class.
    # The status must be one of the following:
    st_not_done = 1
    st_finished = 2

    # Class Type
    # This specifies, if this node is really a node or if this can /
    # must be elaborated in more detail.
    ct_implementable = 1
    ct_detailable = 2

    # Error Status of Requirement
    # (i.e. is the requirment usable?)
    er_fine = 0
    er_error = 1

    def __init__(self, fd, rid, mods, opts, config):
        Digraph.Node.__init__(self, rid)

        self.tags = {}
        self.id = rid
        self.mods = mods
        self.opts = opts
        self.config = config

        self.state = self.er_fine
        self.input(fd)

    def input(self, fd):
        # Read it in from the file (Syntactic input)
        req = RequirementParser.read(fd)
        if req == None:
            self.state = self.er_error
            print("+++ ERROR %s: parser returned error" % self.id)
            return

        # Handle all the modules (Semantic input)
        self.handle_modules_reqtag(req)

        # Do not check for remaining tags here. There must be some
        # left over: all those that work on the whole requirement set
        # (e.g. 'Depends on').

        # If everything's fine, store the rest of the req for later
        # inspection.
        self.req = req

    def handle_modules_reqtag(self, reqs):
        for modkey, module in self.mods.reqtag.items():
            try:
                key, value = module.rewrite(self.id, reqs)
                # Check if there is already a key with the current key
                # in the map.
                if key in self.tags:
                    print("+++ ERROR %s: tag '%s' already defined" %
                          (self.id, key))
                    self.state = er_error
                    # Also continue to get possible further error
                    # messages.
                self.tags[key] = value
            except RMTException, rmte:
                # Some sematic error occured: do not interpret key or
                # value.
                # The error message was already eliminated - so do
                # only one generic
                print("+++ ERROR %s: semantic error occured in '%s'"
                      % (self.id, modkey))
                print("+++ root cause is: '%s'" % rmte)
                self.state = self.er_error
                # Continue (do not return immeditely) to get also
                # possible other errors.

    def ok(self):
        return self.state==self.er_fine

    # Error is an error (no distinct syntax error)
    def mark_syntax_error(self):
        self.state = self.er_error

    # Error is an error (no distinct sematic error)
    def mark_sematic_error(self):
        self.state = self.er_error

    def get_prio(self):
        return self.tags["Priority"]

    def is_open(self):
        return self.tags["Status"] == self.st_not_done

    def is_implementable(self):
        return self.tags["Class"] == self.ct_implementable

    # ToDo: outputXXX should be also done using the tag classes.
    def output_latex(self, directory):
        f = file(os.path.join(directory, self.id + ".tex"), "w")
        f.write("\subsection{%s}\label{%s}\n\\textbf{Description:} %s\n" 
                % (self.tags["Name"], self.id, self.tags["Description"]))

        if "Rationale" in self.tags:
            f.write("\n\\textbf{Rationale:} %s\n" % self.tags["Rationale"])

        if "Note" in self.tags:
            f.write("\n\\textbf{Note:} %s\n" % self.tags["Note"])

        # Only output the depends on when there are fields for output.
        if len(self.outgoing)>0:
            # Create links to the corresponding labels.
            f.write("\n\\textbf{Depends on:} ")
            for d in self.outgoing:
                f.write("\\ref{%s} \\nameref{%s}, " % (d.id, d.id))
            f.write("\n")

        if len(self.incoming)>0:
            # Create links to the corresponding dependency nodes.
            f.write("\n\\textbf{Dependent:} ")
            for d in self.incoming:
                f.write("\\ref{%s} \\nameref{%s}, " % (d.id, d.id))
            f.write("\n")

        if self.tags["Status"]==self.st_finished:
            status = "completed"
        else:
            status = "open"

        if self.tags["Class"]==self.ct_implementable:
            clstr="implementable"
        else:
            clstr="detailable"

        f.write("\n{\small \\begin{longtable}{rlrlrl}\n"
                "\\textbf{Id:} & %s & "
                "\\textbf{Priority:} & %4.2f & "
                "\\textbf{Owner:} & %s \\\ \n"
                "\\textbf{Invented on:} & %s & "
                "\\textbf{Invented by:} & %s & "
                "\\textbf{Status:} & %s \\\ \n"
                "\\textbf{Class:} & %s & & & & \\\ \n"
                "\end{longtable} }"
                % (self.id, self.tags["Priority"]*10, self.tags["Owner"],
                   time.strftime("%Y-%m-%d", self.tags["Invented on"]),
                   self.tags["Invented by"], status, clstr))
        f.close()

    def output_dot(self, dotfile):
        # Colorize the current requirement depending on type
        nodeparam = []
        if self.tags["Type"] == self.rt_initial_requirement:
            nodeparam.append("color=orange")
        if self.tags["Type"] == self.rt_design_decision:
            nodeparam.append("color=green")

        if self.tags["Status"] == self.st_not_done:
            nodeparam.append("fontcolor=red")
            nodeparam.append('label="%s\\n[%4.2f]"' %
                             (self.id, self.tags["Priority"]*10))

        if self.tags["Class"] == self.ct_implementable:
            nodeparam.append("shape=octagon")

        if len(nodeparam)>0:
            dotfile.write("%s [%s];\n" % (self.id, ",".join(nodeparam)))

        for d in self.outgoing:
            dotfile.write("%s -> %s;\n" % (self.id, d.id))
