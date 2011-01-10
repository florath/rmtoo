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
from rmtoo.lib.storagebackend.txtfile.TxtIOConfig import TxtIOConfig

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
    def set_defaults_parser_name(config, name):
        if name not in config.parser:
            config.parser[name] = {}
        # The max line length must be configurable
        if "max_line_length" not in config.parser[name]:
            config.parser[name]["max_line_length"] = 80

    @staticmethod
    def use_or_empty(c, n):
        if not hasattr(c, "parser"):
            return {}
        if n in c.parser:
            return c.parser[n]
        return {}

    @staticmethod
    def set_defaults_parser(config):
        config.txtio = {
            "requirements": TxtIOConfig(
                ConfigUtils.use_or_empty(config, "requirements")),
            "topics": TxtIOConfig(
                ConfigUtils.use_or_empty(config, "topics")), }
        # Remove the used things (to be sure that all use the same config)
        if hasattr(config, "parser"):
            del(config.parser)

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
    def check(config):
        ConfigUtils.check_reqs_spec(config)
        # Parser check is done while initialization
