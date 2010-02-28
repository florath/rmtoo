#
# This implements a tolological sort for a directed graph
#
# (c) 2008, 2010 by flonatel
#
# For licencing details see COPYING
#
# This was initially written for the init4boot project to handle
# dependencies of different modules.  It was adapted to work with a
# Digraph. 
#

import copy

# This algorithm is based upon a depth first search with 'making' some
# special nodes.
# The result is the topological sorted list of nodes.
def topological_sort(dg):
    # List of topological sorted nodes
    tsort = []
    # List of nodes already visited.
    visited = []

    def visit(node):
        if not node in visited:
            visited.append(node)
            for m in node.outgoing:
                visit(m)
            tsort.append(node)
    
    for node in dg.nodes:
        visit(node)

    return tsort
