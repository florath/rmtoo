'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
 Create Make Dependencies
   
 (c) 2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from rmtoo.lib.FuncCall import FuncCall

class CreateMakeDependencies:
    
    @staticmethod
    def cmad(topic_continuum_set):
        '''Create the cmad (Create MAke Dependencies)
           For the whole continuum set.'''
        FuncCall.pcall(