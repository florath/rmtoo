'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Requirement class itself

 (c) 2011,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from rmtoo.lib.RMTException import RMTException


class ClassTypeBase(object):
    """Base class of for the ClassType

    This implements the complete functionality - the
    implementations need only to call the constructor
    and the class does the right thing.
    """

    def __init__(self, ostr, is_implementable):
        self.__output_string = ostr
        self.__is_implementable = is_implementable

    def get_output_string(self):
        """Returns the output string"""
        return self.__output_string

    def is_implementable(self):
        """Returns if the class type is implementable"""
        return self.__is_implementable


class ClassTypeImplementable(ClassTypeBase):
    """ClassType specialization for Implementable"""

    def __init__(self):
        ClassTypeBase.__init__(self, "implementable", True)


class ClassTypeDetailable(ClassTypeBase):
    """ClassType specialization for Detailable"""

    def __init__(self):
        ClassTypeBase.__init__(self, "detailable", False)


class ClassTypeSelected(ClassTypeBase):
    """ClassType specialization for Selected"""

    def __init__(self):
        ClassTypeBase.__init__(self, "selected", True)


def create_class_type(rid, type_desc):
    """Creates the class typed based on the type description"""
    if type_desc == "implementable":
        return ClassTypeImplementable()
    if type_desc == "detailable":
        return ClassTypeDetailable()
    if type_desc == "selected":
        return ClassTypeSelected()

    raise RMTException(95, "%s:class type invalid '%s'" % (rid, type_desc))
