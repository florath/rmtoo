'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Constraint class 

 (c) 2011-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.BaseRMObject import BaseRMObject

class Constraint(BaseRMObject):

    def __init__(self, content, rid, file_path, mls, mods, config):
        BaseRMObject.__init__(self, "ctstag", content, rid, mls, mods,
                              config, "constraints", file_path)

