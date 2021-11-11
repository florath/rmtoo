'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Version Control System.
   Exception.

 (c) 2011,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''


class VCSException(Exception):
    """Exception for Version Control System"""

    def __init__(self, msg):
        Exception.__init__(self, msg)
