'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Version Control System.
   Exception.

 (c) 2011,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''


class VCSException(Exception):

    def __init__(self, msg):
        self.msg = msg
