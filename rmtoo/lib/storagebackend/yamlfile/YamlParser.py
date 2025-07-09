'''
 rmtoo
   Free and Open Source Requirements Management Tool

 YAML Parser

 (c) 2025 by flonatel GmbH & Co. KG / Andreas Florath

 SPDX-License-Identifier: GPL-3.0-or-later

 For licensing details see COPYING
'''

import yaml
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.logging import logger
from rmtoo.lib.logging.LogFormatter import LogFormatter


class YamlParser(object):
    """Parses a YAML representation"""

    @staticmethod
    def parse_yaml_content(content, rid):
        """Parse YAML content and return structured data"""
        try:
            data = yaml.safe_load(content)
            if data is None:
                raise RMTException(79, "Empty YAML document",
                                   rid, 1)
            if not isinstance(data, dict):
                raise RMTException(79, "YAML document must be a dictionary",
                                   rid, 1)
            return data
        except yaml.YAMLError as e:
            line_num = 1
            if hasattr(e, 'problem_mark') and e.problem_mark:
                line_num = e.problem_mark.line + 1
            raise RMTException(
                79, "YAML parsing error: %s" % str(e),
                rid, line_num)

    @staticmethod
    def convert_dict_to_records(data, rid):
        """Convert YAML dictionary to record format compatible with
        TxtParser"""
        records = []

        for key, value in data.items():
            # Convert key to tag format (add colon)
            tag = key + ":"

            # Handle different value types
            if isinstance(value, str):
                # Single line string
                content = [" " + value] if value else [""]
            elif isinstance(value, (list, tuple)):
                # Multi-value items (like dependencies)
                if value:
                    content = [" " + " ".join(str(v) for v in value)]
                else:
                    content = [""]
            elif isinstance(value, dict):
                # Nested dictionary - convert to string representation
                content = [" " + yaml.dump(value,
                                           default_flow_style=False).strip()]
            elif value is None:
                content = [""]
            else:
                # Other types (numbers, booleans, etc.)
                content = [" " + str(value)]

            # Empty comment list for YAML records
            comment = []

            records.append([tag, content, comment])

        return records

    @staticmethod
    def split_entries(content, rid, mls, lineno_offset):
        """Parse YAML content and return record entries in TxtParser format"""
        try:
            data = YamlParser.parse_yaml_content(content, rid)
            records = YamlParser.convert_dict_to_records(data, rid)
            return True, records
        except RMTException as rmte:
            logger.error(LogFormatter.rmte(rmte))
            return False, []
        except Exception as e:
            logger.error(LogFormatter.format(
                79, "Unexpected error parsing YAML: %s" % str(e),
                rid, lineno_offset))
            return False, []

    @staticmethod
    def extract_record_comment(content):
        """Extract initial comments from YAML content"""
        # YAML comments are handled differently - for now return empty
        # TODO: Implement proper YAML comment extraction if needed
        return []

    @staticmethod
    def extract_comment(comment_lines):
        """Extract user-readable comment from YAML comment lines"""
        # For now, return empty string as YAML comments are handled differently
        return ""

    @staticmethod
    def add_newlines(content):
        """Add newlines to content - for YAML this is the original content"""
        if not content:
            return ""
        if isinstance(content, list):
            return "\n".join(content) + "\n"
        return content if content.endswith('\n') else content + '\n'
