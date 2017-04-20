'''
 rmtoo
   Free and Open Source Requirements Management Tool

  TestCase attribute

 (c) 2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from rmtoo.lib.ReqTagGeneric import ReqTagGeneric
from rmtoo.lib.InputModuleTypes import InputModuleTypes


class ReqTestCase(ReqTagGeneric):

    def __init__(self, config):
        ReqTagGeneric.__init__(self, config, "Test Cases",
                               set([InputModuleTypes.reqtag, ]))

    def rewrite(self, _, req):
        '''This attribute is optional.'''
        if self.get_tag() not in req:
            return self.get_tag(), None

        t = req[self.get_tag()]
        tlist = t.get_content().split()
        del req[self.get_tag()]

        return self.get_tag(), tlist
