#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# Requirement class itself
#
# (c) 2011 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.RMTException import RMTException

class ClassTypeImplementable:

    def get_output_string(self):
        return "implementable"

    def is_implementable(self):
        return True


class ClassTypeDetailable:

    def get_output_string(self):
        return "detailable"

    def is_implementable(self):
        return False


class ClassTypeSelected:

    def get_output_string(self):
        return "selected"

    # The selected requirement is a requirement which can be
    # (directly) implemented. 
    def is_implementable(self):
        return True
    

def create_class_type(rid, l):
    if l=="implementable":
        return ClassTypeImplementable()
    if l=="detailable":
        return ClassTypeDetailable()
    if l=="selected":
        return ClassTypeSelected()
    
    raise RMTException(95, "%s:class type invalid '%s'" % (rid, l))
