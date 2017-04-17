"""Initialize the object database module"""

import distutils
import os
import sys

#{ Initialization
def _init_externals():
        """Initialize external projects by putting them into the path"""
        mod_dir = distutils.sysconfig.get_python_lib()
        spath = os.path.join(mod_dir, 'rmtoo', 'contrib', 'gitdb')
        sys.path.append(spath)

#} END initialization

_init_externals()

# default imports
from gitdb.db import *
from gitdb.base import *
from gitdb.stream import *
