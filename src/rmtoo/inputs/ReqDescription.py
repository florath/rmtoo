'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Requirement Tag Description

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import print_function

from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.ReqTagGeneric import ReqTagGeneric
from rmtoo.lib.InputModuleTypes import InputModuleTypes


class ReqDescription(ReqTagGeneric):
    """Requirement description attribute"""

    def __init__(self, config):
        ReqTagGeneric.__init__(
            self, config, "Description",
            set([InputModuleTypes.ctstag, InputModuleTypes.reqtag,
                 InputModuleTypes.testcase]))

    def rewrite(self, rid, req):
        """This tag (Description) is mandatory"""
        self.check_mandatory_tag(rid, req, 2)

        tag = req[self.get_tag()]
        # It must not be too long.
        # (Long text means: split it up!)
        if len(tag.get_content()) > 1024:
            raise RMTException(3, "%s: Description is much too long: "
                               "%d characters" %
                               (rid, len(tag.get_content())))
        if len(tag.get_content()) > 255:
            print("+++ WARNING %s: Description is too long: %d characters"
                  % (rid, len(tag.get_content())))
            print("+++          Please consider split up this requirement")
        # Copy and delete the original
        del req[self.get_tag()]

        return self.get_tag(), tag
