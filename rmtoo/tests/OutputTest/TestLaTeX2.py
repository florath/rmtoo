'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Unit test for Latex output
  
 (c) 2011-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import os

from rmtoo.outputs.latex2 import latex2
from rmtoo.lib.Topic import Topic
from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.storagebackend.RecordEntry import RecordEntry
from rmtoo.lib.CE3Set import CE3Set
from rmtoo.lib.CE3 import CE3
from rmtoo.lib.RequirementSet import RequirementSet
from rmtoo.lib.RequirementStatus import RequirementStatusFinished
from rmtoo.lib.RequirementDNode import RequirementDNode
from rmtoo.lib.ClassType import ClassTypeImplementable
from rmtoo.tests.lib.TestVCS import TestVCS
from rmtoo.tests.lib.TestConfig import TestConfig
from rmtoo.tests.lib.TestTopicSet import TestTopicSet
from rmtoo.tests.lib.Utils import create_tmp_dir, delete_tmp_dir

class TestOutputLaTeX2:

    def test_neg_01(self):
        "LaTeX output: check invalid tag in topic"

        tcfg = TestConfig()
        tcfg.set_output_cfg()

        tvcs = TestVCS(tcfg)
        tfile = tvcs.get_tfile1()

        dg = Digraph()

        topic = Topic(dg, "TName", tvcs, None, tfile, None)
        topic.t = [RecordEntry("CompleteleOther", "My content"), ]
        tmpdir = create_tmp_dir()

        rset = RequirementSet(tcfg)

        ttopic_set = TestTopicSet(rset)

        mconfig = {"output_filename": os.path.join(tmpdir, "TestLateX2Out.tex")}
        l2 = latex2(mconfig)

        try:
            l2.topic_set_pre(ttopic_set)
            topic.execute(l2, "")
            assert(False)
        except RMTException, rmte:
            pass
        l2.topic_set_post(ttopic_set)
        delete_tmp_dir(tmpdir)

    def test_neg_02(self):
        "LaTeX output: check invalid tag in requirement output config"

        tcfg = TestConfig()
        tcfg.set_output_cfg()

        tvcs = TestVCS(tcfg)
        tfile = tvcs.get_tfile1()

        tmpdir = create_tmp_dir()
        mconfig = { "req_attributes": ["Status", "Class", "DoesNotExists"],
                    "output_filename": os.path.join(tmpdir, "TestLateX2Out.tex")}

        l2 = latex2(mconfig)
        req = Requirement(None, "TestReq", None, None, None)
        req.values = {}
        req.values["Name"] = RecordEntry("Name", "my name")
        req.values["Type"] = Requirement.rt_requirement
        req.values["Description"] = RecordEntry("Description", "my desc")
        req.values["Status"] = RequirementStatusFinished(
                None, "rid", "finished:meiner:2011-04-15:4h")
        req.values["Class"] = ClassTypeImplementable()

        dnreq = RequirementDNode(req)

        ce3set = CE3Set()
        ce3 = CE3()
        ce3set.insert("TestReq", ce3)

        rset = RequirementSet(tcfg)
        ttopic_set = TestTopicSet(rset)

        try:
            l2.topic_set_pre(None)
            dnreq.execute(l2, "")
            assert(False)
        except RMTException, rmte:
            pass
        l2.topic_set_post(ttopic_set)
        delete_tmp_dir(tmpdir)

