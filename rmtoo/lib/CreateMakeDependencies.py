'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
 Create Make Dependencies
   
 (c) 2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from rmtoo.lib.Executor import Executor

class CreateMakeDependencies(Executor):

    def __init__(self, filename):
        '''Initializes the cmad object.'''
        self.__output_filename = filename

    @staticmethod
    def call(topic_continuum_set, cmad_obj):
        '''Create the cmad (Create MAke Dependencies)
           For the whole continuum set.'''
        topic_continuum_set.execute(cmad_obj, "cmad_")

    def cmad_topics_continuum_set_pre(self, topics_continuum_set):
        '''Open the file.'''
        self.__ofile = file(self.__output_filename, "w")
#        # Write out the REQS=
#        latest_topicsc.cmad_write_reqs_list(ofile)
#        # Write out the rest
#        latest_topicsc.create_makefile_dependencies(ofile)

    def cmad_topics_continuum_set_post(self, topics_continuum_set):
        '''Close the file.'''
        self.__ofile.close()

