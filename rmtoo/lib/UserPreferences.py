'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Stores user preferences in the ~/.rmtoo directory. 
   
 (c) 2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import os
import tempfile
import json
import shutil

from rmtoo.lib.logging import tracer
from rmtoo.lib.GenNonEmptyDict import GenNonEmptyDict

class FileStorage(object):
    '''Holds all the values which go in one file.'''
        
    def __init__(self, rel_filename, base_dir):
        '''Initializaes the FileStorage with the relative filename.'''
        self.__rel_filename = rel_filename
        self.__base_dir = base_dir
        self.__filename = os.path.join(self.__base_dir, self.__rel_filename)
        self.__dict = {}
        
    def read(self):
        '''Reads in the file content from the filesystem.'''
        with open(self.__filename, 'r') as f:
            s = f.read()
        self.__dict = json.loads(s)
       
    def set_value(self, key, value):
        '''Directly access the underlaying dict.'''
        self.__dict[key] = value
        
    def get_value(self, key):
        '''Directly access the underlaying dict.'''
        return self.__dict[key]
    
    def __write_tmp(self):
        '''Write the data to a temporaty file and return the filename.'''
        tracer.debug("called")
        try:
            tracer.debug("Create temp file")
            tfile = tempfile.NamedTemporaryFile(dir=self.__base_dir, 
                                                delete=False)
            tracer.debug("Write to temp file [%s]." % tfile.name)
            tfile.write(json.dumps(self.__dict, sort_keys=True, indent=2))
            tracer.debug("Wrote to temp file")
        except Exception as ex:
            tracer.warn("Exception during writing temp data [%s]" % ex)
        finally:
            tracer.debug("Close temp file")
            tfile.close()
        tracer.debug("finished")
        return tfile.name
    
    def __move_tmp(self, tmpfilename):
        '''Moves the tmpfilename to the original file - as atomar
           as possible.'''
        tracer.debug("Moving [%s] -> [%s]" % (tmpfilename, self.__filename))
        shutil.move(tmpfilename, self.__filename)
        
    def __remove_tmp(self, tmpfilename):
        '''Remove the tmpfilename - if exists.'''
        try:
            os.remove(tmpfilename)
        except OSError as ose:
            if ose.errno == 2:
                # In this case the file did not exists - so it is removed
                return
            raise
    
    def write(self):
        '''Writes the current content to the file.'''
        tracer.debug("Write preferences data to file")
        try:
            tmpfilename = self.__write_tmp()
            tracer.debug("Wrote data to [%s]" % tmpfilename)
            self.__move_tmp(tmpfilename)
        except Exception as ex:
            tracer.warn("Exception during writing data [%s]: [%s]" 
                        % (self.__rel_filename, ex))            
        finally:
            self.__remove_tmp(tmpfilename)
        tracer.debug("Finished writing properties to file.")
            
class UserPreferences(object):
    '''Global User Preferences handling.
       There are some global user preferences which must be stored
       system wide.  This class with handle these things.'''
    
    __default_rmtoo_home_dir = "~/.rmtoo"
    '''This is the default location of the rmtoo home dir.'''
    
    @staticmethod
    def __eval_rmtoo_home_dir(rmtoo_home_dir):
        '''Evaluates the rmtoo home dir.
           If given (and nor None), the provided directory is used.
           If not given, the default is used.'''
        if rmtoo_home_dir == None:
            return os.path.expanduser("~/.rmtoo")
        else:
            return rmtoo_home_dir

    def __init__(self, rmtoo_home_dir=None):
        '''Constructs a User Preferences object which can hold
           and store configuration values.'''
        
        def __create_new_FileStorage(rel_filename):
            return FileStorage(rel_filename, self.__rmtoo_home_dir)
        
        self.__rmtoo_home_dir = self.__eval_rmtoo_home_dir(rmtoo_home_dir)
        self.__file_storage = GenNonEmptyDict(__create_new_FileStorage)
        
    def read(self):
        '''Reads in all the files in the home directory and puts them
           into internal memory.'''
        for f in os.listdir(self.__rmtoo_home_dir):
            fs = FileStorage(f, self.__rmtoo_home_dir)
            fs.read()
            self.__file_storage.insert(f, fs)
        
    def get_rmtoo_home_dir(self):
        '''Returns the used home directory.'''
        return self.__rmtoo_home_dir
    
    def set_value(self, filename, propname, value):
        '''Sets the property with the name 'propname' to the file
           'filename' to the given value.'''
        self.__file_storage[filename].set_value(propname, value)
        
    def get_value(self, filename, propname):
        '''Gets the property from the file.'''
        return self.__file_storage[filename].get_value(propname)
    
    def write(self):
        '''Write the whole set of files to the directory.'''
        for _, f in self.__file_storage.iteritems():
            f.write()