'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Converts the (allowed) LaTeX markup to other output markup
  formats.

 (c) 2010,2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
import re

from six import iteritems
from stevedore import extension

# General remark:
# Using steverdore for class loading renders all the objects
# only having one method.


# pylint: disable=too-few-public-methods
class MarkupBase(object):
    """Base Markup Class

    This class implements the method to really replace
    the text - based on parameters passed in by sub-classes
    constructor.
    """

    def __init__(self, markup_map):
        self.__markup_map = markup_map

    def replace(self, raw_input_str):
        """Replace the raw_input_str based on the existing markup_map"""
        for pattern, replacement in iteritems(self.__markup_map):
            raw_input_str = re.sub(pattern, replacement,
                                   raw_input_str, flags=re.UNICODE)
        return raw_input_str


# pylint: disable=too-few-public-methods
class LaTeX(object):
    """LaTeX Markup object"""

    def replace(self, raw_input_str):  # pylint: disable=no-self-use
        """Replace LaTeX Markup for LaTeX is a noop"""
        return raw_input_str


class Txt(MarkupBase):
    """Plain Text Markup object"""

    def __init__(self):
        MarkupBase.__init__(self, {
            r"\\par": "",
            r"\\textbf{([\w\s]*)}": "\\1",
            r"\\textsl{([\w\s]*)}": "\\1",
        })


class Html(MarkupBase):
    """HTML Markup object"""

    def __init__(self):
        MarkupBase.__init__(self, {
            r"\\par": "</p><p>",
            r"\\textbf{([\w\s]*)}": "<strong>\\1</strong>",
            r"\\textsl{([\w\s]*)}": "<em>\\1</em>",
        })

    def replace_par(self, raw_input_str):
        """Replaces text inside a complete paragraph"""
        return "<p>" + self.replace(raw_input_str) + "</p>"


class Markup(object):
    """Generic class for Markup (replacement)"""

    def __init__(self, name):
        self.__plugin_manager = extension.ExtensionManager(
            namespace='rmtoo.output.markup',
            invoke_on_load=False)
        self.__impl = self.__plugin_manager[name].plugin()

    def replace(self, raw_input_str):
        """Replaces the raw_input with the real input"""
        return self.__impl.replace(raw_input_str)

    def replace_par(self, raw_input_str):
        """Replaces the input with the real input as a complete paragraph"""
        return self.__impl.replace_par(raw_input_str)
