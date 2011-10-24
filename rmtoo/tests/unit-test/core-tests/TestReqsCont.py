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
import StringIO

from rmtoo.lib.ReqsContinuum import ReqsContinuum
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.RmtooMain import execute_cmds
from rmtoo.lib.configuration.Cfg import Cfg

class TestReqsCont:

    def test_neg_01(self):
        "ReqsContinuum: check exception when vcs is needed but not available"
        try:
            tdir = tempfile.mkdtemp(prefix="rmtoo-tst-ctnt-")

            config = Cfg()
            config.set_value('requirements.input.commit_interval.begin', 'v1')
            config.set_value('requirements.input.commit_interval.end', 'v7')
            config.set_value('requirements.input.directory', tdir)

            ReqsContinuum(None, config)
            assert(False)
        except RMTException, rmte:
            shutil.rmtree(tdir)
            assert(rmte.id() == 40)

    def test_neg_02(self):
        "ReqsContinuum: check exception when vcs is needed but not available \
        (entry point in execute_cmds())"

        tdir = tempfile.mkdtemp(prefix="rmtoo-tst-ctnt-")

        config = Cfg()
        config.set_value('requirements.input.commit_interval.begin', 'v1')
        config.set_value('requirements.input.commit_interval.end', 'v7')
        config.set_value('requirements.input.directory', tdir)

        mstderr = StringIO.StringIO()

        rval = execute_cmds(config, None, None, mstderr)

        assert(rval == False)
        print("ERROR IS [%s]" % mstderr.getvalue())
        assert(mstderr.getvalue() == "+++ ERROR: Problem reading in "
               "the continuum: '[  40]: Based on the config "
               "a repository is needed - but there is none'")
