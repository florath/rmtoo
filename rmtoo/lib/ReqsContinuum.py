#
# ReqsContinuum hold all the different requirement sets from the
# past. 
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

import git
import os
import re
import time

from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.RequirementSet import RequirementSet

class ReqsContinuum:

    # If vers==None the default 'HEAD' is used.
    def __init__(self, directory, mods, opts, config, vers = "HEAD"):
        self.mods = mods
        self.opts = opts
        self.config = config
        self.create_repo(directory)
        self.set_base_commit(vers)
        self.create_base_reqset()

    # This method sets up the repository and splits out the repository
    # dir from the requirements dir.
    def create_repo(self, directory):
        # When the directory is not absolute, convert it to an
        # absolute path that it can be comparted to the outcome of the
        # git.Repo. 
        if not os.path.isabs(directory):
            directory = os.path.abspath(directory)

        self.repo = git.Repo(directory)
        # The path is always absolute and ends in a '.git': therefore
        # cut off the '.git'.
        rpath = self.repo.path[:-4]

        if not directory.startswith(rpath):
            raise RMTException(28, "Cannot split up the given "
                               "directory name")
        
        self.reqs_subdir = directory[len(rpath):]
        self.reqs_subdir_parts = self.reqs_subdir.split("/")

        print("Reqs Subdir='%s'" % self.reqs_subdir)

    # Depending on the vers set the base commit (i.e. the base which
    # to work with during the livetime of the continuum object.)
    def set_base_commit(self, vers):
        self.base_commit = self.repo.commit(vers)

    # Build up the requirements tree
    def get_reqs_tree(self, tree):
        for d in self.reqs_subdir_parts:
            tree = tree[d]
        return tree

    def create_base_reqset(self):
        self.base_requirements_set = \
            RequirementSet(self.mods, self.opts, self.config)
        reqs_tree = self.get_reqs_tree(self.base_commit.tree)
        self.base_requirements_set.read_from_git_tree(reqs_tree)

    # Output all the things should be
    def output(self):
        for ok, ov in self.config.output_specs.items():
            # Call the methos with all the given parameters
            eval("self.output_%s(*%s)" % (ok, ov))

    ### Output methods
            
    # Output: Prios
    def output_prios(self, ofilename):
        # Currently just pass this to the RequirementSet
        self.base_requirements_set.output_prios(ofilename)

    # Output: LaTeX
    def output_latex(self, ofilename):
        # Currently just pass this to the RequirementSet
        self.base_requirements_set.output_latex(ofilename)

    # Output: Graph
    def output_graph(self, ofilename):
        # Currently just pass this to the RequirementSet
        self.base_requirements_set.output_graph(ofilename)

    # Output: Statistics on Requirement Count
    # Note: because this goes the whole history back it takes some
    # time. 
    def output_stats_reqs_cnt(self, ofilename):
        # This can be done only by counting - so this can be done
        # here. 
        ofile = file(ofilename, "w")

        # Get the commit count
        commit_count = self.repo.commit_count()
        # The commits are retreived in steps of 10 (by default)
        commits_seen = 0
        while commits_seen < commit_count:
            # Get all the next bulk of commits
            commits = self.repo.commits(max_count=10, skip=commits_seen)
            #print("Commits bulk Cnt: %d" % len(commits))
            commits_seen += len(commits)

            # Step though the commits and count the number of requirements
            for commit in commits:
                reqs_in_commit = 0

                try:
                    tree = self.get_reqs_tree(commit.tree)
                    for f in tree.items():
                        # Only count the files ending in '.req'.
                        m = re.match("^.*\.req$", f[0])
                        if m==None:
                            continue
                        reqs_in_commit += 1
                    ofile.write("%s %d\n" %
                                (time.strftime("%Y-%m-%d_%H:%M:%S",
                                               commit.authored_date),
                                 reqs_in_commit))
                except KeyError, k:
                    # no doc/requirements in this commit. Skip error
                    pass
        
        # Clean up the file.
        ofile.close()

    ### Dependency generation

    def create_makefile_dependencies(self, ofilename):
        ofile = file(ofilename, "w")
        self.cmad_write_reqs_list(ofile)
        for ok, ov in self.config.output_specs.items():
            # Call the methos with all the given parameters
            eval("self.cmad_%s(ofile, *%s)" % (ok, ov))
        # Shut down the file.
        ofile.close()

    # CMAD write REQS list
    def cmad_write_reqs_list(self, ofile):
        reqs=[]
        # XXX This is nearly a copy: unify this!
        # Get a list of all REQS files
        try:
            tree = self.get_reqs_tree(self.base_commit.tree)
            for f in tree.items():
                # Only add the files ending in '.req'.
                m = re.match("^.*\.req$", f[0])
                if m==None:
                    continue
                reqs.append(f[0])
        except KeyError, k:
            # no doc/requirements in this commit. Skip error
            pass
        # Write out the list
        ofile.write("REQS=")
        for r in reqs:
            ofile.write("%s " % os.path.join(self.opts.directory, r))
        ofile.write("\n")

    # CMAD prios
    def cmad_prios(self, fd, ofilename):
        fd.write("%s: ${REQS}\n\t${CALL_RMTOO}\n" % (ofilename))

    # CMAD latex
    def cmad_latex(self, fd, directory):
        self.base_requirements_set.cmad_latex(
            fd, self.opts.directory, directory)

    # CMAD Stats requirements count
    def cmad_stats_reqs_cnt(self, fd, ofilename):
        fd.write("%s: ${REQS}\n\t${CALL_RMTOO}\n" % (ofilename))

    # CMAD graph
    def cmad_graph(self, fd, ofilename):
        fd.write("%s: ${REQS}\n\t${CALL_RMTOO}\n" % (ofilename))
        
