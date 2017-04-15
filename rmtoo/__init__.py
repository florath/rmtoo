#
# rmtoo __init__.py
#
# (c) 2010,2017 by flonatel (rmtoo@florath.net)
#
# For licensing details see COPYING
#

__package__ = "rmtoo"
__all__ = ["modules", "lib", "tests", "outputs"]

#
# Add shared library path to sys.path
#
import os
import sys
sys.path.append(os.path.join(os.path.split(__file__)[0], sys.platform))
del os
del sys
