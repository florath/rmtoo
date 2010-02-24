#
# Requirement Tag Description
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.ReqTagGeneric import ReqTagGeneric

class ReqDescription(ReqTagGeneric):
    tag = "Description"

    def __init__(self, opts, config):
        ReqTagGeneric.__init__(self, opts, config)

    def rewrite(self, rid, req):
        # This tag (Description) is mandatory
        if not self.check_mandatory_tag(rid, req):
            return False, None, None

        t = req[self.tag]
        # It must not be too long.
        # (Long text means: split it up!)
        # ToDo: one day, check for special words which are not allowed
        # in requirements (like 'or' or 'and')
        # ToDo: Check for words which must appear in a requirement,
        # like 'have to' or 'must'.
        if len(t)>1024:
            print("+++ ERROR %s: Description is much too long: %d characters"
                  % (rid, len(t)))
            print("+++        Please consider split up this requirement")
            return False, None, None
        if len(t)>255:
            print("+++ WARNING %s: Description is too long: %d characters"
                  % (rid, len(t)))
            print("+++          Please consider split up this requirement")
        # Copy and delete the original
        del req[self.tag]

        return True, self.tag, t
            
