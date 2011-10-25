'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
 The memory logging object.
   
 (c) 2011 by flonatel GmhH & Co. KG

 For licensing details see COPYING
'''

import time
from types import ListType

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
        assert(type(param_list) == ListType)
        llen = len(param_list)
        assert(llen == 3)

        return MemLog(param_list[0], param_list[1], param_list[2])

    def to_list(self):
        r = []
        r.append(self.lid)
        # XXX This is not that perfect yet: it would be better 
        # to have here the symbolic output instead of the number.
        # This implies IMHO to move the levels to a sperate class.
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

    def __eq__(self, other):
        print("MemLog.__eq__ [%s] [%s]" %
              (self.lid,
               self.__class__ == other.__class__ \
               and self.lid == other.lid \
               and self.level == other.level \
               and self.msg == other.msg))
        print("eq1 [%s]" % (self.__class__ == other.__class__))
        print("eq2 [%s]" % (self.lid == other.lid))
        print("eq3 [%s]" % (self.level == other.level))
        print("eq4 [%s]" % (self.msg == other.msg))


        return self.__class__ == other.__class__ \
            and self.lid == other.lid \
            and self.level == other.level \
            and self.msg == other.msg
