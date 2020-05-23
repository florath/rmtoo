'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Test case for Command Line Parser

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
import distutils


from rmtoo.lib.configuration.CmdLineParams import CmdLineParams


class RMTTestCmdLineParser(object):
    """Test cases for command line parameter"""

    def rmttest_neg_01(self):
        "Command Line Parser: check -m."

        args = ["-f", "SomeFile"]
        options = CmdLineParams.create_dicts(args)
        mod_dir = distutils.sysconfig.get_python_lib()
        assert [mod_dir] == options[1]["global"]["modules"]["directories"]
