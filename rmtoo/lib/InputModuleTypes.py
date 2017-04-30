'''
 rmtoo
   Free and Open Source Requirements Management Tool

  InputModules
   Some constants which are used by different input modules.

 (c) 2010-2011,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from enum import Enum


class InputModuleTypes(Enum):
    reqtag = 0
    reqdeps = 1
    ctstag = 2
    testcase = 3
