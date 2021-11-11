'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Test topic set.

 (c) 2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''


class TestTopicSet:

    def __init__(self, rset):
        self.__rset = rset

    def get_requirement_set(self):
        return self.__rset
