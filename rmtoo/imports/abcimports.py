'''Import Abstract Base Class

'''
import abc
import sys

if sys.version_info >= (3, 4):
    ABC = abc.ABC
else:
    ABC = abc.ABCMeta('ABC', (object,), {})  # compatible with Python 2 *and* 3


class AbcImports(ABC):
    '''Define an ABC for all imports classes'''

    @abc.abstractmethod
    def __init__(self, self_cfg, import_dest):
        raise NotImplementedError

    @abc.abstractmethod
    def run(self):
        raise NotImplementedError
