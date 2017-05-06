'''
 rmtoo
   Free and Open Source Requirements Management Tool

 Test class for the Configuration.

 (c) 2011,2017 by flonatel

 For licensing details see COPYING
'''


class CfgEx(Exception):
    '''Configuration Exception.
    Thrown in case of an invalid configuration.'''

    def __init__(self, value):
        '''Standard exception constructor.'''
        super(CfgEx, self).__init__("<unavailable message>")
        self.value = value

    def __str__(self):
        return repr(self.value)
