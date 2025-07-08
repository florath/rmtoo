'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Constraints handling

 (c) 2010-2012,2017,2025 by flonatel GmbH & Co. KG / Andreas Florath

 For licensing details see COPYING
'''


from rmtoo.lib.logging import tracer


class Constraints(object):
    '''Helper functions for constraint handling.'''

    @staticmethod
    def set_default_values(cfg):
        '''Set the default values to the given configuration.'''
        cfg.set_value('constraints.search_dirs',
                      ['/usr/share/pyshared/rmtoo/collection/constraints'])

    @staticmethod
    def collect(topic_set):
        '''Collect all the constraints which are used in the given topic.'''
        tracer.debug("Called for topic set.")
        cnsts = {}

        if topic_set is None:
            assert False

        for ctr, cval in \
                topic_set.get_requirement_set().get_constraints().items():
            tracer.debug("Add constraint [%s]", ctr)
            cnsts[ctr] = cval
        tracer.debug("Finished; size [%d]", len(cnsts))
        return cnsts
