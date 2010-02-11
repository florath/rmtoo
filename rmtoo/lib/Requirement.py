#
# Requirement Management Toolset
#  class Requirement
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

import os
import time

class Requirement:

    # Requirment Type
    # Each requirement has exactly one type.
    # The class ReqType sets this from the contents of the file.
    # Note: There can only be one (master requirement)
    rt_master_requirement = 1
    rt_initial_requirement = 2
    rt_design_decision = 3
    rt_requirement = 4

    # Line Type
    # The parse() function returns one of those
    lt_empty = 1
    lt_comment = 2
    lt_continue = 3
    lt_error = 4
    lt_initial = 5

    # Status of Requirement
    # (i.e. is the requirment usable?)
    st_fine = 0
    st_error = 1

    def __init__(self, fd, rid, mods, opts, config):
        self.req = {}
        self.id = rid
        self.mods = mods
        self.opts = opts
        self.config = config
        
        self.state = self.st_fine
        
        self.read(fd)
        self.handle_modules_reqtag()

    def erase_heading_ws(self, l):
        while len(l)>0 and l[0]==" ":
            l = l[1:]
        return l

    def parse_line(self, line, lineno):
        if len(line)>0 and line[-1]=='\n':
            line = line[:-1]
        # Empty line
        if len(line)==0:
            return self.lt_empty, None, None
        # Comment line
        if line[0]=='#':
            return self.lt_comment, None, None
        # Continue line
        if line[0]==' ':
            return self.lt_continue, None, line
        # Is the line toooo long?
        if len(line)>80:
            print("+++ ERROR %s:%d: line too long (%d chars) '%s'"
                  % (self.id, lineno, len(line), line))
        # 'Normal' line
        ls = line.split(":", 1)
        if len(ls)==1:
            # No ':' found
            print("+++ ERROR %s:%d: no ':' in line '%s'" %
                  (self.id, lineno, line))
            return self.lt_error, None, None
        if len(ls[0])==0:
            # ':' is first char in line
            print("+++ ERROR %s:%d: no char before ':'" %
                  (self.id, lineno))
            return self.lt_error, None, None
        # Normal 'initial' case
        return self.lt_initial, ls[0], self.erase_heading_ws(ls[1])

    # This implements a finite state automate with a very small number
    # of states and translations.
    def read(self, fd):
        lineno = 0
        fine=True
        last_key = None
        for line in fd:
            lineno+=1
            line_type, key, content = self.parse_line(line, lineno)

            if line_type==self.lt_empty:
                continue
            if line_type==self.lt_comment:
                continue
            if line_type==self.lt_error:
                fine=False
                continue
            if line_type==self.lt_continue:
                if last_key==None:
                    print("+++ ERROR %s:%d: continue line without " \
                              + "initial line" % (self.id, lineno))
                    fine=False
                self.req[last_key]+=content
                continue
            if line_type==self.lt_initial:
                if key in self.req:
                    print("+++ ERROR %s:%d: key '%d' already exists" %
                          (self.id, lineno, key))
                    fine=False
                    continue
                self.req[key] = content
                last_key = key
                continue
            print("+++ ERROR %s:%d: Invalid line_type '%d'" %
                  (self.id, lineno, line_type))
            fine=False
        return fine

    def handle_modules_reqtag(self):
        for module in self.mods.reqtag:
            self.mods.reqtag[module].rewrite(self)

    # Error is an error (no distinct syntax error)
    def mark_syntax_error(self):
        self.state = self.st_error

    # Error is an error (no distinct sematic error)
    def mark_sematic_error(self):
        self.state = self.st_error

    def output_latex(self, directory):
        f = file(os.path.join(directory, self.id + ".tex"), "w")
        g = file(os.path.join(directory, "dependsgraph.dot"), "a")
        f.write("\subsection{%s}\label{%s}\n\\textbf{Description:} %s\n" 
                % (self.t_Name, self.id, self.t_Description))

        if self.t_Rationale!=None:
            f.write("\n\\textbf{Rationale:} %s\n" % self.t_Rationale)

        if self.t_DependOn!=None:
            # Create links to the corresponding labels.
            f.write("\n\\textbf{Depends on:} ")
            # ToDo: THIS IS UGLY!
            # ToDo: split latex and dot output
            #if self.id[0]=='M':
            #    g.write("%s [color=green]\n" % (self.id[2:]))
            #if self.id[0]=='D':
            #    g.write("%s [color=blue]\n" % (self.id[2:]))
            #if self.id[0]=='I':
            #    g.write("%s [color=orange]\n" % (self.id[2:]))
            for d in self.t_DependOn:
                f.write("\\ref{%s} \\nameref{%s}  " % (d, d))
                g.write("%s -> %s;\n" % (self.id, d))
            f.write("\n")

        f.write("""
\\begin{center}
\\begin{longtable}{|l|p{7cm}|}\hline
\\textbf{Id} & %s \\\ \hline
\\textbf{Priority} & %s \\\ \hline
\\textbf{Owner} & %s \\\ \hline
\\textbf{Invented on} & %s \\\ \hline
\\textbf{Invented by} & %s \\\ \hline
\end{longtable}
\end{center}
""" % (self.id, self.t_Priority, self.t_Owner,
       time.strftime("%Y-%m-%d", self.t_InventedOn),
       self.t_InventedBy))
        g.close()
        f.close()
