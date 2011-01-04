#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# This class defines a method to set configuration parameters (which
# might be not available) to their default values.  This is seen as
# the better way than every class implements it's own default parameter
# handling:
# o This is a central place: when a default changes it must change
#   here.
# o No need to do the handling of one parameter at some places.
# o Simpler and shorter program code: the parameters are 'just'
#   there. 
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.RMTException import RMTException

class ConfigUtils:

    @staticmethod
    def set_defaults_reqs_spec(config):
        # When there is no reqs_spec - add one
        if not hasattr(config, "reqs_spec"):
            config.reqs_spec = {}
        # The dependency notation is by default the (old) Depends on
        # notation. 
        if "dependency_notation" not in config.reqs_spec:
            config.reqs_spec["dependency_notation"] = set(["Depends on",] )

    @staticmethod
    def set_defaults_parser_generic(config):
        # When there is no parser entry add one
        if not hasattr(config, "parser"):
            config.parser = {}

    @staticmethod
    def set_defaults_parser_name(config, name):
        if name not in config.parser:
            config.parser[name] = {}
        # The max line length must be configurable
        if "max_line_length" not in config.parser[name]:
            config.parser[name]["max_line_length"] = 80

    @staticmethod
    def set_defaults_parser(config):
        ConfigUtils.set_defaults_parser_generic(config)
        ConfigUtils.set_defaults_parser_name(config, "requirements")
        ConfigUtils.set_defaults_parser_name(config, "topics")

    @staticmethod
    def set_defaults(config):
        ConfigUtils.set_defaults_reqs_spec(config)
        ConfigUtils.set_defaults_parser(config)


    #####

    @staticmethod
    def check_reqs_spec(config):
        allowed = set(["Depends on", "Solved by"])
        set_diff = config.reqs_spec["dependency_notation"].difference(
            allowed)
        if len(set_diff)>0:
            raise RMTException(70, "Invalid value in "
                               "'dependency_notation': "
                               "should be one of '%s' - but was '%s'"
                               % (allowed, set_diff))

    @staticmethod
    def check_parser_name(config, name):
        v = config.parser[name]["max_line_length"]
        if not isinstance(v, int):
            raise RMTException(71, "Config.parser['%s']['max_line_length'] is "
                               "not an integer - wich should be; type is [%s]"
                               % (name, type(v).__name__))
        if v<0:
            raise RMTException(72, "Config.parser['max_line_length'] is "
                               "negative [%s]" % v)

    @staticmethod
    def check_parser(config):
        ConfigUtils.check_parser_name(config, "requirements")
        ConfigUtils.check_parser_name(config, "topics")

    @staticmethod
    def check(config):
        ConfigUtils.check_reqs_spec(config)
        ConfigUtils.check_parser(config)
