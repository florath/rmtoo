'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Definition of a test-case.

 (c) 2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals

from rmtoo.lib.BaseRMObject import BaseRMObject
from rmtoo.lib.InputModuleTypes import InputModuleTypes


class TestCase(BaseRMObject):
    """Object modelling a TestCase"""

    # pylint: disable=too-many-arguments
    def __init__(self, content, rid, file_path, mods, config):
        BaseRMObject.__init__(self, InputModuleTypes.testcase, content,
                              rid, mods,
                              config, "testcases", file_path)
