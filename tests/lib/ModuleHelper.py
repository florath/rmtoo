#
# Helper for testing modules and related classes
#
# (c) 2010,2017 by flonatel
#
# For licencing details see COPYING
#


def mods_list(lm, mod_base_dir):
    mods_name = mod_base_dir.split("/")
    ml = ["rmtoo"]
    ml.extend(mods_name)
    ml.append(lm)
    return ml
