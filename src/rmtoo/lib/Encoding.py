'''
 rmtoo
   Free and Open Source Requirements Management Tool

 Helper class for Encoding - supports python 2 and 3

 (c) 2017 by flonatel

 For licensing details see COPYING
'''
from __future__ import print_function

import sys


class Encoding(object):
    """Collection of functions for encoding

    This class is a compatibility python 2 and 3 class.
    It encapsulates for other classes the different
    handling of 'str' and 'unicode'.
    """

    @staticmethod
    def is_unicode(obj):
        """Returns is obj is unicode string.

        Depending on the python version this is either 'unicode'
        or 'str'.
        """
        if obj is None:
            return False
        if sys.version_info[0] == 2:
            # The noqa is needed to get pep8 run on python3
            return isinstance(obj, unicode)  # noqa: F821
        if sys.version_info[0] == 3:
            return isinstance(obj, str)
        assert False

    @staticmethod
    def check_unicode(string):
        """Checks is string is unicode - bails out if not"""
        if string is None:
            return
        if isinstance(string, (list, dict)):
            print("+++ ERROR: Must be a string not a [%s]" % type(string))
            assert False
        if not Encoding.is_unicode(string):
            print("+++ ERROR: String [%s] must be unicode" % string)
            assert False
        return

    @staticmethod
    def check_unicode_list(lst):
        """Check if given list is a list of unicode strings"""
        if not isinstance(lst, list):
            print("+++ ERROR: Must be a list not a [%s]" % type(lst))
            assert False
        for string in lst:
            Encoding.check_unicode(string)

    @staticmethod
    def to_unicode(string):
        """Convert string to unicode"""
        if sys.version_info[0] == 2:
            # The noqa is needed to get pep8 run on python3
            return unicode(string)  # noqa: F821
        if sys.version_info[0] == 3:
            return str(string)
        assert False
