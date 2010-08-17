#
# Requirement Management Toolset
#
#   Helper functions for a Requirement Set
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.RequirementSet import RequirementSet
from rmtoo.lib.digraph.ConnectedComponents \
    import connected_components

def reqs_limit_topics(reqset, topicset):
    r = RequirementSet(reqset.mods, reqset.opts, reqset.config)
    used_reqs = topicset.get_all_reqs()

    # Copy over the requirements themselves:
    # Here the incoming and outgoing requirements are the still the
    # old ones.
    # During the loop, build up the mapping from old to new.
    def copy_only_reqs(reqset, used_reqs):
        old2new = {}
        for _, req in reqset.reqs.iteritems():
            if not req in used_reqs:
                print("+++ Info:%s: Skipping requirement because not in topic" 
                      % req.id)
                continue
            req_copy = req.internal_copy_phase1(used_reqs)
            r.add_req(req_copy)
            old2new[req] = req_copy
        return old2new

    old2new = copy_only_reqs(reqset, used_reqs)

    # Replace all the incoming and outgoing from old to new:
    for _, req in r.reqs.iteritems():
        req.internal_copy_phase2(old2new)

    # There is the need for some tests (e.g. is the remaining graph
    # connected) - but the handle_modules_reqdeps() does much more -
    # which is not needed at this point.
    # Therefore the algorithms is called directly from here.
    components = connected_components(r)
    if components.len()>1:
        print("+++ Info: The resulting graph is not connected.")
        print("+++       Found components: '%s'" % components.as_string())

    return r
