'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  StringHelper
   Small helper and utils for the string class
   
 (c) 2011-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

# pylint: disable=W0232
class StringHelper:

    @staticmethod
    def join_ate(delim, jlist):
        '''This is mostly the same as the string 'join()' method, but
           The delimiter is also added to the end of the list.'''
        r = ""
        for j in jlist:
            r += j + delim
        return r

