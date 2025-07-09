'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for YamlIOConfig

 (c) 2025 by flonatel GmbH & Co. KG / Andreas Florath

 SPDX-License-Identifier: GPL-3.0-or-later

 For licensing details see COPYING
'''

import pytest
from rmtoo.lib.storagebackend.yamlfile.YamlIOConfig import YamlIOConfig
from rmtoo.lib.configuration.Cfg import Cfg
from rmtoo.lib.RMTException import RMTException


class RMTTestYamlIOConfig:

    def rmttest_pos_01(self):
        "YamlIOConfig: check default values"
        yic = YamlIOConfig()

        assert yic.get_max_line_length() == 80
        assert yic.get_preserve_order() is True
        assert yic.get_indent_spaces() == 2

    def rmttest_pos_02(self):
        "YamlIOConfig: check new max line length setting"
        config = Cfg()
        config.set_value('max_input_line_length', 120)

        yic = YamlIOConfig(config, 'requirement')

        assert yic.get_max_line_length() == 120

    def rmttest_pos_03(self):
        "YamlIOConfig: check preserve order setting"
        config = Cfg()
        config.set_value('yaml_preserve_order', False)

        yic = YamlIOConfig(config, 'requirement')

        assert yic.get_preserve_order() is False

    def rmttest_pos_04(self):
        "YamlIOConfig: check indent spaces setting"
        config = Cfg()
        config.set_value('yaml_indent_spaces', 4)

        yic = YamlIOConfig(config, 'requirement')

        assert yic.get_indent_spaces() == 4

    def rmttest_pos_05(self):
        "YamlIOConfig: check all custom values"
        config = Cfg()
        config.set_value('max_input_line_length', 150)
        config.set_value('yaml_preserve_order', False)
        config.set_value('yaml_indent_spaces', 6)

        yic = YamlIOConfig(config, 'requirement')

        assert yic.get_max_line_length() == 150
        assert yic.get_preserve_order() is False
        assert yic.get_indent_spaces() == 6

    def rmttest_neg_01(self):
        "YamlIOConfig: check negative max line length"
        config = Cfg()
        config.set_value('max_input_line_length', -10)

        with pytest.raises(RMTException) as exc_info:
            YamlIOConfig(config, 'requirement')

        assert exc_info.value.get_id() == 72
        assert "negative" in str(exc_info.value)

    def rmttest_pos_07(self):
        "YamlIOConfig: check zero max line length is allowed"
        config = Cfg()
        config.set_value('max_input_line_length', 0)

        yic = YamlIOConfig(config, 'requirement')

        assert yic.get_max_line_length() == 0

    def rmttest_neg_03(self):
        "YamlIOConfig: check zero indent spaces"
        config = Cfg()
        config.set_value('yaml_indent_spaces', 0)

        with pytest.raises(RMTException) as exc_info:
            YamlIOConfig(config, 'requirement')

        assert exc_info.value.get_id() == 72
        assert "invalid" in str(exc_info.value)

    def rmttest_neg_04(self):
        "YamlIOConfig: check negative indent spaces"
        config = Cfg()
        config.set_value('yaml_indent_spaces', -2)

        with pytest.raises(RMTException) as exc_info:
            YamlIOConfig(config, 'requirement')

        assert exc_info.value.get_id() == 72
        assert "invalid" in str(exc_info.value)

    def rmttest_pos_06(self):
        "YamlIOConfig: check with None config"
        yic = YamlIOConfig(None, 'requirement')

        assert yic.get_max_line_length() == 80
        assert yic.get_preserve_order() is True
        assert yic.get_indent_spaces() == 2
