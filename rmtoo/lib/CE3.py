'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Constraint Execution and Evaluation Environment
  Heuristics to check the quality of the requirements.

 (c) 2011-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from rmtoo.lib.RMTException import RMTException


# Some common used functions
def ce3assert(bool_expr, errmsg):
    """Checks the bool expression; if false emits an exception"""
    if not bool_expr:
        raise RMTException(90, "Failed CE3 assert: msg [%s]" % errmsg)


class CE3(object):
    """Constraint Execution and Evaluation Environment"""

    def __init__(self):
        self.values = {}

    # This is not found because of the 'exec' call
    # pylint: disable=no-self-use,exec-used,unused-argument
    def eval(self, constraint, class_name, cstr_call):
        """Evaluates the constraint using the provided parameters"""
        constraint_value = constraint.get_value("CE3")
        if constraint_value is None:
            return

        exec_str = ""
        for exec_line in constraint_value.get_content_with_nl():
            exec_str += exec_line[1:] + "\n"

        exec(exec_str) in globals(), locals()
        exec("self.values[class_name] = %s" % cstr_call)

    def has_key(self, k):
        return k in self.values

    def get_keys(self):
        return self.values.keys()

    def get_value(self, k):
        return self.values[k]

    def set_value(self, k, v):
        self.values[k] = v

    def get_values(self):
        return self.values

    def len(self):
        return len(self.values)

    # Try to unite all given ce3s into the local ce3
    def unite(self, oce3s):
        okeys = set()
        for o in oce3s:
            okeys = okeys.union(set(o.get_keys()))

        for k in okeys:
            # Is the key locally available?
            mobj = None
            if k in self.values:
                mobj = self.get_value(k)

            lobj = []
            # Look for this in all other oce3s
            for o in oce3s:
                if k in o.values:
                    lobj.append(o.get_value(k))

            # For the execution one object is needed
            eobj = mobj
            if mobj is None:
                eobj = lobj[0]
                # lobj.add(eobj)

            ro = eobj.unite(mobj, lobj)

            if ro is not None:
                # There is a new constraint for the local key
                assert mobj is None
                self.set_value(k, ro)
