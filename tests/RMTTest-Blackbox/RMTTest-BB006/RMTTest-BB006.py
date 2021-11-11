'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Blackbox rmtoo test

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from BBHelper import BBHelper

cmd_line_parsms = '''json:{"actions": {"create_makefile_dependencies":
"${ENV:rmtoo_test_dir}/makefile_deps"}}'''


class RMTTestBB006(BBHelper):

    out_test_dir = "tests/RMTTest-Blackbox/RMTTest-BB006"
    in_test_dir = "tests/blackbox-test/bb006-test"

    def rmttest_pos_001(self):
        "BB Basic with one requirement - check makefile dependencies"
        self.run_test(unify_output_dirs=["makefile_deps"],
                      relaxed=True,
                      cmd_line_params=[
                          "-j", "file://" + self.out_test_dir
                          + "/input/Config.json",
                          "-j", cmd_line_parsms])
