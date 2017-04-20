'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Test case for Command Line Parser

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
import distutils
import unittest

from rmtoo.lib.configuration.CmdLineParams import CmdLineParams


class RMTTestCmdLineParser(unittest.TestCase):

    def rmttest_neg_01(self):
        "Command Line Parser: check -m."

        args = ["-f", "SomeFile"]
        options = CmdLineParams.create_dicts(args)
        mod_dir = distutils.sysconfig.get_python_lib()
        self.assertEqual(
            [mod_dir], options[1]["global"]["modules"]["directories"])

    def rmttest_additional_old_params(self):
        "Command Line Parser: too many args"

        args = ["-f", "SomeFile", "das", "ist", "was"]
        options = CmdLineParams.create_dicts(args)
        self.assertEqual(
            ['das', 'ist', 'was'],
            options[0]["general"]["command_line_arguments"])
