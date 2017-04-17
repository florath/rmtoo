# __init__.py
# Copyright (C) 2008, 2009 Michael Trier (mtrier@gmail.com) and contributors
#
# This module is part of GitPython and is released under
# the BSD License: http://www.opensource.org/licenses/bsd-license.php

import distutils.sysconfig
import os
import sys
import inspect

__version__ = '0.3.2 RC1'


#{ Initialization
def _init_externals():
        """Initialize external projects by putting them into the path"""
        mod_dir = distutils.sysconfig.get_python_lib()
        print("git MOD DIR", mod_dir)
        spath = os.path.join(mod_dir, 'rmtoo', 'rmtoo', 'contrib', 'gitdb')
        print("gitdb SPATH", spath)
        sys.path.append(spath)
        print("gitdb sys.path", sys.path)
        
        try:
                import gitdb
        except ImportError:
                raise ImportError("'gitdb' could not be found in your PYTHONPATH")
        #END verify import
        
#} END initialization

#################
_init_externals()
#################

#{ Imports

from git.config import GitConfigParser
from git.objects import *
from git.refs import *
from git.diff import *
from git.exc import *
from git.db import *
from git.cmd import Git
from git.repo import Repo
from git.remote import *
from git.index import *
from git.util import (
                                                LockFile, 
                                                BlockingLockFile, 
                                                Stats,
                                                Actor
                                                )

#} END imports

__all__ = [ name for name, obj in locals().items()
                        if not (name.startswith('_') or inspect.ismodule(obj)) ]
                        
