#
# Analytics: Description Words
#
#  The Description is the critical part of the requirement. This
#  module checks for some good and bad words and tries a heuristic to
#  get an idea about bad requirement descriptions.
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

import re

from rmtoo.lib.LaTeXMarkup import LaTeXMarkup

class DescWords:

    # This is the assesment of each word (better regular expression).
    # If the regular expression matches, the value is added.
    # If the resulting number is lower than a given limit, an error is
    # assumed. 
    # The numbers are provided on a level between [-100, 100] where
    # -100 is a very very bad word and 100 is a very very good.
    # Do not add the single word 'not': only do this in pairs,
    # e.g. 'must not'.
    words = [
        [ re.compile("^.*\. .+$"), -15, "Additional fullstop (not only at the end of the desctiption)"],
        [ re.compile("^.* about .*$"), -15, "Usage of the word 'about'"],
        [ re.compile("^.* and .*$"), -10, "Usage of the word 'and'"],
        [ re.compile("^.* approximately .*$"), -100, "Usage of the word 'approximately'"],
        [ re.compile("^.* etc\.? .*$"), -40, "Usage of the word 'etc'"],
        [ re.compile("^.* e\.g\. .*$"), -40, "Usage of the word 'e.g.'"],
        [ re.compile("^.* i\.e\. .*$"), -40, "Usage of the word 'i.e.'"],
        [ re.compile("^.* many .*$"), -20, "Usage of the word 'many'"],
        [ re.compile("^.* may .*$"), 10, "Usage of the word 'may'"],
        [ re.compile("^.* maybe .*$"), -50, "Usage of the word 'maybe'"],
        [ re.compile("^.* might .*$"), 10, "Usage of the word 'might'"],
        [ re.compile("^.* must .*$"),  25, "Usage of the word 'must'"],
        [ re.compile("^.* or .*$"), -15, "Usage of the word 'or'"],
        [ re.compile("^.* perhaps .*$"), -100, "Usage of the word 'perhaps'"],
        [ re.compile("^.* should .*$"), 15, "Usage of the word 'should'"],
        [ re.compile("^.* shall .*$"), 15, "Usage of the word 'shall'"],
        [ re.compile("^.* some .*$"), -25, "Usage of the word 'some'"],
        [ re.compile("^.* vaguely .*$"), -25, "Usage of the word 'vaguely'"],
    ]

    @staticmethod
    def run(config, reqs, topics):
        ok = True
        for _, req in reqs.reqs.iteritems():
            # Must be at least some positive things to get this
            # positive. (An empty description is a bad one.)
            level = -10
            log = []
            for wre, wlvl, wdsc in DescWords.words:
                plain_txt = LaTeXMarkup.replace_txt(
                    req.tags["Description"]).strip()
                if wre.match(plain_txt):
                    level += wlvl
                    log.append("%+4d: %s" % (wlvl, wdsc))
            # Note the result of this test in the requirement itself.
            req.analytics["DescWords"] = [level, log]
            if level<0:
                ok = False
            
        return ok
