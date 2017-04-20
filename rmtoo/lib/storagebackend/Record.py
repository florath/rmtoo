'''
 rmtoo
   Free and Open Source Requirements Management Tool

 Record Document Class
  This is the base class which defines the interface to retrieve or
  store data for the documents used in rmtoo.
  This class is independent of the underlying storage back-end.

 (c) 2011-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.UsableFlag import UsableFlag


class Record(list, UsableFlag):
    '''This class represents one input document for the rmtoo tool
       set.  Additionally to the data only (where mostly everything
       operates on) this class also stores the order of the tags and
       possible empty lines and / or comments.  Also the id is stored
       inside this object.
       There are (at least) two different access and usage methods:
       o tags must be unique and order does not matter.
       o tags need not be unique but order does matter.
       The first can easily be represented by a dictionary, the second by a
       list.'''

    def __init__(self):
        list.__init__(self)
        UsableFlag.__init__(self)
        self.ldict = None

    # The complete record can have a comment
    def get_comment(self):
        return self.comment

    def set_comment(self, comment):
        self.comment = comment

    def convert_to_dict(self):
        self.ldict = {}
        for i in self:
            tag = i.get_tag()
            if tag in self.ldict:
                raise RMTException(81, "Tag '%s' multiple defined" % tag)
            self.ldict[i.get_tag()] = i

    # The dictionary which is returned here must be seen as read only.
    # The data is only valid until the underlying list is changed.
    def get_dict(self):
        if self.ldict is None:
            self.convert_to_dict()
        return self.ldict

    # Insert a new RecordEntry.
    def insert(self, index, o):
        self.ldict is None
        list.insert(self, index, o)

    # Append new RecordEntry
    def append(self, o):
        # This can be added seamlessly to a maybe already existsing ldict
        if self.ldict is not None:
            self.ldict[o.get_tag()] = o
        list.append(self, o)

    # Delete an item
    def __delitem__(self, index):
        self.ldict is None
        list.__delitem__(self, index)

    # Remove the first occurance of value with the given tag
    def remove(self, v):
        for l in self:
            if l.get_tag() == v:
                list.remove(self, l)
                return
        return

    # Set the value for the given key. If not available throws an
    # ValueError.
    def set_content(self, k, c):
        for l in self:
            if l.get_tag() == k:
                l.set_content(c)
                return
        raise ValueError()

    # Checks if the given tag is available
    def is_tag_available(self, tag):
        for i in self:
            if tag == i.get_tag():
                return True
        return False
