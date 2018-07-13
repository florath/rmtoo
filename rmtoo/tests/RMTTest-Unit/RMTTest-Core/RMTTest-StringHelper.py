'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for StringHelper

 (c) 2011,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''


from rmtoo.lib.StringHelper import join_ate


class RMTTestStringHelper(object):
    """Test cases for StringHelper module"""

    def rmttest_pos_01(self):
        "StringHelper.join_ate with elements"

        join_res = join_ate("-", ["a", "b", "c", "d"])
        assert "a-b-c-d-" == join_res

    def rmttest_pos_02(self):
        "StringHelper.join_ate empty list"

        join_res = join_ate("-", [])
        assert "" == join_res
