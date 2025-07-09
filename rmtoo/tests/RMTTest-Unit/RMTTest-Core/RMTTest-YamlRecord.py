'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for YamlRecord

 (c) 2025 by flonatel GmbH & Co. KG / Andreas Florath

 SPDX-License-Identifier: GPL-3.0-or-later

 For licensing details see COPYING
'''

import io
from rmtoo.lib.storagebackend.yamlfile.YamlRecord import YamlRecord
from rmtoo.lib.storagebackend.yamlfile.YamlIOConfig import YamlIOConfig


class RMTTestYamlRecord:

    def setup_method(self):
        """Setup method called before each test"""
        self.yioconfig = YamlIOConfig()

    def rmttest_pos_01(self):
        "YamlRecord: create from valid YAML string"
        yaml_content = "name: Test Requirement\ndescription: This is a test"

        record = YamlRecord.from_string(
            yaml_content, "REQ-001", self.yioconfig)

        assert record.is_usable()
        assert len(record) == 2

    def rmttest_pos_02(self):
        "YamlRecord: create from file descriptor"
        yaml_content = "name: Test Requirement\ndescription: This is a test"
        fd = io.StringIO(yaml_content)

        record = YamlRecord.from_fd(fd, "REQ-001", self.yioconfig)

        assert record.is_usable()
        assert len(record) == 2

    def rmttest_pos_03(self):
        "YamlRecord: check_content_validity with valid YAML"
        yaml_content = "name: Test\ndescription: Valid YAML"
        record = YamlRecord(self.yioconfig)

        result = record.check_content_validity(yaml_content, "REQ-001")

        assert result is True

    def rmttest_pos_04(self):
        "YamlRecord: to_string conversion"
        yaml_content = "name: Test\ndescription: A test requirement"
        record = YamlRecord.from_string(
            yaml_content, "REQ-001", self.yioconfig)

        result = record.to_string()

        assert "name:" in result
        assert "description:" in result
        assert "Test" in result

    def rmttest_pos_05(self):
        "YamlRecord: to_yaml_dict conversion"
        yaml_content = "name: Test\ndescription: A test requirement"
        record = YamlRecord.from_string(
            yaml_content, "REQ-001", self.yioconfig)

        result = record.to_yaml_dict()

        assert isinstance(result, dict)
        assert "name" in result
        assert "description" in result

    def rmttest_pos_06(self):
        "YamlRecord: write_fd with YamlRecordEntry objects"
        yaml_content = "name: Test\ndescription: A test requirement"
        record = YamlRecord.from_string(
            yaml_content, "REQ-001", self.yioconfig)
        output = io.StringIO()

        record.write_fd(output)

        result = output.getvalue()
        assert "name:" in result
        assert "description:" in result

    def rmttest_pos_07(self):
        "YamlRecord: parse with complex YAML structure"
        yaml_content = """name: Complex Test
description: A complex test requirement
depends_on:
  - REQ-001
  - REQ-002
metadata:
  author: John Doe
  version: 1.0"""

        record = YamlRecord.from_string(
            yaml_content, "REQ-003", self.yioconfig)

        assert record.is_usable()
        assert len(record) == 4  # name, description, depends_on, metadata

    def rmttest_pos_08(self):
        "YamlRecord: parse with numeric and boolean values"
        yaml_content = """name: Numeric Test
priority: 5
active: true
effort: 3.5"""

        record = YamlRecord.from_string(
            yaml_content, "REQ-001", self.yioconfig)

        assert record.is_usable()
        assert len(record) == 4

    def rmttest_pos_09(self):
        "YamlRecord: parse with empty values"
        yaml_content = """name: Empty Test
description: ""
optional_field: null"""

        record = YamlRecord.from_string(
            yaml_content, "REQ-001", self.yioconfig)

        assert record.is_usable()
        assert len(record) == 3

    def rmttest_pos_10(self):
        "YamlRecord: original_content is preserved"
        yaml_content = "name: Test\ndescription: A test requirement"
        record = YamlRecord.from_string(
            yaml_content, "REQ-001", self.yioconfig)

        assert record.original_content == yaml_content

    def rmttest_pos_11(self):
        "YamlRecord: write_fd with fallback RecordEntry"
        record = YamlRecord(self.yioconfig)
        # Manually add a record entry that doesn't have to_yaml_dict
        from rmtoo.lib.storagebackend.RecordEntry import RecordEntry
        record.append(RecordEntry("test_tag", "test_content", ""))
        output = io.StringIO()

        record.write_fd(output)

        result = output.getvalue()
        assert "test_tag:" in result

    def rmttest_pos_12(self):
        "YamlRecord: to_string with fallback RecordEntry"
        record = YamlRecord(self.yioconfig)
        from rmtoo.lib.storagebackend.RecordEntry import RecordEntry
        record.append(RecordEntry("test_tag", "test_content", ""))

        result = record.to_string()

        assert "test_tag:" in result
        assert "test_content" in result

    def rmttest_pos_13(self):
        "YamlRecord: to_yaml_dict with fallback RecordEntry"
        record = YamlRecord(self.yioconfig)
        from rmtoo.lib.storagebackend.RecordEntry import RecordEntry
        record.append(RecordEntry("test_tag", "test_content", ""))

        result = record.to_yaml_dict()

        assert isinstance(result, dict)
        assert "test_tag" in result
        assert result["test_tag"] == "test_content"

    def rmttest_pos_14(self):
        "YamlRecord: constructor with private access"
        record = YamlRecord(self.yioconfig)

        assert record.yioconfig == self.yioconfig
        assert record.comment_raw is None
        assert record.original_content is None

    def rmttest_neg_01(self):
        "YamlRecord: create from invalid YAML string"
        yaml_content = "name: Test\ninvalid: [unclosed"

        record = YamlRecord.from_string(
            yaml_content, "REQ-001", self.yioconfig)

        assert not record.is_usable()

    def rmttest_neg_02(self):
        "YamlRecord: check_content_validity with invalid YAML"
        yaml_content = "name: Test\ninvalid: [unclosed"
        record = YamlRecord(self.yioconfig)

        result = record.check_content_validity(yaml_content, "REQ-001")

        assert result is False
        assert not record.is_usable()

    def rmttest_neg_03(self):
        "YamlRecord: parse with empty YAML document"
        yaml_content = ""

        record = YamlRecord.from_string(
            yaml_content, "REQ-001", self.yioconfig)

        assert not record.is_usable()

    def rmttest_neg_04(self):
        "YamlRecord: parse with non-dict YAML"
        yaml_content = "- item1\n- item2"

        record = YamlRecord.from_string(
            yaml_content, "REQ-001", self.yioconfig)

        assert not record.is_usable()

    def rmttest_neg_05(self):
        "YamlRecord: create from invalid file descriptor content"
        yaml_content = "name: Test\ninvalid: [unclosed"
        fd = io.StringIO(yaml_content)

        record = YamlRecord.from_fd(fd, "REQ-001", self.yioconfig)

        assert not record.is_usable()

    def rmttest_pos_15(self):
        "YamlRecord: parse method directly"
        record = YamlRecord(self.yioconfig)
        yaml_content = "name: Direct Parse\ndescription: Testing direct parse"

        record.parse(yaml_content, "REQ-001")

        assert record.is_usable()
        assert len(record) == 2
        assert record.original_content == yaml_content

    def rmttest_pos_16(self):
        "YamlRecord: comment handling"
        record = YamlRecord(self.yioconfig)
        yaml_content = "name: Test\ndescription: With comments"

        record.parse(yaml_content, "REQ-001")

        assert record.comment_raw == []
        assert record.get_comment() == ""
