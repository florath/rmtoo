'''
 rmtoo
   Free and Open Source Requirements Management Tool

 Configuration Utilities.

 (c) 2011-2012,2017 by flonatel

 For licensing details see COPYING
'''
from six import iteritems


# This is a utility class which includes only one function.
class Utils(object):
    '''Configuration Utilities.
       This class contains functions to work on different
       aspects of the configuration.'''

    def __init__(self):
        '''Hidden constructor.'''
        assert False

    @staticmethod
    def internal_merge_dictionary(orig_dict, new_dict):
        '''Copies all the values from the new_dict into the
           orig_dict.  If a value already exists, it is overwritten.'''
        assert type(orig_dict) == dict
        assert type(new_dict) == dict

        for key, value in iteritems(new_dict):
            if key not in orig_dict:
                orig_dict[key] = value
                continue
            if type(orig_dict[key]) == dict and type(value) == dict:
                Utils.internal_merge_dictionary(orig_dict[key], value)
            else:
                orig_dict[key] = value
