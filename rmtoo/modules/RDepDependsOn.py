#
# Requirement Management Toolset
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

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
                == self.mods.reqtag["ReqType"].rt_initial_requirement:
            # There must no 'Depend on'
            if self.tag in rr.req:
                print("+++ ERROR %s: initial requirement has "
                      "Depend on field." % (rr.id))
                return
            return
        # There must be a 'Depend on'
        if self.tag not in rr.req:
            print("+++ ERROR %s: non-initial requirement has "
                  "no 'Depend on' field." % (rr.id))
            return
            
        t = rr.req[self.tag]
        # If there it must not empty
        if len(t)==0:
            print("+++ ERROR %s: 'Depend on' field has len 0" %
                  (rr.id))
            return

        # Step through the list
        tl = t.split()
        for ts in tl:
            if ts not in reqs.reqs:
                print("+++ ERROR %s: 'Depend on' points to a "
                      "non-existing requirement '%s'" %
                      (rr.id, ts))
                return

            dependend = reqs.reqs[ts]

            # Check if the type dependencies make sense
            # requirement -> design -> requirement
            # (but never: requirment -> requirement
            #  or design -> design)
            if rr.t_Type \
                    == self.mods.reqtag["ReqType"].rt_requirement:
                if dependend.t_Type \
                        != self.mods.reqtag["ReqType"].rt_design_decision:
                    print("+++ ERROR %s: 'Depend on' of requirement "
                          "is not a design decision '%s'" %
                          (rr.id, dependend.id))
                    return

            if rr.t_Type \
                    == self.mods.reqtag["ReqType"].rt_design_decision:
                if dependend.t_Type \
                        != self.mods.reqtag["ReqType"].rt_requirement \
                        or \
                        dependend.t_Type \
                        != self.mods.reqtag["ReqType"].rt_initial_requirement:
                    print("+++ ERROR %s: 'Depend on' of design decision "
                          "is not a requirement '%s'" %
                          (rr.id, dependend.id))
                    return
        rr.t_DependOn = t
        del rr[self.tag]

    def rewrite(self, reqs):
        # Run through all the requirements and look for the 'Depend
        # on' (depending on the type of the requirement)
        for r in reqs.reqs:
            rr = reqs.reqs[r]
            self.rewrite_one_req(rr, reqs)

