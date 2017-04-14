'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  This is the definition of the Base rmtoo Management Object
  which can be used as a base object for many different text base 
  major management objects like 'Requirement' or 'Constraint'.
  (Maybe this might also be used for the 'Topic'.) 
   
 (c) 2011-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.storagebackend.txtfile.TxtRecord import TxtRecord
from rmtoo.lib.storagebackend.txtfile.TxtIOConfig import TxtIOConfig
from rmtoo.lib.UsableFlag import UsableFlag
from rmtoo.lib.logging import tracer, logger
from rmtoo.lib.logging.LogFormatter import LogFormatter

class BaseRMObject(UsableFlag):

    def __init__(self, tbhtags, content, rid, mods, config, type_str,
                 file_path):
        UsableFlag.__init__(self)
        # This is the name of the tags which will be handled by the
        # module input. 
        self.tbhtags = tbhtags
        # This are the original tags - when there is no
        # need to convert them to specific values, they are left
        # here.
        self.otags = {}
        # This is the list of converted values.
        self.values = {}
        self.id = rid
        self.mods = mods
        self.config = config
        self.type_str = type_str
        self._file_path = file_path
        self.record = None
        self.brmo = None

        if content != None:
            self.__input(content)

    def get_id(self):
        return self.id

    def get_value(self, key):
        return self.values[key]

    def remove_value(self, key):
        if key in self.values:
            del(self.values[key])

    def get_value_default(self, key, default_value = None):
        if key not in self.values:
            return default_value
        return self.values[key]

    def get_file_path(self):
        return self._file_path

    def is_value_available(self, key):
        return key in self.values

    def is_val_av_and_not_null(self, key):
        return key in self.values \
            and self.get_value(key) != None

    def set_value(self, key, value):
        self.values[key] = value

    def __input(self, content):
        '''Read it in from the file (Syntactic input).'''
        txtio = TxtIOConfig(self.config, self.type_str)

        self.record = TxtRecord.from_string(content, self.id, txtio)
        brmo = self.record.get_dict()
        # This 'brmo' is always valid - if there is a problem, an exception 
        # is raised.

        # Handle all the modules (Semantic input)
        self.handle_modules_tag(brmo)

        # Do not check for remaining tags here. There must be some
        # left over: all those that work on the whole requirement set
        # (e.g. 'Solved by').

        # If everything's fine, store the rest of the req for later
        # inspection.
        self.brmo = brmo
        
    def write_fd(self, fd):
        self.record.write_fd(fd)
        
    def get_record(self):
        '''Returns the record(s).'''
        return self.record

    def handle_modules_tag(self, reqs):
        if self.mods == None:
            return

        for modkey, module in self.mods.get_tagtype(self.tbhtags).items():
            try:
                tracer.debug("handle modules tag modkey [%s] tagtype [%s]"
                      % (modkey, self.tbhtags))
                if self.tbhtags not in module.get_type_set():
                    logger.error(LogFormatter.format(
                                 90, "Wrong module type [%s] not in [%s]" %
                                 (self.tbhtags, module.get_type_set())))
                    continue
                key, value = module.rewrite(self.id, reqs)
                # Check if there is already a key with the current key
                # in the map.
                if key in self.values:
                    logger.error(LogFormatter.format(
                          54, "tag [%s] already defined" %
                          (key), self.id))
                    self._set_not_usable()
                    # Also continue to get possible further error
                    # messages.
                self.values[key] = value
            except RMTException, rmte:
                # Some semantic error occurred: do not interpret key or
                # value.
                logger.error(LogFormatter.rmte(rmte))
                logger.error(LogFormatter.format(
                               41, "semantic error occurred in "
                               "module [%s]" % modkey, self.id))
                self._set_not_usable()
                # Continue (do not return immediately) to get also
                # possible other errors.

        tracer.debug("handled modules tags finished")
