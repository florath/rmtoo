'''
 rmtoo
   Free and Open Source Requirements Management Tool

  This implements a tolological sort for a directed graph

  This was initially written for the init4boot project to handle
  dependencies of different modules.  It was adapted to work with a
  Digraph.

 (c) 2008,2010,2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''


def node_list_sort(lst_of_nodes):
    """Sorts the list ost nodes based on their name"""
    return sorted(lst_of_nodes, key=lambda node: node.name)


def node_list_no_sort(lst_of_nodes):
    """Does not sort the nodes"""
    return lst_of_nodes


def topological_sort(digraph, nodes_sort=node_list_sort):
    '''This algorithm is based upon a depth first search with 'making' some
       special nodes.
       The result is the topological sorted list of nodes.'''
    # List of topological sorted nodes
    tsort = []
    # List of nodes already visited.
    # (This is held here - local to the algorithm - to not modify the
    # nodes themselves.)
    visited = []

    def visit(node):
        """Recursive deep first search function"""
        if node not in visited:
            visited.append(node)
            for out_node in nodes_sort(node.outgoing):
                visit(out_node)
            tsort.append(node)

    # The 'main' function of the topological sort
    for node in nodes_sort(digraph.nodes):
        visit(node)

    return tsort
