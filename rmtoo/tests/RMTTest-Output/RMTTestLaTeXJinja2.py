'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for Latex Jinja2 output

 (c) 2017 Kristoffer Nordstroem

 For licensing details see COPYING
'''
from __future__ import unicode_literals

import os

from rmtoo.outputs.LatexJinja2 import LatexJinja2 as latex2
from rmtoo.lib.Topic import Topic
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.Requirement import Requirement, RequirementType
from rmtoo.lib.storagebackend.RecordEntry import RecordEntry
from rmtoo.lib.CE3Set import CE3Set
from rmtoo.lib.CE3 import CE3
from rmtoo.lib.RequirementSet import RequirementSet
from rmtoo.lib.RequirementStatus import RequirementStatusFinished
from rmtoo.lib.ClassType import ClassTypeImplementable
from rmtoo.tests.lib.TestVCS import TestVCS
from rmtoo.tests.lib.TestConfig import TestConfig
from rmtoo.tests.lib.TestTopicSet import TestTopicSet
from rmtoo.tests.lib.Utils import create_tmp_dir, delete_tmp_dir


class RMTTestOutputLaTeXJinja2(object):
    "Test-Class for the templated latex output class"

    @classmethod
    def setup_class(self):
        self.__tmpdir = create_tmp_dir()
        self.__def_mconfig = {
            "output_filename":
            os.path.join(self.__tmpdir, "TestLateXJinja2Out.tex"),
            "template_path":
            os.path.join(os.environ['contribdir'],
                         'latex', 'LatexJinja2')}

    @classmethod
    def teardown_class(self):
        if self.__tmpdir:
            delete_tmp_dir(self.__tmpdir)

    def rmttest_neg_01(self):
        "LaTeX output: check invalid tag in topic"

        tcfg = TestConfig()
        tcfg.set_output_cfg()

        tvcs = TestVCS(tcfg)
        tfile = tvcs.get_tfile1()

        topic = Topic(None, u"TName", tvcs, None, tfile, None)
        topic.t = [RecordEntry(u"CompleteleOther", u"My content"), ]

        rset = RequirementSet(tcfg)

        ttopic_set = TestTopicSet(rset)

        mconfig = self.__def_mconfig
        req_proc = latex2(mconfig)

        try:
            req_proc.topic_set_pre(ttopic_set)
            topic.execute(req_proc, "")
            assert False
        except RMTException:
            pass
        req_proc.topic_set_post(ttopic_set)

    def rmttest_def_req(self):
        "LaTeX output: compare output to defined value"
        exp_value = r"""
\paragraph{my name}

\hypertarget{TestReq}{TestReq} 
\label{TestReq}

my desc

\textbf{Rationale:} 

\textbf{Note:} 







\par{\small \begin{center}
\begin{tabular}{rlrlrl}
   Id: & TestReq               & Priority: &           & Owner: &  \\
   Invented on: &  & Invented by: &  & Status: & finished (meiner, 2011-04-15, 4 h) \\
   Class: & implementable
\end{tabular}\end{center}
}
""" # noqa

        tcfg = TestConfig()
        tcfg.set_output_cfg()

        mconfig = self.__def_mconfig
        mconfig['req_attributes'] = ["Status", "Class", "DoesNotExists"]

        req_proc = latex2(mconfig)
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

        ''' This is here for future? use.
        rset = RequirementSet(tcfg)
        ttopic_set = TestTopicSet(rset)
        '''

        req_text = req_proc._get_requirement(req)
        try:
            assert req_text == exp_value
        except AssertionError:
            import difflib
            diff = difflib.ndiff(
                req_text.splitlines(True),
                exp_value.splitlines(True))
            print(''.join(diff))
            raise Exception("The template is not equal to it's expected value")
