'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
 Common methods for handling test configuration.
   
 (c) 2011 by flonatel GmhH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.configuration.Cfg import Cfg

class TestConfig(Cfg):

    def __init__(self):
        Cfg.__init__(self)

    def set_solved_by(self):
        self.set_value('requirements.input.dependency_notation', "Solved by")

    def set_depends_on(self):
        self.set_value('requirements.input.dependency_notation', "Depends on")
