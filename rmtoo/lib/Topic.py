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
import os

# Each topic has a level - which indicates the identation of the text
# element. 
# Each topic does link to it's super-topic.  This is the way to detect
# cycles. 

class Topic:

    def __init__(self, tdir, tname, tmaster_map, tlevel=0, 
                 tsuper=None):
        self.dir = tdir
        self.id = tname
        self.master_map = tmaster_map
        self.level = tlevel
        self.super = tsuper
        # This is a list of requirements which contain to this topic.
        self.reqs = []

        self.read()

    # Read in a specific topic
    def read(self):
        self.master_map[self.id] = self
        fd = file(os.path.join(self.dir, self.id + ".tic"))
        self.t = Parser.read_as_list(self.id, fd)
        for tag in self.t:
            # If the topic has subtopics, read them also in.
            if tag[0]=="SubTopic":
                ntopic = Topic(self.dir, tag[1], self.master_map,
                               self.level+1, self)
                tag.append(ntopic)
        fd.close()

    def add_req(self, req):
        self.reqs.append(req)

    # Returns the name of the game
    def get_name(self):
        for nt in self.t:
            if nt[0] == "Name":
                return nt[1]
        return None
