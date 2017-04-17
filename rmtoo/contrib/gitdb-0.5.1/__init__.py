"""Initialize the object database module"""

import distutils
import os
import sys

#{ Initialization
def _init_externals():
        """Initialize external projects by putting them into the path"""
        mod_dir = distutils.sysconfig.get_python_lib()
        print("MOD DIR", mod_dir)
        spath = os.path.join(mod_dir, 'rmtoo', 'rmtoo', 'contrib', 'gitdb')
        print("SPATH", spath)
        sys.path.append(spath)

#} END initialization

_init_externals()

# default imports
from db import *
from base import *
from stream import *
