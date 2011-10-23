#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# Topic
#  This holds one topic - and all subtopics of this topic
#
# (c) 2010-2011 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.storagebackend.txtfile.TxtRecord import TxtRecord
from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.RMTException import RMTException
import os
from rmtoo.lib.storagebackend.txtfile.TxtIOConfig import TxtIOConfig

# Each topic has a level - which indicates the identation of the text
# element. 
# Each topic does link to it's super-topic.  This is the way to detect
# cycles. 
# This needs to be a digraph node, to handle dependencies within the
# topics - e.g. handling of makefile dependencies.

class Topic(Digraph.Node):

    def __init__(self, tdir, tname, dg, txtioconfig, cfg, tlevel=0,
                 tsuper=None):
        Digraph.Node.__init__(self, tname)
        self.dir = tdir
        # Master map is needed for deciping requirements into the
        # appropriate topic.
        self.digraph = dg
        self.txtioconfig = txtioconfig
        self.cfg = cfg
        # Identation level of this topic
        self.level = tlevel
        self.super = tsuper
        # This is a list of requirements which contain to this topic.
        self.reqs = []
        # The name of the Topic is mandatory (and also position
        # independent)
        # Note: there is also a .name field inherited from the
        # Digraph.Node (which hold in this case the topic's id).
        self.topic_name = None

        # This must only be done if there is a directory given
        if self.dir != None:
            self.read()
            self.extract_name()
        else:
            # In this case the tag list is (initally) empty
            self.t = []

    # Extract the name from the list (it's mandatory!)
    def extract_name(self):
        for nt in self.t:
            if nt.get_tag() == "Name":
                self.topic_name = nt.get_content()
                del(nt)
                return
        raise RMTException(62, "Mandatory tag 'Name' not given in topic",
                           self.name)

    # Create Makefile Dependencies
    def cmad(self, reqscont, ofile, tname):
        for req in self.reqs:
            # Add all the included requirements
            ofile.write(" %s.req" %
                         os.path.join(reqscont.config.reqs_spec["directory"],
                                      req.name))
        # Add all the subtopics
        for n in self.outgoing:
            ofile.write(" ${TOPIC_%s_%s_DEPS}" % (tname, n.name))

    # Read in a specific topic
    def read(self):
        self.digraph.add_node(self)
        fd = file(os.path.join(self.dir, self.name + ".tic"))
        self.t = TxtRecord.from_fd(fd, self.name, self.txtioconfig)
        for tag in self.t:
            # If the topic has subtopics, read them also in.
            if tag.get_tag() == "SubTopic":
                ntopic = Topic(self.dir, tag.get_content(), self.digraph,
                               self.txtioconfig, self.cfg, self.level + 1,
                               self)
                #self.outgoing.append(ntopic)
                Digraph.create_edge(self, ntopic)
                #self.outgoing.append(ntopic)
        fd.close()

    def add_req(self, req):
        self.reqs.append(req)

    # Returns the name of the game
    def get_name(self):
        return self.topic_name

