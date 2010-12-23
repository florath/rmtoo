#
# rmtoo
#   Requirements Management Tool
#
# The straight forward way to define dependencies.
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.Requirement import Requirement

class RDepSolvedBy(Digraph.Node):
    depends_on = []
    tag = "Solved by"

    def __init__(self, opts, config):
        Digraph.Node.__init__(self, "RDepSolvedBy")
        self.opts = opts
        self.config = config

    def type(self):
        return "reqdeps"

    def set_modules(self, mods):
        self.mods = mods

    # The rewriting of one requirment is done 'in place'.
    def rewrite_one_req(self, rr, reqset):
        if rr.tags["Type"] == Requirement.rt_master_requirement:
            # It self does not have any depends on nodes
            rr.graph_depends_on = None
            # This is the master!
            # Check if there is already another master:
            if reqset.graph_master_node!=None:
                print("+++ ERROR %s: Another master is already there. "
                      "There can only be one." % (rr.id))
                return False
            # Write a link to the master node to the RequirmentSet.
            reqset.graph_master_node = rr
            # return True

        # It is a 'normal ' case when there is no 'Solved by' (until now).
        if self.tag not in rr.req:
            return True

        t = rr.req[self.tag]
        # If available, it must not empty
        if len(t)==0:
            print("+++ ERROR %s: 'Solved by' field has len 0" %
                  (rr.id))
            return False

        # Step through the list
        tl = t.split()
        for ts in tl:
            if ts not in reqset.reqs:
                reqset.error(74, "'Solved by' points to a "
                             "non-existing requirement '%s'" % ts, rr.id)
                return False
            # It is not allowed to have self-references: it does not
            # make any sense, that a requirement references itself.
            if ts==rr.id:
                reqset.error(75, "'Solved by' points to the "
                             "requirement itself", rr.id)
                return False

            # Mark down the depends on...
            dependend = reqset.reqs[ts]
            # This is exactly the other way as used in the 'Depends on'
            rr.incoming.append(dependend)
            # ... and also the other direction: in the pointed node
            # mark that the current node points to this.
            dependend.outgoing.append(rr)

        # Copy and delete the original tag
        del rr.req[self.tag]
        return True

    def rewrite(self, reqset):
        if self.tag not in self.config.reqs_spec["dependency_notation"]:
            return True

        # Run through all the requirements and look for the 'Solved
        # by'
        everythings_fine = True
        # Prepare the Master Node
        reqset.graph_master_node = None
        for k, v in reqset.reqs.items():
            if not self.rewrite_one_req(v, reqset):
                everythings_fine = False
        # Double check if one was found
        if reqset.graph_master_node==None:
            reqset.error(48, "no master requirement found")
            return False
        return everythings_fine
