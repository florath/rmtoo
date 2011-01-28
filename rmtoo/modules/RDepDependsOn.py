#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# Requirments Depends On Tag handling
#
# (c) 2010-2011 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.digraph.Digraph import Digraph

# This class handles the creation of the full directred graphs: one
# 'Depends on' and one 'Dependent'.  Both graphs are digraphs.
#
# Because this is the central functionalaity where a lot of other
# modules depend on, these things are directy written to the
# Requirments and RequirementSet object.
#
# This is executed on the RequirmentSet level (not on the Requirement
# level!): of course this is needed for inter-dependencies.

class RDepDependsOn(Digraph.Node):
    depends_on = []
    tag = "Depends on"

    def __init__(self, opts, config):
        Digraph.Node.__init__(self, "RDepDependsOn")
        self.opts = opts
        self.config = config

    def type(self):
        return "reqdeps"

    def set_modules(self, mods):
        self.mods = mods

    # The rewriting of one requirment is done 'in place'.
    def rewrite_one_req(self, rr, reqset, also_solved_by):
        if rr.get_value("Type") == Requirement.rt_master_requirement:
            # There must no 'Depends on'
            if self.tag in rr.req:
                print("+++ ERROR %s: initial requirement has "
                      "Depends on field." % (rr.id))
                return False
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
            return True

        # For all other requirments types there must be a 'Depends on'
        if self.tag not in rr.req:
            if also_solved_by:
                # Skip handling this requirement
                return True
            print("+++ ERROR %s: non-initial requirement has "
                  "no 'Depends on' field." % (rr.id))
            return False

        t = rr.req[self.tag] 

        # If available, it must not empty
        if len(t.get_content())==0:
            print("+++ ERROR %s: 'Depends on' field has len 0" %
                  (rr.id))
            return False

        # Step through the list
        tl = t.get_content().split()
        for ts in tl:
            if ts not in reqset.reqs:
                reqset.error(47, "'Depends on' points to a "
                             "non-existing requirement '%s'" % ts, rr.id)
                return False
            # It is not allowed to have self-references: it does not
            # make any sense, that a requirement references itself.
            if ts==rr.id:
                reqset.error(59, "'Depends on' points to the "
                             "requirement itself", rr.id)
                return False

            # Mark down the depends on...
            dependend = reqset.reqs[ts]
            rr.outgoing.append(dependend)
            # ... and also the other direction: in the pointed node
            # mark that the current node points to this.
            dependend.incoming.append(rr)

        # Copy and delete the original tag
        ## XXX Not neede any more? rr.tags["Depends on"] = t.split()
        del rr.req[self.tag]
        return True

    def rewrite(self, reqset):
        if "Depends on" not in self.config.reqs_spec["dependency_notation"]:
            return True

        # Check if the "Solved by" is also available in the config
        also_solved_by = "Solved by" in \
            self.config.reqs_spec["dependency_notation"]

        # Run through all the requirements and look for the 'Depend
        # on' (depending on the type of the requirement)
        everythings_fine = True
        # Prepare the Master Node
        reqset.graph_master_node = None
        for k, v in reqset.reqs.items():
            if not self.rewrite_one_req(v, reqset, also_solved_by):
                everythings_fine = False
        # Double check if one was found
        if reqset.graph_master_node==None:
            reqset.error(48, "no master requirement found")
            return False
        return everythings_fine

