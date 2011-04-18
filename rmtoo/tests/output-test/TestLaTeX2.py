#
# rmtoo 
#   Free and Open Source Requirements Management Tool
#
# Unit test for RequirementSet
#
# (c) 2010-2011 on flonatel
#
# For licencing details see COPYING
#

import StringIO

from rmtoo.outputs.latex2 import latex2
from rmtoo.lib.Topic import Topic
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.storagebackend.RecordEntry import RecordEntry
from rmtoo.lib.CE3Set import CE3Set
from rmtoo.lib.CE3 import CE3

class TestOutputLaTeX2:

    def test_positive_01(self):
        "LaTeX output: check config"

        mconfig = { "req_attributes": ["Id", "Priority",]}

        l = latex2([None, None, mconfig])
        assert(l.config==mconfig)

    def test_neg_01(self):
        "LaTeX output: check invalid tag in topic"

        fd = StringIO.StringIO()
        topic = Topic(None, "TName", None, None)
        topic.t = [RecordEntry("CompleteleOther", "My content"), ]
        l2 = latex2([None, None])
        try:
            l2.output_latex_topic(fd, topic, None)
            assert(False)
        except RMTException, rmte:
            pass

    def test_neg_02(self):
        "LaTeX output: check invalid tag in requirement output config"

        fd = StringIO.StringIO()

        mconfig = { "req_attributes": ["Status", "Class", "DoesNotExists"]}
        
        l2 = latex2([None, None, mconfig])
        req = Requirement(None, "TestReq", None, None, None, None)
        req.values = {}
        req.values["Name"] = RecordEntry("Name", "my name")
        req.values["Description"] = RecordEntry("Description", "my desc")
        req.values["Status"] = RecordEntry("Status", "my status")
        req.values["Class"] = RecordEntry("Class", "my class")

        ce3set = CE3Set()
        ce3 = CE3()
        ce3set.insert("TestReq", ce3)
               
        try:
            l2.output_requirement(fd, req, 2, ce3set)
            assert(False)
        except RMTException, rmte:
            pass

