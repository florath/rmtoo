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

from six import iteritems

from rmtoo.lib.vcs.Interface import Interface
from rmtoo.lib.logging import tracer


# This is a partial implementation only.
# pylint: disable=abstract-method
class FileInterface(Interface):
    """Interface for implementations using file in the filesystem"""

    def __init__(self, config):
        Interface.__init__(self, config)

    # This is overloaded and therefore must be a normal method.
    # pylint: disable=no-self-use
    def _adapt_dir_path(self, directory):
        return directory

    # This is overloaded and therefore must be a normal method.
    # pylint: disable=no-self-use
    def _adapt_ext_path(self, directory):
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
            dirs = list(map(self._adapt_dir_path, config_dirs))
            self._check_list_of_strings(dir_type, dirs)

            new_directories = []
            for directory in dirs:
                self._extended_directory_check(directory)
                new_directories.append(self._adapt_ext_path(directory))
            all_dirs[dir_type] = new_directories

        for dir_type, directory in iteritems(all_dirs):
            tracer.debug("[%s] directories [%s]", dir_type, directory)

        return all_dirs
