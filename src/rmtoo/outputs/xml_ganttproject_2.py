'''
 rmtoo
   Free and Open Source Requirements Management Tool

  xml ganttproject2 output class

 This is a second version of xml ganttproject output.
 This must be seen as alpha software, because there are some base
 problems which might make the use of this output module sensless:
 * How to sort things? ganttproject has a fixed order of tasks. The
   requirements for rmtoo are unsorted.
 * Where to get the start date from?
 * Sub-tasks are done in the way, that each (sub-)topic opens up a
   new level.  The last (innermost) level are the requirements of the
   appropriate (sub)-topic.
 Output handler graph.

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals

import io

from xml.dom.minidom import Document
from rmtoo.lib.Markup import Markup
from rmtoo.lib.RequirementStatus import \
    RequirementStatusAssigned, RequirementStatusFinished
from rmtoo.lib.StdOutputParams import StdOutputParams
from rmtoo.lib.ExecutorTopicContinuum import ExecutorTopicContinuum
from rmtoo.lib.logging import tracer
from rmtoo.lib.CreateMakeDependencies import CreateMakeDependencies


class xml_ganttproject_2(StdOutputParams, ExecutorTopicContinuum,
                         CreateMakeDependencies):

    def __init__(self, oconfig):
        '''Create a graph output object.'''
        tracer.debug("Called.")
        StdOutputParams.__init__(self, oconfig)
        CreateMakeDependencies.__init__(self)
        self.__fd = None
        self.effort_factor = self._config.get_value_default('effort_factor', 1)
        self.req_ids = {}
        self.next_id = 1
        self.__xml_doc = None
        self.__xml_obj_stack = []
        self.__markup = Markup("txt")

    def get_req_id(self, name):
        '''Get an id: if the req is not there a new id will be generated.'''
        if name in self.req_ids:
            return self.req_ids[name]
        self.req_ids[name] = self.next_id
        self.next_id += 1
        return self.req_ids[name]

    def topic_continuum_pre(self, _topics_continuum):
        '''Do the preprocessing: create the empty document.'''
        # Create the minidom document
        self.__xml_doc = Document()

        xml_project = self.__xml_doc.createElement("project")
        self.__xml_doc.appendChild(xml_project)

        # This is needed: if not given, on the left side there is
        # nothing displayed.
        xml_taskdisplaycolumns = \
            self.__xml_doc.createElement("taskdisplaycolumns")
        xml_project.appendChild(xml_taskdisplaycolumns)
        for display_col in [["tpd3", 125], ["tpd4", 25], ["tpd5", 25]]:
            xml_tpd = self.__xml_doc.createElement("displaycolumn")
            xml_tpd.setAttribute("property-id", display_col[0])
            xml_tpd.setAttribute("width", str(display_col[1]))
            xml_taskdisplaycolumns.appendChild(xml_tpd)
        self.__xml_obj_stack.append(xml_project)

    def topic_continuum_sort(self, vcs_commit_ids, topic_sets):
        '''Because gantt2 can only one topic continuum,
           the latest (newest) is used.'''
        return [topic_sets[vcs_commit_ids[-1].get_commit()]]

    def topic_continuum_post(self, _topics_continuum):
        '''Do the postprocessing: create the file.'''
        # Close the (hopefully) last open
        assert len(self.__xml_obj_stack) == 1
        self.__xml_doc.appendChild(self.__xml_obj_stack[0])

        # Write it out.
        with io.open(self._output_filename, "w",
                     encoding="utf-8") as self.__fd:
            self.__fd.write(self.__xml_doc.toprettyxml())

    def topic_pre(self, topic):
        '''This is called in the Topic pre-phase.'''
        xml_task = self.__xml_doc.createElement("task")
        xml_task.setAttribute("name", topic.name)
        xml_task.setAttribute("id", str(self.get_req_id(
                    "TOPIC-" + topic.name)))
        self.__xml_obj_stack.append(xml_task)
        tracer.debug("Finished; xml document stack length [%s]" %
                     len(self.__xml_obj_stack))

    def topic_post(self, _topic):
        '''This is called in the Topic post-phase.'''
        # Add the xml_task to the current document
        xml_task = self.__xml_obj_stack.pop()
        self.__xml_obj_stack[-1].appendChild(xml_task)
        tracer.debug("Finished; xml document stack length [%s]" %
                     len(self.__xml_obj_stack))

    def requirement_set_sort(self, list_to_sort):
        '''Sort by id.'''
        return sorted(list_to_sort, key=lambda r: r.get_id())

    def requirement(self, req):
        '''Output the given requirement.'''
        # There is the need for a unique numeric id
        xml_task = self.__xml_doc.createElement("task")
        xml_task.setAttribute("name", req.get_id())
        xml_task.setAttribute("id", str(self.get_req_id(req.get_id())))
        if req.is_val_av_and_not_null("Effort estimation"):
            # The Effort Estimation is only rounded: ganntproject can
            # only handle integers as duration
            xml_task.setAttribute(
                "duration",
                str(int(req.get_value("Effort estimation")
                        * self.effort_factor + 1)))

        # The Status (a la complete) must be given in percent.
        # Currently rmtoo supports only two states: not done (~0) or
        # finished (~100)
        if req.is_val_av_and_not_null("Status"):
            complete_val = "0"
            if isinstance(req.get_status(), RequirementStatusFinished):
                complete_val = "100"
            elif isinstance(req.get_status(), RequirementStatusAssigned):
                complete_val = "50"
            xml_task.setAttribute("complete", complete_val)

        # Notes
        # Add the description and if available also the rationale and
        # note.
        notes = "== Description ==\n"
        notes += self.__markup.replace(
            req.get_value("Description").get_content())

        if req.is_val_av_and_not_null("Rationale"):
            notes += "\n\n== Rationale ==\n"
            notes += self.__markup.replace(
                req.get_value("Rationale").get_content())

        if req.is_val_av_and_not_null("Note"):
            notes += "\n\n== Note ==\n"
            notes += self.__markup.replace(
                req.get_value("Note").get_content())

        xml_note = self.__xml_doc.createElement("notes")
        xml_text = self.__xml_doc.createCDATASection(notes)
        xml_note.appendChild(xml_text)
        xml_task.appendChild(xml_note)

        # Dependencies
        for node in req.incoming:
            xml_depend = self.__xml_doc.createElement("depend")
            xml_depend.setAttribute("id", str(self.get_req_id(node.get_id())))
            # There are some default attrs
            xml_depend.setAttribute("type", "2")
            xml_depend.setAttribute("difference", "0")
            xml_depend.setAttribute("hardness", "Strong")
            xml_task.appendChild(xml_depend)

        self.__xml_obj_stack[-1].appendChild(xml_task)

    def cmad_topic_continuum_pre(self, _):
        '''Write out the one and only dependency to all the requirements.'''
        tracer.debug("Called.")
        CreateMakeDependencies.write_reqs_dep(self._cmad_file,
                                              self._output_filename)
