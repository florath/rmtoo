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

    def __init__(self, tag, content, comment=None):
        Encoding.check_unicode(tag)
        self.__tag = tag
        Encoding.check_unicode(content)
        self.__content = content
        if comment is not None:
            Encoding.check_unicode(comment)
        self.__comment = comment

    def get_tag(self):
        return self.__tag

    def get_content(self):
        return self.__content.lstrip()

    def set_content(self, c):
        Encoding.check_unicode(c)
        self.__content = c

    def set_comment(self, c):
        Encoding.check_unicode(c)
        self.__comment = c

    def get_comment(self):
        return self.__comment

    def write_fd(self, fd):
        fd.write(self.__tag)
        fd.write(u": ")
        fd.write(self.__content)
        fd.write(u"\n")

        fd.write(u"# ")
        fd.write(self.__comment)
        fd.write(u"\n")

    def __str__(self):
        return "Tag [%s] Content [%s] Comment [%s]" % \
            (self.__tag, self.__content, self.__comment)
