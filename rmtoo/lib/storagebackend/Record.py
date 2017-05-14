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
        self.comment = None

    def get_comment(self):
        """Return the comment of the record"""
        assert self.comment is not None
        return self.comment

    def set_comment(self, comment):
        """Set the comment of the record"""
        self.comment = comment

    def convert_to_dict(self):
        """Convert the (internal) list of entries into a dict"""
        self.ldict = {}
        for i in self:
            tag = i.get_tag()
            if tag in self.ldict:
                raise RMTException(81, "Tag '%s' multiple defined" % tag)
            self.ldict[i.get_tag()] = i

    def get_dict(self):
        """The dictionary which is returned here must be seen as read only.
        The data is only valid until the underlying list is changed.
        """
        if self.ldict is None:
            self.convert_to_dict()
        return self.ldict

    def insert(self, index, o):
        """Insert a new RecordEntry"""
        assert self.ldict is None
        list.insert(self, index, o)

    def append(self, o):
        """Append new RecordEntry"""
        # This can be added seamlessly to a maybe already existsing ldict
        if self.ldict is not None:
            self.ldict[o.get_tag()] = o
        list.append(self, o)

    def __delitem__(self, index):
        """Delete an item"""
        assert self.ldict is None
        list.__delitem__(self, index)

    def remove(self, v):
        """Remove the first occurance of value with the given tag"""
        for element in self:
            if element.get_tag() == v:
                list.remove(self, element)
                return
        return

    def set_content(self, key, value):
        """Set the value for the given key. If not available throws an
        ValueError.
        """
        for element in self:
            if element.get_tag() == key:
                element.set_content(value)
                return
        raise ValueError()

    def is_tag_available(self, tag):
        """Checks if the given tag is available"""
        for i in self:
            if tag == i.get_tag():
                return True
        return False
