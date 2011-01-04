#
# rmtoo
#  Open Source Requirements Management
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
class Record:
    pass

# There are (at least) two different access and usage methods:
# o tags must be unique and order does not matter.
# o tags need not be unique but order does matter.
# The first can easily be represented by a dictionary, the second by a
# list.
# Because both access methods are that different, two classes are
# needed here:

class RecordAsDict(Record, dict):
    
    def __init__(self, parser):
        self.parser = parser
        self.convert_to_dict()

    def convert_to_dict(self):
        for i in self.parser.get_list():
            self[i.id()] = i

class RecordAsList(Record, list):
    pass

