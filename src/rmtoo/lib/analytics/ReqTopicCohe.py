'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Coherence of one requirement to the used topic.

 (c) 2010-2011,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from rmtoo.lib.analytics.Result import Result
from rmtoo.lib.analytics.Base import Base


class ReqTopicCohe(Base):
    """Class representing the coherence of a requirement within a topic"""

    def __init__(self, _):
        '''Sets up the ReqTopicCohe object for use.'''
        Base.__init__(self)

    @staticmethod
    def count_in_out_topic(topic, lst):
        '''Count the number of incoming and outgoing links.'''
        in_cnt = 0
        out_cnt = 0
        for element in lst:
            if element.get_value("Topic") == topic:
                in_cnt += 1
            else:
                out_cnt += 1
        return in_cnt, out_cnt

    def requirement(self, requirement):
        '''Check the topic coherence.'''
        it_in, it_out = ReqTopicCohe.count_in_out_topic(
            requirement.get_value("Topic"), requirement.incoming)
        ot_in, ot_out = ReqTopicCohe.count_in_out_topic(
            requirement.get_value("Topic"), requirement.outgoing)

        # This is only problematic, if the in and out are not
        # really coherent to the topic.
        if it_in < it_out and ot_in < ot_out:
            self.add_result(Result(
                'ReqTopicCoherence',
                requirement.get_id(),
                - 10, ["Requirement topic coherence inadequate: "
                       "incoming %d/%d, outgoing %d/%d"
                       % (it_in, it_out, ot_in, ot_out)]))
            self.set_failed()
