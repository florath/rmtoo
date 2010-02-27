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

from rmtoo.lib.TopologicalSort import topological_sort

class Modules:
    # Read in the modules directory
    def __init__(self, directory, opts, config):
        self.opts = opts
        self.config = config

        # The different types of tags
        self.reqtag = {}
        self.reqdeps = {}

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
            #print("Importing module '%s'" % modulename)
            module = __import__("rmtoo.modules.%s" % modulename,
                                globals(), locals(), modulename)

            # Create object from the module
            o = eval("module.%s(self.opts, self.config)" % modulename)
            # Query the object itself which type it is
            tag = o.type()
            # Add the object to the appropriate directory
            exec("self.%s[modulename]=o" % tag)

        # Not sure, if this is really needed.
        for rd in self.reqdeps:
            self.reqdeps[rd].set_modules(self)

        # Do a topoligical search on the reqdeps modules.
        # Therefore create a dictionary with {'name': ['list', 'of', 'deps']}
        graph = {}
        for k, v in self.reqdeps.items():
            # Fill in the depencencies
            graph[k] = v.depends_on
        # Do the sort
        tsorted_graph = topological_sort(graph)
        # Note that the things where everything depends on is at the
        # end; therefore it must be reversed.
        tsorted_graph.reverse()
        self.reqdeps_sorted = tsorted_graph
