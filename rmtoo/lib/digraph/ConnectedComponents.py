'''
 rmtoo
   Free and Open Source Requirements Management Tool

  This function implements the digraph algorithm finding the connected
  components of a digraph.

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.RMTException import RMTException


class ConnectedComponents(object):
    """Class that holds the connected components of a digraph"""

    def __init__(self):
        self.__cs = []

    def get_length(self):
        """Return the number of components"""
        return len(self.__cs)

    @staticmethod
    def set_as_string(node_set):
        """Return list of names from a set of nodes"""
        result = set()
        for node in node_set:
            result.add(node.name)
        return result

    def as_string(self):
        """Return the connected component set as list of sets"""
        result = []
        for node in self.__cs:
            result.append(self.set_as_string(node))
        return result

    def add_component(self, node):
        """Add a component that contains only the single given node"""
        self.__cs.append(set([node]))

    def find(self, node):
        """Search if the given node is in the connected component.

        If so return the set and the index of the set.
        If not, raise an exeption."
        """
        set_idx = 0
        for cc_set in self.__cs:
            if node in cc_set:
                return set_idx, cc_set
            set_idx += 1
        # Node not found
        raise RMTException(68, "Node [%s] not found" % node)

    def contract(self, node_a, node_b):
        """Contract the sets which contain both given nodes"""
        _, set_a = self.find(node_a)
        set_b_idx, set_b = self.find(node_b)
        if set_a == set_b:
            # Already in one component - nothing to do
            return
        # Append elements from set_b to set_a
        set_a |= set_b
        # Remove h
        del self.__cs[set_b_idx]


def connected_components(digraph):
    """Compute the connected components of the given digraph"""
    # This hold the components:
    #  the lists of the nodes which are in one component
    components = ConnectedComponents()

    for node in digraph.nodes:
        # Each node itself is a separate component
        components.add_component(node)

    for node in digraph.nodes:
        # Run through the incoming and outgoing and collect the
        # different components
        for connected_node in node.incoming:
            components.contract(node, connected_node)
        for connected_node in node.outgoing:
            components.contract(node, connected_node)

    return components
