#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# Requirement Tag Description
#
# (c) 2010-2011 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.ReqTagGeneric import ReqTagGeneric

class ReqDescription(ReqTagGeneric):
    tag = "Description"
    ltype = set(["reqtag", "ctstag"])

    def __init__(self, opts, config):
        ReqTagGeneric.__init__(self, opts, config)

    def rewrite(self, rid, req):
        # This tag (Description) is mandatory
        self.check_mandatory_tag(rid, req, 2)

        t = req[self.tag]
        # It must not be too long.
        # (Long text means: split it up!)
        # ToDo: one day, check for special words which are not allowed
        # in requirements (like 'or' or 'and')
        # ToDo: Check for words which must appear in a requirement,
        # like 'have to' or 'must'.
        if len(t.get_content())>1024:
            raise RMTException(3, "%s: Description is much too long: "
                               "%d characters" % (rid, len(t.get_content())))
        if len(t.get_content())>255:
            print("+++ WARNING %s: Description is too long: %d characters"
                  % (rid, len(t.get_content())))
            print("+++          Please consider split up this requirement")
        # Copy and delete the original
        del req[self.tag]

        return self.tag, t
            
