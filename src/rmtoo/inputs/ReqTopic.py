'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Topic attribute

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.ReqTagGeneric import ReqTagGeneric
from rmtoo.lib.InputModuleTypes import InputModuleTypes


class ReqTopic(ReqTagGeneric):
    """Class holding a topic"""

    def __init__(self, config):
        ReqTagGeneric.__init__(self, config, "Topic",
                               set([InputModuleTypes.reqtag, ]))

    def rewrite(self, rid, req):
        """This tag (Name) is mandatory"""
        self.check_mandatory_tag(rid, req, 9)

        tcontent = req[self.get_tag()].get_content()
        del req[self.get_tag()]
        return self.get_tag(), tcontent
