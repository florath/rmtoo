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


class CE3(dict):
    """Constraint Execution and Evaluation Environment

    All results from the execution phase are stored in the dict.
    """

    def __hash__(self):
        return hash(tuple(self.keys()))

    def __repr__(self):
        return "<CE3 %s>" % list(self.keys())

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
        exec("self[class_name] = %s" % cstr_call)

    def unite(self, oce3s):
        """Try to unite all given ce3s into the local ce3"""
        okeys = set()
        for oce in oce3s:
            okeys = okeys.union(set(oce.keys()))

        for k in okeys:
            # Is the key locally available?
            mobj = None
            if k in self:
                mobj = self[k]

            lobj = []
            # Look for this in all other oce3s
            for oce in oce3s:
                if k in oce:
                    lobj.append(oce[k])

            # For the execution one object is needed
            eobj = mobj
            if mobj is None:
                eobj = lobj[0]
                # lobj.add(eobj)

            new_constraint = eobj.unite(mobj, lobj)

            if new_constraint is not None:
                # There is a new constraint for the local key
                assert mobj is None
                self[k] = new_constraint
