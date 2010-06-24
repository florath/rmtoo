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
    def __init__(self, tparam):
        assert(len(tparam)==2)
        # This holds a map from id->object
        self.master_map = {}
        self.read_topics(tparam[0], tparam[1])

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

