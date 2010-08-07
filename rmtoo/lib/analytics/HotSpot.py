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

    max_incoming = 7
    max_outgoing = 4
    
    @staticmethod
    def run(config, reqs, topics):
        ok = True
        for _, req in reqs.reqs.iteritems():
            if len(req.incoming)>HotSpot.max_incoming:
                req.analytics["HotSpot"] = \
                    [-10, ["Number of incoming links is too high: %d" % 
                      len(req.incoming)]]
                ok = False
               
            if len(req.outgoing)>HotSpot.max_outgoing:
                req.analytics["HotSpot"] = \
                    [-10, ["Number of outgoing links is too high: %d" % 
                      len(req.outgoing)]]
                ok = False

        return ok
