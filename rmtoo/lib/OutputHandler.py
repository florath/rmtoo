#
# OutputHandler
#
#  This class coordinates all the different output methods.
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

# TODO: This class is deprecated and must be removed.
# It is replaced by the TopicOutputHandler which is a sub-object
# of Topic.

class OutputHandler:

    def __init__(self, config, topics):
        assert(False)
        self.config = config
        self.topics = topics
        self.omods = []
        self.init_output_modules()

    ### Internal Helper Methods

    # Handle the output module loading
    def load_output_module(self, mod_name):
        assert(False)
        # Concat the needed names
        o = ["rmtoo", "outputs", mod_name]
        ostr = ".".join(o)

        # Load the module
        return __import__(ostr, globals(), locals(), ostr)

    # Load the module and also call the constructor
    def load_output_mod_call_constructor(self, mod_name, params):
        assert(False)
        # Load the appropriate module
        output_module = self.load_output_module(mod_name)
        # Call the constructor
        obj = eval("output_module.%s(%s)"
                   % (mod_name, params))
        obj.set_topics(self.topics)
        return obj

    # Initializas the list of all needed output modules.
    # The list is given in the configuration file.
    def init_output_modules(self):
        assert(False)
        for ok, ov in self.config.output_specs:
            # Create the object from the module
            o = self.load_output_mod_call_constructor(ok, ov)
            self.omods.append(o)

    ### Dependency generation

    def create_makefile_dependencies(self, ofile, rc):
        assert(False)
        for ok, ov in self.config.output_specs:
            # Create the object from the module
            o = self.load_output_mod_call_constructor(ok, ov)
            # Call the cmad method
            o.cmad(rc, ofile)

    ### Output Handling

    # Output the given RequirementsContinuum to all the outputs?
    def output(self, rc):
        assert(False)
        for o in self.omods:
            o.output(rc)

