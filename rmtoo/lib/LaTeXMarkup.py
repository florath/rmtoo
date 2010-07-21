#
# LaTeXMarkup
#
#  Converts the (allowed) LaTeX markup to other output markup
#  formats. 
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

import re

# At the moment there is no need to have multiple files, because there
# is only one additional markup.

class LaTeXMarkup2HTML:
    convert_markup = [
        "</p><p>",
        "<b>\\1</b>",
        "<i>\\1</i>",
        ]

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
        
