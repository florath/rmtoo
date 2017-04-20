'''
 rmtoo
   Free and Open Source Requirements Management Tool

  InputModules
   This handles all the different input modules.

 (c) 2010-2011,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
import os
import copy

from rmtoo.lib.digraph.StronglyConnectedComponents \
    import strongly_connected_components
from rmtoo.lib.digraph.StronglyConnectedComponents \
    import check_for_strongly_connected_components
from rmtoo.lib.digraph.TopologicalSort \
    import topological_sort
from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.InputModuleTypes import InputModuleTypes


class InputModules(Digraph):
    '''The modules class is also a digraph for the reqdeps modules which
       are the modules which can depend on each other.
       Therefore all the nodes (i.e. modules) must also be stored in the
       Digraph.nodes list.'''

    @staticmethod
    def _split_directory(directory):
        '''Work with directory components: this is used for directory
           access as well as for module name handling.
           The local directory must be handled in a special way
           (because there is no way to ".".join("."))'''
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

    def __init__(self, directory, config,
                 add_dir_components=["rmtoo", "inputs"],
                 mod_components=["rmtoo", "inputs"]):
        '''Read in the modules directory.'''
        Digraph.__init__(self)
        self._config = config
        self.__reqdeps_sorted = None

        # The different types of tags
        self.__tagtypes = {}
        self.__tagtypes[InputModuleTypes.reqtag] = {}
        self.__tagtypes[InputModuleTypes.reqdeps] = {}
        self.__tagtypes[InputModuleTypes.ctstag] = {}
        self.__tagtypes[InputModuleTypes.testcase] = {}

        # Split it up into components
        dir_components = self._split_directory(directory)
        dir_components.extend(add_dir_components)

        self.__load(dir_components, mod_components)

    def __load(self, dir_components, mod_components):
        '''Load the modules.'''
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
            # print("Loading module '%s' from '%s'" %
            #      (modulename, ".".join(mod_components)))
            module = __import__(".".join(mc),
                                globals(), locals(), modulename)

            # Create object from the module
            o = eval("module.%s(self._config)" % modulename)
            # Query the object itself which type it is
            types = o.get_type_set()
            # Add the objects to the appropriate directory
            for ltype in types:
                self.__tagtypes[ltype][modulename] = o
            # If a reqdeps type, put also the in the nodes list.
            if InputModuleTypes.reqdeps in types:
                self.nodes.append(o)

        # Connect the different nodes
        # After his, all the reqdeps modules are a Digraph.
        self.__connect_nodes()
        # Then check, if there are circles in the dependency.
        self.__check_for_circles()
        # And if this succeeds, do the topological sort.
        self.__topological_sort()

    def __connect_nodes(self):
        '''Precondition: the depends_on must be set.
           The method connect all the nodes based on this value.'''
        for mod_name, mod in self.__tagtypes[InputModuleTypes.reqdeps].items():
            for n in mod.depends_on:
                # Connect in both directions
                if n not in self.__tagtypes[InputModuleTypes.reqdeps]:
                    raise RMTException(27, "Module '%s' depends on "
                                       "'%s' - which does not exists"
                                       % (mod_name, n))
                self.create_edge(mod,
                                 self.__tagtypes[InputModuleTypes.reqdeps][n])

    def __check_for_circles(self):
        '''This does check if there is a directed circle (e.g. an strongly
           connected component) in the modules graph.'''
        scc = strongly_connected_components(self)
        if check_for_strongly_connected_components(scc):
            raise RMTException(26, "There is a strongly connected "
                               "component in the modules graph '%s'"
                               % scc)

    def __topological_sort(self):
        '''Do a topological sort on the reqdeps modules.'''
        self.__reqdeps_sorted = topological_sort(self)

    def get_reqdeps_sorted(self):
        '''Return the sorted requirements dependencies.'''
        return self.__reqdeps_sorted

    def get_tagtype(self, imtype):
        '''Return the tags for the given type.'''
        return self.__tagtypes[imtype]
