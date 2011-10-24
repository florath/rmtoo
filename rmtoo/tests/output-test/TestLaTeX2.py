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
from rmtoo.lib.RequirementStatus import RequirementStatusNotDone, \
    RequirementStatusAssigned, RequirementStatusFinished
from rmtoo.lib.ClassType import ClassTypeImplementable

class TestOutputLaTeX2:

    def test_positive_01(self):
        "LaTeX output: check config"

        mconfig = { "req_attributes": ["Id", "Priority", ],
                    "output_filename": "/please/ignore/me"}

        l = latex2(None, mconfig)
        assert(l.config == mconfig)

    def test_neg_01(self):
        "LaTeX output: check invalid tag in topic"

        fd = StringIO.StringIO()
        topic = Topic(None, "TName", None, None, None)
        topic.t = [RecordEntry("CompleteleOther", "My content"), ]
        mconfig = {"output_filename": "/please/ignore/me"}
        l2 = latex2(None, mconfig)
        try:
            l2.output_latex_topic(fd, topic, None)
            assert(False)
        except RMTException, rmte:
            pass

    def test_neg_02(self):
        "LaTeX output: check invalid tag in requirement output config"

        fd = StringIO.StringIO()

        mconfig = { "req_attributes": ["Status", "Class", "DoesNotExists"],
                    "output_filename": "/please/ignore/me"}

        l2 = latex2(None, mconfig)
        req = Requirement(None, "TestReq", None, None, None)
        req.values = {}
        req.values["Name"] = RecordEntry("Name", "my name")
        req.values["Description"] = RecordEntry("Description", "my desc")
        req.values["Status"] = RequirementStatusFinished(
                None, "rid", "finished:meiner:2011-04-15:4h")
        req.values["Class"] = ClassTypeImplementable()

        ce3set = CE3Set()
        ce3 = CE3()
        ce3set.insert("TestReq", ce3)

        try:
            l2.output_requirement(fd, req, 2, ce3set)
            assert(False)
        except RMTException, rmte:
            pass

