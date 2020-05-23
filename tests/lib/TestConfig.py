'''
 rmtoo
   Free and Open Source Requirements Management Tool

 Common methods for handling test configuration.

 (c) 2011-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals

from rmtoo.lib.configuration.Cfg import Cfg


class TestConfig(Cfg):

    def set_solved_by(self):
        self.set_value('requirements.input.dependency_notation', "Solved by")

    def set_depends_on(self):
        self.set_value('requirements.input.dependency_notation', "Depends on")

    def set_output_cfg(self):
        self.set_value("topic_root_node", "TopicRootNode")
