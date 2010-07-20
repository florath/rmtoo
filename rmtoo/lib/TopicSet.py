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

from rmtoo.lib.Topic import Topic
from rmtoo.lib.RMTException import RMTException

class TopicSet:
    
    # The 'tparam' must be a list:
    #  tparam[0]: topic directory
    #  tparam[1]: Initial / Master topic
    def __init__(self, name, tparam):
        assert(len(tparam)==2)
        self.name = name
        self.topic_dir = tparam[0]
        self.master_topic = tparam[1]
        # Was the cmad() method already called?
        self.cmad_already_called = False
        # This holds a map from id->object
        self.master_map = {}
        self.read_topics(self.topic_dir, self.master_topic)

    # Create Makefile Dependencies
    # This must not be called more than once
    def cmad(self, reqscont, ofile):
        if self.cmad_already_called:
            return
        self.cmad_already_called = True
        tsort = topological_sort(self.topic)
        # XXXX
        for t in tsort:
            putptu.sss.sss.t

    def read_topics(self, tdir, initial_topic):
        self.topic = Topic(tdir, initial_topic, self.master_map)

    # Resolve the 'Topic' tag of the requirement to the correct
    # topic. 
    def depict(self, reqset):
        for req in reqset.nodes:
            if "Topic" in req.tags \
                    and req.tags["Topic"]!=None:
                # A referenced topic must exists!
                ref_topic = req.tags["Topic"]
                if not ref_topic in self.master_map:
                    raise RMTException(36, "Topic '%s' referenced "
                                       "by '%s' - but topic does not exists"
                                       % (ref_topic, req.id))
                self.master_map[ref_topic].add_req(req)

