'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Converts the (allowed) LaTeX markup to other output markup
#  formats.
   
 (c) 2010,2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import re

# At the moment there is no need to have multiple files, because there
# is only one additional markup.

# pylint: disable=W0232
class LaTeXMarkup2HTML:
    convert_markup = [
        "</p><p>",
        "<b>\\1</b>",
        "<i>\\1</i>",
        ]

# pylint: disable=W0232
class LaTeXMarkup2Txt:
    convert_markup = [
        "",
        "\\1",
        "\\1",
        ]

# pylint: disable=W0232
class LaTeXMarkup:
    markup = [
        "\\\\par",               # New paragraph
        "\\\\textbf{([\w\s]*)}", # Bold
        "\\\\textsl{([\w\s]*)}", # Italics
        ]

    @staticmethod
    def replace_generic(cmdset, t):
        for i in xrange(len(LaTeXMarkup.markup)):
            t = re.sub(LaTeXMarkup.markup[i], cmdset[i], t)
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
