#
# xml ganttproject2 output class
#
# This is a second version of xml ganttproject output.
# This must be seen as alpha software, because there are some base
# problems which might make the use of this output module sensless:
# * How to sort things? ganttproject has a fixed order of tasks. The
#   requirements for rmtoo are unsorted.
# * Where to get the start date from?
# * Sub-tasks are done in the way, that each (sub-)topic opens up a
#   new level.  The last (innermost) level are the requirements of the
#   appropriate (sub)-topic.
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from xml.dom.minidom import Document
from rmtoo.lib.Requirement import Requirement

class xml_ganttproject_2:

    def __init__(self, param):
        self.topic_name = param[0]
        self.output_filename = param[1]
        self.effot_factor = param[2]
        self.req_ids = {}
        self.next_id = 1

    # Create Makefile Dependencies
    def cmad(self, reqscont, ofile):
        ofile.write("%s: ${REQS}\n\t${CALL_RMTOO}\n" % (self.output_filename))

    def set_topics(self, topics):
        self.topic_set = topics.get(self.topic_name)

    # Get an id: if the req is not there a new id will be generated.
    def get_req_id(self, name):
        if name in self.req_ids:
            return self.req_ids[name]
        self.req_ids[name] = self.next_id
        self.next_id += 1
        return self.req_ids[name] 

    def output_req(self, req, reqset, doc, sobj):
        # There is the need for a unique numeric id
        xml_task = doc.createElement("task")
        xml_task.setAttribute("name", req.id)
        xml_task.setAttribute("id", str(self.get_req_id(req.id)))
        if "Effort estimation" in req.tags \
                and req.tags["Effort estimation"]!=None:
            # The Effort Estimation is only rounded: ganntproject can
            # only handle integers as duration
            xml_task.setAttribute(
                "duration", 
                str(int(req.tags["Effort estimation"]*self.effot_factor+1)))

        # The Status (a la complete) must be given in percent.
        # Currently rmtoo supports only two states: not done (~0) or
        # finished (~100)
        if "Status" in req.tags and req.tags["Status"]!=None:
            v = "0"
            if req.tags["Status"]==Requirement.st_finished:
                v = "100"
            xml_task.setAttribute("complete", v)
            
        # Dependencies
        for node in req.outgoing:
            xml_depend = doc.createElement("depend")
            xml_depend.setAttribute("id", str(self.get_req_id(node.id)))
            # There are some default attrs
            xml_depend.setAttribute("type", "2")
            xml_depend.setAttribute("difference", "0")
            xml_depend.setAttribute("hardness", "Strong")
            xml_task.appendChild(xml_depend)

        sobj.appendChild(xml_task)

    # Run through all the topics
    # (Deep first search / output)
    def output_reqset(self, reqset, doc, sobj):
        self.output_topic(self.topic_set.get_master(), reqset, doc, sobj)

    # First output all the requirements in this topic - then all the
    # subtopics. 
    def output_topic(self, topic, reqset, doc, sobj):
        # Add a new level (task)
        xml_task = doc.createElement("task")
        xml_task.setAttribute("name", topic.name)
        xml_task.setAttribute("id", str(self.get_req_id(
                    "TOPIC-" + topic.name)))

        # Run through all the requirements and output them
        for req in topic.reqs:
            self.output_req(req, reqset, doc, xml_task)
        # After this have a look at the (sub-)topics
        for st in topic.outgoing:
            self.output_topic(st, reqset, doc, xml_task)

        # Add the xml_task to the current document
        sobj.appendChild(xml_task)

    def output(self, reqscont):
        # Create the minidom document
        doc = Document()

        xml_project = doc.createElement("project")
        doc.appendChild(xml_project)

        # This is needed: if not given, on the left side there is
        # nothing displayed. 
        xml_taskdisplaycolumns = doc.createElement("taskdisplaycolumns")
        xml_project.appendChild(xml_taskdisplaycolumns)
        for s in [["tpd3", 125] , ["tpd4", 25], ["tpd5", 25]]:
            xml_tpd = doc.createElement("displaycolumn")
            xml_tpd.setAttribute("property-id", s[0])
            xml_tpd.setAttribute("width", str(s[1]))
            xml_taskdisplaycolumns.appendChild(xml_tpd)
        
        # Output all the 'tasks' (i.e. requirements)
        self.output_reqset(reqscont.continnum_latest(), doc, xml_project)

        fd = file(self.output_filename, "w")
        fd.write(doc.toprettyxml())
        fd.close()

