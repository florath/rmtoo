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
class Record:

    def __init__(self):
        self.llist = []
        self.ldict = None

    # The complete record can have a comment
    def get_comment(self):
        return self.comment

    def set_comment(self, comment):
        self.comment = comment
    
    def convert_to_dict(self):
        self.ldict = {}
        for i in self.llist:
            self.ldict[i.get_tag()] = i

    # The dict which is returned here must be seen as read only.
    # The data is only valid until the underlaying list is changed.
    def get_dict(self):
        if self.ldict==None:
            self.convert_to_dict()
        return self.ldict

    # Insert a new RecordEntry.
    def insert(self, index, o):
        self.ldict = None
        self.llist.insert(index, o)

    # Delete an item
    def __delitem__(self, index):
        self.ldict = None
        self.llist.__delitem__(index)

