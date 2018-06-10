'''Parsing status of a requirement from an external file

For licensing details see COPYING

'''
import os
import re
import xml.etree.ElementTree as ET

from stevedore import extension

from rmtoo.lib.RMTException import RMTException


class VerificationStatusParserFactory(object):
    """Factory handling parser parsing with stevedore"""
    def __init__(self):
        self.__plugin_manager = extension.ExtensionManager(
            namespace='rmtoo.input.requirement_status_parser',
            invoke_on_load=False)

    def parse(self, rid, rhash, filename, parser):
        """Parse file with given parser"""
        parser = self._get_parser(rid, rhash, filename, parser)
        return parser.parse()

    def _get_parser(self, rid, rhash, filename, parser):
        try:
            return self.__plugin_manager[parser].plugin(
                rid, rhash, filename)
        except KeyError:
            raise RMTException(91, "%s: Status tag invalid '%s'" % (
                rid, parser))


class VerificationStatusParserFileInfo(object):
    def __init__(self):
        self.rid_match = False
        self.bool_status = False
        self._raw_results = None

    def __bool__(self):
        return self.rid_match and self.bool_status

    def __nonzero__(self):
        return self.__bool__()

    def get_output_string_short(self):
        if not self.rid_match:
            return "open"
        elif self.bool_status:
            return "passed"
        else:
            return "failed"


class VerificationStatusParserXUnit(object):
    """Parse XUnit output where the *requirement id* is either a property
    of the testcase with name="req" and the value="req_id". This is
    the preferred variant.

    Alternatively the *requirement id* can be the a suffix to the testcase.
    This is not supported at the moment however.

    rhash -- Hash uniquely identifying the requirement. Ignored if None.
    """
    def __init__(self, rid, rhash, filename):
        self._filename = filename
        self._rid = rid
        self._hash = rhash

    def parse(self):
        if not self._filename or (not os.path.isfile(self._filename)):
            return None
        req_status = VerificationStatusParserFileInfo()

        found_testcases = self._parse_xml_node()
        if not found_testcases:
            return req_status
        else:
            req_status.rid_match = True

        req_status._raw_results = found_testcases
        req_status.bool_status = True
        for testcase in found_testcases:
            property_req = testcase.find("properties/property[@name='req']")
            req_id = property_req.get('value')
            if self._hash is not None:
                a = re.match(self._rid + "." + self._hash, req_id)
                if not a:
                    req_status.bool_status = False
            failure = testcase.findall('failure')
            if failure:
                req_status.bool_status = False
        return req_status

    def _parse_xml_node(self):
        tree = ET.parse(self._filename)
        root = tree.getroot()

        testcases = []
        for i in root.findall(".//properties/property[@name='req']/../.."):
            if i:
                property_req = i.find("properties/property[@name='req']")
                req_id = property_req.get('value')
                if re.match(r"\b" + self._rid + r"\b", req_id):
                    testcases.append(i)
        return testcases


PARSE_FACTORY = VerificationStatusParserFactory()


def parse_file_with_requirement(rid, rhash, filename, parser):
    """ Parse a file with a parser that has been registered in stevedore"""
    return PARSE_FACTORY.parse(rid, rhash, filename, parser)


def parse_config_with_requirement(rid, rhash, config):
    return VerificationStatusParserRidInfo(rid, rhash, config)


class VerificationStatusParserRidInfo(object):
    """Contains verification information about requirement id

    :ivar rid_match: anything matched, i.e., if False, requirement is
    untouched.
    :ivar parsed_status: pass/fail criterion (if rid_match
    is True).

    """

    def __bool__(self):
        return self.rid_match and self.parsed_status

    def __nonzero__(self):
        return self.__bool__()

    def __init__(self, rid, rhash, config):
        self.rid_match = False
        self.parsed_status = True
        self.result = dict()

        for file_id_short, file_info in config['files'].items():
            parsed_file = parse_file_with_requirement(
                rid, rhash, file_info[0], file_info[1])
            if parsed_file is not None:
                self.rid_match = self.rid_match or parsed_file.rid_match
            self.parsed_status = self.parsed_status and bool(parsed_file)
            self.result[file_id_short] = parsed_file

    def get_output_string_short(self):
        if not self.rid_match:
            return "open"
        elif self:
            return "passed"
        else:
            return "failed"

    def get_output_string(self):
        """This might be subject to change soon.

        The idea is to provide detailed information where to find the
        close-out reference.

        """
        return self.get_output_string_short()

    def get_file_status_string_short(self, file_id_short):
        result = self.result[file_id_short]
        return result.get_output_string_short()

    def get_status_failed(self):
        """Return true if requirement id matched and not passed.

        This indicates that action is required by the user.

        """
        if self._verification_status.rid_match and (
                not self._verification_status.parsed_status):
            return True
        else:
            return False
