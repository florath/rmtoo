'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Analytics result.

 (c) 2011-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''


class Result(object):
    """Class holding an analytics result"""

    def __init__(self, analytics_name, object_path_name,
                 analytics_value, message_list):
        self.__analytics_name = analytics_name
        self.__object_path_name = object_path_name
        self.__analytics_value = analytics_value
        self.__message_list = message_list

    def get_value(self):
        """Return the analytics value"""
        return self.__analytics_value

    def write_error(self, mfd):
        '''Write out an error - if the result is an error.'''
        if self.__analytics_value >= 0:
            return
        mfd.write("+++ Error:Analytics:%s:%s:result is '%+3d'\n"
                  % (self.__analytics_name, self.__object_path_name,
                     self.__analytics_value))
        for msg in self.__message_list:
            mfd.write("+++ Error:Analytics:%s:%s:%s\n" %
                      (self.__analytics_name, self.__object_path_name, msg))

    def __str__(self):
        '''Return a string representation of the object.'''
        return "Analytics name [%s] object path [%s] value [%d] "\
            "message list [%s]" % (
                self.__analytics_name,
                self.__object_path_name, self.__analytics_value,
                self.__message_list)
