#
# rmtoo
#  Open Source Requirements Management
#
# Text Document Class
#  This is the base class for handling input and output of the used
#  text documents. 
#
# (c) 2010-2011 by flonatel
#
# For licencing details see COPYING
#

# This class represents one input text documents for the rmtoo tool
# set.  Additionally to the data only (where mostly everything
# operates on) this class also stores the order of the tags and
# possible empty lines and / or comments.  Also the id is stored
# inside this object.
# The parsing is delayed until the first value is needed: Therefore
# during construction of the object, only the buffer is read in but no
# further operation is done.
class TxtDoc:
    # State field constants
    st_uninitialized = 1
    st_buffer_read = 2

    def __init__(self, rid, fd, config, delay_parsing = True):
        self.state = TxtDoc.st_uninitialized
        self.txt_objs = []
        self.id = rid
        self.config = config
        self.raw_in_buffer = fd.read()
        self.state = TxtDoc.st_buffer_read
        if not delay_parsing:
            self.parse()

    # This method checks if this document was already parsed. If not,
    # it parses it.
    def check_parse(self):
        if self.state==TxtDoc.st_buffer_read:
            self.parse()

# This must be used, if the order must be preserved and one tag can
# occure multiple times.
class TxtDocAsList(TxtDoc, list):
    pass

# This must be used, if there is no need to preserve the order and
# each tag can only exists once.
class TxtDocAsMap(TxtDoc, dict):

    def __init__(self, rid, fd, config, delayed_parsing = True):
        super(TxtDocAsMap, self).__init__(rid, fd, config, delayed_parsing)

    def __getitem__(self, name):
        print("getitem [%s] called" % name)
        self.check_parse()
        return dict.__getitem__(self, name)
