'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Analytics result.
   
 (c) 2011 by flonatel GmhH & Co. KG

 For licensing details see COPYING
'''

class Result:

    def __init__(self, analytics_name, object_path_name,
                 analytics_value, message_list):
        self.__analytics_name = analytics_name
        self.__object_path_name = object_path_name
        self.__analytics_value = analytics_value
        self.__message_list = message_list

    def get_value(self):
        return self.__analytics_value

    # TODO: Better output
    def __str__(self):
        return "analytics name [%s] object path [%s] value [%d] "\
            "message list [%s]" % (self.__analytics_name,
            self.__object_path_name, self.__analytics_value,
            self.__message_list)
