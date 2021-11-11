'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Note attribute

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.ReqTagGeneric import ReqTagGeneric
from rmtoo.lib.InputModuleTypes import InputModuleTypes


class ReqNote(ReqTagGeneric):
    """Note attribute"""

    def __init__(self, config):
        ReqTagGeneric.__init__(
            self, config, "Note",
            set([InputModuleTypes.ctstag, InputModuleTypes.reqtag,
                 InputModuleTypes.testcase]))

    def rewrite(self, _, req):
        '''This attribute is optional.'''
        return self.handle_optional_tag(req)
