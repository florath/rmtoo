'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  This implements a tolological sort for a directed graph

  This was initially written for the init4boot project to handle
  dependencies of different modules.  It was adapted to work with a
  Digraph. 
   
 (c) 2008,2010,2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

def topological_sort(dg):
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
        '''Recursive deep first search function.'''
        if not node in visited:
            visited.append(node)
            for onode in node.get_iter_outgoing():
                visit(onode)
            tsort.append(node)

    # The 'main' function of the topological sort
    for node in dg.get_iter_nodes_values():
        visit(node)

    return tsort
