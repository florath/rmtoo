'''
 rmtoo
   Free and Open Source Requirements Management Tool

 Helper to simply access and handle a hirachical dict.

 (c) 2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from functools import reduce

from rmtoo.lib.configuration.CfgEx import CfgEx


# python 2 and 3 compat hack:
try:
    unicode
except NameError:
    unicode = str


def cfg_key(key):
    """Configuration key handling

    If the key is a string, it is converted to the internally
    used list of strings.
    The original string is split at '.'.
    """
    if type(key) in [bytes, str, unicode]:
        return key.split('.')
    return key


def pop_value(d, key):
    """Get the value of the 'path' and remove it,

    Returns the value of the 'path' if exists - and remove
    this entry from the dict.  If it does not exists, a
    RMTException is raised.
    """


def get_raw(d, key):
    """Returns the value of the given key.

    If the key is not found a CfgEx is raised.
    """
    ckey = cfg_key(key)
    try:
        rval = reduce(dict.get, ckey, d)
    except TypeError:
        # This is raised when dict.get finds a None instead of a dict.
        raise CfgEx("Key [%s] not found" % ckey)

    if rval is None:
        raise CfgEx("Key [%s] not found" % ckey)
    # This is the tricky part: With this construct each
    # sub-configuration is again a configuration.
    return rval


def set_value(d, key, value):
    ckey = cfg_key(key)

    def dict_extend(d, k):
        if k not in d:
            d[k] = {}
        return dict.get(d, k)

    reduce(dict_extend, ckey[:-1], d)[ckey[-1]] = value
