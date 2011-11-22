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
    def run(config, latest_topicsc):
        ok = True  
        for _, topic_set in latest_topicsc.get_topic_sets().iteritems():
            if not HotSpot.topic_set_check(topic_set):
                ok = False          
        return ok
            
        
    @staticmethod
    def topic_set_check(topic_set):
        ok = True
        for topic in topic_set.nodes:
            if not HotSpot.requirements_check(topic.reqs):
                ok = False
        return ok

    @staticmethod
    def requirements_check(reqs):
        ok = True
        for req in reqs:
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
