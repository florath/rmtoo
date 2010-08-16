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
    def add_releation(tcnt, topic, ltopic):
        # If not there, add the initial count [0, 0]
        for t in ltopic.name, topic.name:
            if not t in tcnt:
                tcnt[t] = [0, 0]

        # Add releation to both directions if the topic is the same or
        # a parent of the topic.

        # Iff self: add a 3!
        if ltopic==topic:
            tcnt[topic.name][0] += 3
        elif ltopic.is_self_of_ancient(topic):
            # 2: because it is one incoming and one outgoing
            tcnt[topic.name][0] += 2
        else:
            tcnt[topic.name][1] += 1
            tcnt[ltopic.name][1] += 1


    @staticmethod
    def count(tcnt, topic_set, topic_name, li):
        topic = topic_set.get_named_node(topic_name)
        for l in li:
            # Count only, if the requirement is in the current chosen
            # topic set.
            ltopic = l.tags["Topic"]
            if topic_set.get_named_node_no_throw(ltopic)!=None:
                TopicCohe.add_releation(tcnt, topic,
                                        topic_set.get_named_node(ltopic))

    # Return the correct topic set to analyze
    @staticmethod
    def get_topic_set(config, topics):
        return topics.get(config.analytics_specs["topics"])

    # For each topic count the inner links and the outer links
    @staticmethod
    def run(config, reqs, topics):
        topic_set = TopicCohe.get_topic_set(config, topics)

        ok = True

        tcnt = {}
        # There is only the need to count either the incoming or
        # outgoing.
        # Use the requirements from the topic here.
        for req in topics.get(config.analytics_specs["topics"]).get_all_reqs():
             TopicCohe.count(tcnt, topic_set, req.tags["Topic"], req.incoming)

        for k, t in tcnt.iteritems():
            if t[0]<=t[1]:
                reqs.analytics["TopicCohe"] = \
                    [-10, ["%s: Topic coherence inadequate: "
                           "inner %d / outer %d"
                           % (k, t[0], t[1])]]

        return ok
