#
# Parser for rmtoo input files
#
#  There are a lot of different input files for the rmtoo but they all
#  share the same format.  This parser reads in these files.
#  Note that some functions rely on the order in which tags/values are 
#  given in the input file.
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

class Parser:
    # Line Type
    # The parse() function returns one of those
    lt_empty = 1
    lt_comment = 2
    lt_continue = 3
    lt_error = 4
    lt_initial = 5

    # Erase leading whithspace
    @staticmethod
    def erase_leading_ws(l):
        while len(l)>0 and l[0]==" ":
            l = l[1:]
        return l
    
    # Cut off a possible tailing newline at the end of the line    
    @staticmethod
    def erase_tailing_newline(line):
        if len(line)>0 and line[-1]=='\n':
            return line[:-1]
        return line

    # The 'parse_line()' does the whole job.  It reads in line, cuts
    # them down and also handle special lines like comments or emtpy
    # lines.
    # It returns three paramters:
    # 1) The line_type
    # 2) If line_type is continue: the additional characters for the
    #    tag. 
    # 3) If line_type is initial: the tag and the beginning of the
    #    characters for the tag.
    @staticmethod
    def parse_line(rid, line, lineno):
        line = Parser.erase_tailing_newline(line)
        # Empty line
        if len(line)==0:
            return Parser.lt_empty, None, None
        # Comment line
        if line[0]=='#':
            return Parser.lt_comment, None, None
        # Continue line
        if line[0]==' ':
            return Parser.lt_continue, None, line
        # Is the line toooo long?
        if len(line)>80:
            print("+++ ERROR %s:%d: line too long (%d chars) '%s'"
                  % (rid, lineno, len(line), line))
            return Parser.lt_error, None, None
        # 'Normal' line
        ls = line.split(":", 1)
        if len(ls)==1:
            # No ':' found
            print("+++ ERROR %s:%d: no ':' in line '%s'" %
                  (rid, lineno, line))
            return Parser.lt_error, None, None
        if len(ls[0])==0:
            # ':' is first char in line
            print("+++ ERROR %s:%d: no char before ':'" %
                  (rid, lineno))
            return Parser.lt_error, None, None
        # Normal 'initial' case
        return Parser.lt_initial, ls[0], \
            Parser.erase_leading_ws(ls[1])

    # This implements a finite state automate with a small number
    # of states and transitions.
    @staticmethod
    def read_as_container(rid, fd, cntr):
        # The linenumber is only used for log messages.
        lineno = 0
        fine = True
        # This stores the last seen key for handling continue lines. 
        last_key = None
        for line in fd:
            lineno += 1
            line_type, key, content = Parser.parse_line(rid, line, lineno)

            # Skip empty lines
            if line_type==Parser.lt_empty:
                continue
            # Skip comments
            if line_type==Parser.lt_comment:
                continue
            # Handle low-level parse errors
            if line_type==Parser.lt_error:
                fine = False
                print("+++ ERROR: cannot parse line")
                continue
            # It's a continue line from a previous already introduced
            # tag. 
            if line_type==Parser.lt_continue:
                if last_key==None:
                    print("+++ ERROR %s:%d: continue line without "
                          "initial line" % (rid, lineno))
                    fine = False
                    continue
                cntr.append_to_last(last_key, content)
                continue
            # New line with initial tag.
            if line_type==Parser.lt_initial:
                if not cntr.insert(rid, lineno, key, content):
                    fine = False
                    continue
                last_key = key
                continue
            # Uups: nothing of them all: must be something strange.
            # Results in an error.
            print("+++ ERROR %s:%d: Invalid line_type '%d'" %
                  (rid, lineno, line_type))
            print("+++ please report this to sf@flonatel.org")
            assert(False)

        return fine

    @staticmethod
    def read_common(rid, fd, cntr):
        if not Parser.read_as_container(rid, fd, cntr):
            return None
        return cntr.r

    # This read returns a list of key-value pairs.
    # Each list element contains a pair (list) of the key and the
    # value.
    # Parameters:
    #   rid: the requirement id for logging
    #   fd: the file to read from
    @staticmethod
    def read_as_list(rid, fd):
        
        # Result containter for list
        class list_container:

            def __init__(self):
                self.r = []

            def append_to_last(self, last_key, content):
                assert(self.r[-1][0]==last_key)
                self.r[-1][1] += content

            def insert(self, rid, lineno, key, content):
                self.r.append([key, content])
                return True

        return Parser.read_common(rid, fd, list_container())

    # This method returns a dictionary.  The key-value pairs can
    # directly be found inside the dict.
    # Parameters:
    #   rid: the requirement id for logging
    #   fd: the file to read from
    @staticmethod
    def read_as_map(rid, fd):

        # Result containter for dictionary
        class dict_container:

            def __init__(self):
                self.r = {}

            def append_to_last(self, last_key, content):
                self.r[last_key] += content

            def insert(self, rid, lineno, key, content):
                if key in self.r:
                    print("+++ ERROR %s:%d: key '%s' already exists" %
                          (rid, lineno, key))
                    return False
                self.r[key] = content
                return True

        return Parser.read_common(rid, fd, dict_container())
