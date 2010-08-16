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

def reqs_limit_topics(reqset, topicset):
    r = RequirementSet(reqset.mods, reqset.opts, reqset.config)
    used_reqs = topicset.get_all_reqs()

    # Copy over the requirements themselfs:
    # Here the incoming and outgoing requirements are the still the
    # old ones.
    # During the loop, build up the mapping from old to new.
    old2new = {}
    for _, req in reqset.reqs.iteritems():
        if not req in used_reqs:
            print("+++ Info:%s: Skipping requirement because not in topic" 
                  % req.id)
            continue
        req_copy = req.copy(used_reqs)
        r.add_req(req_copy)
        old2new[req] = req_copy

    # Replace all the incoming and outgoing from old to new:
    for _, req in r.reqs.iteritems():
        outgoing = []
        for o in req.outgoing:
            outgoing.append(old2new[o])
        req.outgoing = outgoing

        incoming = []
        for o in req.incoming:
            incoming.append(old2new[o])
        req.incoming = incoming

    return r
