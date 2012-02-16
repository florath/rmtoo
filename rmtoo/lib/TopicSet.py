'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Collection of topics.
  Note that the TopicSet is a tree where the leaves are 
  orders - i.e. it is not possible to put them into a set_value.
   
 (c) 2010-2011 by flonatel GmhH & Co. KG

 For licensing details see COPYING
'''

import os

from rmtoo.lib.Topic import Topic
from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RequirementSet import RequirementSet
from rmtoo.lib.digraph.TopologicalSort import topological_sort
from rmtoo.lib.digraph.ConnectedComponents import connected_components
from rmtoo.lib.logging.MemLogStore import MemLogStore
from rmtoo.lib.TopicSetOutputHandler import TopicSetOutputHandler
from rmtoo.lib.storagebackend.txtfile.TxtIOConfig import TxtIOConfig
from rmtoo.lib.logging.EventLogging import tracer
from rmtoo.lib.UsableFlag import UsableFlag

class TopicSet(Digraph, MemLogStore, UsableFlag):
    '''A Collection of Topics.
       With other words: a hierarchy of requirements.'''

    def __init__(self, config, input_handler, commit, object_cache, input_mods):
        '''Read in all the dependent topics and the requirements.'''
        tracer.info("Called.")
        Digraph.__init__(self)
        MemLogStore.__init__(self)
        UsableFlag.__init__(self)
        self._config = config
        self.__input_handler = input_handler
        self.__commit = commit
        self.__object_cache = object_cache
        self.__input_mods = input_mods

        # First: read in all the requirements.
        self.__complete_requirement_set = None
        self.__read_requirement_set()
        # Second: read in all the topics.
        # Stored here is the initial node of the topic digraph.
        self.__topic = self.__read_topics()
        # Third: restrict requirements to those which are 
        #    needed in the topic.
        self.__requirement_set = self.__restrict_requirements_set()
        tracer.debug("Finished.")

    def __read_requirement_set(self):
        '''Reads in the requirement set.
           First checks if this is already available in the object cache.'''
        req_set_vcs_id = \
            self.__input_handler.get_vcs_id_with_type(
                            self.__commit, "requirements")
        req_set = self.__object_cache.get("RequirementSet", req_set_vcs_id)
        if req_set == None:
            req_set = RequirementSet(self._config)
            req_set.read_requirements(self.__input_handler, self.__commit,
                                      self.__input_mods, self.__object_cache)
            self.__object_cache.add(req_set_vcs_id,
                                    "RequirementSet", req_set)
            self._adapt_usablility(req_set)
        self.__complete_requirement_set = req_set

    def __read_topics(self):
        '''Read in the topics for this topic set.
           Also topics are handled by the object cache.
           Note that the algorithm has a basic difference to the one
           used to read in the requirements.
           This one known the base topic and therefore all dependent 
           sub-topics - the algorithm reading in the requirements
           just takes all the available files.'''
        tracer.debug("Called.")

        topic_base = self.__input_handler.get_topic_base_file_info(self.__commit)
        tracer.debug("Topic base [%s]." % topic_base)
        return Topic(self, self._config, self.__input_handler,
                     self.__commit, topic_base, self.__complete_requirement_set)

    def __restrict_requirements_set(self):
        '''Restricts all the available requirements (as stored in the 
           RequirementsSet variable) to the topics.'''
        available_topics = self.__topic.get_topic_names_flattened()
        return self.__complete_requirement_set \
            .restrict_to_topics(available_topics)

    def execute(self, executor):
        '''Execute the parts which are needed for TopicsSet.'''
        tracer.info("Calling pre.")
        executor.topics_set_pre(self)
        tracer.info("Calling sub topic.")
        self.__topic.execute(executor)
#        tracer.info("Calling sub requirement set.")
#        self.__requirement_set.execute(executor)
        tracer.info("Calling post.")
        executor.topics_set_post(self)
        tracer.info("Finished.")

    def get_requirement_set(self):
        '''Returns the requirement set for the whole topic set.'''
        return self.__requirement_set


#### EVERYTHING BENEATH THIS IS DEPRECATED!!!

    def DEPRECATED_internal_init_requirements(self):
        '''Read in all the requirements and store them
           for later use.'''

    def DEPRECATED___init__(self, config, name, config_prefix_str, req_input_dir):
        tracer.info("name [%s] config_prefix [%s] req_input_dir [%s]"
                    % (name, config_prefix_str, req_input_dir))
        Digraph.__init__(self)
        MemLogStore.__init__(self)
        # The name of the TopicSet.
        self.name = name
        # The directory where all topics are stored.
        self.topic_dir = config.get_value(config_prefix_str + '.directory')
        # The master (i.e. the initial) topic.
        self.master_topic = config.get_value(config_prefix_str + '.name')
        self.config = config
        self.internal_init_requirements()

# TODO: is this needed????
#        if all_reqs != None:
#            self.mReqset = self.reqs_limit(all_reqs)

        self.output_handlers = []
        self.init_output_handler()

    def DEPRECATED_create_makefile_name(self, topicn):
        return "TOPIC_%s_%s_DEPS" % (self.name, topicn)

    def DEPRECATED_get_master(self):
        return self.get_named_node(self.master_topic)

    # Create Makefile Dependencies
    def DEPRECATED_cmad(self, reqscont, ofile):
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
    def DEPRECATED_read_all_topic_names(self, tdir):
        self.all_topic_names = set()
        for f in os.listdir(tdir):
            # Ignore Emacs Backup Files
            if f.endswith(".tic~"):
                continue
            if not f.endswith(".tic"):
                self.warning(64, "Topic '%s' ends not in .tic - ignoring" % f)
                continue
            self.all_topic_names.add(f[:-4])

    def DEPRECATED_read_topics(self, tdir, initial_topic):
        '''Read all topics from the given directory starting
           with the initial topic.'''
        tracer.debug("called: directory [%s] initial topic [%s]"
                     % (tdir, initial_topic))
        txtioconfig = TxtIOConfig(self.config, "topics")
        Topic(tdir, initial_topic, self, txtioconfig, self.config)
        self.read_all_topic_names(tdir)

    # Resolve the 'Topic' tag of the requirement to the correct
    # topic. 
    def DEPRECATED_internal_depict(self, reqset):
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

    def DEPRECATED_reqs_limit(self, reqset):
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

    def DEPRECATED_init_output_handler(self):
        # It is possible for one topic to have different output methods.
        # Even each output method can be called multiple times.
        # The data structure used is:
        # { map of different output methods: 
        #   [ list of different parameter sets for the different parameter
        #     sets ] }
        ohconfig = self.config.get_value(['topics', self.name, 'output'])
        for outmeth, params in ohconfig.get_dict().iteritems():
            for param in params:
                self.output_handlers.append(
                    TopicSetOutputHandler(self.config, outmeth, param, self))

    def DEPRECATED_output(self, rc):
        for output_handler in self.output_handlers:
            output_handler.output(rc)
