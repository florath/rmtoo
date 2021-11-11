'''
 rmtoo
   Free and Open Source Requirements Management Tool

 Record Entry Class
  This base class holds one entry in the record.
  Different storage backends can inherit from this class - but must
  handle newly added entries from this base class.

 (c) 2011,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
# Note: all things must be done via methods (do not change an entry
# directly!)  This gives the underlaying (inherited) class the chance
# to overwrite these settings and do other things which might be
# needed.

from rmtoo.lib.Encoding import Encoding


class RecordEntry(object):
    """Class holding one entry of a record"""

    def __init__(self, tag, content, comment=None):
        Encoding.check_unicode(tag)
        self.__tag = tag
        Encoding.check_unicode(content)
        self.__content = content
        if comment is not None:
            Encoding.check_unicode(comment)
        self.__comment = comment

    def get_tag(self):
        """Return the tag"""
        return self.__tag

    def get_content(self):
        """Return the content (stipped)"""
        return self.__content.lstrip()

    def set_content(self, content):
        """Set the content"""
        Encoding.check_unicode(content)
        self.__content = content

    def set_comment(self, comment):
        """Set the comment"""
        Encoding.check_unicode(comment)
        self.__comment = comment

    def get_comment(self):
        """Get comment"""
        return self.__comment

    def write_fd(self, out_file):
        """Write the record entry to the given file descriptor"""
        out_file.write(self.__tag)
        out_file.write(u": ")
        out_file.write(self.__content)
        out_file.write(u"\n")

        out_file.write(u"# ")
        out_file.write(self.__comment)
        out_file.write(u"\n")

    def __str__(self):
        return "Tag [%s] Content [%s] Comment [%s]" % \
            (self.__tag, self.__content, self.__comment)
