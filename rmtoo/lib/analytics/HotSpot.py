#
# Analytics: HotSpot
#
#  Sometimes there are so called 'Requirements Hotspots'.  These are
#  requirements which have too many links.
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

class HotSpot:

    max_incoming = 4
    max_outgoing = 7
    
    @staticmethod
    def run(reqs):
        ok = True
        for _, req in reqs.reqs.iteritems():
            if len(req.incoming)>HotSpot.max_incoming:
                reqs.error(49, "Number of incoming "
                           "links is too high: %d" % 
                           len(req.incoming), req.id)
                ok = False
               
            if len(req.outgoing)>HotSpot.max_outgoing:
                reqs.error(50, "Number of outgoing "
                           "links is too high: %d" % 
                           len(req.outgoing), req.id)
                ok = False

        return ok
