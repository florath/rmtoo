'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Effort estimation attribute

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
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

    def rewrite(self, rid, req):
        '''This attrbute is optional.'''
        tag, value = self.handle_optional_tag(req)
        if value is None:
            return tag, value

        ival = int(value.get_content())
        if ival not in self.valid_values:
            raise RMTException(4, "%s: effort estimation must be one of %s"
                               % (rid, self.valid_values))
        return tag, ival
