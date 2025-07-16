'''
 rmtoo
   Free and Open Source Requirements Management Tool

 Command line parameter handling.

 (c) 2011, 2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import argparse
import distutils.sysconfig

from rmtoo.lib.Encoding import Encoding


class CmdLineParams(object):
    '''Utility class for handling the old style command line
       parameters (like -f, -m and -c) as well as the new
       command line parameters.'''

    def __init__(self):
        '''Utility class with 'hidden' constructor'''
        assert False

    @staticmethod
    def initialize_parser():
        '''Initializases the command line parser.'''
        return argparse.ArgumentParser()

    @staticmethod
    def add_deprecated_parameters(parser):
        '''Add the deprecated parameters to the given option parser.'''
        parser.add_argument("-f", "--file-config", dest="config_file",
                            help="Configuration file")
        parser.add_argument("-m", "--modules-directory",
                            dest="modules_directory",
                            help="Directory with modules")
        parser.add_argument("-c", "--create-makefile-dependencies",
                            dest="create_makefile_dependencies",
                            help="Create makefile dependencies")

    @staticmethod
    def add_deprecated_values(options):
        '''Add all the values to the dictionary which were specified
           with the help of the old and deprecated command line options.'''
        ldict = {}

        if options.config_file is not None:
            ldict['configuration'] \
                = {'deprecated':
                   {'config_file': Encoding.to_unicode(options.config_file)}}

        if options.modules_directory is not None:
            ldict['global'] \
                = {'modules': {'directories':
                               [Encoding.to_unicode(
                                   options.modules_directory)]}}
        else:
            # If there is no modules directory given, use the pyshared one.
            mod_dir = distutils.sysconfig.get_python_lib()
            ldict['global'] = {'modules':
                               {'directories':
                                [Encoding.to_unicode(mod_dir)]}}

        if options.create_makefile_dependencies is not None:
            ldict['actions'] \
                = {'create_makefile_dependencies':
                   Encoding.to_unicode(options.create_makefile_dependencies)}

        # Handle new logging options
        if hasattr(options, 'verbose') and options.verbose:
            if 'global' not in ldict:
                ldict['global'] = {}
            if 'logging' not in ldict['global']:
                ldict['global']['logging'] = {}
            ldict['global']['logging']['verbose'] = True

        if hasattr(options, 'logfile') and options.logfile is not None:
            if 'global' not in ldict:
                ldict['global'] = {}
            if 'logging' not in ldict['global']:
                ldict['global']['logging'] = {}
            ldict['global']['logging']['logfile'] = \
                Encoding.to_unicode(options.logfile)

        if hasattr(options, 'log_level') and options.log_level is not None:
            if 'global' not in ldict:
                ldict['global'] = {}
            if 'logging' not in ldict['global']:
                ldict['global']['logging'] = {}
            ldict['global']['logging']['log_level'] = options.log_level

        return ldict

    @staticmethod
    def add_parameters(parser):
        '''Add the command line parameters to the given parser.'''
        parser.add_argument(
            "-j", "--json", dest="json",
            action="append",
            help="JSON string or file which is merged into the "
            "existing configuration. Can be specified multiple "
            "times.")
        parser.add_argument(
            "-y", "--yaml", dest="yaml",
            action="append",
            help="YAML string or file which is merged into the "
            "existing configuration. Can be specified multiple "
            "times.")
        parser.add_argument(
            "-v", "--verbose", dest="verbose",
            action="store_true",
            help="Enable verbose logging to stdout/stderr")
        parser.add_argument(
            "--logfile", dest="logfile",
            help="Log to specified file instead of default location")
        parser.add_argument(
            "--log-level", dest="log_level",
            choices=["DEBUG", "INFO", "WARN", "ERROR", "CRITICAL"],
            default="INFO",
            help="Set logging level (default: INFO)")

    @staticmethod
    def add_values(soptions, name):
        '''Add all the new command line parameter values.'''
        if soptions is None:
            return {}

        opts = []
        for opt in soptions:
            uopt = Encoding.to_unicode(opt)
            if uopt.startswith("file://") or uopt.startswith(name + ":"):
                opts.append(uopt)
            else:
                opts.append(name + ":" + uopt)
        return {'configuration': {name: opts}}

    @staticmethod
    def add_args(args):
        '''Add the arguments to the configuration.'''
        if args is None or args == []:
            return {}
        return {'general': {'command_line_arguments': args}}

    @staticmethod
    def create_dicts(args):
        '''Creates a dictionary from all the command line parameters.'''
        parser = CmdLineParams.initialize_parser()
        CmdLineParams.add_deprecated_parameters(parser)
        CmdLineParams.add_parameters(parser)

        args = parser.parse_args(args=args)

        lresult = []
        lresult.append(CmdLineParams.add_args(args))
        lresult.append(CmdLineParams.add_deprecated_values(args))
        lresult.append(CmdLineParams.add_values(args.json, "json"))
        lresult.append(CmdLineParams.add_values(args.yaml, "yaml"))
        return lresult
