#
# Count the requirements for each existing commit.
#
#  set timefmt "%Y-%m-%d_%H:%M:%S"
#  set xdata time
#  plot 'reqs.cnt' using 1:2

import re
import time
import git

def main():
    # Get the repo itself
    repo = git.Repo(".")
    # and the commit count
    commit_count = repo.commit_count()

    # The commits are retreived in steps of 10.
    commits_seen = 0
    while commits_seen < commit_count:
        # Get all the next bulk of commits
        commits = repo.commits(max_count=10, skip=commits_seen)
        #print("Commits bulk Cnt: %d" % len(commits))
        commits_seen += len(commits)

        # Step though the commits and count the number of requirements
        for commit in commits:
            reqs_in_commit = 0

            try:
                tree = commit.tree["doc"]["requirements"]
                for f in tree.items():
                    m = re.match("^.*\.req$", f[0])
                    if m==None:
                        continue
                    reqs_in_commit += 1
                print("%s %d" % (time.strftime("%Y-%m-%d_%H:%M:%S", commit.authored_date), reqs_in_commit))
            except KeyError, k:
                # no doc/requirements in this commit. Skip error
                pass

if __name__=="__main__":
    main()
