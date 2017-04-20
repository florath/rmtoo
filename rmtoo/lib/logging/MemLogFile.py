'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Extended MemLog message object which also includes
  information when handling files.

 (c) 2010-2011,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from types import ListType
from rmtoo.lib.logging.MemLog import MemLog


class MemLogFile(MemLog):
    '''Extension of the MemLog for handling additional information
       of a file, like filename and line number.'''

    def __init__(self, lid, level, msg, efile, eline):
        '''Constructor for the extended MemLog object.
           This object additional contains information about
           the filename as well as about the file number.'''
        MemLog.__init__(self, lid, level, msg)
        self.efile = efile
        self.eline = eline

    def write_log(self, file_descriptor):
        '''Writes the message to the given file descriptor.'''
        MemLog.write_log_prefix(self, file_descriptor)
        if self.efile is not None:
            file_descriptor.write("%s:" % self.efile)
        if self.eline is not None:
            file_descriptor.write("%s:" % self.eline)
        MemLog.write_log_suffix(self, file_descriptor)

    def to_list(self):
        '''Returns a list of the MemLogFile.'''
        result = MemLog.to_list(self)
        if self.efile is not None:
            result.append(self.efile)
            if self.eline is not None:
                result.append(self.eline)
        else:
            if self.eline is not None:
                result.append(None)
                result.append(self.eline)
        return result

    @staticmethod
    def create_ml(param_list):
        '''This is mostly a second constructor for a message which can be
           called with a list.'''
        assert(type(param_list) == ListType)
        llen = len(param_list)
        assert(llen > 3)
        assert(llen <= 5)

        efile = None
        if llen > 3:
            efile = param_list[3]

        eline = None
        if llen > 4:
            eline = param_list[4]

        return MemLogFile(param_list[0], param_list[1], param_list[2],
                          efile, eline)

    def __eq__(self, other):
        '''The equal method: if everything is the same, it's true.'''
        return MemLog.__eq__(self, other) \
            and self.efile == other.efile \
            and self.eline == other.eline
