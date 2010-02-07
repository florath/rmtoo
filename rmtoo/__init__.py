#
# rmtoo __init__.py
#
# (c) 2010 by flonatel (sf@flonatel.org)
#
# For licensing details see COPYING
#

__package__ = "rmtoo"
__all__ = ["modules", "lib" ]

#
# Add shared library path to sys.path
#
import os, sys
sys.path.append(os.path.join(os.path.split(__file__)[0], sys.platform))
del os
del sys
