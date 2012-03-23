'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Definition of a test-case.
   
 (c) 2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from rmtoo.lib.BaseRMObject import BaseRMObject
from rmtoo.lib.InputModuleTypes import InputModuleTypes

class TestCase(BaseRMObject):
    
     def __init__(self, content, rid, file_path, mods, config):
        BaseRMObject.__init__(self, InputModuleTypes.testcase, content, 
                              rid, mods,
                              config, "testcases", file_path)

