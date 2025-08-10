"""Import data from other sources and write to the file system entries

(c) 2018, 2020 by Kristoffer
SPDX-License-Identifier: GPL-3.0-or-later
This file is part of rmtoo.
For licensing details see COPYING

"""
from __future__ import unicode_literals
from stevedore import extension
from six import iteritems

from rmtoo.lib.logging import tracer
from rmtoo.lib.configuration.Cfg import Cfg
from rmtoo.imports.abcimports import AbcImports


class Import:
    """Class parsing the configuration and importing from configured
    import locations to configured input location.

    The idea is to not deal with, e.g., Excel sheets in this tool but
    to enable seamless import and export.

    The default configuration provides no information about the
    location of the *ts_topics.sources* location.

    :ivar _input_dir: latest item with requirements_dir and topics_dir

    :Example: an example configuration looks as follows.
        "import": {
            "xls": {
                "import_filename": "import/requirements.xls"
            }
        }

    """

    DEFAULT_CONFIG = {"xls": {"import_filename": None}}

    def __init__(self, config):
        """Sets up Import for use."""
        tracer.info("called")
        self.__plugin_manager = extension.ExtensionManager(
            namespace="rmtoo.imports.plugin", invoke_on_load=False)

        assert config  # we need a configuration
        if "import" in config:
            self._config = config["import"]
        else:
            self._config = self.DEFAULT_CONFIG
        self._cfg = Cfg(self._config)

        self._input_dir = {"requirements_dirs": None, "topics_dirs": None}
        self._extract_input_dir(config)

        self._import_obj = []
        self._set_run_modules()
        tracer.debug("Finished.")

    def _extract_input_dir(self, config):
        input_cfg = Cfg(config)
        sources_dirs = "topics.ts_common.sources"
        for cfg in input_cfg.get_value(sources_dirs):
            for req_idx in [
                    "requirements_dirs", "topics_dirs", "sources_dirs"
            ]:
                if req_idx in cfg[1]:
                    self._input_dir[req_idx] = cfg[1][req_idx]

    def _set_run_modules(self):
        for module_name, cfg in iteritems(self._config):
            import_obj = self.__plugin_manager[module_name].plugin(
                cfg, self._input_dir)
            if isinstance(import_obj, AbcImports):
                self._import_obj.append(import_obj)

    @staticmethod
    def execute(config):
        """Process Import with configuration file"""
        foreign_import = Import(config)
        foreign_import.process_all()

    def process_all(self):
        """Process all members"""
        for module in self._import_obj:
            module.run()
