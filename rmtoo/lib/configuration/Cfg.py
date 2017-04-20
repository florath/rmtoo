'''
 rmtoo
   Free and Open Source Requirements Management Tool

 The Configuration Class hold values from the different configuration
 sources, i.e. configuration class, JSON configuration objects and the
 command line.

 (c) 2011-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
import os
import json

from rmtoo.lib.configuration.CfgEx import CfgEx
from rmtoo.lib.configuration.CmdLineParams import CmdLineParams
from rmtoo.lib.configuration.Utils import Utils
from rmtoo.lib.configuration.InternalCfg import InternalCfg
from rmtoo.lib.RMTException import RMTException


# python 2 and 3 compat hack:
try:
    unicode
except NameError:
    unicode = str


class Cfg(object):
    '''
    Configuration Class

    Stores all the values from different sources into one data container
    which is a dictionary.

    Each part of a Cfg is again a Cfg - except the last step where it is
    a value.

    Has some special access methods like get_value("key.subkey.subsubkey")
    to simplify configuration access.
    '''

    def __init__(self, initial_values=None):
        '''Constructs an empty configuration
           This can be filled later on with the different merge
           methods.'''
        self.config = {}
        if initial_values is not None:
            self.__init_initial_values(initial_values)

    def __init_initial_values(self, initial_values):
        '''Initializes the initial values.
           Depending on the type of the given value, the initial
           values are set.'''
        if type(initial_values) == dict:
            self.__merge_dictionary(initial_values)
            return
        if isinstance(initial_values, Cfg):
            self.config = initial_values.get_dict()
            return
        assert(False)

    @staticmethod
    def new_by_json_str(jstr):
        '''Creates a new Cfg object with the contents of the given
           string.  The string must be a valid JSON structure.
           This is a static factory method.'''
        config = Cfg()
        config.merge_json_str(jstr)
        return config

    def merge_json_str(self, jstr):
        '''Adds all the values from the given JSON string to
           the existing configuration.'''
        if jstr.startswith("json:"):
            jstr = jstr[5:]
        jdict = json.loads(jstr)
        if type(jdict) != dict:
            raise CfgEx("Given JSON string encodes no dictionary.")
        self.__merge_dictionary(jdict)

    def __merge_json_file(self, jfile):
        '''Adds all the values from the given JSON file to
           the existing configuration.'''
        if jfile.startswith("file://"):
            jfile = jfile[7:]
        with open(jfile, "r") as jfd:
            jdict = json.load(jfd)
        if type(jdict) != dict:
            raise CfgEx("Given JSON string encodes no dictionary.")
        self.__merge_dictionary(jdict)

    def __merge_dictionary(self, ldict):
        '''Merges the contents of the local dictionary into the
           existing one.
           If a value already exists, it is overwritten'''
        Utils.internal_merge_dictionary(self.config, ldict)

    def merge_cmd_line_params(self, args):
        '''Merges the command line arguments into the
           existing configuration.'''
        ldicts = CmdLineParams.create_dicts(args)
        for ldict in ldicts:
            self.__merge_dictionary(ldict)

    def __merge_json_url(self, json_url):
        '''Depending on the JSON URL the low level method to
           merge the configuration is called.'''
        if json_url.startswith("json:"):
            self.merge_json_str(json_url)
        elif json_url.startswith("file:"):
            self.__merge_json_file(json_url)

    def __evaluate_json_once(self, json_config):
        '''Evaluates the given json configuration and merges it
           into the current configuration.'''
        for jcfg in json_config:
            self.__merge_json_url(jcfg)

    def __evaluate_json(self):
        '''As long as there are JSON parameters, handle them.'''
        try:
            while True:
                json_config = self.get_value(['configuration', 'json'])
                # This must be removed before the evaluation, because it
                # is possible that during the evaluation additional
                # entries will appear.
                del(self.config['configuration']['json'])
                self.__evaluate_json_once(json_config)
        except RMTException:
            # Nothing to do: JSON entries not available
            pass

    def evaluate(self):
        '''Evaluates the configuration.
           This does two things:
           o Read in the new configuration'''
        self.__evaluate_json()

    def get_raw(self, key):
        '''Returns the value of the given key.
           If the key is not found a CfgEx is raised.'''
        key = InternalCfg.convert_key(key)
        rval = InternalCfg.get_value(key, self.config)
        # This is the tricky part: With this construct each
        # sub-configuration is again a configuration.
        if type(rval) == dict:
            return Cfg(rval)
        return rval

    def get_value(self, key):
        '''Returns the value of the given key.
           If key is not found a RMTException is thrown.'''
        try:
            return self.get_raw(key)
        except CfgEx as cex:
            raise RMTException(96, "Mandatory configuration parameter "
                               "[%s] not found. (Root cause: [%s])"
                               % (key, cex))

    @staticmethod
    def __replace_env(estr):
        '''Resolves the environment variable and returns it.'''
        try:
            return os.environ[estr]
        except KeyError:
            # If not there, use original string.
            return estr

    def __replace_key(self, key):
        '''Resolves the key and returns is.'''
        return self.get_value(key)

    def __replace(self, cstr):
        '''Looks if the given string exists as variable.
           If so, returns the resolved string.'''
        if cstr.startswith("ENV:"):
            return self.__replace_env(cstr[4:])
        return self.__replace_key(cstr)

    def __dollar_replace_string(self, cstr):
        '''Replaces all occurrences of ${} with the appropriate value.'''
        while True:
            dstart = cstr.find("${")
            if dstart == -1:
                # No ${} any more...
                return cstr
            dend = cstr.find("}", dstart + 2)
            if dend == -1:
                # No }: no way to replace things
                return cstr
            vname = cstr[dstart + 2:dend]
            rep = self.__replace(vname)
            cstr = cstr[:dstart] + rep + cstr[dend + 1:]

    def __dollar_replace_list(self, value):
        '''Replaces all occurrences of ${} for list.'''
        res = []
        for vstr in value:
            res.append(self.__dollar_replace_string(vstr))
        return res

    def dollar_replace(self, value):
        '''Replaces all occurrences of ${} for different types.'''
        if type(value) in [bytes, str, unicode]:
            return self.__dollar_replace_string(value)
        if type(value) == list:
            return self.__dollar_replace_list(value)
        # Never reached: unknown type
        print("Never reached: [%s]" % type(value))
        assert False

    def get_rvalue(self, key):
        '''Returns the real value of the given key.
           If found the value is interpreted as string -
           and the ${} replacement takes place.
           If key is not found a RMTException is thrown.'''
        return self.dollar_replace(self.get_value(key))

    def get_rvalue_default(self, key, default_value):
        '''Return the value of the key from the configuration.
           Replacement of ${} is done, if the key is available,
           If the key is not available, the default_value is returned.'''
        try:
            return self.dollar_replace(self.get_raw(key))
        except CfgEx:
            return default_value

    def get_value_wo_throw(self, key):
        '''Returns the value of the given key.
           If key is not found None is returned.'''
        return self.get_value_default(key, None)

    def get_value_default(self, key, default_value):
        '''Return the value of the key from the configuration.
           If the key is not available, the default_value is returned.'''
        try:
            return self.get_raw(key)
        except CfgEx:
            return default_value

    def set_value(self, key, value):
        '''Sets the value. If the key is already there a CfgEx is
           raised.'''
        key = InternalCfg.convert_key(key)
        InternalCfg.set_value(self.config, key, value)

    def append_list(self, key, value):
        '''Appends value to existing list under key.
           If key does not exists, a new list is created.'''
        key = InternalCfg.convert_key(key)
        InternalCfg.append_list(self.config, key, value)

    def get_dict(self):
        '''Returns the dictionary which holds all the values.
           This is needed for the usage of handling easy access
           to the configuration parameters.
           You should really knowing what you are doing when using
           this method.'''
        return self.config

    def get_bool(self, key, default_value):
        '''Returns the value of the key - converted to a boolean.
           If key does not exists, the default value is returned.'''
        try:
            return self.get_raw(key) in ['True', 'true', 'on', '1',
                                         'Yes', 'yes', True]
        except CfgEx:
            return default_value

    def get_integer(self, key, default_value):
        '''Returns the value of the key - converted to an integer.
           If key does not exists, the default value is returned.'''
        try:
            return int(self.get_raw(key))
        except CfgEx:
            return default_value

    def is_available(self, key):
        '''Returns true if the given key is available in the configuration.'''
        return self.get_value_wo_throw(key) is not None
