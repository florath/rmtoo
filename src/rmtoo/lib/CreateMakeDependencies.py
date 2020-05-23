'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Helper class for creating make dependencies.

 (c) 2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from rmtoo.lib.logging import tracer


class CreateMakeDependencies(object):
    """Class for creating the Makefile dependencies"""

    def __init__(self):
        '''Creates the object.'''
        self._cmad_file = None

    def init_cmad_(self, cmad_file):
        '''This is called when the cmad should be written.'''
        tracer.debug("Called.")
        self._cmad_file = cmad_file

    @staticmethod
    def write_reqs_dep(filed, filename):
        '''Writes out the dependency to all requirements.'''
        filed.write("%s: ${REQS}\n\t${CALL_RMTOO}\n" % (filename))

    @staticmethod
    def _get_call_rmtoo_line():
        return "\t${CALL_RMTOO}\n"
