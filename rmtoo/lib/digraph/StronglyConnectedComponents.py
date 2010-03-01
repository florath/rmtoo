#
# This implements an algothim for digraphs which computes the strongly
# connected components.
#
# The algorithm was introduced by Trajan and it's typically called
# 'Trajan's algorithm'.
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

# This algorithm is based upon a depth first search.  It assigns a
# number to each visited node.
def strongly_connected_components(dg):
    # This is the number the next node is assigned. (There is no other
    # way to access local varaibles?)
    index = [0]
    # The stack (list) of nodes - initially empty.
    S = []
    # Two maps for storing algorithm-local data.
    indizes = {}
    lowlinks = {}
    # The result is a list of lists containg nodes which form the
    # strongly connected component
    scc = []

    def trajan(v):
        # Mark the current node
        indizes[v] = index[0]
        lowlinks[v] = index[0]
        # Increase the all time DFS counter
        index[0] += 1
        # Append currnet node to stack
        S.append(v)

        # For all successors of v:
        for vl in v.outgoing:
            #print("+++ INNTRO +++")
            #print(vl.name)
            #print(indizes)
            #print(lowlinks)

            # Only check it, if it is not visited already.
            if vl not in indizes:
                #print("NOT VISITED")
                trajan(vl)
                lowlinks[v] = min(lowlinks[v], lowlinks[vl])
            elif vl in S:
                lowlinks[v] = min(lowlinks[v], lowlinks[vl])

        # Is this a SCC?
        if lowlinks[v] == indizes[v]:
            #print("SCC: ")
            new_scc = []
            while len(S)>0:
                vv = S.pop()
                #print(vv.name)
                new_scc.append(vv)
                if vv == v:
                    break
            scc.append(new_scc)


    # The 'main' of the algorithm: for every node (which is not yet)
    # already indexed, call the trajan() function.
    for v in dg.nodes:
        if v not in indizes:
            trajan(v)

    # Return the result
    return scc
