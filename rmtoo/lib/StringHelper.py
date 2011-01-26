#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# StringHelper
#   Small helper and utils for the string class
#
# (c) 2011 by flonatel
#
# For licencing details see COPYING
#

class StringHelper:

    # This is mostly the same as the string 'join()' method, but
    # The delimiter is also added to the end of the list.
    @staticmethod
    def join_ate(delim, jlist):
        r = ""
        for j in jlist:
            r += j + delim
        return r

