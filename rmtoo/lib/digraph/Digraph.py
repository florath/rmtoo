'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Digraph Pyhton library

 (c) 2010,2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from rmtoo.lib.RMTException import RMTException


class Digraph:

    class Node:
        def __init__(self, name=None):
            # Incoming and outgoing are lists of nodes.  Typically one
            # direction is provided and the other can be automatically
            # computed.
            self.incoming = []
            self.outgoing = []
            self.name = name

        def __hash__(self):
            return self.name.__hash__()

        # Return given list as list of names.
        @staticmethod
        def as_named_list(il):
            # Start with an empty list
            l = []
            for o in il:
                l.append(o.name)
            return l

        # Return the names of all outgoing nodes as a list.
        def outgoing_as_named_list(self):
            return self.as_named_list(self.outgoing)

        # Return the names of all incoming nodes as a list.
        def incoming_as_named_list(self):
            return self.as_named_list(self.incoming)

        # Find a subnode with the given name
        def find_outgoing(self, name):
            for o in self.outgoing:
                if o.name == name:
                    return o
            return None

        # This checks, if onode is in the ancient (parent, parent of
        # parent, ...) of the current node.
        # A depth first search is done.
        def is_self_of_ancient(self, onode):
            # Check for break
            if self == onode:
                # Stop iff found.
                return True

            # If not (yet) found: have a look at the ancestors.
            for node in self.incoming:
                if node.is_self_of_ancient(onode):
                    # Found is somewhere in history.
                    return True

            # Did not find the other node.
            return False

    # Create a digraph from the given dictionary representation.
    # If no dictionary is given, an empty digraph will be created.
    def __init__(self, d=None, node_gen_func=Node):
        self.nodes = []
        self.named_nodes = None
        if d is not None:
            self.create_from_dict(d, node_gen_func)

    # Creates an edge from a to b - both must be nodes.
    @staticmethod
    def create_edge(a, b):
        a.outgoing.append(b)
        b.incoming.append(a)

    # Adds a new node to the graph
    def add_node(self, a):
        # Check if the node with the same name already exists.
        for n in self.nodes:
            if n.name == a.name:
                raise RMTException(39, "Node with name '%s' already exists"
                                   % a.name)
        self.nodes.append(a)

    # Low level creation method, which really does the job of
    # converting a given dictionary to a digraph
    def create_from_dict(self, d, node_gen_func=Node):
        # First run: create all nodes
        named_nodes = {}
        for node_name in d:
            # Create the node and put it into the object list of all
            # nodes and into the local dictionary of named nodes.
            named_node = node_gen_func(node_name)
            self.nodes.append(named_node)
            named_nodes[node_name] = named_node

        # Second run: run thorugh all nodes and create the edges.
        for node_name, outs in d.items():
            for o in outs:
                if o not in named_nodes:
                    raise RMTException(24, "Node '%s' is referenced "
                                       "but not specified" % o)
                self.create_edge(named_nodes[node_name],
                                 named_nodes[o])

    # Reverse operation: outputs this digraph and create a dictionary
    # from it.
    def output_to_dict(self):
        # Start with an empty dictionary
        rv = {}
        for n in self.nodes:
            rv[n.name] = n.outgoing_as_named_list()
        return rv

    # Find a node with a given name
    def find(self, name):
        for n in self.nodes:
            if name == n.name:
                return n
        return None

    # Build up a dictionary with name:node pairs.
    # This will only be done, iff every node has a name (None is not a
    # name) and all names are different.
    def build_named_nodes(self):
        self.named_nodes = {}
        for n in self.nodes:
            if n.name is None:
                # Delete the whole dictionary first
                self.named_nodes = None
                raise RMTException(20, "cannot create node dictionary "
                                   "- node has no name")
            if n.name in self.named_nodes:
                # Also: delete the whole dictionary first.
                self.named_nodes = None
                raise RMTException(21, "same name for (at least) two "
                                   "nodes '%s'" % n.name)

            # Ok. Then put it into the dictionary:
            self.named_nodes[n.name] = n

    # This is the appropriate accessor: get the content only if there
    # is the dictionary.
    def get_named_node_no_throw(self, name):
        if not hasattr(self, "named_nodes") or self.named_nodes is None:
            raise RMTException(22, "no named_nodes dictionary available "
                               "- maybe call 'build_named_nodes()' first")
        if name not in self.named_nodes:
            return None
        # When all checks succeed: return the value
        return self.named_nodes[name]

    # Mostly the same as before, but throws if the node can not be found.
    def get_named_node(self, name):
        r = self.get_named_node_no_throw(name)
        if r is None:
            raise RMTException(23, "node with name '%s' not available"
                               % name)
        return r
