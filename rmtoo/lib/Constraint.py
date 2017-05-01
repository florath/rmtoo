'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Constraint class

 (c) 2011-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals

from rmtoo.lib.BaseRMObject import BaseRMObject
from rmtoo.lib.InputModuleTypes import InputModuleTypes


class Constraint(BaseRMObject):
    """Defines a constraint"""

    # pylint: disable=too-many-arguments
    def __init__(self, content, rid, file_path, mods, config):
        BaseRMObject.__init__(self, InputModuleTypes.ctstag, content,
                              rid, mods,
                              config, "constraints", file_path)
