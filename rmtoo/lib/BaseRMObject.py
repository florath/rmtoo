'''
 rmtoo
   Free and Open Source Requirements Management Tool

  This is the definition of the Base rmtoo Management Object
  which can be used as a base object for many different text base
  major management objects like 'Requirement' or 'Constraint'.
  (Maybe this might also be used for the 'Topic'.)

 (c) 2011-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from rmtoo.lib.Encoding import Encoding
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.storagebackend.txtfile.TxtRecord import TxtRecord
from rmtoo.lib.storagebackend.txtfile.TxtIOConfig import TxtIOConfig
from rmtoo.lib.UsableFlag import UsableFlag
from rmtoo.lib.logging import tracer, logger
from rmtoo.lib.logging.LogFormatter import LogFormatter


# pylint: disable=too-many-instance-attributes
class BaseRMObject(UsableFlag):
    """Base of a Requirements Management Object"""

    # pylint: disable=too-many-arguments
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
        Encoding.check_unicode(rid)
        self._id = rid
        self.mods = mods
        self.config = config
        Encoding.check_unicode(type_str)
        self.type_str = type_str
        self._file_path = file_path
        self.record = None
        self.brmo = None

        # The analytic modules store the results in this map:
        self.analytics = {}
        if content is not None:
            self.__input(content)

    def get_id(self):
        """Returns the ID (name) of the object"""
        return self._id

    def get_value(self, key):
        """Returns the value of the key"""
        return self.values[key]

    def get_value_default(self, key, default_value=None):
        """Returns the value of the key - if not available return default"""
        if key not in self.values:
            return default_value
        return self.values[key]

    def get_file_path(self):
        """Return the file path of the object"""
        return self._file_path

    def is_value_available(self, key):
        """Check if the key is available"""
        return key in self.values

    def is_val_av_and_not_null(self, key):
        """Check if the key is not available and is not None"""
        return key in self.values \
            and self.get_value(key) is not None

    def set_value(self, key, value):
        """Sets the key to value"""
        self.values[key] = value

    def __input(self, content):
        '''Read it in from the file (Syntactic input).'''
        txtio = TxtIOConfig(self.config, self.type_str)
        Encoding.check_unicode(content)
        self.record = TxtRecord.from_string(content, self._id, txtio)

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

    def handle_modules_tag(self, reqs):
        """Process all the modules"""
        if self.mods is None:
            return

        for modkey, module in self.mods.get_tagtype(self.tbhtags).items():
            try:
                tracer.debug("handle modules tag modkey [%s] tagtype [%s]",
                             modkey, self.tbhtags)
                if self.tbhtags not in module.get_type_set():
                    logger.error(LogFormatter.format(
                        90, u"Wrong module type [%s] not in [%s]" %
                        (self.tbhtags, list(module.get_type_set()))))
                    continue
                key, value = module.rewrite(self._id, reqs)
                # Check if there is already a key with the current key
                # in the map.
                if key in self.values:
                    logger.error(LogFormatter.format(
                        54, u"tag [%s] already defined" %
                        (key), self._id))
                    self._set_not_usable()
                    # Also continue to get possible further error
                    # messages.
                self.values[key] = value
            except RMTException as rmte:
                # Some semantic error occurred: do not interpret key or
                # value.
                logger.error(LogFormatter.rmte(rmte))
                logger.error(LogFormatter.format(
                    41, "semantic error occurred in "
                    "module [%s]" % modkey, self._id))
                self._set_not_usable()
                # Continue (do not return immediately) to get also
                # possible other errors.

        tracer.debug("handled modules tags finished")
