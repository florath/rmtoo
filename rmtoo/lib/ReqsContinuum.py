#
# ReqsContinuum hold all the different requirement sets from the
# past. 
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

import git

from rmtoo.lib.RMTException import RMTException

class ReqsContinuum:

    # If vers==None the default 'HEAD' is used.
    def __init__(self, directory, vers = "HEAD"):
        self.create_repo(directory)
        self.set_base_commit(vers)

    # This method sets up the repository and splits out the repository
    # dir from the requirements dir.
    def create_repo(self, directory):
        self.repo = git.Repo(directory)
        rpath = self.repo.path[:-4]

        if not directory.startswith(rpath):
            raise RMTException(28, "Cannot split up the given "
                               "directory name")
        
        self.reqs_subdir = directory[len(rpath):]
        self.reqs_subdir_parts = self.reqs_subdir.split("/")

    # Depending on the vers set the base commit (i.e. the base which
    # to work with during the livetime of the continuum object.)
    def set_base_commit(self, vers):
        self.base_commit = self.repo.commit(vers)
