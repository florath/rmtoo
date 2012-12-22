'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Some small helper functions for digraph
   
 (c) 2010,2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.digraph.Digraph import Digraph

def node_list_to_node_name_list(node_list):
    '''Converts a node list into a list of the corresponding node names.'''
    node_name_list = []
    for n in node_list:
        node_name_list.append(n.get_name())
    return node_name_list

def node_set_to_node_name_set(node_set):
    '''Mostly the same: but this time for sets.'''
    node_name_set = set()
    for n in node_set:
        node_name_set.add(n.get_name())
    return node_name_set

def node_sl_to_node_name_sl(node_sl):
    '''Converts a node set_value list into a list of sets of the corresponding
       node names.'''
    node_name_sl = []
    for n in node_sl:
        node_name_sl.append(node_set_to_node_name_set(n))
    return node_name_sl

def remove_single_element_lists_name_rest(scc):
    '''Remove all lists in the list which has maximal one element.  The
       other lists convert to names.'''
    res = []
    for s in scc:
        if len(s) > 1:
            res.append(node_list_to_node_name_list(s))
    return res

def digraph_create_from_dict(init_dgraph, node_gen_func=Digraph.Node):
    '''Creates a new digraph based on the given information.'''
    digraph = Digraph()
    digraph.create_from_dict(init_dgraph, node_gen_func)
    return digraph
