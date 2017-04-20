'''
 rmtoo
   Free and Open Source Requirements Management Tool

  StringHelper
   Small helper and utils for the string class

 (c) 2011-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''


class StringHelper:
    '''String Helper class function collection.'''

    @staticmethod
    def join_ate(delim, jlist):
        '''This is mostly the same as the string 'join()' method, but
           The delimiter is also added to the end of the list.'''
        res = u""
        for j in jlist:
            res += j + delim
        return res
