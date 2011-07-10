#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# Requirement class itself
#
# (c) 2010-2011 by flonatel
#
# For licencing details see COPYING
#

import os
import time
import operator

from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.MemLogStore import MemLogStore
from rmtoo.lib.BaseRMObject import BaseRMObject

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Requirement(Digraph.Node, BaseRMObject):

    # Requirment Type
    # Each requirement has exactly one type.
    # The class ReqType sets this from the contents of the file.
    # Note: There can only be one (master requirement)
    rt_master_requirement = 1
    # Initial requirement is deprecated
    rt_initial_requirement = 2
    rt_design_decision = 3
    rt_requirement = 4

    def __init__(self, fd, rid, mls, mods, opts, config):
        Digraph.Node.__init__(self, rid)
        BaseRMObject.__init__(self, "reqtag", fd, rid, mls, mods, opts, 
                              config, "requirements")

### Looks that these functions are not used at all

    # Error is an error (no distinct syntax error)
#    def mark_syntax_error(self):
#        self.state = self.er_error

    # Error is an error (no distinct sematic error)
#    def mark_sematic_error(self):
#        self.state = self.er_error

    def get_prio(self):
        return self.values["Priority"]

#    def is_open(self):
#        return self.values["Status"] == self.st_not_done

    def get_status(self):
        return self.values["Status"]

    # Returns the EfE units or 0 if not available.
    def get_efe_or_0(self):
        efe = self.get_value("Effort estimation")
        if efe==None:
            return 0
        return efe

    def is_implementable(self):
        return self.values["Class"].is_implementable()

    # Write out the analytics results.
    def write_analytics_result(self, mstderr):
        for k, v in sorted(self.analytics.items(),
                           key=operator.itemgetter(0)):
            if v[0]<0:
                mstderr.write("+++ Error:Analytics:%s:%s:result is '%+3d'\n"
                              % (k, self.id, v[0]))
                for l in v[1]:
                    mstderr.write("+++ Error:Analytics:%s:%s:%s\n" % 
                                  (k, self.id, l))

    # The following functions are declared internal because they are
    # for internal use only.
    # To copy a requirement (functionally deep copy) two phases are
    # needed: First copy the requirements themselfs then adapt the
    # incoming and outgoing lists to the new requirements.

    # internal copy phase 1
    # Create a deep copy without all requirements (incoming and
    # outgoing) which are not part of one of the given topics.
    # The reqs_included set is a set of pointers to the old
    # requirements. 
    def internal_copy_phase1(self, topic_name_list):
        # Create the new Requirement itself.
        r = Requirement(None, self.id, self.mls, self.mods,
                        self.opts, self.config)
        r.otags = self.otags
        r.values = self.values

        # The only things to copy over are the incoming and the
        # outgoing lists.
        # These are pointers to the old ones!!!
        for req in self.incoming:
            if req.values["Topic"] in topic_name_list:
                r.incoming.append(req)
        for req in self.outgoing:
            if req.values["Topic"] in topic_name_list:
                r.outgoing.append(req)

        return r

    # Adapt the incoming and outgoing list: given a dictionary to map
    # from old to new.
    def internal_copy_phase2(self, old2new):
        outgoing = []
        for o in self.outgoing:
            outgoing.append(old2new[o])
        self.outgoing = outgoing

        incoming = []
        for o in self.incoming:
            incoming.append(old2new[o])
        self.incoming = incoming
        
