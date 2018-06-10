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

from rmtoo.lib.VerificationStatusParser import (
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
        parse_file_with_requirement(None, None, None, 'dummyParser')
        assert excinfo.lid == 91


def rmttest_negative_test_xunit_no_file():
    "Non-existing file will fail"
    i = parse_file_with_requirement(None, None, None, 'xunit')
    assert i is None


"""Define tests that parse the file defined hereafter."""
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME_SIMPLE = os.path.join(FILE_DIR, "RMTTest-ReqStatusParser.simple.xml")


def rmttest_negative_test_simple_example():
    "Simple query to xunit output with property req"
    filename = FILE_NAME_SIMPLE
    ret = parse_file_with_requirement("dummyReq", None, filename, 'xunit')
    # File exists
    assert ret is not None
    # dummyReq does not exists
    assert not bool(ret)


def rmttest_positive_test_StatusAssigned_req(record_property):
    """Simple query to xunit output with property req. Simplest status
    parser test at the moment.

    """
    record_property("req", "StatusExternalParser-db77a22c")
    filedir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(filedir, "RMTTest-ReqStatusParser.simple.xml")
    ret = parse_file_with_requirement("StatusAssigned", None,
                                      filename, 'xunit')
    assert ret
    assert len(ret._raw_results) == 2


def rmttest_positive_test_StatusExternal_deadbeef_req(record_property):
    "Simple query to xunit output with property req and correct hash"
    record_property("req", "ReqToBeDefinedEventually")
    filedir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(filedir, "RMTTest-ReqStatusParser.simple.xml")
    ret = parse_file_with_requirement("StatusExternal", "deadbeef",
                                      filename, 'xunit')
    assert ret
    assert len(ret._raw_results) == 1


def rmttest_negative_test_StatusExternal_deadcoffee_req(record_property):
    "Simple query to xunit output with property req and incorrect hash"
    record_property("req", "ReqToBeDefinedEventually")
    filedir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(filedir, "RMTTest-ReqStatusParser.simple.xml")
    ret = parse_file_with_requirement("StatusExternal", "deadcoffee",
                                      filename, 'xunit')
    assert not bool(ret)


def rmttest_positive_test_failed_test():
    "Simple query to xunit output with property req"
    filedir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(filedir, "RMTTest-ReqStatusParser.simple.xml")
    ret = parse_file_with_requirement("FailsAlways", None, filename, 'xunit')
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
    ret = parse_config_with_requirement(
        "StatusAssigned", None, SIMPLE_CONFIG)
    assert ret.rid_match is True
    assert bool(ret) is True
    assert ret.get_output_string() == "passed"


def rmttest_positive_test_config_parser_2(record_property):
    """Simple configuration test with rid *StatusAssigned* to xunit output
    with property req. Test with two files parsed twice for
    simplicity.

    """
    record_property("req", "ReqToBeDefinedEventually2")
    ret = parse_config_with_requirement(
        "StatusAssigned", None, DOUBLE_CONFIG)
    assert ret.rid_match is True
    assert bool(ret) is True
    assert len(ret.result) == 2
    assert ret.get_output_string() == "passed"


def rmttest_positive_test_config_parser_3(record_property):
    """Simple configuration test with rid *FailsAlways* to xunit output
    with property req. Make sure the test fails and is reported appropriately.

    """
    record_property("req", "ReqToBeDefinedEventually2")
    ret = parse_config_with_requirement(
        "FailsAlways", None, DOUBLE_CONFIG)
    assert ret.rid_match is True
    assert bool(ret) is False
    assert len(ret.result) == 2
    assert ret.get_output_string() == "failed"


def rmttest_positive_test_config_parser_4(record_property):
    """Simple configuration test with rid not found in xunit output.
    Test shouldn't fail but report open

    """
    record_property("req", "ReqToBeDefinedEventually2")
    ret = parse_config_with_requirement(
        "InexistingReqForTestPurposes", None, DOUBLE_CONFIG)
    assert ret.rid_match is False
    assert bool(ret) is False
    assert len(ret.result) == 2  # Parsing two files
    assert ret.get_output_string() == "open"
