'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Coherence of one topic.

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from six import iteritems

from rmtoo.lib.analytics.Base import Base
from rmtoo.lib.analytics.Result import Result
from rmtoo.lib.logging import tracer


class TopicCohe(Base):
    '''Class for checking topic coherence.'''

    def __init__(self, _):
        '''Sets up the TopicCohe object for use.'''
        Base.__init__(self)
        self.__req2topics = {}
        self.__tcnt = {}

    def __add_req2topic(self, req_id, topic):
        '''Add req_id / topic to cache.'''
        if req_id not in self.__req2topics:
            self.__req2topics[req_id] = []
        self.__req2topics[req_id].append(topic)

    def topic_pre(self, topic):
        '''Collect the relation between requirement and topic.'''
        req_set = topic.get_requirement_set()
        if req_set is None:
            return
        for req_id in req_set.get_all_requirement_ids():
            self.__add_req2topic(req_id, topic)

    def _get_tcnt(self):
        '''Returns the internal state.
           This is only used by the unit tests.'''
        return self.__tcnt

    def _add_topic_relation(self, topic_a, topic_b):
        '''Add the relation between topic_a and topic_b.
           (Here only one _ is used because this is used by the unit tests.)'''
        # If not there, add the initial count [0, 0]
        for topic in [topic_a.name, topic_b.name]:
            if topic not in self.__tcnt:
                self.__tcnt[topic] = [0, 0]

        # Add relation to both directions if the topic is the same or
        # a parent of the topic.

        # Iff self: add a 3!
        if topic_a == topic_b:
            self.__tcnt[topic_a.name][0] += 3
        elif topic_a.is_self_of_ancient(topic_b):
            # 2: because it is one incoming and one outgoing
            self.__tcnt[topic_b.name][0] += 2
        else:
            self.__tcnt[topic_a.name][1] += 1
            self.__tcnt[topic_b.name][1] += 1

    def __eval_link(self, req_a, req_b):
        '''Add all the links between all topics of req_a and req_b.'''
        # If either one of the requirements is not in the topic,
        # skip this step
        if req_a.get_id() not in self.__req2topics \
           or req_b.get_id() not in self.__req2topics:
            tracer.debug("One of the requirements is not in the topic - "
                         "skipping evaluation [%s] [%s]",
                         req_a.get_id(), req_b.get_id())
            return

        for topic_a in self.__req2topics[req_a.get_id()]:
            for topic_b in self.__req2topics[req_b.get_id()]:
                self._add_topic_relation(topic_a, topic_b)

    def topic_set_post(self, topic_set):
        '''This is call in the TopicsSet post-phase.'''
        # pylint: disable=consider-iterating-dictionary
        for req_id in self.__req2topics.keys():
            req_a = topic_set.get_topic_set().get_requirement_set().\
                       get_requirement(req_id)
            for req_b in req_a.incoming:
                self.__eval_link(req_a, req_b)

        for topic, cnt in iteritems(self.__tcnt):
            if cnt[0] <= cnt[1]:
                self.add_result(Result(
                    "TopicCohe", topic,
                    - 10, ["%s: Topic coherence inadequate: "
                           "inner %d / outer %d"
                           % (topic, cnt[0], cnt[1])]))
