'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Invented on attribute

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.ReqTagGeneric import ReqTagGeneric
from rmtoo.lib.DateUtils import parse_date
from rmtoo.lib.InputModuleTypes import InputModuleTypes


class ReqInventedOn(ReqTagGeneric):
    """Invented on tag"""

    def __init__(self, config):
        ReqTagGeneric.__init__(
            self, config, "Invented on",
            set([InputModuleTypes.ctstag, InputModuleTypes.reqtag,
                 InputModuleTypes.testcase]))

    def rewrite(self, rid, req):
        """This tag (Invented on) is mandatory"""
        self.check_mandatory_tag(rid, req, 7)

        tag = req[self.get_tag()]
        tcontent = parse_date(rid, tag.get_content())
        del req[self.get_tag()]
        return self.get_tag(), tcontent
