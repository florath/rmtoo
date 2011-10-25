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
import copy

from rmtoo.lib.digraph.StronglyConnectedComponents \
    import strongly_connected_components
from rmtoo.lib.digraph.StronglyConnectedComponents \
    import check_for_strongly_connected_components
from rmtoo.lib.digraph.TopologicalSort \
    import topological_sort
from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.RMTException import RMTException

#
# The modules class is also a digraph for the reqdeps modules which
# are the modules which can depend on each other.
# Therefore all the nodes (i.e. modules) must also be stored in the
# Digraph.nodes list.
#
class Modules(Digraph):

    @staticmethod
    def split_directory(directory):
        # Work with directory components: this is used for directory
        # access as well as for module name handling.
        # The local directory must be handled in a special way
        # (because there is no way to ".".join("."))
        if directory == ".":
            dir_components = []
        else:
            dir_components = directory.split("/")
            # When using an absolute path, the first component is
            # empty though! Remove this and prepend a / for the next
            # one. 
            if len(dir_components) > 0 and dir_components[0] == "":
                dir_components[0] = "/"
        return dir_components

    # Read in the modules directory
    def __init__(self, directory, config,
                 add_dir_components=["rmtoo", "modules"],
                 mod_components=["rmtoo", "modules"]):
        Digraph.__init__(self)
        self.config = config

        # The different types of tags
        self.tagtypes = {}
        self.tagtypes["reqtag"] = {}
        self.tagtypes["reqdeps"] = {}
        self.tagtypes["ctstag"] = {}

        # Split it up into components
        dir_components = self.split_directory(directory)
        dir_components.extend(add_dir_components)

        self.load(dir_components, mod_components)

    def load(self, dir_components, mod_components):
        for filename in sorted(os.listdir(os.path.join(*dir_components))):
            if not filename.endswith(".py"):
                continue
            modulename = filename[:-3]

            # Skip __init__.py
            if modulename == "__init__":
                continue

            # Because the mod_components can be empty, before using
            # the mod_components append the modulename to the list.
            # This must be done on a copy of the original list.
            mc = copy.deepcopy(mod_components)
            mc.append(modulename)

            # Import module
            #print("Loading module '%s' from '%s'" %
            #      (modulename, ".".join(mod_components)))
            module = __import__(".".join(mc),
                                globals(), locals(), modulename)

            # Create object from the module
            o = eval("module.%s(self.config)" % modulename)
            # Query the object itself which type it is
            types = o.type()
            # Add the objects to the appropriate directory
            for ltype in types:
                self.tagtypes[ltype][modulename] = o
            # If a reqdeps type, put also the in the nodes list.
            if "reqdeps" in types:
                self.nodes.append(o)

        # Not sure, if this is really needed.
#        print("***** NEEDED?????????")        
#        for rd in self.reqdeps:
#            self.reqdeps[rd].set_modules(self)

        # Connect the different nodes
        # After his, all the reqdeps modules are a Digraph.
        self.connect_nodes()
        # Then check, if there are circles in the dependency.
        self.check_for_circles()
        # And if this succeeds, do the topological sort.
        self.topological_sort()

    # Precondition: the depends_on must be set.
    # The method connect all the nodes based on this value.
    def connect_nodes(self):
        for mod_name, mod in self.tagtypes["reqdeps"].items():
            for n in mod.depends_on:
                # Connect in both directions
                if n not in self.tagtypes["reqdeps"]:
                    raise RMTException(27, "Module '%s' depends on "
                                       "'%s' - which does not exists"
                                       % (mod_name, n))
                self.create_edge(mod, self.tagtypes["reqdeps"][n])

    # This does check if there is a directed circle (e.g. an strongly
    # connected component) in the modules graph.
    def check_for_circles(self):
        scc = strongly_connected_components(self)
        if check_for_strongly_connected_components(scc):
            raise RMTException(26, "There is a strongly connected "
                               "component in the modules graph '%s'"
                               % scc)

    def topological_sort(self):
        # Do a topoligical sort on the reqdeps modules.
        self.reqdeps_sorted = topological_sort(self)
