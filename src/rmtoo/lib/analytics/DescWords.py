# -*- coding: utf-8 -*-
'''
 rmtoo
   Free and Open Source Requirements Management Tool

  The Description is the critical part of the requirement. This
  module checks for some good and bad words and tries a heuristic to
  get an idea about bad requirement descriptions.

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals

import re

from rmtoo.lib.Markup import Markup
from rmtoo.lib.analytics.Result import Result
from rmtoo.lib.analytics.Base import Base
from rmtoo.lib.logging import tracer


class DescWords(Base):
    """This is the assessment of each word (better regular expression).
    If the regular expression matches, the value is added.
    If the resulting number is lower than a given limit, an error is
    assumed.
    The numbers are provided on a level between [-100, 100] where
    -100 is a very very bad word and 100 is a very very good.
    Do not add the single word 'not': only do this in pairs,
    e.g. 'must not'.
    """
    words_en_GB = [
        [re.compile(r"\. "), -15,
         "Additional fullstop (not only at the end of the desctiption)"],
        [re.compile(" about "), -15, "Usage of the word 'about'"],
        [re.compile(" and "), -10, "Usage of the word 'and'"],
        [re.compile(" approximately "), -100,
         "Usage of the word 'approximately'"],
        [re.compile(r" etc\.? "), -40, "Usage of the word 'etc'"],
        [re.compile(r" e\.g\. "), -40, "Usage of the word 'e.g.'"],
        [re.compile(" has to "), 20, "Usage of the word 'has to'"],
        [re.compile(" have to "), 20, "Usage of the word 'have to'"],
        [re.compile(r" i\.e\. "), -40, "Usage of the word 'i.e.'"],
        [re.compile(" many "), -20, "Usage of the word 'many'"],
        [re.compile(" may "), 10, "Usage of the word 'may'"],
        [re.compile(" maybe "), -50, "Usage of the word 'maybe'"],
        [re.compile(" might "), 10, "Usage of the word 'might'"],
        [re.compile(" must "), 25, "Usage of the word 'must'"],
        [re.compile(" or "), -15, "Usage of the word 'or'"],
        [re.compile(" perhaps "), -100, "Usage of the word 'perhaps'"],
        [re.compile(" should "), 15, "Usage of the word 'should'"],
        [re.compile(" shall "), 15, "Usage of the word 'shall'"],
        [re.compile(" some "), -25, "Usage of the word 'some'"],
        [re.compile(" vaguely "), -25, "Usage of the word 'vaguely'"],
    ]

    words_de_DE = [
        [re.compile(r"\. "), -15,
         "Additional fullstop (not only at the end of the desctiption)"],
        [re.compile(r" ca\. "), -75, "Usage of the word 'ca.'"],
        [re.compile(" möglicherweise "), -100,
         "Usage of the word 'möglicherweise'"],
        [re.compile(" muss "), 25, "Usage of the word 'muss'"],
        [re.compile(" oder "), -15, "Usage of the word 'oder'"],
        [re.compile(" und "), -10, "Usage of the word 'und'"],
        [re.compile(" usw."), -40, "Usage of the word 'usw'"],
        [re.compile(" vielleicht "), -25, "Usage of the word 'vielleicht'"],
        [re.compile(r" z\.B\. "), -40, "Usage of the word 'z.B.'"],
    ]

    words = {"en_GB": words_en_GB,
             "de_DE": words_de_DE}

    def __init__(self, config):
        '''Sets up the DescWord object for use.'''
        Base.__init__(self)
        self.lwords = DescWords.get_lang(config)
        self.markup = Markup("txt")

    @staticmethod
    def get_lang(config):
        """Get the language from the config.

        If not present, return en_GB as default.
        """
        def_lang = config.get_value_default(
            'requirements.input.default_language', 'en_GB')

        if def_lang in DescWords.words:
            return DescWords.words[def_lang]
        tracer.warning("Language [%s] not supported, using en_GB", def_lang)
        return DescWords.words["en_GB"]

    def analyse(self, lname, text):
        """Analyse the text.

        Must be at least some positive things to get this
        positive. (An empty description is a bad one.)
        """
        level = -10
        log = []
        for wre, wlvl, wdsc in self.lwords:
            plain_txt = self.markup.replace(text).strip()
            fal = len(wre.findall(plain_txt))
            if fal > 0:
                level += fal * wlvl
                log.append("%+4d:%d*%d: %s" % (fal * wlvl, fal, wlvl, wdsc))
                # Note the result of this test in the requirement itself.
        return Result('DescWords', lname, level, log)

    def topic_continuum_set_sort(self, list_to_sort):
        '''Can only handle from the last version.'''
        return [list(list_to_sort)[-1]]

    def topic_continuum_sort(self, vcs_commit_ids, topic_sets):
        '''Because graph2 can only one topic continuum,
           the latest (newest) is used.'''
        return [topic_sets[vcs_commit_ids[-1].get_commit()]]

    def requirement_set_sort(self, list_to_sort):
        '''Sort by id.'''
        return sorted(list_to_sort, key=lambda r: r.get_id())

    def requirement(self, requirement):
        '''Checks all the requirements.
           If the result is positive, it is good.'''
        result = self.analyse(
            requirement.get_id(),
            requirement.get_value("Description").get_content())
        if result.get_value() < 0:
            self.set_failed()
        self.add_result(result)
