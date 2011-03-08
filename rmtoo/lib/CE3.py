#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# Constraint Execution and Evaluation Environment
#
# (c) 2011 by flonatel
#
# For licencing details see COPYING
#

class CE3:

    def __init__(self):
        self.values = {}

    def eval(self, cs, class_name, cstr_call):
        print("EVAL CS %s / %s / %s" % (cs, class_name, cstr_call))
        print("DDDDDDDDDDD %s" % cs.values)
        v = cs.get_value("CE3")
        print("EVAL CS V %s" % v.get_content_with_nl())

        s = ""
        for r in v.get_content_with_nl():
            s += r[1:] + "\n"

        exec(s)
        exec("self.values[class_name] = %s" % cstr_call)

        print("HJKHKJHKJHKJHKJH %s" % self.values)

    def has_key(self, k):
        return k in self.values

    def get_keys(self):
        return self.values.keys()

    def get_value(self, k):
        return self.values[k]

    # Try to unite all given ce3s into the local ce3
    def unite(self, oce3s):
        okeys = set()
        for o in oce3s:
            print("OOOOOOOOOOOOOOOOOOOO %s" % o.get_keys())
            print("OOOOOOOOOOOOOOOOOOOO %s" % set(o.get_keys()))
            okeys = okeys.union(set(o.get_keys()))
            print("OOOOOOOOOOOOOOOOOOOO %s" % okeys)
        print("OOOKKKKKKKKK %s" % okeys)
 
        for k in okeys:
            # Is the key locally available?
            mobj = None
            if self.has_key(k):
                mobj = self.get_value(k)

            print("KKKKKVVVVVVVVVVVVV %s" % k)
            lobj = []
            # Look for this in all other oce3s
            for o in oce3s:
                print("OOOOOOOOOOO %s" % o)
                if o.has_key(k):
                    lobj.append(o.get_value(k))
            print("LLLLLLLLLLLLOOOOOOOOOOOOOOOBBBBBBBBBBJJJJJ %s" % lobj)
            
            # For the execution one object is needed
            eobj = mobj
            if mobj==None:
                eobj = lobj[0]
                ### lobj.add(eobj)
                
            eobj.unite(mobj, lobj)
