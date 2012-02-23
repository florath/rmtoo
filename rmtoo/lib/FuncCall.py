'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Helper for generic function call.
   
 (c) 2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

class FuncCall:
    
    def __init__(self):
        '''Hide the constructor.'''
        assert False
    
    @staticmethod
    def pcall(obj, method_name, *args):
        '''Possible CALL a method.
           Call the method with the method_name on the given object
           with the given arguments - if the method exists.'''
        if not hasattr(obj, method_name):
            # No way to call the method.
            return
        return getattr(obj, method_name)(*args)