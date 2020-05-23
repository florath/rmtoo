'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Test Module

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.InputModuleTypes import InputModuleTypes


class Module01:
    def __init__(self, config):
        pass

    def get_type_set(self):
        return set([InputModuleTypes.reqtag, ])
