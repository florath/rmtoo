'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Name attribute

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.ReqTagGeneric import ReqTagGeneric
from rmtoo.lib.InputModuleTypes import InputModuleTypes


class ReqName(ReqTagGeneric):
    """Name attribute"""

    def __init__(self, config):
        ReqTagGeneric.__init__(
            self, config, "Name",
            set([InputModuleTypes.ctstag, InputModuleTypes.reqtag,
                 InputModuleTypes.testcase]))

    def rewrite(self, rid, req):
        """This tag (Name) is mandatory"""
        self.check_mandatory_tag(rid, req, 37)
        return self.get_and_remove(req)
