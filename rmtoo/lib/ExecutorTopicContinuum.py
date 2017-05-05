'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Base class for handling different executions in and
  beneath the TopicContinuum.

 (c) 2011-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''


# Because of the nature that mostly all methods are only dummy
# implementations, there is no way of 'self' using.
# pylint: disable=no-self-use
class ExecutorTopicContinuum(object):
    """Base Executor class for TopicContinuum

    This implements the Executor defaults for the TopicContinuum
    which does mostly nothing.

    It is not possible to have this as a ABC - because there is no
    need for the inherited classes to overwrite all the methods.
    """

    def topic_continuum_pre(self, _topic_continuum):
        '''This is called in the TopicsContinuum pre-phase.
           This is typically the phase where all the output modules
           will be used.'''
        return

    def topic_continuum_sort(self, vcs_commit_ids, topic_sets):
        '''Sort the list of continuums.
           The commits are the commits in chronological order.
           The vcs_ids are the ids in chronological order.
           The topic_sets is a dictionary where the id is the key.
           The default implementation here takes all topic sets in
           the chronological order.'''
        res = []
        for vcs_id in vcs_commit_ids:
            res.append(topic_sets[vcs_id.get_commit()])
        return res

    def topic_continuum_post(self, _topics_continuum):
        '''This is called in the TopicsContinuum post-phase.'''
        return

    def topic_set_pre(self, _topic_set):
        '''This is called in the TopicsSet pre-phase.'''
        return

    def topic_set_sort(self, list_to_sort):
        '''Sort the list of contimuums.'''
        return list_to_sort

    def topic_set_post(self, _topic_set):
        '''This is called in the TopicsSet post-phase.'''
        return

    def topic_pre(self, _topic):
        '''This is called in the Topic pre-phase.'''
        return

    def topic_name(self, _name):
        '''Called when the Name tag appears in the topic.'''
        return

    def topic_text(self, _text):
        '''Called when there is text to be outputted.'''
        return

    def topic_sub_pre(self, _subtopic):
        '''Called when before the subtopic is called.'''
        return

    def topic_sub_post(self, _subtopic):
        '''Called when after the subtopic is called.'''
        return

    def topic_post(self, _topic):
        '''This is called in the Topic post-phase.'''
        return

    def requirement_set_pre(self, _requirement_set):
        '''This is called in the RequirementSet pre-phase.'''
        return

    def requirement_set_sort(self, list_to_sort):
        '''Sort the list of requirement set.'''
        return list_to_sort

    def requirement_set_post(self, _requirement_set):
        '''This is called in the RequirementSet post-phase.'''
        return

    def requirement(self, _requirement):
        '''This is called in the Requirement phase.'''
        return
