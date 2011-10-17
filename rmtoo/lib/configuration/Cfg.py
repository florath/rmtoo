'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
 The Configuration Class hold values from the different configuration
 sources, i.e. configuration class, JSON configuration objects and the
 command line.
 
 History: this is a new implementation of the old Configuration 
 and command line parameter handling. 
   
 (c) 2011 by flonatel GmhH & Co. KG

 For licensing details see COPYING
'''
import json

from types import StringType, DictType
from rmtoo.lib.configuration.CfgEx import CfgEx
from rmtoo.lib.configuration.CmdLineParams import CmdLineParams
from rmtoo.lib.configuration.Utils import Utils

class Cfg:
    '''
    Configuration Class

    Stores all the values from different sources into one data container
    which is a dictionary.

    Has some special access methods like get_value("key.subkey.subsubkey")
    to simplify configuration access.
    '''

    def __init__(self):
        '''Constructs an empty configuration
           This can be filled later on with the different merge
           methods.'''
        self.config = {}

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
        print("STR [%s]" % jstr)
        jdict = json.loads(jstr)
        if type(jdict) != DictType:
            raise CfgEx("Given JSON string encodes no dictionary.")
        self.merge_dictionary(jdict)

    def merge_json_file(self, jfile):
        '''Adds all the values from the given JSON file to
           the existing configuration.'''
        if jfile.startswith("file://"):
            jfile = jfile[7:]
        jfd = file(jfile, "r")
        jdict = json.load(jfd)
        jfd.close()
        if type(jdict) != DictType:
            raise CfgEx("Given JSON string encodes no dictionary.")
        self.merge_dictionary(jdict)

    def merge_dictionary(self, ldict):
        '''Merges the contents of the local dictionary into the 
           existing one.
           If a value already exists, it is overwritten'''
        Utils.internal_merge_dictionary(self.config, ldict)

    def merge_cmd_line_params(self, args):
        '''Merges the command line arguments into the 
           existing configuration.'''
        ldicts = CmdLineParams.create_dicts(args)
        for ldict in ldicts:
            self.merge_dictionary(ldict)

    def internal_merge_json_url(self, json_url):
        '''Depending on the JSON URL the low level method to
           merge the configuration is called.'''
        if json_url.startswith("json:"):
            self.merge_json_str(json_url)
        elif json_url.startswith("file:"):
            self.merge_json_file(json_url)

    def internal_evaluate_json_once(self, json_config):
        '''Evaluates the given json configuration and merges it
           into the current configuration.'''
        for jcfg in json_config:
            self.internal_merge_json_url(jcfg)

    def internal_evaluate_json(self):
        '''As long as there are JSON parameters, handle them.'''
        try:
            while True:
                json_config = self.get_value(['configuration', 'json'])
                # This must be removed before the evaluation, because it
                # is possible that during the evaluation additional
                # entries will appear.
                del(self.config['configuration']['json'])
                self.internal_evaluate_json_once(json_config)
        except CfgEx, cfgex:
            # Nothing to do: JSON entries not available
            pass

    def evaluate(self):
        '''Evaluates the configuration.
           This does two things:
           o Read in the 'old' configuration
           o Read in the new configuration'''
        self.internal_evaluate_json()
        # assert(False)
        # TODO: evaluate old style config missing

    @staticmethod
    def internal_parse_key_string(key):
        '''Parses the given string and splits it up for using with
           the configuration dictionary'''
        return key.split('.')

    @staticmethod
    def internal_get_value(key, ldict):
        '''Returns the key from the given dictionary.
           If this is not the last part of the key, this method
           is called recursively.'''
        assert(type(ldict) == DictType)
        assert(len(key) > 0)
        if key[0] not in ldict:
            raise CfgEx("(Sub-)Key [%s] not found." % key[0])
        val = ldict[key[0]]
        # No more keys to go for.
        if len(key) == 1:
            return val
        if type(val) != DictType:
            raise CfgEx("(Sub-)Type of configuration for key [%s] not a "
                        "dictionary " % key[0])
        return Cfg.internal_get_value(key[1:], val)

    def get_value(self, key):
        '''Returns the value of the given key.
           If key is not found a CfgEx is thrown.'''
        # If the type is a string, this must first be parsed.
        if type(key) == StringType:
            key = self.internal_parse_key_string(key)
        return Cfg.internal_get_value(key, self.config)
