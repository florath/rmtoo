'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Common statistics functions

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import datetime
from scipy import stats

from rmtoo.lib.RequirementStatus import RequirementStatusNotDone, \
    RequirementStatusAssigned, RequirementStatusFinished
from rmtoo.lib.ClassType import ClassTypeSelected


class Statistics(object):

    @staticmethod
    def inc_stats(rv, start_date, idx, invented_on, today, efe):
        start_index = (invented_on - start_date).days
        end_index = (today - start_date).days
        for i in range(start_index, end_index + 1):
            rv[i][idx] += efe

    @staticmethod
    def prepare_result_vector(start_date, end_date):
        rv = []
        diff = end_date - start_date
        diff_in_days = diff.days

        for _ in range(0, diff_in_days + 1):
            rv.append([0, 0, 0])
        return rv

    @staticmethod
    def get_units_generic(rset, start_date, end_date, skip_requirement):
        # Run through the requirements and count the not done
        # depending on the date.
        rv = Statistics.prepare_result_vector(start_date, end_date)

        for _, req in rset.get_requirements_iteritems():
            invented_on = req.get_value("Invented on")

            if start_date > invented_on:
                invented_on = start_date

            assert(end_date >= invented_on)

            status = req.get_status()
            efe = req.get_value("Effort estimation")
            if efe is None:
                continue

            if skip_requirement(req):
                continue

            if isinstance(status, RequirementStatusNotDone):
                # Only count those which are implementable
                #                rclass = req.get_value("Class")
                if req.get_value("Class").is_implementable():
                    Statistics.inc_stats(rv, start_date, 0, invented_on,
                                         end_date, efe)
            elif isinstance(status, RequirementStatusAssigned):
                assigned_date = status.get_date()

                if assigned_date < start_date:
                    assigned_date = start_date

                adm1 = assigned_date - datetime.timedelta(1)

                # Count from start_date until it was assigned as open:
                Statistics.inc_stats(rv, start_date, 0, start_date,
                                     adm1, efe)
                # Count from assigned date until end_date as assigned
                Statistics.inc_stats(rv, start_date, 1, assigned_date,
                                     end_date, efe)

            elif isinstance(status, RequirementStatusFinished):
                finished_date = status.get_date()

                if finished_date is None:
                    continue

                if finished_date < start_date:
                    finished_date = start_date

                adm1 = finished_date - datetime.timedelta(1)

                # Count from start_date until it was finished as open:
                Statistics.inc_stats(rv, start_date, 0, start_date,
                                     adm1, efe)
                # Count from assigned date until end_date as assigned
                Statistics.inc_stats(rv, start_date, 2, finished_date,
                                     end_date, efe)
        return rv

    @staticmethod
    def get_units(rset, start_date, end_date):

        def skip_never(_):
            return False

        return Statistics.get_units_generic(rset, start_date,
                                            end_date, skip_never)

    @staticmethod
    def get_units_sprint(rset, start_date, end_date):

        def skip_not_selected(req):
            return not isinstance(req.get_value("Class"), ClassTypeSelected)

        return Statistics.get_units_generic(rset, start_date, end_date,
                                            skip_not_selected)

    @staticmethod
    def output_stat_files(filename, start_date, rv):
        with open(filename, "w") as ofile:
            one_day = datetime.timedelta(1)
            iday = start_date
            for r in rv:
                ofile.write("%s %d %d %d %d\n"
                            % (iday.isoformat(), r[0], r[1], r[2],
                               r[0] + r[1]))
                iday += one_day

        # Estimation file
        with open(filename + ".est", "w") as eofile:
            x = list(i for i in range(0, len(rv)))
            y = list(x[0] + x[1] for x in rv)

            gradient, intercept, _r_value, _p_value, _std_err \
                = stats.linregress(x, y)

            if gradient >= 0.0:
                print("+++ WARN: gradient is positive [%d]: "
                      "you get more than you finished" % gradient)
                eofile.close()
                return

            d = intercept / -gradient
            end_date = start_date + datetime.timedelta(d)

            eofile.write("%s %d\n" % (start_date, intercept))
            eofile.write("%s 0\n" % end_date)
