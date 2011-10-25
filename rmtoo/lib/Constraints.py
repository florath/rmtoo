#
# rmtoo 
#   Free and Open Source Requirements Management Tool
#
# Constraints handling
#
# (c) 2010-2011 by flonatel
#
# For licencing details see COPYING
#

class Constraints:

    @staticmethod
    def set_default_values(cfg):
        cfg.set_value('constraints.search_dirs',
                      ['/usr/share/pyshared/rmtoo/collection/constraints'])

    @staticmethod
    def collect(topic_set):
        t = topic_set.get_master()
        cnsts = {}

        # Recursive (local) function to ge the constraints container filled
        # up.
        def collect_constraints_rec(topic):
            for req in topic.reqs:
                if req.values["Constraints"] != None:
                    for k, v in req.values["Constraints"].items():
                        cnsts[k] = v

            for ltopic in topic.outgoing:
                collect_constraints_rec(ltopic)

        collect_constraints_rec(t)
        return cnsts


