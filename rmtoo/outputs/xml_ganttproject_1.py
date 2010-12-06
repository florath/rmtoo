#
# xml ganttproject output class
#
# This is a first version of xml output.
# This must be seen as alpha software, because there are some base
# problems which might make the use of this output module sensless:
# * How to sort things? ganttproject has a fixed order of tasks. The
#   requirements for rmtoo are unsorted.
# * Where to get the start date from?
# * It is impossible to have sub-tasks: in rmtoo one requirement can
#   depend from many other requirements in ganttproject one task can
#   only be a subtask of another task.
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from xml.dom.minidom import Document
from rmtoo.lib.Requirement import Requirement

class xml_ganttproject_1:

    def __init__(self, param):
        print("+++ Warning: The output module 'xml_ganttproject_1' "
              "is deprecated")
        print("+++ Warning: Limited support will end 2011-03-15")

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
        for node in req.incoming:
            xml_depend = doc.createElement("depend")
            xml_depend.setAttribute("id", str(self.get_req_id(node.id)))
            # There are some default attrs
            xml_depend.setAttribute("type", "2")
            xml_depend.setAttribute("difference", "0")
            xml_depend.setAttribute("hardness", "Strong")
            xml_task.appendChild(xml_depend)

        sobj.appendChild(xml_task)

    def output_reqset(self, reqset, doc, sobj):
        for v in sorted(self.topic_set.reqset.nodes, key = lambda r: r.id):
            self.output_req(v, reqset, doc, sobj)

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
        self.output_reqset(reqscont.continuum_latest(), doc, xml_project)

        fd = file(self.output_filename, "w")
        fd.write(doc.toprettyxml())
        fd.close()

