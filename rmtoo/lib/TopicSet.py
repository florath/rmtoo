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
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RequirementSet import RequirementSet
from rmtoo.lib.digraph.TopologicalSort import topological_sort
from rmtoo.lib.digraph.ConnectedComponents import connected_components
from rmtoo.lib.digraph.Helper import node_list_to_node_name_list

import traceback

# The TopicSet does contain the RequirementSet which is limited to the
# topic and all subtopics.

class TopicSet(Digraph):
    
    # The 'tparam' must be a list:
    #  tparam[0]: topic directory
    #  tparam[1]: Initial / Master topic
    def __init__(self, all_reqs, name, tparam):
        Digraph.__init__(self)
        assert(len(tparam)==2)
        self.name = name
        self.topic_dir = tparam[0]
        self.master_topic = tparam[1]
        self.read_topics(self.topic_dir, self.master_topic)

        if all_reqs!=None:
            self.reqset = self.reqs_limit(all_reqs)

    def create_makefile_name(self, topicn):
        return "TOPIC_%s_%s_DEPS" % (self.name, topicn)

    def get_master(self):
        return self.get_named_node(self.master_topic)

    # Create Makefile Dependencies
    def cmad(self, reqscont, ofile):
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

    # Read in all the topics to decide whether the topic exists or not
    # - to differentiate between the non-existance of a topic vs a
    # topic which is not a children of the currently chosen topic.
    def read_all_topic_names(self, tdir):
        self.all_topic_names = set()
        for f in os.listdir(tdir):
            if not f.endswith(".tic"):
                print("+++ WARNING: Topic '%s' ends not in .tic")
                continue
            self.all_topic_names.add(f[:-4])

    def read_topics(self, tdir, initial_topic):
        Topic(tdir, initial_topic, self)
        self.read_all_topic_names(tdir)

    # Resolve the 'Topic' tag of the requirement to the correct
    # topic. 
    def internal_depict(self, reqset):
        # The named_node dictionary must exists before it is possible
        # to access it. 
        self.build_named_nodes()
        for req in reqset.nodes:
            if "Topic" in req.tags \
                    and req.tags["Topic"]!=None:
                # A referenced topic must exists!
                ref_topic = req.tags["Topic"]
                assert(ref_topic in self.named_nodes)
                self.named_nodes[ref_topic].add_req(req)

    def reqs_limit(self, reqset):
        # Get a list of all topic names.
        self.build_named_nodes()
        topic_name_list = self.named_nodes.keys()

        # Create the new RequirementSet
        r = RequirementSet(reqset.mods, reqset.opts, reqset.config)

        # Copy over the requirements themselves:
        # Here the incoming and outgoing requirements are the still the
        # old ones.
        # During the loop, build up the mapping from old to new.
        def copy_only_reqs(lreqset, ltopic_name_list, lall_topic_names):
            old2new = {}
            for _, req in lreqset.reqs.iteritems():
                topic = req.tags["Topic"]
                # If the referenced topic does not exists at all, emit
                # an error.
                if topic not in lall_topic_names:
                    lreqset.error(58, "Topic does not exist. Typo "
                                  "in topic name?", req.id)
                    lreqset.not_usable()
                    continue
                if not req.tags["Topic"] in ltopic_name_list:
                    print("+++ Debug:%s: Skipping requirement because "
                          "not in topic" % req.id)
                    continue
                req_copy = req.internal_copy_phase1(ltopic_name_list)
                r.add_req(req_copy)
                old2new[req] = req_copy
            return old2new

        old2new = copy_only_reqs(reqset, topic_name_list,
                                 self.all_topic_names)

        # Replace all the incoming and outgoing from old to new:
        for _, req in r.reqs.iteritems():
            req.internal_copy_phase2(old2new)

        # Now there is a fully limited version of the requirement set
        # to the topic set.  Assign the requirements to the given
        # topics.
        self.internal_depict(r)

        # There is the need for some tests (e.g. is the remaining graph
        # connected) - but the handle_modules_reqdeps() does much more -
        # which is not needed at this point.
        # Therefore the algorithms is called directly from here.
        components = connected_components(r)
        if components.len()>1:
            print("+++ Info: The resulting graph is not connected.")
            print("+++       Found components: '%s'" % components.as_string())

        # Run through all the requirements and check, if there are
        # requirements which has no incoming.
        for _, req in r.reqs.iteritems():
            if len(req.outgoing)==0 and \
                    req.tags["Type"]!=Requirement.rt_master_requirement:
                print("+++ Info:%s: no outgoing edges" % req.name)

        return r
