'''
 rmtoo
   Free and Open Source Requirements Management Tool

  InputModules
   Some constants which are used by different input modules.

 (c) 2010-2011,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from enum import Enum


# pylint: disable=too-few-public-methods
class InputModuleTypes(Enum):
    """Models the possible different types of input modules"""
    reqtag = 0
    reqdeps = 1
    ctstag = 2
    testcase = 3
