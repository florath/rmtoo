'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
 Test class for the Configuration.
 
 (c) 2011 by flonatel

 For licensing details see COPYING
'''

class CfgEx(Exception):
    '''Configuration Exception.
       Thrown in case of an invalid configuration.'''

    # pylint: disable=W0231
    def __init__(self, value):
        '''Standard exception constructor.'''
        self.value = value

    def __str__(self):
        return repr(self.value)
