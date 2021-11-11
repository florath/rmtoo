'''
 rmtoo
   Free and Open Source Requirements Management Tool

 The Configuration Class hold values from the different configuration
 sources, i.e. configuration class, JSON configuration objects and the
 command line.

 (c) 2011-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import print_function

from abc import ABCMeta, abstractmethod
import os
import json
from six import iteritems
import yaml

import rmtoo.lib.configuration.DictHelper as DictHelper
from rmtoo.lib.Encoding import Encoding
from rmtoo.lib.configuration.CfgEx import CfgEx
from rmtoo.lib.configuration.CmdLineParams import CmdLineParams
from rmtoo.lib.RMTException import RMTException


class CfgFormatBase:
    """Common base class for format configuration objects"""

    __metaclass__ = ABCMeta

    def __init__(self, cfg, name):
        """Set up a CfgFormatJson object"""
        self.__cfg = cfg
        self.__name = name

    @abstractmethod
    def create_cfg_from_str(self, url):
        """Create configuration from given string"""
        return

    @abstractmethod
    def create_cfg_from_file(self, url):
        """Create configuration from given file"""
        return

    def __create_cfg_from_url(self, url):
        '''Depending on the URL the low level method to
           create the configuration is called.'''
        if url.startswith(self.__name + ":"):
            return self.create_cfg_from_str(url)
        elif url.startswith("file:"):
            return self.create_cfg_from_file(url)
        assert False

    def __evaluate_once(self, config):
        """Evaluates the given configuration and returns it"""
        cfg = {}
        for cfg_idx in config:
            DictHelper.merge(cfg, self.__create_cfg_from_url(cfg_idx))
        return cfg

    def evaluate(self):
        """As long as there are parameters, handle them."""
        try:
            while True:
                config = self.__cfg.get_value(
                    ['configuration', self.__name])
                # This must be removed before the evaluation, because it
                # is possible that during the evaluation additional
                # entries will appear.
                del self.__cfg['configuration'][self.__name]
                DictHelper.merge(self.__cfg, self.__evaluate_once(config))
        except RMTException:
            # Nothing to do: entries not available
            pass


class CfgFormatJson(CfgFormatBase):
    """Handles configuration written in JSON"""

    def create_cfg_from_str(self, url):
        """Create config from JSON string"""
        if url.startswith("json:"):
            url = url[5:]
        jdict = json.loads(url)
        if not isinstance(jdict, dict):
            raise CfgEx("Given JSON string encodes no dictionary.")
        return jdict

    def create_cfg_from_file(self, url):
        """Creates dict from JSON file"""
        if url.startswith("file://"):
            url = url[7:]
        with open(url, "r") as jfd:
            jdict = json.load(jfd)
        if not isinstance(jdict, dict):
            raise CfgEx("Given JSON string encodes no dictionary.")
        return jdict


def custom_str_constructor(loader, node):
    """This takes care that all the configuration is read in
    using unicode.
    """
    return Encoding.to_unicode(loader.construct_scalar(node))


yaml.SafeLoader.add_constructor(
    u'tag:yaml.org,2002:str', custom_str_constructor)


class CfgFormatYaml(CfgFormatBase):
    """Handles configuration written in YAML"""

    def create_cfg_from_str(self, url):
        """Create config from YAML string"""
        if url.startswith("yaml:"):
            url = url[5:]
        ydict = yaml.safe_load(url)
        if not isinstance(ydict, dict):
            raise CfgEx("Given YAML string encodes no dictionary.")
        return ydict

    def create_cfg_from_file(self, url):
        """Creates dict from YAML file"""
        if url.startswith("file://"):
            url = url[7:]
        with open(url, "r") as yfd:
            ydict = yaml.safe_load(yfd)
        if not isinstance(ydict, dict):
            raise CfgEx("Given YAML string encodes no dictionary.")
        return ydict


class Cfg(dict):
    '''
    Configuration Class

    Stores all the values from different sources into one data container
    which is a dictionary.

    Each part of a Cfg is again a Cfg - except the last step where it is
    a value.

    Has some special access methods like get_value("key.subkey.subsubkey")
    to simplify configuration access.
    '''

    @staticmethod
    def new_by_json_str(jstr):
        """Creates a new Cfg object with the contents of the given
        string.  The string must be a valid JSON structure.
        This is a static factory method.
        """
        config = Cfg()
        cfg_format = CfgFormatJson(config, 'json')
        DictHelper.merge(config, cfg_format.create_cfg_from_str(jstr))
        return config

    def merge_json_str(self, jstr):
        """Merges a JSON config into an already existing"""
        cfg_format = CfgFormatJson(self, 'json')
        DictHelper.merge(self, cfg_format.create_cfg_from_str(jstr))

    def merge_cmd_line_params(self, args):
        '''Merges the command line arguments into the
           existing configuration.'''
        ldicts = CmdLineParams.create_dicts(args)
        for ldict in ldicts:
            DictHelper.merge(self, ldict)

    def evaluate(self):
        """Evaluates the configuration.

        This does two things: read in the different configurations
        of different formats and merges them into one big configuration
        object.
        """
        cfgs = {'json': CfgFormatJson(self, 'json'),
                'yaml': CfgFormatYaml(self, 'yaml')}
        for _, cfg_obj in iteritems(cfgs):
            cfg_obj.evaluate()

    def get_value(self, key):
        '''Returns the value of the given key.
           If key is not found a RMTException is thrown.'''
        try:
            rval = DictHelper.get_raw(self, key)
            if isinstance(rval, dict):
                return Cfg(rval)
            return rval
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
        if Encoding.is_unicode(value):
            return self.__dollar_replace_string(value)
        if isinstance(value, list):
            return self.__dollar_replace_list(value)
        # Never reached: unknown type
        print("Cfg never reached [%s] [%s]" % (type(value), value))
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
            return self.dollar_replace(DictHelper.get_raw(self, key))
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
            return DictHelper.get_raw(self, key)
        except CfgEx:
            return default_value

    def set_value(self, key, value):
        '''Sets the value. If the key is already there a CfgEx is
           raised.'''
        ckey = DictHelper.cfg_key(key)
        DictHelper.set_value(self, ckey, value)

#    def append_list(self, key, value):
#        '''Appends value to existing list under key.
#           If key does not exists, a new list is created.'''
#        key = InternalCfg.convert_key(key)
#        InternalCfg.append_list(self.config, key, value)

    def get_bool(self, key, default_value):
        '''Returns the value of the key - converted to a boolean.
           If key does not exists, the default value is returned.'''
        try:
            return DictHelper.get_raw(self, key) \
                in ['True', 'true', 'on', '1',
                    'Yes', 'yes', True]
        except CfgEx:
            return default_value

    def get_integer(self, key, default_value):
        '''Returns the value of the key - converted to an integer.
           If key does not exists, the default value is returned.'''
        try:
            return int(DictHelper.get_raw(self, key))
        except CfgEx:
            return default_value

    def is_available(self, key):
        '''Returns true if the given key is available in the configuration
        and the valus is not None.'''
        return self.get_value_wo_throw(key) is not None
