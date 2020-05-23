'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Blackbox rmtoo test

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from BBHelper import BBHelper


class RMTTestBB001(BBHelper):

    out_test_dir = "tests/RMTTest-Blackbox/RMTTest-BB001"
    in_test_dir = "tests/blackbox-test/bb001-test"

    def rmttest_pos_001(self):
        "BB Basic with one requirement - reqs only from git"
        self.run_test(container_files=["reqspricing.ods", ])

# ToDo:
# This runs into a strange error: exact in the oopricing
# there is a difference in some (three!) attributes.
#    def rmttest_pos_002(self):
#        "BB Basic with one requirement - reqs only from git (yaml)"
#        self.run_test(yaml=True, container_files=["reqspricing.ods", ])


if __name__ == '__main__':
    rtest = RMTTestBB001()
    rtest.rmttest_pos_001()
