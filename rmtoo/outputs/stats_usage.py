'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
 Usage statistics.
   
 (c) 2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.StdOutputParams import StdOutputParams
from rmtoo.lib.ExecutorTopicContinuum import ExecutorTopicContinuum
from rmtoo.lib.logging import tracer
from rmtoo.lib.CreateMakeDependencies import CreateMakeDependencies

class stats_usage(StdOutputParams, ExecutorTopicContinuum,
                  CreateMakeDependencies):
    
    def __init__(self, oconfig):
        '''Create a usage statistics object.'''
        tracer.debug("Called.")
        StdOutputParams.__init__(self, oconfig)
        CreateMakeDependencies.__init__(self)
        self.__ofile = None
        self.__stats = {}
        tracer.debug("Finished.")
    
    def __inc(self, name, num=1):
        '''Increments the given name by the given number.
           If the name does not exists, it is created.'''
        if name not in self.__stats:
            self.__stats[name] = 0
        self.__stats[name] += num
    
    def topic_continuum_pre(self, _topics_continuum_set):
        tracer.debug("Called.")
        self.__inc("TopicContinuum")
        
    def topic_continuum_post(self, _topics_continuum_set):
        '''Output all the collected statistics.
           This is the last-to-get phase of this object.'''
        tracer.info("Usage statistics: %s" % self.__stats)
        
    def topic_set_pre(self, _topic_set):
        tracer.debug("Called.")
        self.__inc("TopicSet")

    def topic_pre(self, _topic):
        tracer.debug("Called.")
        self.__inc("Topic")

    def topic_sub_pre(self, _sub_topic):
        tracer.debug("Called.")
        self.__inc("SubTopic")

    def requirement_set_pre(self, _req_set):
        tracer.debug("Called.")
        self.__inc("RequirmentSet")

    def requirement(self, _req):
        tracer.debug("Called.")
        self.__inc("Requirment")
        