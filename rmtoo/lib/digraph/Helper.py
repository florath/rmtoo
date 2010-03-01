#
# Some small helper functions
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

# Converts a node list into a list of the corresponding node names.
def node_list_to_node_name_list(node_list):
    node_name_list = []
    for n in node_list:
        node_name_list.append(n.name)
    return node_name_list

# Mostly the same: but this time for sets
def node_set_to_node_name_set(node_set):
    node_name_set = set()
    for n in node_set:
        node_name_set.add(n.name)
    return node_name_set

# Converts a node set list into a list of sets of the corresponding
# node names. 
def node_sl_to_node_name_sl(node_sl):
    node_name_sl = []
    for n in node_sl:
        node_name_sl.append(node_set_to_node_name_set(n))
    return node_name_sl

# Remove all lists in the list which has maximal one element.  The
# other lists convert to names.
def remove_single_element_lists_name_rest(scc):
    res = []
    for s in scc:
        if len(s)>1:
            res.append(node_list_to_node_name_list(s))
    return res
