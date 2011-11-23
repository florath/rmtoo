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
        self.analytics_name = analytics_name
        self.object_path_name = object_path_name
        self.analytics_value = analytics_value
        self.message_list = message_list

    def get_value(self):
        return self.analytics_value
