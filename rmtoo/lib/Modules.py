#
# Requirement Management Toolset
#  class Modules
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

import os
import re

class Modules:
    # Read in the modules directory
    def __init__(self, directory, opts, config):
        self.opts = opts
        self.config = config

        # The different types of tags
        self.reqtag = {}

        self.load(directory)

    def load(self, directory):
        for filename in os.listdir(os.path.join(
                 directory, "rmtoo", "modules")):
            if not filename.endswith(".py"):
                continue
            modulename = filename[:-3]

            # Skip __init__.py
            if modulename == "__init__":
                continue

            # Import module
            print("Importing module '%s'" % modulename)
            module = __import__("rmtoo.modules.%s" % modulename,
                                globals(), locals(), modulename)

            # Create object from the module
            o = eval("module.%s(self.opts, self.config)" % modulename)
            # Query the object itself which type it is
            tag = o.type()
            # Add the object to the appropriate directory
            exec("self.%s[modulename]=o" % tag)



