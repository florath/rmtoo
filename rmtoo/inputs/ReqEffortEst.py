'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Effort estimation attribute

 (c) 2010-2012,2017,2020 by flonatel GmbH & Co. KG

 SPDX-License-Identifier: GPL-3.0-or-later

 This file is part of rmtoo.

 rmtoo is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 rmtoo is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with rmtoo.  If not, see <https://www.gnu.org/licenses/>.
'''

#
# The 'Effort estimation' must be one of
#   0, 1, 2, 3, 5, 8, 13, 21, 34
#

from rmtoo.lib.ReqTagGeneric import ReqTagGeneric
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.InputModuleTypes import InputModuleTypes


class ReqEffortEst(ReqTagGeneric):
    '''Implements the Effort estimation attribute.'''
    valid_values = [0, 1, 2, 3, 5, 8, 13, 21, 34]

    def __init__(self, config):
        ReqTagGeneric.__init__(self, config, "Effort estimation",
                               set([InputModuleTypes.reqtag, ]))

        self.__value_check = self.get_config().get_value_default(
            "requirements.effort_estimation_values_check", True)

    def rewrite(self, rid, req):
        '''This attrbute is optional.'''
        tag, value = self.handle_optional_tag(req)
        if value is None:
            return tag, value

        ival = int(value.get_content())
        if self.__value_check \
           and self.valid_values and ival not in self.valid_values:
            raise RMTException(4, "%s: effort estimation must be one of %s"
                               % (rid, self.valid_values))
        return tag, ival
