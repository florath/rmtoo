'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Sometimes there are so called 'Requirements Hotspots'.  These are
  requirements which have too many links.
   
 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.analytics.Result import Result
from rmtoo.lib.analytics.Base import Base

class HotSpot(Base):

    max_incoming = 7
    max_outgoing = 4

    def __init__(self, _):
        Base.__init__(self)

    def requirement(self, req):
        if req.get_incoming_cnt() > HotSpot.max_incoming:
            self.add_result(
                Result("HotSpot", req.get_name(), -10,
                    ["Number of incoming links is too high: %d" %
                       req.get_incoming_cnt()]))
            self.set_failed()

        if req.get_outgoing_cnt() > HotSpot.max_outgoing:
            self.add_result(
                Result("HotSpot", req.get_name(), -10,
                 ["Number of outgoing links is too high: %d" %
                    req.get_outgoing_cnt()]))
            self.set_failed()

