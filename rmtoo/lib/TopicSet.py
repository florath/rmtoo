#
# TopicSet
#
#  Collection of all topics.
#  Note that the TopicSet is a tree where the leaves are 
#  orders - i.e. it is not possible to put them into a set.
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

import os

from rmtoo.lib.Topic import Topic
from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.digraph.TopologicalSort import topological_sort
from rmtoo.lib.digraph.Helper import node_list_to_node_name_list

import traceback

class TopicSet(Digraph):
    
    # The 'tparam' must be a list:
    #  tparam[0]: topic directory
    #  tparam[1]: Initial / Master topic
    def __init__(self, name, tparam):
        Digraph.__init__(self)
        assert(len(tparam)==2)
        self.name = name
        self.topic_dir = tparam[0]
        self.master_topic = tparam[1]
        # Was the cmad() method already called?
        self.cmad_already_called = False
        self.read_topics(self.topic_dir, self.master_topic)

    def create_makefile_name(self, topicn):
        return "TOPIC_%s_%s_DEPS" % (self.name, topicn)

    def get_master(self):
        return self.get_named_node(self.master_topic)

    # Create Makefile Dependencies
    def cmad(self, reqscont, ofile):
        # This must not be called more than once
        if self.cmad_already_called:
            return
        self.cmad_already_called = True

        # Because the variables must be defined before they can be
        # accessed, the topological sort is needed here.
        tsort = topological_sort(self)
        for t in tsort:
            ofile.write("%s: %s.tic" %
                        (self.create_makefile_name(t.name),
                         os.path.join(self.topic_dir, t.name)))
            # Path the dependency handling of the requirements to the
            # Topic object itself.
            t.cmad(reqscont, ofile, self.name)
            ofile.write("\n")

    def read_topics(self, tdir, initial_topic):
        Topic(tdir, initial_topic, self)

    # Resolve the 'Topic' tag of the requirement to the correct
    # topic. 
    def depict(self, reqset):
        # The named_node dictionary must exists before it is possible
        # to access it. 
        self.build_named_nodes()
        for req in reqset.nodes:
            if "Topic" in req.tags \
                    and req.tags["Topic"]!=None:
                # A referenced topic must exists!
                ref_topic = req.tags["Topic"]
                if not ref_topic in self.named_nodes:
                    raise RMTException(36, "Topic '%s' referenced "
                                       "by '%s' - but topic does not exists"
                                       % (ref_topic, req.id))
                self.named_nodes[ref_topic].add_req(req)

