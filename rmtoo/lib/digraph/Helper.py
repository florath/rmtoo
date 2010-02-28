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
