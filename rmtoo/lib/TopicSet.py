#
# rmtoo
#   Free and Open Source Requirements Management Tool
#
# TopicSet
#
#  Collection of all topics.
#  Note that the TopicSet is a tree where the leaves are 
#  orders - i.e. it is not possible to put them into a set_value.
#
# (c) 2010-2011 by flonatel
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
from rmtoo.lib.MemLogStore import MemLogStore
from rmtoo.lib.TopicSetOutputHandler import TopicSetOutputHandler
from rmtoo.lib.configuration.Cfg import Cfg

import traceback
from rmtoo.lib.storagebackend.txtfile.TxtIOConfig import TxtIOConfig

# The TopicSet does contain the RequirementSet which is limited to the
# topic and all subtopics.

class TopicSet(Digraph, MemLogStore):

    # The 'tparam' must be a list:
    #  tparam[0]: topic directory
    #  tparam[1]: Initial / Master topic
    def __init__(self, all_reqs, config, name, config_prefix_str):
        Digraph.__init__(self)
        MemLogStore.__init__(self)
        self.name = name
        self.topic_dir = config.get_value(config_prefix_str + '.directory')
        self.master_topic = config.get_value(config_prefix_str + '.name')
        self.cfg = config
        self.read_topics(self.topic_dir, self.master_topic)

        if all_reqs != None:
            self.reqset = self.reqs_limit(all_reqs)

        self.output_handlers = []
        self.init_output_handler()

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
        # NEW: Also all the dependend things must be called.
        for output_handler in self.output_handlers:
            output_handler.cmad(reqscont, ofile)

    # Read in all the topics to decide whether the topic exists or not
    # - to differentiate between the non-existance of a topic vs a
    # topic which is not a children of the currently chosen topic.
    def read_all_topic_names(self, tdir):
        self.all_topic_names = set()
        for f in os.listdir(tdir):
            # Ignore Emacs Backup Files
            if f.endswith(".tic~"):
                continue
            if not f.endswith(".tic"):
                self.warning(64, "Topic '%s' ends not in .tic - ignoring" % f)
                continue
            self.all_topic_names.add(f[:-4])

    def read_topics(self, tdir, initial_topic):
        txtioconfig = TxtIOConfig(self.cfg, "topics")
        Topic(tdir, initial_topic, self, txtioconfig, self.cfg)
        self.read_all_topic_names(tdir)

    # Resolve the 'Topic' tag of the requirement to the correct
    # topic. 
    def internal_depict(self, reqset):
        # The named_node dictionary must exists before it is possible
        # to access it. 
        self.build_named_nodes()
        for req in reqset.nodes:
            if req.is_value_available("Topic") \
                    and req.get_value("Topic") != None:
                # A referenced topic must exists!
                ref_topic = req.get_value("Topic")
                assert(ref_topic in self.named_nodes)
                self.named_nodes[ref_topic].add_req(req)

    def reqs_limit(self, reqset):
        # Get a list of all topic names.
        self.build_named_nodes()
        topic_name_list = self.named_nodes.keys()

        # Create the new RequirementSet
        r = RequirementSet(reqset.mods, reqset.config)

        # Copy over the requirements themselves:
        # Here the incoming and outgoing requirements are the still the
        # old ones.
        # During the loop, build up the mapping from old to new.
        def copy_only_reqs(lreqset, ltopic_name_list, lall_topic_names):
            old2new = {}
            for _, req in lreqset.reqs.iteritems():
                topic = req.get_value("Topic")
                # If the referenced topic does not exists at all, emit
                # an error.
                if topic not in lall_topic_names:
                    lreqset.error(58, "Topic does not exist. Typo "
                                  "in topic name?", req.id)
                    lreqset.not_usable()
                    continue
                if not req.get_value("Topic") in ltopic_name_list:
                    lreqset.debug(65, "Skipping requirement because "
                          "not in topic", req.id)
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

        # Now there is a fully limited version of the requirement set_value
        # to the topic set_value.  Assign the requirements to the given
        # topics.
        self.internal_depict(r)

        # There is the need for some tests (e.g. is the remaining graph
        # connected) - but the handle_modules_reqdeps() does much more -
        # which is not needed at this point.
        # Therefore the algorithms is called directly from here.
        components = connected_components(r)
        if components.len() > 1:
            reqset.info(67, "The resulting graph is not connected. "
                        "Found components: [%s]" % components.as_string())

        # Run through all the requirements and check, if there are
        # requirements which has no incoming.
        for _, req in r.reqs.iteritems():
            if len(req.outgoing) == 0 and \
                    req.get_value("Type") != Requirement.rt_master_requirement:
                print("+++ Info:%s: no outgoing edges" % req.name)

        return r

    def init_output_handler(self):
        # It is possible for one topic to have different output methods.
        # Even each output method can be called multiple times.
        # The data structure used is:
        # { map of different output methods: 
        #   [ list of different parameter sets for the different parameter
        #     sets ] }
        ohconfig = self.cfg.get_value(['topics', self.name, 'output'])
        print("CONFIG [%s]" % self.cfg.config)
        for outmeth, params in ohconfig.get_dict().iteritems():
            print("BEFORE OMETH [%s] [%s]" % (outmeth, params))
            for param in params:
                self.output_handlers.append(
                    TopicSetOutputHandler(self.cfg, outmeth, param, self))
            print("OMETH [%s] [%s]" % (outmeth, params))

    def output(self, rc):
        for output_handler in self.output_handlers:
            output_handler.output(rc)
