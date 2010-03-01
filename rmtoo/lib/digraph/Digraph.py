#
# Digraph Pyhton library
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

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

        # Return the names of all outgoing nodes as a list.
        def outgoing_as_named_list(self):
            # Start with an empty list
            l = []
            for o in self.outgoing:
                l.append(o.name)
            return l

    # Create a digraph from the given dictionary representation. 
    # If no dictionary is given, an empty digraph will be created.
    def __init__(self, d=None):
        self.nodes = []
        if d!=None:
            self.create_from_dict(d)

    # Creates an edge from a to b - both must be nodes.
    def create_edge(self, a, b):
        a.outgoing.append(b)
        b.incoming.append(a)

    # Low level creation method, which really does the job of
    # converting a given dictionary to a digraph
    def create_from_dict(self, d):
        # First run: create all nodes
        named_nodes = {}
        for node_name in d:
            # Create the node and put it into the object list of all
            # nodes and into the local dictionary of named nodes.
            named_node = self.Node(node_name)
            self.nodes.append(named_node)
            named_nodes[node_name] = named_node

        # Second run: run thorugh all nodes and create the edges.
        for node_name, outs in d.items():
            for o in outs:
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
            
