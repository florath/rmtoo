'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Heuristics to check the quality of the requirements. 
   
 (c) 2011 by flonatel GmhH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.analytics.HotSpot import HotSpot
from rmtoo.lib.analytics.DescWords import DescWords
from rmtoo.lib.analytics.ReqTopicCohe import ReqTopicCohe
from rmtoo.lib.analytics.TopicCohe import TopicCohe
from rmtoo.lib.Executor import Executor
from rmtoo.lib.logging.EventLogging import tracer

class Analytics(Executor):
    '''Collection class which calls the other analytics modules.'''

    def __init__(self, config):
        '''Hide the constructor for the utility class.'''
        self.__config = config
        self.__desc_words = DescWords(config)
        self.__hot_spot = HotSpot(config)
        self.__req_topic_cohe = ReqTopicCohe(config)
        # The req topics cohe is counted in the following way:
        # 1) topic_set_pre: values are set to 0
        # 2) topic_pre: values are updated
        # 3) topic_set_post: values are evaluated
        self.__topic_cohe = None
        # The results of the different analytics modules are collected
        # here.
        self.__results = []
        # If one result of one module failed, success is set to False. 
        self.__success = True

    def topics_set_pre(self, topics_set):
        '''This is call in the TopicsSet pre-phase.'''
        pass

    def topics_set_post(self, topics_set):
        '''This is call in the TopicsSet post-phase.'''
        # TODO: evaluate _topic_cohe
        assert False

    def requirement(self, requirement):
        '''This is call in the Requirement phase.'''
        tracer.debug("called: name [%s]" % requirement.get_id())

        for ana_module in [self.__desc_words, self.__hot_spot,
                           self.__req_topic_cohe]:
            success, findings = ana_module.check_requirement(
                            requirement.get_id(), requirement)
            if not success:
                self.__success = False
            self.__results.extend(findings)

    def write_analytics_result(self, mstderr):
        '''Writes all the results to the given stream.'''
        for result in self.__results:
            if result.get_value() < 0:
                mstderr.write("%s\n" % result)

    # The argument to the analytics modules is the (latest) set of
    # requirements.  (It makes sense only to check them.)
    @staticmethod
    def run(config, topicsc):
        '''The argument to the analytics modules is the (latest) set of
           requirements.  (It makes sense only to check them.)'''
        eval_result = True
        findings = []

        for ana_class in HotSpot, DescWords, ReqTopicCohe, TopicCohe:
            ana_obj = ana_class(config)
            check_result, lfindings = ana_obj.check(topicsc)
            findings.extend(lfindings)
            print("FINDINGS UNTIL NOW [%s]" % findings)
            if not check_result:
                eval_result = False

        return eval_result, findings
