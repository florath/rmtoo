#
# LaTeX output class
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

import os
import re

class latex:

    def __init__(self, param):
        self.directory = param[0]

    # Create MAkefile Dependencies
    def cmad(self, reqscont, ofile):
        self.cmad_reqset(reqscont.base_requirement_set, ofile,
                         reqscont.opts.directory)

    def cmad_reqset(self, reqset, ofile, req_subdir):
        reqs_latex_dir = os.path.join(self.directory, "reqs")
        # Print out the REQS_TEX variable
        ofile.write("REQS_TEX=")
        for r in reqset.reqs:
            ofile.write("%s/reqs/%s.tex " % (self.directory, reqset.reqs[r].id))
        ofile.write("\n")
        # For each requirement get the dependency correct
        for r in reqset.reqs:
            ofile.write("%s/reqs/%s.tex: %s/%s.req\n\t${CALL_RMTOO}\n"
                        % (self.directory, reqset.reqs[r].id,
                           req_subdir, reqset.reqs[r].id))

    def output(self, reqscont):
        # Currently just pass this to the RequirementSet
        self.output_reqset(reqscont.base_requirement_set)

    # This is a major heuristic
    # ToDo: have a very, very close look, because it might work (or
    # not) 
    def output_latex_check_master(self, reqset):
        f = file(os.path.join(self.directory, "requirements.tex"), "r")

        included = set()
        for line in f:
            if len(line)>0 and line[-1]=='\n':
                line = line[:-1]
            m=re.match("^\\\input\{reqs/(.*)\.tex\}$", line)
            if m!=None:
                included.add(m.group(1))

        ks = set(reqset.reqs.keys())

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
                
    def output_reqset(self, reqset):
        if not self.output_latex_check_master(reqset):
            print("+++ ERROR: please fix errors first")
            return
        reqs_dir = os.path.join(self.directory, "reqs")
        try:
            os.makedirs(reqs_dir)
        except OSError:
            # This is not a problem: the directory already exists.
            pass
        # Call all requirments to write their files.
        for r in reqset.reqs:
            reqset.reqs[r].output_latex(reqs_dir)
