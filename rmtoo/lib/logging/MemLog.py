'''
 rmtoo
   Free and Open Source Requirements Management Tool

 The memory logging object.

 (c) 2011,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
import time
from rmtoo.lib.logging import logger


class MemLog:
    '''This represents one memory log message.
       It contains some deep information about the file and line number.
       Also it contains a unique log message.'''

    def __init__(self, lid, level, msg):
        '''The log message is constant.'''
        self.timestamp = time.time()
        self.lid = lid
        self.level = level
        self.msg = msg

    @staticmethod
    def create_ml(param_list):
        '''This is mostly a second constructor for a message which can be
           called with a list.'''
        assert type(param_list) == list
        llen = len(param_list)
        assert llen == 3

        return MemLog(param_list[0], param_list[1], param_list[2])

    def to_list(self):
        r = []
        r.append(self.lid)
        r.append(self.level.get_symbolic_str())
        r.append(self.msg)
        return r

    def write_log_prefix(self, fd):
        fd.write("+++ ")
        fd.write(self.level.get_output_str())
        fd.write(":")
        fd.write("%3d:" % self.lid)

    def write_log_suffix(self, fd):
        fd.write("%s" % self.msg)
        fd.write("\n")

    def write_log(self, file_descriptor):
        self.write_log_prefix(file_descriptor)
        self.write_log_suffix(file_descriptor)

    def write_to_logger(self):
        logger.log(self.level, "%3d:%s" % (self.lid, self.msg))

    def __eq__(self, other):
        return self.__class__ == other.__class__ \
            and self.lid == other.lid \
            and self.level == other.level \
            and self.msg == other.msg
