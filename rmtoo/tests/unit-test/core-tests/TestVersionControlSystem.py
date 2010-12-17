#
# Tests for the Version Control System Class
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.VersionControlSystem import VCSException, VCSGit

class Dummy:
    pass

class TestVersionControlSystem:

    def test_pos_01(self):
        "VCSGit: Check error handling of set_directories"
        
        # The problem is here to create an object without having 
        # a git repo available.
        class InHerVCS(VCSGit):

            def __init__(self, directory):
                self.repo = Dummy()
                self.repo.git_dir = directory

        vcs = InHerVCS("/hahaha")

        try:
            vcs.set_directories("/huhuhu")
            assert(False)
        except RMTException, rmte:
            assert(rmte.id()==28)

                                           
    def test_pos_02(self):
        "VCSGit: Check error handling of rh_one_rs"
        
        # The problem is here to create an object without having 
        # a git repo available.
        class InHerVCS(VCSGit):

            def __init__(self, directory):
                self.repo = Dummy()
                self.repo.git_dir = directory

        vcs = InHerVCS("/hahaha")

        class Files:
            name = "/tmp/huhu.noreq"

        files = [Files()]

        class RS:
            reqs = []

        rs = RS()

        vcs.rh_one_rs(None, rs, files)

