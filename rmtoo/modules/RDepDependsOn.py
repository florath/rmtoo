#
# Requirement Management Toolset
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

# This is executed on the RequirmentSet level (not on the Requirement
# level!): of course this is needed for inter-dependencies.

class RDepDependsOn:

    def __init__(self, opts, config):
        self.opts = opts
        self.config = config
        self.tag = "Depends on"

    def type(self):
        return "reqdeps"

    def set_modules(self, mods):
        self.mods = mods

    def rewrite_one_req(self, rr, reqs):
        if rr.t_Type \
                == self.mods.reqtag["ReqType"].rt_master_requirement:
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
            if ts not in reqs.reqs:
                print("+++ ERROR %s: 'Depends on' points to a "
                      "non-existing requirement '%s'" %
                      (rr.id, ts))
                return

            dependend = reqs.reqs[ts]

        # Copy and delete the original
        rr.t_DependOn = t.split()
        del rr.req[self.tag]

    def rewrite(self, reqs):
        # Run through all the requirements and look for the 'Depend
        # on' (depending on the type of the requirement)
        for r in reqs.reqs:
            rr = reqs.reqs[r]
            self.rewrite_one_req(rr, reqs)

