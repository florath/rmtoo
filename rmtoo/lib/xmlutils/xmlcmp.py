"""Library for comparing XML documents.

It has been replaced by the generic `xmldiff` library.

"""
from xmldiff import main


def xmlcmp_files(file1, file2):
    '''Compares two xml files.'''
    xdiff = main.diff_files(file1, file2)
    if xdiff == []:
        return True, None
    return False, str(xdiff)


def xmlcmp_strings(str1, str2):
    '''Compares two xml string.'''
    xdiff = main.diff_texts(str1, str2)
    if xdiff == []:
        return True, None
    return False, "Strings not equal"
