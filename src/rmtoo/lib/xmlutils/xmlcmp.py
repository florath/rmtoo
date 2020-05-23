'''
 rmtoo
   Free and Open Source Requirements Management Tool

 Library for comparing XML documents.

 There is the need to compare XML documents when running test cases:
 the expected documents are compared with the test-case generated
 ones.
 Looks that there is currently no existing out of the box solution
 for python to do this.
 The 'xmldiff' project does a similar thing, but with a different
 aspect: it outputs a (minimal) diff set which can be applied to one
 of the document to get the other.  This is much more than needed for
 the test result comparison: here only a 'yes they are the same' or
 'no they are not the same' (maybe with a hint of the difference's
 location) is needed.

 (c) 2011,2017,2020 by flonatel GmbH & Co. KG
 For licensing details see COPYING

 SPDX-License-Identifier: GPL-3.0-or-later

 This file is part of rmtoo.

 rmtoo is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 rmtoo is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with rmtoo.  If not, see <https://www.gnu.org/licenses/>.
'''
from __future__ import unicode_literals

import copy

from xml.dom.minidom import parse, parseString
from rmtoo.lib.logging import tracer
from rmtoo.lib.logging.LogFormatter import LogFormatter


def xml_check_type(xml_doc_a, xml_doc_b, xpath):
    '''Check for the type.'''
    if xml_doc_a.nodeType != xml_doc_b.nodeType:
        return False, "Node types differ [%s] != [%s] at [%s]" % \
            (xml_doc_a.nodeType, xml_doc_b.nodeType, xpath)
    return None, None


def xml_check_text_content(xml_doc_a, xml_doc_b, xpath):
    '''Check for Text content.'''
    if xml_doc_a.nodeType == xml_doc_a.TEXT_NODE \
       or xml_doc_a.nodeType == xml_doc_a.CDATA_SECTION_NODE:
        if xml_doc_a.data != xml_doc_b.data:
            return False, "Text Node data differs [%s] != [%s] at [%s]" % \
                (xml_doc_a.data, xml_doc_b.data, xpath)
        return True, None
    return None, None


def xml_check_name(xml_doc_a, xml_doc_b, xpath):
    '''Check for the name.'''
    if xml_doc_a.tagName != xml_doc_b.tagName:
        return False, "Tag names differ [%s] != [%s] at [%s]" % \
            (xml_doc_a.tagName, xml_doc_b.tagName, xpath)
    return None, None


def xml_check_attributes(xml_doc_a, xml_doc_b, xpath):
    '''Check for the attributes.'''
    a_attr_sorted = sorted(xml_doc_a.attributes.items())
    b_attr_sorted = sorted(xml_doc_b.attributes.items())
    if a_attr_sorted != b_attr_sorted:
        return False, "Attributes for tag [%s] " \
            "differ: [%s] != [%s] at [%s]" % \
            (xml_doc_a.tagName, a_attr_sorted, b_attr_sorted, xpath)
    return None, None


def xml_check_child_count(xml_doc_a, xml_doc_b, xpath):
    '''Checks if both nodes contain the same number of child nodes.'''
    if len(xml_doc_a.childNodes) != len(xml_doc_b.childNodes):
        return False, "Number of child nodes differs " \
            "[%s] != [%s] at [%s]" % \
            (len(xml_doc_a.childNodes), len(xml_doc_b.childNodes), xpath)
    return None, None


def xml_check_children(xml_doc_a, xml_doc_b, xpath):
    '''Create a shallow copy of b's children (and remove nodes which
       are seen as equal).'''
    bcn = []
    for child in xml_doc_b.childNodes:
        bcn.append(copy.copy(child))

    # Iterate through the child nodes of 'a' ...
    bcn_found_cnt = len(bcn)
    for a_children in xml_doc_a.childNodes:
        tracer.debug(LogFormatter.format(
            97, "xmlcmp: comparing child node [%s]" % a_children))
        # ... check if there is the same one in 'b'
        found_ac = False
        for b_children in bcn:
            result, err_msg = xmlequals(a_children, b_children,
                                        xpath + "/" + xml_doc_a.tagName)
            if result:
                # a_children and b_children are equal: remove b_children
                # from bcn and skip to the next a_children
                bcn_found_cnt -= 1
                found_ac = True
                tracer.debug(LogFormatter.format(
                    98, "[%s] xmlcmp: found equal subtrees [%s]"
                    % (xpath, a_children)))
                tracer.debug(LogFormatter.format(
                    99, "[%s] xmlcmp: remaining elements [%s]"
                    % (xpath, bcn)))
                break
        if not found_ac:
            return False, "Child node [%s] not found at [%s] - " \
                "last error was [%s]" % (a_children, xpath, err_msg)

    assert bcn_found_cnt == 0
    return True, None


def xmlequals(xml_doc_a, xml_doc_b, xpath):
    '''Calls the different xml_check helper functions.
       Returns True, None if xml document a and b are the same,
       Returns False and an error message if they differ.'''
    for check_func in [xml_check_type, xml_check_text_content,
                       xml_check_name, xml_check_attributes,
                       xml_check_child_count, xml_check_children]:
        result, err_msg = check_func(xml_doc_a, xml_doc_b, xpath)
        if result in (False, True):
            assert result is not None
            return result, err_msg
        assert result is None
    return True, None


def xmlcmp_files(file1, file2):
    '''Compares two xml files.'''
    doc1 = parse(file1)
    doc2 = parse(file2)
    return xmlequals(doc1.documentElement, doc2.documentElement, "")


def xmlcmp_strings(str1, str2):
    '''Compares two xml string.'''
    doc1 = parseString(str1)
    doc2 = parseString(str2)
    return xmlequals(doc1.documentElement, doc2.documentElement, "")
