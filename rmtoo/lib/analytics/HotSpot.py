'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Sometimes there are so called 'Requirements Hotspots'.  These are
  requirements which have too many links.
   
 (c) 2010-2011 by flonatel GmhH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.analytics.Base import Base
from rmtoo.lib.analytics.Result import Result

class HotSpot(Base):

    max_incoming = 7
    max_outgoing = 4

    def check_requirement(self, lname, req):
        eval_result = True
        findings = []
        if len(req.incoming) > HotSpot.max_incoming:
            findings.append(
                Result("HotSpot", lname, -10,
                    ["Number of incoming links is too high: %d" %
                       len(req.incoming)]))
            eval_result = False

        if len(req.outgoing) > HotSpot.max_outgoing:
            findings.append(
                Result("HotSpot", lname, -10,
                 ["Number of outgoing links is too high: %d" %
                    len(req.outgoing)]))
            eval_result = False

        return eval_result, findings
