'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Base class for Analytics.
  
  This class provides some basic functionality and the interface
  for the analytics classes. 
   
 (c) 2010-2011 by flonatel GmhH & Co. KG

 For licensing details see COPYING
'''

import abc

class Base:
    '''Base class for all analytics checks.
       This class provides the basic methods and infrastructure
       to handle the analytics.  The check itself must be 
       implemented using the 'check_requirement()' method.'''
    __metaclass__ = abc.ABCMeta

    def __init__(self, config):
        '''Initializes a new object with the given configuration.'''
        self.config = config

    @abc.abstractmethod
    def check_requirement(self, topic_path, req):
        '''Checks the given requirement.'''
        assert topic_path
        assert req
        assert False

    def check_requirements_array(self, topic_path, requirements_array):
        '''Checks all the requirements from the given array.'''
        eval_result = True
        findings = []
        # TODO: Sort
        for req in requirements_array:
            # TODO: if (req already checked) continue
            check_result, lfindings = \
                self.check_requirement(topic_path, req)
            findings.extend(lfindings)
            if not check_result:
                eval_result = False
        return eval_result, findings

    # TODO: create the complete name for logging.
    def check_topic_set(self, topic_set_name, topic_set):
        '''Checks the given topic set.
           All topic sets are checked, even if one failed to
           evaluate.'''
        eval_result = True
        findings = []
        # TODO: Sort
        for topic in topic_set.nodes:
            topic_path = topic_set_name + "." + topic.name
            print("TOPIC PATH [%s]" % topic_path)
            check_result, lfindings = \
                self.check_requirements_array(topic_path, topic.reqs)
            findings.extend(lfindings)
            if not check_result:
                eval_result = False
        return eval_result, findings

    def check(self, topicsc):
        '''Checks the given topic set collection.
           This runs through all the different set collections -
           even if one failed to evaluate.  This is done, that
           in one run possible all errors are found.'''
        eval_result = True
        findings = []
        # TODO: Sort
        for topic_set_name, topic_set in topicsc.get_topic_sets().iteritems():
            print("Check Topic Set [%s]" % topic_set_name)
            check_result, lfindings = \
                self.check_topic_set(topic_set_name, topic_set)
            findings.extend(lfindings)
            if not check_result:
                eval_result = False
        return eval_result, findings
