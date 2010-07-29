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
        self.topic_name = param[0]
        self.output_filename = param[1]

    def set_topics(self, topics):
        self.topic_set = topics.get(self.topic_name)

    # Create Makefile Dependencies
    def cmad(self, reqscont, ofile):
        ofile.write("%s: ${REQS}\n\t${CALL_RMTOO}\n" % (self.output_filename))

    # XXXX NOT USED ANYMORE
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

    # XXXX NOT USED ANYMORE
    # If there is no repo available, just output the current date /
    # time and the current number of requirements
    def output_stats_reqs_cnt_files(self, reqscont, ofile):
        ofile.write("%s %d\n" %
                    (time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime()),
                     len(reqscont.base_requirement_set.reqs)))


    def output(self, reqscont):
        # Depending on the number of elements in the continuum, this
        # might be a list or, if only FILES should be used, exactly
        # one value (the current time).
        ofile = file(self.output_filename, "w")

        for cid in reqscont.continuum_order:
            rs = reqscont.continuum[cid]
            ofile.write("%s %d\n" %
                        (time.strftime("%Y-%m-%d_%H:%M:%S", 
                                       time.localtime(rs.timestamp())),
                         rs.reqs_count()))

        # Clean up the file.
        ofile.close()

