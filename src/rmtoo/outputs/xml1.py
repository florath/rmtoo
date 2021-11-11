'''
 rmtoo
   Free and Open Source Requirements Management Tool

 This is a first version of xml output.

 (c) 2011,2017 by flonatel

 For licensing details see COPYING
'''
from xml.dom.minidom import Document
from rmtoo.lib.Requirement import Requirement


# ToDo: Can this class be removed? There are (currently) no tests.
class Xml1:

    def __init__(self, topic_set, param):
        self.topic_set = topic_set
        self.output_filename = param[0]

    # ToDo: Needed? (param is not defined!)
    # def set_topics(self, topics):
    #    self.topic_set = topics.get(param[1])

    # Create MAkefile Dependencies
    def cmad(self, reqscont, ofile):
        ofile.write("%s: ${REQS}\n\t${CALL_RMTOO}\n" % (self.output_filename))

    @staticmethod
    def name2xmltag(name):
        return name.replace(" ", "_").lower()

    def output_req(self, req, doc, sobj):
        # Create the req element
        req_xml = doc.createElement("requirement")
        sobj.appendChild(req_xml)

        for t in ["Name", "Priority", "Effort estimation",
                  "Invented by", "Invented on", "Description",
                  "Rationale", "Factor", "Owner", ]:
            tm = doc.createElement(self.name2xmltag(t))
            req_xml.appendChild(tm)

            if req.tags[t] is not None:
                tn = doc.createTextNode(str(req.tags[t]))
            tm.appendChild(tn)

        if "Status" in req.tags:
            tm = doc.createElement("status")
            req_xml.appendChild(tm)
            if req.tags["Status"] == Requirement.st_not_done:
                tn = doc.createTextNode("not done")
            else:
                tn = doc.createTextNode("finished")
            tm.appendChild(tn)

        if "Type" in req.tags:
            tm = doc.createElement("type")
            req_xml.appendChild(tm)
            if req.tags["Type"] == Requirement.rt_master_requirement:
                tn = doc.createTextNode("master requirement")
            elif req.tags["Type"] == Requirement.rt_initial_requirement:
                tn = doc.createTextNode("initial requirement")
            elif req.tags["Type"] == Requirement.rt_design_decision:
                tn = doc.createTextNode("design decision")
            elif req.tags["Type"] == Requirement.rt_requirement:
                tn = doc.createTextNode("requirement")
            else:
                assert(False)
            tm.appendChild(tn)

        if "Class" in req.tags:
            tm = doc.createElement("class")
            req_xml.appendChild(tm)
            if req.tags["Class"] == Requirement.ct_implementable:
                tn = doc.createTextNode("implementable")
            elif req.tags["Class"] == Requirement.ct_selected:
                tn = doc.createTextNode("selected")
            else:
                tn = doc.createTextNode("detailable")
            tm.appendChild(tn)

    def output_reqset(self, reqset, doc, sobj):
        # Create the reqset element
        reqset_xml = doc.createElement("reqset")
        sobj.appendChild(reqset_xml)

        for v in self.topic_set.all_reqs:
            self.output_req(v, doc, reqset_xml)

    def output(self, reqscont):
        # Create the minidom document
        doc = Document()

        # This outputs only the current set of requirements (not the
        # whole history).
        reqscont_xml = doc.createElement("reqscont")
        doc.appendChild(reqscont_xml)

        self.output_reqset(reqscont.base_requirement_set, doc, reqscont_xml)

        with open(self.output_filename, "w") as fd:
            fd.write(doc.toxml())
