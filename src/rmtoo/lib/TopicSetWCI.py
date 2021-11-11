'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Collection of topics.
  This class contains a 'plain' topic set - with additional information
  about the commit.

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from rmtoo.lib.logging import tracer
from rmtoo.lib.FuncCall import FuncCall


class TopicSetWCI(object):
    '''Class for storing topic set and it's commit info.
       This is implemented in the way it is (using fields
       instead of inheritance) because in this way the topic_set
       object can be reused (and stored in the object cache).'''

    def __init__(self, topic_set, commit_info):
        '''Creates an object with the given values.'''
        self.__topic_set = topic_set
        self.__commit_info = commit_info

    def get_topic_set(self):
        '''Returns the underlaying topic set.'''
        return self.__topic_set

    def get_commit_info(self):
        '''Returns the commit info.'''
        return self.__commit_info

    def execute(self, executor, func_prefix):
        '''Execute the parts which are needed for TopicsSet.'''
        tracer.debug("Calling pre.")
        FuncCall.pcall(executor, func_prefix + "topic_set_pre", self)
        tracer.debug("Calling sub topic.")
        self.__topic_set.execute(executor, func_prefix)
        tracer.debug("Calling post.")
        FuncCall.pcall(executor, func_prefix + "topic_set_post", self)
        tracer.debug("Finished.")

    def create_makefile_name(self, name, topicn):
        """Create the name that can be used in a Makefile"""
        return self.__topic_set.create_makefile_name(name, topicn)

    def get_master_topic(self):
        """Returns the one and only master topic"""
        return self.__topic_set.get_master_topic()

    def get_requirement_set(self):
        """Get the Topic's Requirements Set"""
        return self.__topic_set.get_requirement_set()
