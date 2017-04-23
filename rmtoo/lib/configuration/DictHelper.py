'''
 rmtoo
   Free and Open Source Requirements Management Tool

 Helper to simply access and handle a hirachical dict.

 (c) 2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import print_function

# pylint: disable=W0622
#  This is needed, because in python3 this was moved
#  from internal to the functool
from functools import reduce

from rmtoo.lib.configuration.CfgEx import CfgEx
from rmtoo.lib.Encoding import Encoding


def cfg_key(key):
    """Configuration key handling

    If the key is a string, it is converted to the internally
    used list of strings.
    The original string is split at '.'.
    """
    if isinstance(key, list):
        return key
    if Encoding.is_unicode(key):
        return key.split('.')
    print("Invalid key type [%s]" % type(key))
    assert False


def pop_value(ldict, key):
    """Get the value of the 'path' and remove it,

    Returns the value of the 'path' if exists - and remove
    this entry from the dict.  If it does not exists, a
    RMTException is raised.
    """
    # ToDo: implement
    assert ldict
    assert key
    assert False


def get_raw(ldict, key):
    """Returns the value of the given key.

    If the key is not found a CfgEx is raised.
    """
    ckey = cfg_key(key)
    try:
        rval = reduce(dict.get, ckey, ldict)
    except TypeError:
        # This is raised when dict.get finds a None instead of a dict.
        raise CfgEx("Key [%s] not found" % ckey)

    if rval is None:
        raise CfgEx("Key [%s] not found" % ckey)
    # This is the tricky part: With this construct each
    # sub-configuration is again a configuration.
    return rval


def set_value(ldict, key, value):
    """Sets the value of the hirachical dict"""
    ckey = cfg_key(key)

    def dict_extend(ldict, k):
        """dict.get method that extends the dict hirachy"""
        if k not in ldict:
            ldict[k] = {}
        return dict.get(ldict, k)

    reduce(dict_extend, ckey[:-1], ldict)[ckey[-1]] = value
