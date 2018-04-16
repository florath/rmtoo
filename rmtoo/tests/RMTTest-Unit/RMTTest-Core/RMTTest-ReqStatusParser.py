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

from rmtoo.lib.RMTException import RMTException

from rmtoo.lib.RequirementStatusParser import (
    parse_file_with_requirement, parse_config_with_requirement)


"""
def rmttest_negative_test_by_design(record_property):
    "Non-existing parser fails, needed to generate sample XML"
    record_property("req", "FailsAlways")
    assert False
"""


def rmttest_negative_test_parser_not_existing():
    "Non-existing parser fails"
    with pytest.raises(RMTException) as excinfo:
        parse_file_with_requirement(None, None, 'dummyParser')
        assert excinfo.lid == 91


def rmttest_negative_test_xunit_no_file():
    "Non-existing file will fail"
    i = parse_file_with_requirement(None, None, 'xunit')
    assert i is None


"""Define tests that parse the file defined hereafter."""
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME_SIMPLE = os.path.join(FILE_DIR, "RMTTest-ReqStatusParser.simple.xml")


def rmttest_negative_test_simple_example():
    "Simple query to xunit output with property req"
    filename = FILE_NAME_SIMPLE
    ret = parse_file_with_requirement("dummyReq", filename, 'xunit')
    # File exists
    assert ret is not None
    # dummyReq does not exists
    assert not ret


def rmttest_positive_test_StatusAssigned_req(record_property):
    "Simple query to xunit output with property req"
    record_property("req", "ReqToBeDefinedEventually")
    filedir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(filedir, "RMTTest-ReqStatusParser.simple.xml")
    ret = parse_file_with_requirement("StatusAssigned", filename, 'xunit')
    assert ret
    assert len(ret._raw_results) == 2


def rmttest_positive_test_failed_test():
    "Simple query to xunit output with property req"
    filedir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(filedir, "RMTTest-ReqStatusParser.simple.xml")
    ret = parse_file_with_requirement("FailsAlways", filename, 'xunit')
    assert not ret


"""Parse a configuration for one or more files"""
SIMPLE_CONFIG = {'files': {"UT": (FILE_NAME_SIMPLE, "xunit")}}
DOUBLE_CONFIG = {'files': {"UT": (FILE_NAME_SIMPLE, "xunit"),
                           "SPE": (FILE_NAME_SIMPLE, "xunit")}}


def rmttest_positive_test_config_parser_1(record_property):
    """Simple configuration test with rid *StatusAssigned* to xunit output
    with property req

    """
    record_property("req", "ReqToBeDefinedEventually2")
    ret = parse_config_with_requirement("StatusAssigned", SIMPLE_CONFIG)
    assert ret.rid_match is True
    assert bool(ret) is True


def rmttest_positive_test_config_parser_2(record_property):
    """Simple configuration test with rid *StatusAssigned* to xunit output
    with property req. Test with two files parsed twice for
    simplicity.

    """
    record_property("req", "ReqToBeDefinedEventually2")
    ret = parse_config_with_requirement("StatusAssigned", DOUBLE_CONFIG)
    assert ret.rid_match is True
    assert bool(ret) is True
    assert len(ret.result) == 2
