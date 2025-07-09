'''
 rmtoo
   Free and Open Source Requirements Management Tool

  YAML Record Input / Output class

  This is the parser and output module for YAML file format.

 (c) 2025 by flonatel GmbH & Co. KG / Andreas Florath

 SPDX-License-Identifier: GPL-3.0-or-later

 For licensing details see COPYING
'''
import yaml
from rmtoo.lib.Encoding import Encoding
from rmtoo.lib.storagebackend.Record import Record
from rmtoo.lib.storagebackend.yamlfile.YamlParser import YamlParser
from rmtoo.lib.storagebackend.yamlfile.YamlRecordEntry import YamlRecordEntry
from rmtoo.lib.logging import logger
from rmtoo.lib.logging.LogFormatter import LogFormatter


class YamlRecord(Record):
    """The YAML specialization of the record"""

    def __init__(self, yioconfig):
        '''PRIVATE constructor!
        Please use the from_xxx methods for creating objects of
        YamlRecord from client code.
        '''
        super(YamlRecord, self).__init__()
        self.yioconfig = yioconfig
        self.comment_raw = None
        self.original_content = None

    @classmethod
    def from_string(cls, in_str, rid, yioconfig):
        '''Construct a YamlRecord from a given string.
           rid is the Requirement ID.'''
        Encoding.check_unicode(in_str)
        obj = cls(yioconfig)
        obj.parse(in_str, rid)
        return obj

    @classmethod
    def from_fd(cls, file_des, rid, yioconfig):
        """Construct a YamlRecord from a given file descriptor
        rid is the Requirement ID.
        """
        obj = cls(yioconfig)
        # Read the entire file content
        content = file_des.read()
        obj.parse(content, rid)
        return obj

    def write_fd(self, file_des):
        """Write to filesystem as YAML"""
        # Convert all entries to YAML format
        yaml_data = {}
        for element in self:
            if hasattr(element, 'to_yaml_dict'):
                yaml_data.update(element.to_yaml_dict())
            else:
                # Fallback for standard RecordEntry
                yaml_data[element.get_tag()] = element.get_content().strip()

        # Write as YAML
        yaml.dump(yaml_data, file_des, default_flow_style=False,
                  allow_unicode=True)

    def check_content_validity(self, content, rid):
        """Check if the YAML content is valid"""
        try:
            yaml.safe_load(content)
            return True
        except yaml.YAMLError as e:
            line_num = 1
            if hasattr(e, 'problem_mark') and e.problem_mark:
                line_num = e.problem_mark.line + 1
            logger.error(LogFormatter.format(
                79, "Invalid YAML content: %s" % str(e),
                rid, line_num))
            self._set_not_usable()
            return False

    def parse(self, record, rid):
        """Parse everything from a YAML string"""
        Encoding.check_unicode(record)
        self.original_content = record

        # Check if content is valid YAML
        if not self.check_content_validity(record, rid):
            return

        # Extract initial comments (for now, empty)
        self.comment_raw = YamlParser.extract_record_comment(record)
        self.set_comment(YamlParser.extract_comment(self.comment_raw))

        # Parse the YAML content
        success, parsed_record = YamlParser.split_entries(
            record, rid, self, 1)

        # If there was an error during parsing - stop processing
        if not success:
            self._set_not_usable()
            return

        # Convert parsed records to YamlRecordEntry objects
        for record_data in parsed_record:
            self.append(YamlRecordEntry(record_data))

    def to_string(self):
        """Convert to YAML string"""
        # Build YAML data structure
        yaml_data = {}

        for element in self:
            if hasattr(element, 'to_yaml_dict'):
                yaml_data.update(element.to_yaml_dict())
            else:
                # Fallback for standard RecordEntry
                yaml_data[element.get_tag()] = element.get_content().strip()

        # Convert to YAML string
        return yaml.dump(yaml_data, default_flow_style=False,
                         allow_unicode=True)

    def to_yaml_dict(self):
        """Convert entire record to YAML-compatible dictionary"""
        yaml_data = {}

        for element in self:
            if hasattr(element, 'to_yaml_dict'):
                yaml_data.update(element.to_yaml_dict())
            else:
                # Fallback for standard RecordEntry
                yaml_data[element.get_tag()] = element.get_content().strip()

        return yaml_data
