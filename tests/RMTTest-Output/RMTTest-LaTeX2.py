'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for Latex output

 (c) 2011-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals

import os

from rmtoo.outputs.latex2 import latex2
from rmtoo.lib.Topic import Topic
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.Requirement import Requirement, RequirementType
from rmtoo.lib.storagebackend.RecordEntry import RecordEntry
from rmtoo.lib.CE3Set import CE3Set
from rmtoo.lib.CE3 import CE3
from rmtoo.lib.RequirementSet import RequirementSet
from rmtoo.lib.RequirementStatus import RequirementStatusFinished
from rmtoo.lib.ClassType import ClassTypeImplementable
from TestVCS import TestVCS
from TestConfig import TestConfig
from TestTopicSet import TestTopicSet
from Utils import create_tmp_dir, delete_tmp_dir


class RMTTestOutputLaTeX2:

    def rmttest_neg_01(self):
        "LaTeX output: check invalid tag in topic"

        tcfg = TestConfig()
        tcfg.set_output_cfg()

        tvcs = TestVCS(tcfg)
        tfile = tvcs.get_tfile1()

        topic = Topic(None, u"TName", tvcs, None, tfile, None)
        topic.t = [RecordEntry(u"CompleteleOther", u"My content"), ]
        tmpdir = create_tmp_dir()

        rset = RequirementSet(tcfg)

        ttopic_set = TestTopicSet(rset)

        mconfig = {"output_filename":
                   os.path.join(tmpdir, "TestLateX2Out.tex")}
        out_l2 = latex2(mconfig)

        try:
            out_l2.topic_set_pre(ttopic_set)
            topic.execute(out_l2, "")
            assert False
        except RMTException:
            pass
        out_l2.topic_set_post(ttopic_set)
        delete_tmp_dir(tmpdir)

    def rmttest_neg_02(self):
        "LaTeX output: check invalid tag in requirement output config"

        tcfg = TestConfig()
        tcfg.set_output_cfg()

        # ToDo: is this needed? tvcs = TestVCS(tcfg)
        # ToDo: is this needed? tfile = tvcs.get_tfile1()

        tmpdir = create_tmp_dir()
        mconfig = {"req_attributes": ["Status", "Class", "DoesNotExists"],
                   "output_filename":
                   os.path.join(tmpdir, "TestLateX2Out.tex")}

        out_l2 = latex2(mconfig)
        req = Requirement(None, u"TestReq", None, None, None)
        req.values = {}
        req.values[u"Name"] = RecordEntry(u"Name", u"my name")
        req.values[u"Type"] = RequirementType.requirement
        req.values[u"Description"] = RecordEntry(u"Description", u"my desc")
        req.values[u"Status"] = RequirementStatusFinished(
            None, u"rid", u"finished:meiner:2011-04-15:4h")
        req.values[u"Class"] = ClassTypeImplementable()

        ce3set = CE3Set()
        ce3 = CE3()
        ce3set.insert(u"TestReq", ce3)

        rset = RequirementSet(tcfg)
        ttopic_set = TestTopicSet(rset)

        try:
            out_l2.topic_set_pre(None)
            req.execute(out_l2, "")
            assert False
        except RMTException:
            pass
        out_l2.topic_set_post(ttopic_set)
        delete_tmp_dir(tmpdir)
