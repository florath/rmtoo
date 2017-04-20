'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Status of a requirement

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from rmtoo.lib.DateUtils import parse_date, format_date
from rmtoo.lib.RMTException import RMTException


class RequirementStatusNotDone:
    tval = "not done"

    def __init__(self, _config, rid, t):
        if t != self.tval:
            raise RMTException(92, "%s: Not done contains "
                               "additional data '%s'" % (rid, t))

    def get_output_string(self):
        return self.tval


class RequirementStatusAssigned:
    tval = "assigned"

    def __init__(self, _config, rid, t):
        ts = t.split(":")

        if len(ts) != 3:
            raise RMTException(93, "%s: Assigned values invalid '%s'"
                               % (rid, t))
        assert ts[0] == self.tval
        self.person = ts[1]
        self.date = parse_date(rid, ts[2])

    def get_person(self):
        return self.person

    def get_date_str(self):
        return format_date(self.date)

    def get_date(self):
        return self.date

    def get_output_string(self):
        return "%s (%s, %s)" % (self.tval, self.person, self.get_date_str())


class RequirementStatusFinished:
    tval = "finished"

    def __init__(self, _config, rid, t):
        if t == self.tval:
            # This is the old way: only 'finished' is specified.
            self.person = None
            self.date = None
            self.duration = None
            return
        ts = t.split(":")
        if len(ts) != 4:
            raise RMTException(94, "%s: Finished values invalid [%s]"
                               % (rid, ts))
        assert ts[0] == self.tval
        self.person = ts[1]
        self.date = parse_date(rid, ts[2])
        assert ts[3][-1] == 'h'
        self.duration = int(ts[3][:-1])

    def get_date_str(self):
        if self.date is None:
            return ""
        return format_date(self.date)

    def get_date(self):
        return self.date

    def get_duration(self):
        return self.duration

    def get_output_string(self):
        return "%s (%s, %s, %s h)" % (self.tval, self.person,
                                      self.get_date_str(), self.duration)

    def get_person(self):
        return self.person


# Factory for the RequirementStati
def create_requirement_status(config, rid, l):
    for rs in [RequirementStatusNotDone, RequirementStatusAssigned,
               RequirementStatusFinished]:
        if l.startswith(rs.tval):
            return rs(config, rid, l)

    raise RMTException(91, "%s: Status tag invalid '%s'" % (rid, l))
