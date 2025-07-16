'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Common statistics functions

 (c) 2010-2012,2017,2025 by flonatel GmbH & Co. KG / Andreas Florath

 For licensing details see COPYING
'''

import datetime
import math
from scipy import stats

from rmtoo.lib.RequirementStatus import RequirementStatusNotDone, \
    RequirementStatusAssigned, RequirementStatusFinished
from rmtoo.lib.ClassType import ClassTypeSelected


class Statistics(object):
    """Statistics handling"""

    # pylint: disable=too-many-arguments
    @staticmethod
    def inc_stats(result_vec, start_date, idx, invented_on, today, efe):
        """Increment statistics for the given time period"""
        start_index = (invented_on - start_date).days
        end_index = (today - start_date).days
        for i in range(start_index, end_index + 1):
            result_vec[i][idx] += efe

    @staticmethod
    def prepare_result_vector(start_date, end_date):
        """Prepares a statistics result vector for the given time period"""
        result_vec = []
        diff = end_date - start_date
        diff_in_days = diff.days

        for _ in range(0, diff_in_days + 1):
            result_vec.append([0, 0, 0])
        return result_vec

    @staticmethod
    def get_units_generic(rset, start_date, end_date, skip_requirement):
        """Run through the requirements and count the not done
        depending on the date.
        """
        result_vec = Statistics.prepare_result_vector(start_date, end_date)

        for _, req in rset.get_requirements_iteritems():
            invented_on = req.get_value("Invented on")

            if start_date > invented_on:
                invented_on = start_date

            assert end_date >= invented_on

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
                    Statistics.inc_stats(
                        result_vec, start_date, 0, invented_on,
                        end_date, efe)
            elif isinstance(status, RequirementStatusAssigned):
                assigned_date = status.get_date()

                if assigned_date < start_date:
                    assigned_date = start_date

                adm1 = assigned_date - datetime.timedelta(1)

                # Count from start_date until it was assigned as open:
                Statistics.inc_stats(result_vec, start_date, 0, start_date,
                                     adm1, efe)
                # Count from assigned date until end_date as assigned
                Statistics.inc_stats(result_vec, start_date, 1, assigned_date,
                                     end_date, efe)

            elif isinstance(status, RequirementStatusFinished):
                finished_date = status.get_date()

                if finished_date is None:
                    continue

                if finished_date < start_date:
                    finished_date = start_date

                adm1 = finished_date - datetime.timedelta(1)

                # Count from start_date until it was finished as open:
                Statistics.inc_stats(result_vec, start_date, 0, start_date,
                                     adm1, efe)
                # Count from assigned date until end_date as assigned
                Statistics.inc_stats(result_vec, start_date, 2, finished_date,
                                     end_date, efe)
        return result_vec

    @staticmethod
    def get_units(rset, start_date, end_date):
        """Retreive all units"""

        def _skip_never(_):
            return False

        return Statistics.get_units_generic(rset, start_date,
                                            end_date, _skip_never)

    @staticmethod
    def get_units_sprint(rset, start_date, end_date):
        """Retreive units from sprint"""

        def _skip_not_selected(req):
            return not isinstance(req.get_value("Class"), ClassTypeSelected)

        return Statistics.get_units_generic(rset, start_date, end_date,
                                            _skip_not_selected)

    @staticmethod
    def _output_stat_files_stats(filename, start_date, result_vec):
        """Write the stats file"""
        with open(filename, "w") as ofile:
            if not result_vec:
                # Write minimal fallback data for empty result set
                ofile.write("# No data available for statistics\n")
                ofile.write("%s 0 0 0 0\n" % start_date.isoformat())
                return

            one_day = datetime.timedelta(1)
            iday = start_date
            for result in result_vec:
                ofile.write("%s %d %d %d %d\n"
                            % (iday.isoformat(), result[0], result[1],
                               result[2], result[0] + result[1]))
                iday += one_day

    @staticmethod
    def _output_stat_files_est(filename, start_date, result_vec):
        """Write the estimation file"""
        # x, y and d are completely sensible names here
        # pylint: disable=invalid-name
        with open(filename + ".est", "w") as eofile:
            x = list(i for i in range(0, len(result_vec)))
            y = list(item[0] + item[1] for item in result_vec)

            # Check for sufficient data before regression analysis
            if len(result_vec) < 2:
                print("+++ WARN: insufficient data for regression analysis")
                # Write minimal fallback data for visualization
                eofile.write("# Insufficient data for regression analysis\n")
                eofile.write("%s 0\n" % start_date)
                eofile.close()
                return

            gradient, intercept, _r_value, _p_value, _std_err \
                = stats.linregress(x, y)

            # Check for NaN values from insufficient data
            if math.isnan(gradient) or math.isnan(intercept):
                print("+++ WARN: insufficient data for regression analysis")
                # Write minimal fallback data for visualization
                eofile.write("# Insufficient data for regression analysis\n")
                eofile.write("%s 0\n" % start_date)
                eofile.close()
                return

            if gradient >= 0.0:
                print("+++ WARN: gradient is positive [%d]: "
                      "you get more than you finished" % gradient)
                eofile.close()
                return

            # Gradient too small, no meaningful progress
            if abs(gradient) < 0.001:
                print("+++ WARN: gradient is too small [%e]: "
                      "no meaningful progress detected" % gradient)
                eofile.close()
                return

            d = intercept / -gradient
            try:
                end_date = start_date + datetime.timedelta(d)
            except OverflowError:
                print("+++ WARN: calculated end date would overflow: "
                      "prediction too far in the future")
                eofile.close()
                return

            eofile.write("%s %d\n" % (start_date, intercept))
            eofile.write("%s 0\n" % end_date)

    @staticmethod
    def output_stat_files(filename, start_date, result_vec):
        """Write the statistics to the output file"""
        Statistics._output_stat_files_stats(filename, start_date, result_vec)
        Statistics._output_stat_files_est(filename, start_date, result_vec)
