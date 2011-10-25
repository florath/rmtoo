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
   
 (c) 2011 by flonatel GmhH & Co. KG

 For licensing details see COPYING
'''

import copy
from xml.dom.minidom import parse, parseString

def xmlequals(a, b, xpath, trace_equals=False):

    # Check for the type
    if a.nodeType != b.nodeType:
        return False, "Node types differ [%s] != [%s] at [%s]" % \
            (a.nodeType, b.nodeType, xpath)

    # Check for Text content
    if a.nodeType == a.TEXT_NODE or a.nodeType == a.CDATA_SECTION_NODE:
        if a.data != b.data:
            return False, "Text Node data differs [%s] != [%s] at [%s]" % \
                (a.data, b.data, xpath)
        else:
            return True, None

    # Check for the name
    if a.tagName != b.tagName:
        return False, "Tag names differ [%s] != [%s] at [%s]" % \
            (a.tagName, b.tagName, xpath)

    # Check for the attibutes
    a_attr_sorted = sorted(a.attributes.items())
    b_attr_sorted = sorted(b.attributes.items())
    if a_attr_sorted != b_attr_sorted:
        return False, "Attributes for tag [%s] " \
            "differ: [%s] != [%s] at [%s]" % \
            (a.tagName, a_attr_sorted, b_attr_sorted, xpath)

    if len(a.childNodes) != len(b.childNodes):
        return False, "Number of child nodes differs " \
            "[%s] != [%s] at [%s]" % \
            (len(a.childNodes), len(b.childNodes), xpath)

    # Create a shallow copy of b's children (and remove nodes which
    # are seen as equal)
    bcn = copy.copy(b.childNodes)

    # Iterate through the child nodes of 'a' ...
    for ac in a.childNodes:
        if trace_equals:
            print("xmlcmp trace: comparing child node [%s]" % ac)
        # ... check if there is the same one in 'b'
        found_ac = False
        for bc in bcn:
            r, s = xmlequals(ac, bc, xpath + "/" + a.tagName)
            if r:
                # ac and bc are equal: remove bc from bcn and skip to
                # the next ac
                bcn.remove(bc)
                found_ac = True
                if trace_equals:
                    print("[%s] xmlcmp trace: found equal subtrees [%s]" \
                          % (xpath, ac))
                    print("[%s] xmlcmp trace: remaining elements [%s]" \
                          % (xpath, bcn))
                break
        if not found_ac:
            return False, "Child node [%s] not found at [%s] - " \
                "last error was [%s]" % (ac, xpath, s)

    assert(len(bcn) == 0)

    return True, None

def xmlcmp_files(f1, f2, trace_equals=False):
    d1 = parse(f1)
    d2 = parse(f2)
    return xmlequals(d1.documentElement, d2.documentElement, "", trace_equals)

def xmlcmp_strings(s1, s2, trace_equals=False):
    d1 = parseString(s1)
    d2 = parseString(s2)
    return xmlequals(d1.documentElement, d2.documentElement, "", trace_equals)

