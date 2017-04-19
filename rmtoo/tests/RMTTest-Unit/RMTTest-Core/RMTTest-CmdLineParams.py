'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Test case for Command Line Parser

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import distutils

from rmtoo.lib.configuration.CmdLineParams import CmdLineParams
from rmtoo.lib.RMTException import RMTException

class RMTTest_CmdLineParser:

    def rmttest_neg_01(self):
        "Command Line Parser: check -m."

        args = ["-f", "SomeFile" ]
        options = CmdLineParams.create_dicts(args)
        mod_dir = distutils.sysconfig.get_python_lib()
        assert(options[1]["global"]["modules"]["directories"] == [mod_dir])

    def rmttest_additional_old_params(self):
        "Command Line Parser: too many args"

        args = ["-f", "SomeFile", "das", "ist", "was"]
        options = CmdLineParams.create_dicts(args)
        assert(options[0]["general"]["command_line_arguments"] == \
               ['das', 'ist', 'was'])
