'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Directed Graph implementation
   
 (c) 2010,2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.RMTException import RMTException

class Digraph(object):
    '''Implements a directed graph.
       The minimum requirement is, that each node has a unique name,'''

    class Node(object):
        '''A directed graph node.
           This holds the incoming and outgoing edges as well as the 
           nodes' name,'''
        def __init__(self, name):
            '''Incoming and outgoing are lists of nodes.  Typically one
               direction is provided and the other can be automatically
               computed.'''
            self.__name = name
            self.__incoming = set()
            self.__outgoing = set()

        def __hash__(self):
            '''Calculates the hash based on the node's name.'''
            return self.__name.__hash__()

        def get_name(self):
            '''Returns the name of the node.'''
            return self.__name

        def get_iter_incoming(self):
            '''Return an iterator over the incoming nodes.'''
            return iter(self.__incoming)

        def get_iter_outgoing(self):
            '''Return an iterator over the outgoing nodes.'''
            return iter(self.__outgoing)

        def add_incoming(self, node):
            '''Add node to the incoming list.'''
            self.__incoming.add(node)

        def add_outgoing(self, node):
            '''Add node to the incoming list.'''
            self.__outgoing.add(node)

        @staticmethod
        def __as_named_list(inlist):
            '''Return given list as list of names.'''
            # pylint: disable=W0141
            return map(lambda x: x.get_name(), inlist)

        def get_outgoing_as_named_list(self):
            '''Return the names of all outgoing nodes as a list.'''
            return self.__as_named_list(self.__outgoing)

        def get_incoming_as_named_list(self):
            '''Return the names of all incoming nodes as a list.'''
            return self.__as_named_list(self.__incoming)

        def find_outgoing(self, name):
            '''Find a subnode with the given name.'''
            for onode in self.__outgoing:
                if onode.get_name() == name:
                    return onode
            return None

        def is_self_of_ancient(self, onode):
            '''Checks, if onode is in the ancient (parent, parent of
               parent, ...) of the current node.
               A depth first search is done.'''
            # Check for break
            if self == onode:
                # Stop iff found.
                return True

            # If not (yet) found: have a look at the ancestors.
            for node in self.__incoming:
                if node.is_self_of_ancient(onode):
                    # Found is somewhere in history.
                    return True

            # Did not find the other node.
            return False

        def debug_output(self):
            '''Prints out the internal state of the object to stdout.'''
            print("Node [%s] Outgoing %s Incoming %s"
                  % (self.get_name(), self.get_outgoing_as_named_list(),
                     self.get_incoming_as_named_list()))

    def __init__(self):
        '''Create a digraph from the given dictionary representation. 
           If no dictionary is given, an empty digraph will be created.'''
        self._named_nodes = {}

    @staticmethod
    def create_edge(anode, bnode):
        '''Creates an edge from a to b - both must be nodes.'''
        assert isinstance(anode, Digraph.Node)
        assert isinstance(bnode, Digraph.Node)
        anode.add_outgoing(bnode)
        bnode.add_incoming(anode)

    def add_node(self, anode):
        '''Adds a new node to the graph.
           Check if the node with the same name already exists.'''
        assert isinstance(anode, Digraph.Node)

        for node in self._named_nodes.values():
            if node.get_name() == anode.get_name():
                raise RMTException(39, "Node with name '%s' already exists"
                                   % anode.get_name())
        self._named_nodes[anode.get_name()] = anode

    def get_iter_nodes_values(self):
        '''Returns the nodes dict.'''
        return iter(self._named_nodes.values())

    def as_dict(self):
        '''Outputs this digraph and create a dictionary.'''
        # Start with an empty dictionary
        rval = {}
        for node in self._named_nodes.values():
            rval[node.get_name()] = node.get_outgoing_as_named_list()
        return rval

    def find(self, name):
        '''Get the node with the given name.
           Return None if not available.'''
        if name not in self._named_nodes:
            return None
        # When all checks succeed: return the value
        return self._named_nodes[name]

    def find_wt(self, name):
        '''Get the node with the given name.
           Throw if not available.'''
        res = self.find(name)
        if res == None:
            raise RMTException(23, "node with name '%s' not available" % name)
        return res

    def debug_output(self):
        '''Writes out some graph skeleton to the stdout.'''
        print("Digraph output:")
        for node in self._named_nodes.values():
            node.debug_output()
        print("Digraph output end.")
