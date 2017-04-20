'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Converts the (allowed) LaTeX markup to other output markup
  formats.

 (c) 2010,2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
import re

# At the moment there is no need to have multiple files, because there
# is only one additional markup.


class LaTeXMarkup2HTML(object):
    convert_markup = [
        "</p><p>",
        "<strong>\\1</strong>",
        "<em>\\1</em>",
        ]


class LaTeXMarkup2Txt(object):
    convert_markup = [
        "",
        "\\1",
        "\\1",
        ]


class LaTeXMarkup(object):
    markup = [
        "\\\\par",                # New paragraph
        "\\\\textbf{([\w\s]*)}",  # Bold
        "\\\\textsl{([\w\s]*)}",  # Italics
        ]

    @staticmethod
    def replace_generic(cmdset, t):
        for i in range(len(LaTeXMarkup.markup)):
            t = re.sub(LaTeXMarkup.markup[i], cmdset[i], t,
                       flags=re.UNICODE)
        return t

    @staticmethod
    def replace_html(t):
        return LaTeXMarkup.replace_generic(
            LaTeXMarkup2HTML.convert_markup, t)

    @staticmethod
    def replace_html_par(t):
        return "<p>" + LaTeXMarkup.replace_generic(
            LaTeXMarkup2HTML.convert_markup, t) + "</p>"

    @staticmethod
    def replace_txt(t):
        return LaTeXMarkup.replace_generic(
            LaTeXMarkup2Txt.convert_markup, t)
