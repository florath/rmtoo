'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  cvs1 output
  
  Comma separated file output

  (c) 2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.StdOutputParams import StdOutputParams
from rmtoo.lib.ExecutorTopicContinuum import ExecutorTopicContinuum
from rmtoo.lib.CreateMakeDependencies import CreateMakeDependencies
from rmtoo.lib.logging import tracer
from rmtoo.lib.LaTeXMarkup import LaTeXMarkup

class csv1(StdOutputParams, ExecutorTopicContinuum,
           CreateMakeDependencies):

    def __init__(self, oconfig):
        '''Create a graph output object.'''
        tracer.debug("Called.")
        StdOutputParams.__init__(self, oconfig)
        CreateMakeDependencies.__init__(self)
        self.__fd = None
        
    def topic_continuum_pre(self, _topics_continuum):
        '''Do the preprocessing: create the empty document.'''
        self.__fd = file(self._output_filename, "w")

    def topic_continuum_sort(self, vcs_commit_ids, topic_sets):
        '''Because gantt2 can only one topic continuum,
           the latest (newest) is used.'''
        return [ topic_sets[vcs_commit_ids[-1].get_commit()] ]

    def topic_continuum_post(self, _topics_continuum):
        '''Do the postprocessing: create the file.'''
        # Close the (hopefully) last open
        self.__fd.close()

    def topic_pre(self, topic):
        '''This is called in the Topic pre-phase.'''
        self.__fd.write('topic,"%s"\n' % topic.name)
        
    def requirement_set_sort(self, list_to_sort):
        '''Sort by id.'''
        return sorted(list_to_sort, key=lambda r: r.id)

    def requirement(self, req):
        '''Output the given requirement.'''
        desc = LaTeXMarkup.replace_txt(
                    req.get_value("Description").get_content())
        priority = req.get_value("Priority")
        effort = "n/a"
        if req.is_val_av_and_not_null("Effort estimation"):
            effort = req.get_value("Effort estimation")
            
        status = ""
        if req.is_val_av_and_not_null("Status"):
            status = req.get_value("Status").get_output_string()
            
        testcases = ""
        if req.is_val_av_and_not_null("Test Cases"):
            testcases = req.get_value("Test Cases")

        rationale = ""
        if req.is_val_av_and_not_null("Rationale"):
            rationale = LaTeXMarkup.replace_txt(
                                req.get_value("Rationale").get_content())
        
        self.__fd.write('requirement,"%s",%4.3f,"%s","%s","%s","%s","%s"\n' 
                        % (status, priority, effort, req.get_id(), desc,
                           rationale, ", ".join(testcases)))
