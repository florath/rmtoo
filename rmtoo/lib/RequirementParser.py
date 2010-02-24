#
# Parser for Requirments
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

class RequirementParser:
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
    def parse_line(line, lineno):
        if len(line)>0 and line[-1]=='\n':
            line = line[:-1]
        # Empty line
        if len(line)==0:
            return RequirementParser.lt_empty, None, None
        # Comment line
        if line[0]=='#':
            return RequirementParser.lt_comment, None, None
        # Continue line
        if line[0]==' ':
            return RequirementParser.lt_continue, None, line
        # Is the line toooo long?
        if len(line)>80:
            print("+++ ERROR %s:%d: line too long (%d chars) '%s'"
                  % (self.id, lineno, len(line), line))
        # 'Normal' line
        ls = line.split(":", 1)
        if len(ls)==1:
            # No ':' found
            print("+++ ERROR %s:%d: no ':' in line '%s'" %
                  (self.id, lineno, line))
            return RequirementParser.lt_error, None, None
        if len(ls[0])==0:
            # ':' is first char in line
            print("+++ ERROR %s:%d: no char before ':'" %
                  (self.id, lineno))
            return RequirementParser.lt_error, None, None
        # Normal 'initial' case
        return RequirementParser.lt_initial, ls[0], \
            RequirementParser.erase_leading_ws(ls[1])

    # This implements a finite state automate with a small number
    # of states and transitions.
    @staticmethod
    def read(fd):
        # This dictionaly is the container where the input is
        # collected.
        reqs = {}
        # The linenumber is only used for log messages.
        lineno = 0
        fine = True
        # This stores the last seen key for handling continue lines. 
        last_key = None
        for line in fd:
            lineno += 1
            line_type, key, content = RequirementParser.parse_line(line, lineno)

            # Skip empty lines
            if line_type==RequirementParser.lt_empty:
                continue
            # Skip comments
            if line_type==RequirementParser.lt_comment:
                continue
            # Handle low-level parse errors
            if line_type==RequirementParser.lt_error:
                fine = False
                print("+++ ERROR: cannot parse line")
                continue
            # It's a continue line from a previous already introduced
            # tag. 
            if line_type==RequirementParser.lt_continue:
                if last_key==None:
                    print("+++ ERROR %s:%d: continue line without " \
                              + "initial line" % (RequirementParser.id, lineno))
                    fine = False
                reqs[last_key] += content
                continue
            # New line with initial tag.
            if line_type==RequirementParser.lt_initial:
                if key in reqs:
                    print("+++ ERROR %s:%d: key '%s' already exists" %
                          (RequirementParser.id, lineno, key))
                    fine = False
                    continue
                reqs[key] = content
                last_key = key
                continue
            # Uups: nothing of them all: must be something strange.
            # Results in an error.
            print("+++ ERROR %s:%d: Invalid line_type '%d'" %
                  (RequirementParser.id, lineno, line_type))
            fine = False

        if fine:
            return reqs
        else:
            return None
    
