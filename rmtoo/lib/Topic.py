#
# Topic
#
#  This holds one topic - and all subtopics of this topic
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.Parser import Parser
from rmtoo.lib.digraph.Digraph import Digraph
import os

# Each topic has a level - which indicates the identation of the text
# element. 
# Each topic does link to it's super-topic.  This is the way to detect
# cycles. 
# This needs to be a digraph node, to handle dependencies within the
# topics - e.g. handling of makefile dependencies.

class Topic(Digraph.Node):

    def __init__(self, tdir, tname, dg, tlevel=0, 
                 tsuper=None):
        Digraph.Node.__init__(self, tname)
        self.dir = tdir
        # Master map is needed for deciping requirements into the
        # appropriate topic.
        self.digraph = dg
        # Identiation level of this topic
        self.level = tlevel
        self.super = tsuper
        # This is a list of requirements which contain to this topic.
        self.reqs = []

        self.read()

    # Create Makefile Dependencies
    def cmad(self, reqscont, ofile, tname):
        for req in self.reqs:
            # Add all the included requirements
            ofile.write(" %s.req" % 
                         os.path.join(reqscont.opts.directory, req.name))
        # Add all the subtopics
        for n in self.outgoing:
            ofile.write(" ${TOPIC_%s_%s_DEPS}" % (tname, n.name))

    # Read in a specific topic
    def read(self):
        self.digraph.add_node(self)
        fd = file(os.path.join(self.dir, self.name + ".tic"))
        self.t = Parser.read_as_list(self.name, fd)
        for tag in self.t:
            # If the topic has subtopics, read them also in.
            if tag[0]=="SubTopic":
                ntopic = Topic(self.dir, tag[1], self.digraph,
                               self.level+1, self)
                #self.outgoing.append(ntopic)
                Digraph.create_edge(self, ntopic)
                #self.outgoing.append(ntopic)
        fd.close()

    def add_req(self, req):
        self.reqs.append(req)

    # Returns the name of the game
    def get_name(self):
        for nt in self.t:
            if nt[0] == "Name":
                return nt[1]
        return None
