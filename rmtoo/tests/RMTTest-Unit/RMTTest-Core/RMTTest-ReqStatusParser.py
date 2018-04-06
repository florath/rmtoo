'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for ReqStatusParser

 (c) 2018 Kristoffer

 For licensing details see COPYING
'''
from __future__ import unicode_literals
import os
import pytest

from rmtoo.inputs.ReqStatus import ReqStatus
from rmtoo.lib.RMTException import RMTException
from rmtoo.tests.lib.ReqTag import create_parameters
from rmtoo.lib.storagebackend.RecordEntry import RecordEntry

from rmtoo.lib.RequirementStatusParser import parse_file_with_requirement

def rmttest_negative_test_parser_fails():
    "Non-existing parser fails"
    with pytest.raises(RMTException) as excinfo:
        parse_file_with_requirement(None, None, 'dummyParser')
        assert excinfo.lid == 91

def rmttest_negative_test_simple_example():
    "Simple query to xunit output with property req"
    filedir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(filedir, "RMTTest-ReqStatusParser.simple.xml")
    ret = parse_file_with_requirement("dummyReq", filename, 'xunit')
    # File exists
    assert ret is not None
    # dummyReq does not exists
    assert not ret
