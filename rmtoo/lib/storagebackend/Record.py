#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# Record Document Class
#  This is the base class which defines the interface to retrieve or
#  store data for the documents used in rmtoo.
#  This class is independend of the underlaying storage backend.
#
# (c) 2010-2011 by flonatel
#
# For licencing details see COPYING
#

# This class represents one input document for the rmtoo tool
# set.  Additionally to the data only (where mostly everything
# operates on) this class also stores the order of the tags and
# possible empty lines and / or comments.  Also the id is stored
# inside this object.
# There are (at least) two different access and usage methods:
# o tags must be unique and order does not matter.
# o tags need not be unique but order does matter.
# The first can easily be represented by a dictionary, the second by a
# list.
class Record(list):

    def __init__(self):
        self.ldict = None
        # XXX not complete....

    # The complete record can have a comment
    def get_comment(self):
        pass
    
    def convert_to_dict(self):
        self.ldict = {}
        for i in self:
            self.ldict[i.get_tag()] = i

    def get_dict(self):
        if self.ldict==None:
            self.convert_to_dict()
        return self.ldict

    # XXX When adding / removing something, this must also be
    # reflected to the underlaying parser.

    # XXX Methods which change something might invalidate (remove) the
    # ldict. 

