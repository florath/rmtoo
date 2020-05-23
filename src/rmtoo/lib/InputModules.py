'''
 rmtoo
   Free and Open Source Requirements Management Tool

  InputModules
   This handles all the different input modules.

 (c) 2010-2011,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from stevedore import extension

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

    def __init__(self, config):
        '''Read in the modules'''
        Digraph.__init__(self)
        self._config = config
        self.__reqdeps_sorted = None

        # The different types of tags
        self.__tagtypes = {}
        self.__tagtypes[InputModuleTypes.reqtag] = {}
        self.__tagtypes[InputModuleTypes.reqdeps] = {}
        self.__tagtypes[InputModuleTypes.ctstag] = {}
        self.__tagtypes[InputModuleTypes.testcase] = {}

        self.__plugin_manager = extension.ExtensionManager(
            namespace='rmtoo.input.plugin',
            invoke_on_load=False)

        self.__load()

    def __load(self):
        '''Load the modules.'''
        for input_obj_name in self.__plugin_manager.entry_points_names():
            input_obj = self.__plugin_manager[input_obj_name].plugin(
                self._config)
            types = input_obj.get_type_set()
            # Add the objects to the appropriate directory
            for ltype in types:
                self.__tagtypes[ltype][input_obj_name] = input_obj
            # If a reqdeps type, put also the in the nodes list.
            if InputModuleTypes.reqdeps in types:
                self.nodes.append(input_obj)

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
            for node in mod.depends_on:
                # Connect in both directions
                if node not in self.__tagtypes[InputModuleTypes.reqdeps]:
                    raise RMTException(27, "Module '%s' depends on "
                                       "'%s' - which does not exists"
                                       % (mod_name, node))
                self.create_edge(
                    mod, self.__tagtypes[InputModuleTypes.reqdeps][node])

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
