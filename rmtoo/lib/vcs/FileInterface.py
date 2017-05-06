'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Abstract Base Class (ABC) to handle different version control systems.
  This is a specialization for files stored in the file system
  (like plain filesystem or VCS).

 (c) 2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals

import os

from six import iteritems

from rmtoo.lib.vcs.Interface import Interface
from rmtoo.lib.logging import tracer


# This is a partial implementation only.
# pylint: disable=abstract-method
class FileInterface(Interface):
    """Interface for implementations using file in the filesystem"""

    def __init__(self, config):
        Interface.__init__(self, config)

    @staticmethod
    def _abs_path(directory):
        '''Convert the given directory path into an absolute path.'''
        if not os.path.isabs(directory):
            return os.path.abspath(directory)
        return directory

    # pylint: disable=no-self-use,unused-argument
    def _extended_directory_check(self, directory):
        """The default implementation does nothing"""
        return

    def _setup_directories(self, cfg):
        '''Cleans up and unifies the directories.'''
        all_dirs = {}
        tracer.debug("Called.")
        for dir_type in ["requirements", "topics", "constraints", "testcases"]:
            config_dirs = cfg.get_rvalue_default(dir_type + "_dirs", None)
            if config_dirs is None:
                tracer.info("Directory [%s] not configured - skipping.",
                            dir_type)
                continue
            dirs = list(map(self._abs_path, config_dirs))
            self._check_list_of_strings(dir_type, dirs)

            new_directories = []
            for directory in config_dirs:
                self._extended_directory_check(directory)
                new_directories.append(directory)
            all_dirs[dir_type] = new_directories

        for dir_type, directory in iteritems(all_dirs):
            tracer.debug("[%s] directories [%s]", dir_type, directory)

        return all_dirs
