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

class Analytics:
    '''Collection class which calls the other analytics modules.'''

    def __init__(self):
        '''Hide the constructor for the utility class.'''
        assert False

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
