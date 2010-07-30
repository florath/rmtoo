"""Initialize the object database module"""

import sys
import os

#{ Initialization
def _init_externals():
	"""Initialize external projects by putting them into the path"""
	sys.path.append(os.path.join(os.path.dirname(__file__), 'ext'))
	
#} END initialization

_init_externals()

# default imports
from db import *
from base import *
from stream import *

