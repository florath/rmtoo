'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Digraph Pyhton library

 (c) 2010,2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from rmtoo.lib.RMTException import RMTException


class Digraph(object):
    """Model of a directed graph"""

    class Node(object):
        """Model of a directed graph's node"""
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
        def as_named_list(ilist):
            """Return as named list"""
            # Start with an empty list
            res_list = []
            for node in ilist:
                res_list.append(node.name)
            return res_list

        # Return the names of all outgoing nodes as a list.
        def outgoing_as_named_list(self):
            """Return the outgoing nodes as named list"""
            return self.as_named_list(self.outgoing)

        # Return the names of all incoming nodes as a list.
        def incoming_as_named_list(self):
            """Return the incoming nodes as named list"""
            return self.as_named_list(self.incoming)

        # Find a subnode with the given name
        def find_outgoing(self, name):
            """Find an outgoing node with the given name.

            If not found, return None.
            """
            for out in self.outgoing:
                if out.name == name:
                    return out
            return None

        def is_self_of_ancient(self, onode):
            """This checks, if onode is in the ancient (parent, parent of
            parent, ...) of the current node.
            A depth first search is done.
            """
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

    @staticmethod
    def create_edge(node_a, node_b):
        """Creates an edge from a to b - both must be nodes."""
        node_a.outgoing.append(node_b)
        node_b.incoming.append(node_a)

    def add_node(self, node_a):
        """Adds a new node to the graph"""
        # Check if the node with the same name already exists.
        for node_idx in self.nodes:
            if node_idx.name == node_a.name:
                raise RMTException(39, "Node with name '%s' already exists"
                                   % node_a.name)
        self.nodes.append(node_a)

    def create_from_dict(self, digraph_as_dict, node_gen_func=Node):
        """Low level creation method, which really does the job of
        converting a given dictionary to a digraph.
        """
        # First run: create all nodes
        named_nodes = {}
        for node_name in digraph_as_dict:
            # Create the node and put it into the object list of all
            # nodes and into the local dictionary of named nodes.
            named_node = node_gen_func(node_name)
            self.nodes.append(named_node)
            named_nodes[node_name] = named_node

        # Second run: run thorugh all nodes and create the edges.
        for node_name, outgoing in digraph_as_dict.items():
            for out in outgoing:
                if out not in named_nodes:
                    raise RMTException(24, "Node '%s' is referenced "
                                       "but not specified" % out)
                self.create_edge(named_nodes[node_name],
                                 named_nodes[out])

    def output_to_dict(self):
        """Reverse operation: outputs this digraph and create a dictionary
        from it.
        """
        # Start with an empty dictionary
        result_dict = {}
        for node in self.nodes:
            result_dict[node.name] = node.outgoing_as_named_list()
        return result_dict

    def find(self, name):
        """Find a node with a given name"""
        for node in self.nodes:
            if name == node.name:
                return node
        return None

    def build_named_nodes(self):
        """Build up a dictionary with name:node pairs.

        This will only be done, iff every node has a name (None is not a
        name) and all names are different.
        """
        self.named_nodes = {}
        for node in self.nodes:
            if node.name is None:
                # Delete the whole dictionary first
                self.named_nodes = None
                raise RMTException(20, "cannot create node dictionary "
                                   "- node has no name")
            if node.name in self.named_nodes:
                # Also: delete the whole dictionary first.
                self.named_nodes = None
                raise RMTException(21, "same name for (at least) two "
                                   "nodes '%s'" % node.name)

            # Ok. Then put it into the dictionary:
            self.named_nodes[node.name] = node

    def get_named_node_no_throw(self, name):
        """This is the appropriate accessor: get the content only if there
        is the dictionary.
        """
        if not hasattr(self, "named_nodes") or self.named_nodes is None:
            raise RMTException(22, "no named_nodes dictionary available "
                               "- maybe call 'build_named_nodes()' first")
        if name not in self.named_nodes:
            return None
        # When all checks succeed: return the value
        return self.named_nodes[name]

    def get_named_node(self, name):
        """Mostly the same as before, but throws if the node can
        not be found."""
        res = self.get_named_node_no_throw(name)
        if res is None:
            raise RMTException(23, "node with name '%s' not available"
                               % name)
        return res
