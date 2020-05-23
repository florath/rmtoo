'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Some small helper functions for digraph

 (c) 2010,2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''


def node_list_to_node_name_list(node_list):
    '''Converts a node list into a list of the corresponding node names.'''
    node_name_list = []
    for node in node_list:
        node_name_list.append(node.name)
    return node_name_list


def node_set_to_node_name_set(node_set):
    '''Mostly the same: but this time for sets.'''
    node_name_set = set()
    for node in node_set:
        node_name_set.add(node.name)
    return node_name_set


def node_sl_to_node_name_sl(node_sl):
    '''Converts a node set_value list into a list of sets of the corresponding
    node names.
    '''
    node_name_sl = []
    for node in node_sl:
        node_name_sl.append(node_set_to_node_name_set(node))
    return node_name_sl


def remove_single_element_lists_name_rest(scc):  # pylint: disable=invalid-name
    '''Remove all lists in the list which has maximal one element.  The
    other lists convert to names.
    '''
    res = []
    for i in scc:
        if len(i) > 1:
            res.append(node_list_to_node_name_list(i))
    return res
