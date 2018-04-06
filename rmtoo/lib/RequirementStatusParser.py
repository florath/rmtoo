'''Parsing status of a requirement from an external file

For licensing details see COPYING

'''
from stevedore import extension

from rmtoo.lib.RMTException import RMTException

class RequirementStatusParserFactory(object):
    """Factory handling parser parsing with stevedore"""
    def __init__(self):
        self.__plugin_manager = extension.ExtensionManager(
            namespace='rmtoo.input.requirement_status_parser',
            invoke_on_load=False)

    def parse(self, rid, filename, parser):
        """Parse file with given parser"""
        parser = self._get_parser(rid, filename, parser)
        return parser.parse()

    def _get_parser(self, rid, filename, parser):
        try:
            return self.__plugin_manager[parser].plugin(
                rid, filename)
        except KeyError:
            raise RMTException(91, "%s: Status tag invalid '%s'" % (rid, parser))


class RequirementStatusParserXUnit(object):
    """Parse XUnit output where the *requirement id* is either a property
    of the testcase with name="req" and the value="req_id". This is
    the preferred variant.

    Alternatively the *requirement id* can be the a suffix to the testcase.

    """
    def __init__(self, rid, filename):
        self._filename = filename
        self._rid = rid

    def parse(self):
        with open(self._filename, 'r', encoding='utf-8') as fh:
            return []
        return None


PARSE_FACTORY = RequirementStatusParserFactory()

def parse_file_with_requirement(rid, filename, parser):
    """ Parse a file with a parser that has been registered in stevedore"""
    return PARSE_FACTORY.parse(rid, filename, parser)
