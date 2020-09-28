'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Master __init__.py

 (c) 2011,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
import os
from pathlib import Path


__all__ = ["inputs", "lib", "tests", "outputs"]
__version__ = "25.0.1"


def rmtoo_contrib_dir():
    """Prints the path of the `contrib` directory"""
    file_wd = Path(__file__).parent
    print(os.path.join(file_wd, "contrib"))
