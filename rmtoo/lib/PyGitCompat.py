#
# Python Git (http://gitorious.org/git-python) is under heavy
# development at the moment.
#
# This compat module checks for the used version and calls the
# appropriate methods which is available in the version.
# (It is currently impossible to directly switch to the new version,
# because the old 0.1.6* version is packed with Debian, Suse, ...)
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.RMTException import RMTException
import git
import time

#
# Checks are done based on features - not version numbers.  This gives
# a better flexibility and the possibility that also versions work
# without prior testing them and inserting them into some kind of
# list. 
#

class PyGitCompatClass:

    class Repo:

        # The path is always absolute and ends in a '.git': therefore
        # cut off the '.git'.
        @staticmethod
        def git_dir(repo):
            # The try-except is for compatibility reasons only:
            # The old version (0.1.6) uses 'path' (which was
            # undocumented) 
            # The new version (>=0.2.0) call this 'git_dir' now.

            if hasattr(repo, "path"):
                return repo.path[:-4]
            if hasattr(repo, "git_dir"):
                return repo.git_dir[:-4]
            raise RMTException(30, "Don't know how to access the "
                               "git_dir / path of the git repo")

    class Tree:

        # Return a iteratable container of all tree items.
        # (Starting with python-git 0.2.0 the tree is no dictionary any
        # more but a list.)
        @staticmethod
        def items(tree):
            if hasattr(tree, "items"):
                # The old version (<=0.1.6)
                return tree.items()

            # The new version (>=0.2.0)
            return tree

        # Access the different values from the iterator
        @staticmethod
        def iter_name(itr):
            # The new versions supplies a 'name' attribute.
            if hasattr(itr, "name"):
                return itr.name
            # The old is just the first element in the list.
            return itr[0]
        
        # Mostly the same as iter_name, but this time the data is
        # accessed. 
        @staticmethod
        def iter_data(itr):
            # The new versions supplies a 'data' attribute.
            if hasattr(itr, "data"):
                return itr.data
            # The old is just the second element in the list
            # dereferenced to the attribute 'data'.
            return itr[1].data

    class Commit:

        # Return the number of commits
        @staticmethod
        def commit_count(repo):
            # The old version (<=0.1.6) directly supports this call.
            if hasattr(repo, "commit_count"):
                return repo.commit_count()
            # The new version must indirected over the Commit object.
            return repo.commit().count()

        # Iterates over the commits
        @staticmethod
        def iter_commits(repo, mc, mcskip):
            # The old version uses the name 'commits'
            if hasattr(repo, "commits"):
                return repo.commits(max_count=mc, skip=mcskip)
            # The new version uses 'iter_commits':
            if hasattr(repo, "iter_commits"):
                return repo.iter_commits(max_count=mc, skip=mcskip)

            raise RMTException(31, "Don't know how to access the "
                               "iter_commits of the git repo")

        # Get the localtime of the authored_data
        @staticmethod
        def authored_date_lt(commit):
            # In old days (<=0.1.6) this was a struct time
            if isinstance(commit.authored_date, time.struct_time):
                return commit.authored_date
            # Nowadays (since 0.2.0) this is a int.
            if isinstance(commit.authored_date, int):
                return time.localtime(commit.authored_date)

PyGitCompat = PyGitCompatClass()
