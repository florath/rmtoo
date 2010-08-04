#
# Analytics: ReqTopicCohe
#
#  Coherence of one requirement to the used topic.
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

class ReqTopicCohe:

    # Count the number of incoming and outgoing links: once the 
    @staticmethod
    def count_in_out_topic(topic, li):
        in_cnt = 0 
        out_cnt = 0
        for l in li:
            if l.tags["Topic"]==topic:
                in_cnt += 1
            else:
                out_cnt += 1
        return in_cnt, out_cnt

    @staticmethod
    def run(config, reqs, topics):
        ok = True
        for _, req in reqs.reqs.iteritems():
            it_in, it_out = ReqTopicCohe.count_in_out_topic(
                req.tags["Topic"], req.incoming)
            ot_in, ot_out = ReqTopicCohe.count_in_out_topic(
                req.tags["Topic"], req.outgoing)
            
            # This is only problematic, if the in and out are not
            # really coherent to the topic.
            if it_in<it_out and ot_in<ot_out:
                req.analytics["ReqTopicCohe"] = \
                    [-10, ["Requirement topic coherence inadequate: "
                           "incoming %d/%d, outgoing %d/%d"
                           % (it_in, it_out, ot_in, ot_out)]]
                ok = False

        return ok
