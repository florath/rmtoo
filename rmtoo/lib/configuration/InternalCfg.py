'''
 rmtoo
   Free and Open Source Requirements Management Tool

 This file contains the internals handling of the
 configuration classes.

 (c) 2011,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from rmtoo.lib.configuration.CfgEx import CfgEx

# python 2 and 3 compat hack:
try:
    unicode
except NameError:
    unicode = str


class InternalCfg(object):
    '''Internal configuration utility class.'''

    def __init__(self):
        '''Hide utility class constructor.'''
        assert False

    @staticmethod
    def convert_key(key):
        '''If the key is a string, it is converted to the internally
           used list of strings.
           The original string is split at '.'.'''
        if type(key) in [bytes, str, unicode]:
            return InternalCfg.parse_key_string(key)
        return key

    @staticmethod
    def parse_key_string(key):
        '''Parses the given string and splits it up for using with
           the configuration dictionary'''
        return key.split('.')

    @staticmethod
    def get_value(key, ldict):
        '''Returns the key from the given dictionary.
           If this is not the last part of the key, this method
           is called recursively.'''
        assert type(ldict) == dict
        assert len(key) > 0
        if key[0] not in ldict:
            raise CfgEx("(Sub-)Key [%s] not found." % key[0])
        val = ldict[key[0]]
        # No more keys to go for.
        if len(key) == 1:
            return val
        if type(val) != dict:
            raise CfgEx("(Sub-)Type of configuration for key [%s] not a "
                        "dictionary " % key[0])
        return InternalCfg.get_value(key[1:], val)

    @staticmethod
    def change(ldict, key, empty_val, change_func):
        '''Change the given key with the help of the change_func.
           If value does not exists, the empty_val is used for
           initial initialization.'''
        assert type(ldict) == dict
        assert len(key) > 0

        # Only use the given empty value for the last value in the
        # key-chain.  All others must be dictionaries.
        if key[0] not in ldict:
            if len(key) > 1:
                ldict[key[0]] = {}
            else:
                ldict[key[0]] = empty_val

        if len(key) == 1:
            # Really insert the value (if not there).
            change_func(ldict, key[0])
            return

        InternalCfg.change(ldict[key[0]], key[1:], empty_val, change_func)

    @staticmethod
    def set_value(ldict, key, value):
        '''Sets the value for the appropriate key.
           If the key has already a value (i.e. exists)
           a CfgEx is raised.'''
        def assign_value(ldict, key):
            '''Change function for a dictionary.'''
            ldict[key] = value

        InternalCfg.change(ldict, key, None, assign_value)

    @staticmethod
    def append_list(ldict, key, value):
        '''Appends the value to the list at key.
           If key is not available a new list is created.'''
        def append_value(ldict, key):
            '''Change function for a list.'''
            ldict[key].append(value)

        InternalCfg.change(ldict, key, [], append_value)
