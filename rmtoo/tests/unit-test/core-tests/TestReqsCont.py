#
# Requirement Management Toolset
#
#  Unit test for ReqsContinuum
#
# (c) 2010 on flonatel
#
# For licencing details see COPYING
#

import tempfile
import shutil

from rmtoo.lib.ReqsContinuum import ReqsContinuum
from rmtoo.lib.RMTException import RMTException

class TestOutputHandler:

    def test_positive_01(self):
        try:
            tdir = tempfile.mkdtemp(prefix="rmtoo-tst-ctnt-")

            class Config:
                reqs_spec = {"commit_interval": ["v1", "v7"],
                             "directory": tdir }
                
            ReqsContinuum(None, None, Config)
            assert(False)
        except RMTException, rmte:
            shutil.rmtree(tdir)
            assert(rmte.id()==40)
