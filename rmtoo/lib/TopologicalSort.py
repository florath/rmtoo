#
# This implements a tolological sort for the dependencies
#
# (c) 2008, 2010 by flonatel
#
# For licencing details see COPYING
#
# (This is part of the init4boot project, but fits also perfectly
# here.) 
#

import copy

# The graph must be a dictionary. The key is the node name where the
# edge(s) start, the value a list of nodes where the edge(s) end.
# Example:
#  {'Generic': [], 'iSCSI': ['Generic'], 'multipath': ['iSCSI', 'Generic']}
# The result is the topological sorted list of nodes.

def topological_sort(graph):

    # This function looks, if there exists a edge to node 'm':
    def edges_to_m(graph, m):
        for o in graph.keys():
            if m in graph[o]:
                return True
        return False

    # Do a topological sorting:
    # tsort is the topological sorted list
    tsort = []
    # nie: (set of) no incoming edges
    nie = set()
    # First: get all the edges
    for d in graph.keys():
        nie.add(d)
        nie.update(graph[d])
    # Remove all with incoming edges
    for d in graph.keys():
        nie.difference_update(graph[d])
    # At this point, the nie variable holds all nodes with no incoming edges.

    while len(nie)>0:
        n = nie.pop()
        tsort.append(n)
        ngraph = copy.deepcopy(graph[n])
        for m in ngraph:
            # Remove edge
            graph[n].remove(m)
            # Are there other edges to m?
            if not edges_to_m(graph, m):
                nie.add(m)

    return tsort
