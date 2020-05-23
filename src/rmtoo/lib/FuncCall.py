'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Helper for generic function call.

 (c) 2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from rmtoo.lib.logging import tracer


# pylint: disable=too-few-public-methods
class FuncCall(object):
    """Calls a function - if available"""

    @staticmethod
    def pcall(obj, method_name, *args):
        '''Possible CALL a method.

        Call the method with the method_name on the given object
        with the given arguments - if the method exists.
        '''
        tracer.debug("pcall: trying to call [%s]", method_name)
        if not hasattr(obj, method_name):
            tracer.debug("pcall: method [%s] does not exist.", method_name)
            # No way to call the method.
            return
        tracer.debug("pcall: calling method [%s]", method_name)
        return getattr(obj, method_name)(*args)
