#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# Common statistics functions
#
# (c) 2010-2011 by flonatel
#
# For licencing details see COPYING
#

import datetime

from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RequirementStatus import RequirementStatusNotDone, \
    RequirementStatusAssigned, RequirementStatusFinished
from rmtoo.lib.ClassType import ClassTypeImplementable, \
    ClassTypeDetailable, ClassTypeSelected

class Statistics:

    @staticmethod
    def inc_stats(rv, start_date, idx, invented_on, today, efe):
        start_index = (invented_on - start_date).days
        end_index = (today - start_date).days
        for i in xrange(start_index, end_index + 1):
            rv[i][idx] += efe

    @staticmethod
    def prepare_result_vector(start_date):
        today = datetime.date.today()
        rv = []
        diff = today - start_date
        diff_in_days = diff.days

        for i in xrange(0, diff_in_days + 1):
            rv.append([0, 0, 0])
        return rv
    
    @staticmethod
    def get_units_generic(rset, start_date, skip_requirement):
        # Run through the requirements and count the not done
        # depending on the date.
        rv = Statistics.prepare_result_vector(start_date)
        today = datetime.date.today()

        for rid, req in rset.reqs.iteritems():
            invented_on = req.get_value("Invented on")

            if start_date > invented_on:
                invented_on = start_date

            assert(today>=invented_on)

            status = req.get_status()
            efe = req.get_value("Effort estimation")
            if efe==None:
                continue

            if skip_requirement(req):
                continue

            if isinstance(status, RequirementStatusNotDone):
                # Only count those which are implementable
                rclass = req.get_value("Class")
                if req.get_value("Class").is_implementable():
                    Statistics.inc_stats(rv, start_date, 0, invented_on, 
                                         today, efe)
            elif isinstance(status, RequirementStatusAssigned):
                assigned_date = status.get_date()

                if assigned_date < start_date:
                    assigned_date = start_date

                adm1 = assigned_date - datetime.timedelta(1)

                # Count from start_date until it was assigned as open:
                Statistics.inc_stats(rv, start_date, 0, start_date, 
                                     adm1, efe)
                # Count from assigned date until today as assigned
                Statistics.inc_stats(rv, start_date, 1, assigned_date, 
                                     today, efe)

            elif isinstance(status, RequirementStatusFinished):
                finished_date = status.get_date()
                
                if finished_date == None:
                    continue

                if finished_date < start_date:
                    finished_date = start_date

                adm1 = finished_date - datetime.timedelta(1)

                # Count from start_date until it was finished as open:
                Statistics.inc_stats(rv, start_date, 0, start_date, 
                                     adm1, efe)
                # Count from assigned date until today as assigned
                Statistics.inc_stats(rv, start_date, 2, finished_date, 
                                     today, efe)
        return rv

    @staticmethod
    def get_units(rset, start_date):

        def skip_never(req):
            return False

        return Statistics.get_units_generic(rset, start_date, skip_never)

    @staticmethod
    def get_units_sprint(rset, start_date):

        def skip_not_selected(req):
            return not isinstance(req.get_value("Class"), ClassTypeSelected)

        return Statistics.get_units_generic(rset, start_date, skip_not_selected)
