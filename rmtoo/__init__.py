'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Master __init__.py

 (c) 2011,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
__all__ = ["inputs", "lib", "tests", "outputs"]
__version__ = "24.3.1"

import os
filepath = os.path.dirname(os.path.realpath(__file__))
os.environ['contribdir'] = os.path.join(filepath, '..',
                                        'contrib', 'template_project')
