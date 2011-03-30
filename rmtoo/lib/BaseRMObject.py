#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# This is the definition of the Base rmtoo Management Object
# which can be used as a base object for many different text base 
# major management objects like 'Requirement' or 'Constraint'.
# (Maybe this might also be used for the 'Topic'.)
#
# (c) 2011 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.storagebackend.txtfile.TxtRecord import TxtRecord

class BaseRMObject:

    # Error Status of Requirement
    # (i.e. is the requirment usable?)
    er_fine = 0
    er_error = 1

    def internal_init(self, tbhtags, rid, mls, mods, opts, config, type_str):
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
        self.mls = mls
        self.mods = mods
        self.opts = opts
        self.config = config
        self.type_str = type_str

        # The analytic modules store the results in this map:
        self.analytics = {}

        self.state = self.er_fine

    def __init__(self, tbhtags, fd, rid, mls, mods, opts, config,
                 type_str):
        self.internal_init(tbhtags, rid, mls, mods, opts, config, type_str)
        if fd!=None:
            self.input(fd)
    
    def ok(self):
        return self.state==self.er_fine

    def get_id(self):
        return self.id

    def get_value(self, key):
        return self.values[key]

    def is_value_available(self, key):
        return key in self.values

    def is_val_av_and_not_null(self, key):
        return key in self.values \
            and self.get_value(key)!=None

    def set_value(self, key, value):
        self.values[key] = value

    def input(self, fd):
        # Read it in from the file (Syntactic input)
        self.record = TxtRecord.from_fd(fd, self.id,
                                 self.config.txtio[self.type_str])
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
        for modkey, module in self.mods.tagtypes[self.tbhtags].items():
            try:
                #print("handle_modules_tag [%s] [%s] [%s] [%s]" 
                #      % (modkey, module, self.tbhtags, module.type()))
                if self.tbhtags not in module.type():
                    self.mls.error(90, "Wrong module type [%s] not in [%s]" %
                                   (self.tbhtags, module.type()))
                    continue
                key, value = module.rewrite(self.id, reqs)
                # Check if there is already a key with the current key
                # in the map.
                if key in self.values:
                    self.mls.error(54, "tag '%s' already defined" %
                          (key), self.id)
                    self.state = self.er_error
                    # Also continue to get possible further error
                    # messages.
                self.values[key] = value
            except RMTException, rmte:
                # Some sematic error occured: do not interpret key or
                # value.
                self.mls.error_from_rmte(rmte)
                self.mls.error(41, "semantic error occured in "
                               "module '%s'" % modkey, self.id)
                #print("+++ root cause is: '%s'" % rmte)
                self.state = self.er_error
                # Continue (do not return immeditely) to get also
                # possible other errors.
