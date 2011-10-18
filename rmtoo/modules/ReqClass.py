#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# Requirement Management Toolset
#
# (c) 2010-2011 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.ReqTagGeneric import ReqTagGeneric
from rmtoo.lib.ClassType import create_class_type, ClassTypeDetailable

# Note:
# The class of the requirement is used in the 'Depends on' checker.
# So if something changes here - possible also there must be changed
# something.

class ReqClass(ReqTagGeneric):
    tag = "Class"
    ltype = set(["reqtag", ])

    def __init__(self, config):
        ReqTagGeneric.__init__(self, config)

    def rewrite(self, rid, req):
        # This tag (Class) is mandatory optional
        # (which means: if it's not there, there is a default - but
        # every requirment do own one class)
        if "Class" not in req:
            v = ClassTypeDetailable()
        else:
            t = req['Class'].get_content()
            v = create_class_type(rid, t)
            del req['Class']
        return self.tag, v
