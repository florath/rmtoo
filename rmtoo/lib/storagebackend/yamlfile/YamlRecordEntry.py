'''
 rmtoo
   Free and Open Source Requirements Management Tool

  YAML Record Entry Class
   This class holds the YAML representation of each record entry.

 (c) 2025 by flonatel GmbH & Co. KG / Andreas Florath

 SPDX-License-Identifier: GPL-3.0-or-later

 For licensing details see COPYING
'''
import yaml
from rmtoo.lib.Encoding import Encoding
from rmtoo.lib.storagebackend.yamlfile.YamlParser import YamlParser
from rmtoo.lib.storagebackend.RecordEntry import RecordEntry


class YamlRecordEntry(RecordEntry):
    """Holds the YAML entry.

    This is needed if a YAML file must be written: it should maintain
    the original structure as much as possible.
    """
    def __init__(self, se):
        '''There must be three entries:
           1) tag with colon
           2) content lines
           3) comment lines (usually empty for YAML)
        '''
        assert len(se) == 3
        Encoding.check_unicode(se[0])
        self.tag_raw = se[0]
        Encoding.check_unicode_list(se[1])
        self.content_raw = se[1]
        Encoding.check_unicode_list(se[2])
        self.comment_raw = se[2]
        # Parse the rest
        tag = self.tag_raw[0:-1]  # Remove the colon
        value = "".join(se[1])
        comment = YamlParser.extract_comment(se[2])
        RecordEntry.__init__(self, tag, value, comment)

    def to_string(self):
        """Return the entry as a YAML string"""
        # For YAML output, we need to format as key: value
        content = self.get_content().strip()
        result = self.get_tag() + ": " + content + "\n"

        # Add comments if any
        if self.comment_raw:
            result += YamlParser.add_newlines(self.comment_raw)

        return result

    def __str__(self):
        return self.to_string()

    @staticmethod
    def format_entry(line):
        '''For 'Normal' RecordEntries there is the need to convert them
        into YAML ones.
        '''
        # Format as YAML key: value
        content = line.get_content().strip()
        result = line.get_tag() + ": " + content + "\n"

        # Add comment if present
        if line.get_comment():
            result += "# " + line.get_comment() + "\n"

        return result

    def write_fd(self, out_file):
        '''Write record entry to filesystem as YAML.'''
        # Write as YAML key: value format
        out_file.write(self.get_tag())
        out_file.write(": ")

        content = self.get_content().strip()
        out_file.write(content)
        out_file.write("\n")

        # Write comments if any
        if self.comment_raw:
            for comment_line in self.comment_raw:
                out_file.write(comment_line)
                out_file.write("\n")

    def set_content(self, content):
        '''Set content and clear raw content cache.'''
        RecordEntry.set_content(self, content)
        self.content_raw = None

    def set_comment(self, comment):
        '''Set the comment and clear raw comment cache.'''
        RecordEntry.set_comment(self, comment)
        self.comment_raw = None

    def get_content_with_nl(self):
        """Return the raw content"""
        return self.content_raw

    def to_yaml_dict(self):
        """Convert entry to YAML-compatible dictionary format"""
        content = self.get_content().strip()

        # Try to parse as YAML value to preserve types
        try:
            parsed_value = yaml.safe_load(content)
            return {self.get_tag(): parsed_value}
        except yaml.YAMLError:
            # If parsing fails, treat as string
            return {self.get_tag(): content}
