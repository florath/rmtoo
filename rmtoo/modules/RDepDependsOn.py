#
# Requirement Management Toolset
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.Requirement import Requirement

# This is executed on the RequirmentSet level (not on the Requirement
# level!): of course this is needed for inter-dependencies.

class RDepDependsOn:
    tag = "Depends on"

    def __init__(self, opts, config):
        self.opts = opts
        self.config = config

    def type(self):
        return "reqdeps"

    def set_modules(self, mods):
        self.mods = mods

    # The rewriting of one requirment is done 'in place'.
    def rewrite_one_req(self, rr, reqs):
        if rr.tags["Type"] == Requirement.rt_master_requirement:
            # There must no 'Depends on'
            if self.tag in rr.req:
                print("+++ ERROR %s: initial requirement has "
                      "Depends on field." % (rr.id))
                return
            rr.t_DependOn = None
            return
        # There must be a 'Depends on'
        if self.tag not in rr.req:
            print("+++ ERROR %s: non-initial requirement has "
                  "no 'Depends on' field." % (rr.id))
            return
            
        t = rr.req[self.tag]
        # If there it must not empty
        if len(t)==0:
            print("+++ ERROR %s: 'Depends on' field has len 0" %
                  (rr.id))
            return

        # Step through the list
        tl = t.split()
        for ts in tl:
            if ts not in reqs:
                print("+++ ERROR %s: 'Depends on' points to a "
                      "non-existing requirement '%s'" %
                      (rr.id, ts))
                return

            dependend = reqs[ts]

        # Copy and delete the original
        rr.tags["Depends on"] = t.split()
        del rr.req[self.tag]

    def rewrite(self, reqs):
        # Run through all the requirements and look for the 'Depend
        # on' (depending on the type of the requirement)
        for k, v in reqs.items():
            self.rewrite_one_req(v, reqs)

