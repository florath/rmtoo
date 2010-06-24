#
# OutputHandler
#
#  This class coordinates all the different output methods.
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

class OutputHandler:

    def __init__(self, config):
        self.config = config
        self.omods = []
        self.init_output_modules()

    ### Internal Helper Methods

    # Handle the output module loading
    def load_output_module(self, mod_name):
        # Concat the needed names
        o = ["rmtoo", "outputs", mod_name]
        ostr = ".".join(o)
            
        # Load the module
        return __import__(ostr, globals(), locals(), ostr)

    # Load the module and also call the constructor
    def load_output_mod_call_constructor(self, mod_name, params):
        # Load the appropriate module
        output_module = self.load_output_module(mod_name)
        # Call the constructor
        return eval("output_module.%s(%s)" % (mod_name, params))

    # Initializas the list of all needed output modules.
    # The list is given in the configuration file.
    def init_output_modules(self):
        for ok, ov in self.config.output_specs.items():
            # Create the object from the module
            o = self.load_output_mod_call_constructor(ok, ov)
            self.omods.append(o)

    ### Dependency generation

    def create_makefile_dependencies(self, ofile, rc):
        for ok, ov in self.config.output_specs.items():
            # Create the object from the module
            o = self.load_output_mod_call_constructor(ok, ov)
            # Call the cmad method
            o.cmad(rc, ofile)

    ### Output Handling

    # Output the given RequirementsContinuum to all the outputs?
    def output(self, rc):
        for o in self.omods:
            o.output(rc)

