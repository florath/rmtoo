'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Requirement class itself

 (c) 2011,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from rmtoo.lib.RMTException import RMTException


class ClassTypeImplementable:

    @staticmethod
    def get_output_string():
        return "implementable"

    @staticmethod
    def is_implementable():
        return True


class ClassTypeDetailable:

    @staticmethod
    def get_output_string():
        return "detailable"

    @staticmethod
    def is_implementable():
        return False


class ClassTypeSelected:

    @staticmethod
    def get_output_string():
        return "selected"

    @staticmethod
    def is_implementable():
        """Return if requirement is implementable

        The selected requirement is a requirement which can be
        (directly) implemented.
        """
        return True


def create_class_type(rid, l):
    if l == "implementable":
        return ClassTypeImplementable()
    if l == "detailable":
        return ClassTypeDetailable()
    if l == "selected":
        return ClassTypeSelected()

    raise RMTException(95, "%s:class type invalid '%s'" % (rid, l))
