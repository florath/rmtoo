"""Import xls spreadsheets again

Suits love Excel.

(c) 2020 by Kristoffer
SPDX-License-Identifier: GPL-3.0-or-later
This file is part of rmtoo.
For licensing details see COPYING

"""
from __future__ import unicode_literals
import os
import codecs
import datetime
import distutils.file_util
from collections import OrderedDict
import openpyxl

from rmtoo.lib.logging import tracer
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.configuration.Cfg import Cfg
from rmtoo.imports.abcimports import AbcImports


class XlsImport(AbcImports):
    """Import an xls-sheet created in the output plugins"""

    default_config = {
        "import_filename": None,
        "requirement_ws": "Requirements",
        "topics_sheet": "Topics",
    }

    def __init__(self, self_cfg, import_dest):
        tracer.info("called")
        self.useable = False
        self._cfg = dict(self.default_config)
        self._cfg.update(self_cfg)
        self._dest = dict()
        self._entries = None
        self._topics = None

        import_dest_cfg = Cfg(import_dest)
        try:
            req_dirs = import_dest_cfg.get_rvalue("requirements_dirs")
            if req_dirs[0] and os.path.isdir(req_dirs[0]):
                self.useable = True
                self._dest["requirements_dirs"] = req_dirs[0]
        except RMTException:
            self.useable = False
        try:
            topics_dirs = import_dest_cfg.get_rvalue("topics_dirs")
            if topics_dirs[0] and os.path.isdir(topics_dirs[0]):
                self.useable = True
                self._dest["topics_dirs"] = topics_dirs[0]
        except RMTException:
            self.useable = False
        self._wb = None
        tracer.debug("Finished.")

    def run(self):
        if self.useable:
            filename = self._cfg["import_filename"]
            if filename and os.path.isfile(filename):
                self.import_file(filename)

    def import_file(self, filename):
        self._wb = openpyxl.load_workbook(filename)
        headers, self._entries, self._topics = self._extract_dict()
        self._entries = self._verify_entries(self._entries)
        self._write_to_files(self._entries, self._topics)
        self._post_process_file(filename)

    def _extract_dict(self):
        headers = None
        entries = []
        req_wb = self._wb[self._cfg["requirement_ws"]]
        for row in req_wb:
            if row[0].value == "ID":
                headers = [cell.value for cell in row]
            elif headers and row[0].value:
                req = OrderedDict([(headers[i], cell.value)
                                   for i, cell in enumerate(row)])
                entries.append(req)

        topics = OrderedDict()
        topics_ws = self._wb[self._cfg["topics_sheet"]]
        for row in topics_ws.rows:
            if row[0].value:
                topic_name = row[0].value
                topics[topic_name] = []
            if len(row) >= 3 and row[1].value:
                topics[topic_name].append((row[1].value, row[2].value))

        return headers, entries, topics

    @staticmethod
    def _verify_entries(entries):
        """Verify requirement id are not twice in the list. It could easily a
        copy-paste error

        Future inventedOn dates causes errors.

        """
        ids = []
        for entry in entries:
            assert entry["ID"] not in ids
            ids.append(entry["ID"])

        for entry in entries:
            if (entry.get("Invented on", datetime.datetime.now()) >
                    datetime.datetime.now()):
                raise RMTException(118, "Future inventedOn not accepted")

        # add unsolved entries to first
        # Add first to list to avoid self-solving
        solved_entries = [entries[0]["ID"]]
        for entry in entries:
            solved_str = entry.get("Solved by", "")
            if solved_str:
                solved = solved_str.split(" ")
                solved_purged = [x for x in solved if x.strip()]
                solved_entries.extend(solved_purged)

        added_entries = []
        for entry in entries:
            if entry["ID"] not in solved_entries:
                added_entries.append(entry["ID"])
        if added_entries:
            if entries[0]["Solved by"]:
                entries[0]["Solved by"] = (entries[0]["Solved by"].strip()
                                           + " " + " ".join(added_entries))
            else:
                entries[0]["Solved by"] = " ".join(added_entries)
        return entries

    def _write_to_files(self, entries, topics):
        for entry in entries:
            filepath = os.path.join(self._dest["requirements_dirs"],
                                    entry["ID"] + ".req")
            with codecs.open(filepath, "w", "utf-8") as fhdl:
                for key, value in entry.items():
                    content = None
                    if key == "ID":
                        pass
                    elif isinstance(value, datetime.date):
                        content = str(value.date())
                    elif value:
                        content = "\n  ".join(str(value).splitlines())
                    if content:
                        fhdl.write(": ".join([key, content]) + os.linesep)

        for name in topics.keys():
            filepath = os.path.join(self._dest["topics_dirs"], name + ".tic")
            with codecs.open(filepath, "w", "utf-8") as fhdl:
                for key, value in topics[name]:
                    fhdl.write(": ".join([key, value]) + os.linesep)

    @staticmethod
    def _post_process_file(filename):
        old_file = filename.split(".")
        app = datetime.datetime.now().isoformat()
        dest_file = old_file[:-1] + [app] + old_file[-1:]
        dest = ".".join(dest_file)
        distutils.file_util.move_file(filename, dest)
