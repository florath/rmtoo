'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Collection of collection of collection of topics.
  The continuum holds all the different versions of TopicSetCollections
  from the whole time of being.
   
 (c) 2011 by flonatel GmhH & Co. KG

 For licensing details see COPYING
'''

class TopicContinuum:
    '''Class holding all the available TopicSetCollections
       of the past and possible the current.'''

    def __init__(self, config):
        '''Sets up a TopicContinuum for use.'''
        self.config = config

        # This is the list of all requirements sets - ordered by time.
        # (The newest versions are on top - sorted backwards.)
        ## COMMENT!?!?
        self.ordered_ids = []
        # The continuum itself - accessable by the version.
        ## COMMENT!?!?
        self.continuum = {}

        self.init_continuum()

