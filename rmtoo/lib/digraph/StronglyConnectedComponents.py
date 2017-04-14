'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  This implements an algorithm for digraphs which computes the strongly
  connected components.
 
  The algorithm was introduced by Trajan and it's typically called
  'Trajan's algorithm'.
   
 (c) 2010,2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

def strongly_connected_components(dg):
    '''This algorithm is based upon a depth first search.  It assigns a
       number to each visited node.'''
    # This is the number the next node is assigned. (There is no other
    # way to access local variables?)
    index = [0]
    # The stack (list) of nodes - initially empty.
    S = []
    # Two maps for storing algorithm-local data.
    indizes = {}
    lowlinks = {}
    # The result is a list of lists containing nodes which form the
    # strongly connected component
    scc = []

    def trajan(v):
        # Mark the current node
        indizes[v] = index[0]
        lowlinks[v] = index[0]
        # Increase the all time DFS counter
        index[0] += 1
        # Append current node to stack
        S.append(v)

        # For all successors of v:
        for vl in v.get_iter_outgoing():
            # Only check it, if it is not visited already.
            if vl not in indizes:
                trajan(vl)
                lowlinks[v] = min(lowlinks[v], lowlinks[vl])
            elif vl in S:
                lowlinks[v] = min(lowlinks[v], lowlinks[vl])

        # Is this a SCC?
        if lowlinks[v] == indizes[v]:
            new_scc = []
            while len(S) > 0:
                vv = S.pop()
                new_scc.append(vv)
                if vv == v:
                    break
            scc.append(new_scc)

    # The 'main' of the algorithm: for every node (which is not yet)
    # already indexed, call the trajan() function.
    for v in dg.get_iter_nodes_values():
        if v not in indizes:
            trajan(v)

    # Return the result
    return scc

# This checks if there are at least one strongly connected component
# with a size equal or larger than the given number.
# The default '2' checks, if there is at least one strongly connected
# component which contains more than one node.
def check_for_strongly_connected_components(scc, minsize=2):
    for s in scc:
        if len(s) >= minsize:
            # Jep there is one scc -> jump out.
            return True
    # Nope - no sccs.
    return False
