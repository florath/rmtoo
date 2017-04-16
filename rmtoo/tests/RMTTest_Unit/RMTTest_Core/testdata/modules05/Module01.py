'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Test Module

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.InputModuleTypes import InputModuleTypes


class Module01(Digraph.Node):
    depends_on = []

    def __init__(self, config):
        Digraph.Node.__init__(self, "Module01")

    def get_type_set(self):
        return set([InputModuleTypes.reqtag, ])

    def set_modules(self, mods):
        pass

    def rewrite(self, rid, reqs):
        return "SameTag", None
