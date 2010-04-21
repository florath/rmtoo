#
# stats_reqs_cnt output class
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

import re
import time

from rmtoo.lib.PyGitCompat import PyGitCompat

class stats_reqs_cnt:

    def __init__(self, param):
        self.output_filename = param[0]

    # Create MAkefile Dependencies
    def cmad(self, reqscont, ofile):
        ofile.write("%s: ${REQS}\n\t${CALL_RMTOO}\n" % (self.output_filename))

    # Output: Statistics on Requirement Count
    # Note: because this goes the whole history back it takes some
    # time.
    def output_stats_reqs_cnt_repo(self, reqscont, ofile):
        # Get the commit count
        commit_count = PyGitCompat.Commit.commit_count(reqscont.repo)
        # The commits are retreived in steps of 10 (by default)
        commits_seen = 0
        while commits_seen < commit_count:
            # Get all the next bulk of commits
            commits = PyGitCompat.Commit.iter_commits(
                reqscont.repo, reqscont.commit_bulk_size, commits_seen)

            # Step though the commits and count the number of requirements
            for commit in commits:
                commits_seen += 1
                reqs_in_commit = 0

                try:
                    tree = reqscont.get_reqs_tree(commit.tree)
                    for f in PyGitCompat.Tree.items(tree):
                        # Only count the files ending in '.req'.
                        m = re.match("^.*\.req$", PyGitCompat.Tree.iter_name(f))
                        if m==None:
                            continue
                        reqs_in_commit += 1
                    ofile.write("%s %d\n" %
                                (time.strftime("%Y-%m-%d_%H:%M:%S",
                                               PyGitCompat.Commit.
                                               authored_date_lt(commit)),
                                 reqs_in_commit))
                except KeyError, k:
                    # no doc/requirements in this commit. Skip error
                    pass

    # If there is no repo available, just output the current date /
    # time and the current number of requirements
    def output_stats_reqs_cnt_files(self, ofile):
        ofile.write("%s %d\n" %
                    (time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime()),
                     len(self.base_requirement_set.reqs)))

    def output(self, reqscont):
        # This can be done only when a repo is available.  If no repo
        # is available output only the current number of
        # requirements. 
        ofile = file(self.output_filename, "w")

        if reqscont.repo_available:
            self.output_stats_reqs_cnt_repo(reqscont, ofile)
        else:
            self.output_stats_reqs_cnt_files(ofile)
        
        # Clean up the file.
        ofile.close()

