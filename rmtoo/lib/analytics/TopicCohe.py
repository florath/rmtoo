#
# Analytics: TopicCohe
#
#  Coherence of one topic.
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

class TopicCohe:

    @staticmethod
    def add_releation(tcnt, ltopic, topic):
        # If not there, add the initial count [0, 0]
        for t in ltopic, topic:
            if not t in tcnt:
                tcnt[t] = [0, 0]

        # Add releation to both directions
        if ltopic==topic:
            # 2: because it is one incoming and one outgoing
            tcnt[topic][0] += 2
        else:
            tcnt[topic][1] += 1
            tcnt[ltopic][1] += 1


    @staticmethod
    def count(tcnt, topic, li):
        for l in li:
            TopicCohe.add_releation(tcnt, l.tags["Topic"], topic)

    # For each topic count the inner links and the outer links
    @staticmethod
    def run(reqs):
        ok = True

        tcnt = {}
        # There is only the need to count either the incoming or
        # outgoing
        for _, req in reqs.reqs.iteritems():
             TopicCohe.count(tcnt, req.tags["Topic"], req.incoming)

        for k, t in tcnt.iteritems():
            if t[0]<=t[1]:
                reqs.analytics["TopicCohe"] = \
                    [-10, ["%s: Topic coherence inadequate: "
                           "inner %d / outer %d"
                           % (k, t[0], t[1])]]

        return ok
