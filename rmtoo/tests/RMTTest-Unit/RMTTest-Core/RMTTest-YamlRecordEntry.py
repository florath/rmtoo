'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for YamlRecordEntry

 (c) 2025 by flonatel GmbH & Co. KG / Andreas Florath

 SPDX-License-Identifier: GPL-3.0-or-later

 For licensing details see COPYING
'''

import pytest
import io
from rmtoo.lib.storagebackend.yamlfile.YamlRecordEntry import YamlRecordEntry
from rmtoo.lib.storagebackend.RecordEntry import RecordEntry


class RMTTestYamlRecordEntry:

    def rmttest_pos_01(self):
        "YamlRecordEntry: create with basic string content"
        se = ["name:", [" Test Requirement"], []]

        entry = YamlRecordEntry(se)

        assert entry.get_tag() == "name"
        assert "Test Requirement" in entry.get_content()

    def rmttest_pos_02(self):
        "YamlRecordEntry: to_string formatting"
        se = ["description:", [" A test requirement"], []]
        entry = YamlRecordEntry(se)

        result = entry.to_string()

        assert result == "description: A test requirement\n"

    def rmttest_pos_03(self):
        "YamlRecordEntry: __str__ method"
        se = ["name:", [" Test"], []]
        entry = YamlRecordEntry(se)

        result = str(entry)

        assert result == "name: Test\n"

    def rmttest_pos_04(self):
        "YamlRecordEntry: format_entry static method"
        line = RecordEntry("priority", "high", "Important requirement")

        result = YamlRecordEntry.format_entry(line)

        assert "priority: high\n" in result
        assert "# Important requirement\n" in result

    def rmttest_pos_05(self):
        "YamlRecordEntry: format_entry without comment"
        line = RecordEntry("status", "draft", "")

        result = YamlRecordEntry.format_entry(line)

        assert result == "status: draft\n"

    def rmttest_pos_06(self):
        "YamlRecordEntry: write_fd method"
        se = ["type:", [" functional"], []]
        entry = YamlRecordEntry(se)
        output = io.StringIO()

        entry.write_fd(output)

        result = output.getvalue()
        assert result == "type: functional\n"

    def rmttest_pos_07(self):
        "YamlRecordEntry: write_fd with comments"
        se = ["effort:", [" 5"], ["# This is estimated effort"]]
        entry = YamlRecordEntry(se)
        output = io.StringIO()

        entry.write_fd(output)

        result = output.getvalue()
        assert "effort: 5\n" in result
        assert "# This is estimated effort\n" in result

    def rmttest_pos_08(self):
        "YamlRecordEntry: set_content method"
        se = ["name:", [" Original"], []]
        entry = YamlRecordEntry(se)

        entry.set_content("Modified Content")

        assert entry.get_content() == "Modified Content"
        assert entry.content_raw is None

    def rmttest_pos_09(self):
        "YamlRecordEntry: set_comment method"
        se = ["name:", [" Test"], ["# Original comment"]]
        entry = YamlRecordEntry(se)

        entry.set_comment("New comment")

        assert entry.get_comment() == "New comment"
        assert entry.comment_raw is None

    def rmttest_pos_10(self):
        "YamlRecordEntry: get_content_with_nl method"
        se = ["description:", [" Multi", " line", " content"], []]
        entry = YamlRecordEntry(se)

        result = entry.get_content_with_nl()

        assert result == [" Multi", " line", " content"]

    def rmttest_pos_11(self):
        "YamlRecordEntry: to_yaml_dict with simple value"
        se = ["priority:", [" high"], []]
        entry = YamlRecordEntry(se)

        result = entry.to_yaml_dict()

        assert isinstance(result, dict)
        assert result == {"priority": "high"}

    def rmttest_pos_12(self):
        "YamlRecordEntry: to_yaml_dict with numeric value"
        se = ["effort:", [" 5"], []]
        entry = YamlRecordEntry(se)

        result = entry.to_yaml_dict()

        assert isinstance(result, dict)
        assert result == {"effort": 5}

    def rmttest_pos_13(self):
        "YamlRecordEntry: to_yaml_dict with boolean value"
        se = ["active:", [" true"], []]
        entry = YamlRecordEntry(se)

        result = entry.to_yaml_dict()

        assert isinstance(result, dict)
        assert result == {"active": True}

    def rmttest_pos_14(self):
        "YamlRecordEntry: to_yaml_dict with list value"
        se = ["depends_on:", [" [REQ-001, REQ-002]"], []]
        entry = YamlRecordEntry(se)

        result = entry.to_yaml_dict()

        assert isinstance(result, dict)
        assert result == {"depends_on": ["REQ-001", "REQ-002"]}

    def rmttest_pos_15(self):
        "YamlRecordEntry: to_yaml_dict with invalid YAML content"
        se = ["invalid:", [" [unclosed"], []]
        entry = YamlRecordEntry(se)

        result = entry.to_yaml_dict()

        assert isinstance(result, dict)
        assert result == {"invalid": "[unclosed"}

    def rmttest_pos_16(self):
        "YamlRecordEntry: create with empty content"
        se = ["optional:", [""], []]
        entry = YamlRecordEntry(se)

        result = entry.to_string()

        assert result == "optional: \n"

    def rmttest_pos_17(self):
        "YamlRecordEntry: create with whitespace content"
        se = ["spaced:", ["   "], []]
        entry = YamlRecordEntry(se)

        result = entry.to_string()

        assert result == "spaced: \n"

    def rmttest_pos_18(self):
        "YamlRecordEntry: to_string with comment"
        se = ["name:", [" Test"], ["# This is a comment"]]
        entry = YamlRecordEntry(se)

        result = entry.to_string()

        assert "name: Test\n" in result
        assert "# This is a comment" in result

    def rmttest_pos_19(self):
        "YamlRecordEntry: constructor with unicode content"
        se = ["title:", [" Tëst Rëquïrëmënt"], []]
        entry = YamlRecordEntry(se)

        assert entry.get_tag() == "title"
        assert "Tëst Rëquïrëmënt" in entry.get_content()

    def rmttest_pos_20(self):
        "YamlRecordEntry: constructor with multi-line content"
        se = ["description:", [" Line 1", " Line 2", " Line 3"], []]
        entry = YamlRecordEntry(se)

        assert entry.get_tag() == "description"
        content = entry.get_content()
        assert "Line 1" in content
        assert "Line 2" in content
        assert "Line 3" in content

    def rmttest_pos_21(self):
        "YamlRecordEntry: write_fd with empty comments"
        se = ["name:", [" Test"], []]
        entry = YamlRecordEntry(se)
        output = io.StringIO()

        entry.write_fd(output)

        result = output.getvalue()
        assert result == "name: Test\n"

    def rmttest_pos_22(self):
        "YamlRecordEntry: write_fd with multiple comment lines"
        se = ["complex:", [" value"], ["# Comment 1", "# Comment 2"]]
        entry = YamlRecordEntry(se)
        output = io.StringIO()

        entry.write_fd(output)

        result = output.getvalue()
        assert "complex: value\n" in result
        assert "# Comment 1\n" in result
        assert "# Comment 2\n" in result

    def rmttest_pos_23(self):
        "YamlRecordEntry: to_yaml_dict with null value"
        se = ["null_field:", [" null"], []]
        entry = YamlRecordEntry(se)

        result = entry.to_yaml_dict()

        assert isinstance(result, dict)
        assert result == {"null_field": None}

    def rmttest_pos_24(self):
        "YamlRecordEntry: format_entry with complex content"
        line = RecordEntry(
            "metadata", "author: John\nversion: 1.0", "Complex field")

        result = YamlRecordEntry.format_entry(line)

        assert "metadata: author: John" in result
        assert "# Complex field\n" in result

    def rmttest_neg_01(self):
        "YamlRecordEntry: constructor with invalid structure"
        se = ["incomplete"]  # Missing required elements

        with pytest.raises(AssertionError):
            YamlRecordEntry(se)
