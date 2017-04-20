'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Class attribute

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.ReqTagGeneric import ReqTagGeneric
from rmtoo.lib.ClassType import create_class_type, ClassTypeDetailable
from rmtoo.lib.InputModuleTypes import InputModuleTypes


class ReqClass(ReqTagGeneric):

    def __init__(self, config):
        ReqTagGeneric.__init__(self, config, "Class",
                               set([InputModuleTypes.reqtag, ]))

    def rewrite(self, rid, req):
        # This tag (Class) is mandatory optional
        # (which means: if it's not there, there is a default - but
        # every requirement do own one class)
        if self.get_tag() not in req:
            v = ClassTypeDetailable()
        else:
            t = req[self.get_tag()].get_content()
            v = create_class_type(rid, t)
            del req[self.get_tag()]
        return self.get_tag(), v
