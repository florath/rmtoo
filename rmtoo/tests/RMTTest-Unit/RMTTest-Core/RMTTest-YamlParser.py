'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for YamlParser

 (c) 2025 by flonatel GmbH & Co. KG / Andreas Florath

 SPDX-License-Identifier: GPL-3.0-or-later

 For licensing details see COPYING
'''

import pytest
from rmtoo.lib.storagebackend.yamlfile.YamlParser import YamlParser
from rmtoo.lib.RMTException import RMTException


class RMTTestYamlParser:

    def rmttest_pos_01(self):
        "YamlParser: parse simple YAML content"
        content = "name: Test Requirement\ndescription: This is a test"

        data = YamlParser.parse_yaml_content(content, "REQ-001")

        assert isinstance(data, dict)
        assert data["name"] == "Test Requirement"
        assert data["description"] == "This is a test"

    def rmttest_pos_02(self):
        "YamlParser: convert dict to records with string values"
        data = {"name": "Test", "description": "A test requirement"}

        records = YamlParser.convert_dict_to_records(data, "REQ-001")

        assert len(records) == 2
        assert any(r[0] == "name:" for r in records)
        assert any(r[0] == "description:" for r in records)

    def rmttest_pos_03(self):
        "YamlParser: convert dict to records with list values"
        data = {"depends_on": ["REQ-001", "REQ-002"]}

        records = YamlParser.convert_dict_to_records(data, "REQ-003")

        assert len(records) == 1
        assert records[0][0] == "depends_on:"
        assert "REQ-001 REQ-002" in records[0][1][0]

    def rmttest_pos_04(self):
        "YamlParser: convert dict to records with empty list"
        data = {"depends_on": []}

        records = YamlParser.convert_dict_to_records(data, "REQ-003")

        assert len(records) == 1
        assert records[0][0] == "depends_on:"
        assert records[0][1] == [""]

    def rmttest_pos_05(self):
        "YamlParser: convert dict to records with None value"
        data = {"optional_field": None}

        records = YamlParser.convert_dict_to_records(data, "REQ-001")

        assert len(records) == 1
        assert records[0][0] == "optional_field:"
        assert records[0][1] == [""]

    def rmttest_pos_06(self):
        "YamlParser: convert dict to records with numeric value"
        data = {"priority": 5, "effort": 3.5}

        records = YamlParser.convert_dict_to_records(data, "REQ-001")

        assert len(records) == 2
        priority_record = next(r for r in records if r[0] == "priority:")
        effort_record = next(r for r in records if r[0] == "effort:")
        assert " 5" in priority_record[1][0]
        assert " 3.5" in effort_record[1][0]

    def rmttest_pos_07(self):
        "YamlParser: convert dict to records with boolean value"
        data = {"active": True, "deprecated": False}

        records = YamlParser.convert_dict_to_records(data, "REQ-001")

        assert len(records) == 2
        active_record = next(r for r in records if r[0] == "active:")
        deprecated_record = next(r for r in records if r[0] == "deprecated:")
        assert " True" in active_record[1][0]
        assert " False" in deprecated_record[1][0]

    def rmttest_pos_08(self):
        "YamlParser: convert dict to records with nested dict"
        data = {"metadata": {"author": "John", "version": "1.0"}}

        records = YamlParser.convert_dict_to_records(data, "REQ-001")

        assert len(records) == 1
        assert records[0][0] == "metadata:"
        assert "author: John" in records[0][1][0]
        assert "version: '1.0'" in records[0][1][0]

    def rmttest_pos_09(self):
        "YamlParser: split_entries successful parsing"
        content = "name: Test\ndescription: A test requirement"

        success, records = YamlParser.split_entries(
            content, "REQ-001", None, 1)

        assert success is True
        assert len(records) == 2
        assert any(r[0] == "name:" for r in records)

    def rmttest_pos_10(self):
        "YamlParser: extract_record_comment returns empty"
        content = "name: Test\n# This is a comment"

        comments = YamlParser.extract_record_comment(content)

        assert comments == []

    def rmttest_pos_11(self):
        "YamlParser: extract_comment returns empty string"
        comment_lines = ["# This is a comment", "# Another comment"]

        comment = YamlParser.extract_comment(comment_lines)

        assert comment == ""

    def rmttest_pos_12(self):
        "YamlParser: add_newlines with content"
        content = "Some content"

        result = YamlParser.add_newlines(content)

        assert result == "Some content\n"

    def rmttest_pos_13(self):
        "YamlParser: add_newlines with content already having newline"
        content = "Some content\n"

        result = YamlParser.add_newlines(content)

        assert result == "Some content\n"

    def rmttest_pos_14(self):
        "YamlParser: add_newlines with empty content"
        content = ""

        result = YamlParser.add_newlines(content)

        assert result == ""

    def rmttest_pos_15(self):
        "YamlParser: convert dict with empty string value"
        data = {"empty_field": ""}

        records = YamlParser.convert_dict_to_records(data, "REQ-001")

        assert len(records) == 1
        assert records[0][0] == "empty_field:"
        assert records[0][1] == [""]

    def rmttest_neg_01(self):
        "YamlParser: parse invalid YAML content"
        content = "name: Test\ninvalid: [unclosed"

        with pytest.raises(RMTException) as exc_info:
            YamlParser.parse_yaml_content(content, "REQ-001")

        assert exc_info.value.get_id() == 79
        assert "YAML parsing error" in str(exc_info.value)

    def rmttest_neg_02(self):
        "YamlParser: parse empty YAML document"
        content = ""

        with pytest.raises(RMTException) as exc_info:
            YamlParser.parse_yaml_content(content, "REQ-001")

        assert exc_info.value.get_id() == 79
        assert "Empty YAML document" in str(exc_info.value)

    def rmttest_neg_03(self):
        "YamlParser: parse YAML with non-dict content"
        content = "- item1\n- item2"

        with pytest.raises(RMTException) as exc_info:
            YamlParser.parse_yaml_content(content, "REQ-001")

        assert exc_info.value.get_id() == 79
        assert "must be a dictionary" in str(exc_info.value)

    def rmttest_neg_04(self):
        "YamlParser: split_entries with invalid YAML"
        content = "name: Test\ninvalid: [unclosed"

        success, records = YamlParser.split_entries(
            content, "REQ-001", None, 1)

        assert success is False
        assert records == []

    def rmttest_neg_05(self):
        "YamlParser: split_entries with unexpected error"
        # This simulates an unexpected error by passing invalid parameters
        content = None

        success, records = YamlParser.split_entries(
            content, "REQ-001", None, 1)

        assert success is False
        assert records == []

    def rmttest_pos_16(self):
        "YamlParser: convert dict with tuple values"
        data = {"coordinates": (1, 2, 3)}

        records = YamlParser.convert_dict_to_records(data, "REQ-001")

        assert len(records) == 1
        assert records[0][0] == "coordinates:"
        assert "1 2 3" in records[0][1][0]
