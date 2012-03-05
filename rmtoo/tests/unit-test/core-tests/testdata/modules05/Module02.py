'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Test Module
   
 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.digraph.Digraph import Digraph

class Module02(Digraph.Node):
    depends_on = ["Module01"]

    def __init__(self, config):
        Digraph.Node.__init__(self, "Module02")

    def get_type_set(self):
        return set(["reqtag", ])

    def set_modules(self, mods):
        pass

    def rewrite(self, rid, reqs):
        return "SameTag", None
