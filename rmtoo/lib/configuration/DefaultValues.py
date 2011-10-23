'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
 Default values for the new configuration.
   
 (c) 2011 by flonatel GmhH & Co. KG

 For licensing details see COPYING
'''

# TODO: Better way is to have simple classes handling the config
# (and the default values)
class DefaultValues:

    def __init__(self):
        '''Hidden constructor for utility class.'''
        assert(False)

    @staticmethod
    def set_default_values(cfg):
        cfg.set_value('constraints.search_dirs',
                      ['/usr/share/pyshared/rmtoo/collection/constraints'])
