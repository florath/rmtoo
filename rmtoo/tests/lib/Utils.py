'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
 Test utilities.
 
 (c) 2011 by flonatel

 For licensing details see COPYING
'''

import tempfile
import shutil

def create_tmp_dir():
    '''Create a temporary directory.'''
    return tempfile.mkdtemp(prefix="rmtoo-tst-ris-")

def delete_tmp_dir(dirname):
    '''Deletes a temporary directory.'''
    shutil.rmtree(dirname)

