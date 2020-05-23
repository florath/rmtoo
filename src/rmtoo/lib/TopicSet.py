'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Collection of topics.
  Note that the TopicSet is a tree where the leaves are
  orders - i.e. it is not possible to put them into a set_value.

 (c) 2010-2011,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from rmtoo.lib.Topic import Topic
from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.RequirementSet import RequirementSet
from rmtoo.lib.logging import tracer
from rmtoo.lib.UsableFlag import UsableFlag


# pylint: disable=too-many-instance-attributes
class TopicSet(Digraph, UsableFlag):
    '''A Collection of Topics.
       With other words: a hierarchy of requirements.'''

    # pylint: disable=too-many-arguments
    def __init__(self, config, input_handler, commit, object_cache,
                 input_mods):
        '''Read in all the dependent topics and the requirements.'''
        tracer.info("Called; commit timestamp [%s]",
                    input_handler.get_timestamp(commit))
        Digraph.__init__(self)
        UsableFlag.__init__(self)
        self._config = config
        self.__input_handler = input_handler
        self.__commit = commit
        self.__object_cache = object_cache
        self.__input_mods = input_mods

        # Because it is possible that things are failing, there is the need to
        # have some defaults here:
        self.__complete_requirement_set = None
        self.__topic = None
        self.__requirement_set = None

        # First: read in all the requirements.
        self.__read_requirement_set()
        if not self.is_usable():
            tracer.error("Errors during reading the requirements.")
            return
        # Second: read in all the topics.
        # Stored here is the initial node of the topic digraph.
        self.__topic = self.__read_topics()
        if not self.is_usable():
            tracer.error("Errors during reading the topics.")
            return
        # Third: restrict requirements to those which are
        #    needed in the topic.
        self.__requirement_set = self.__restrict_requirements_set()
        if not self.is_usable():
            tracer.error("Errors during restriction of the requirements.")
            return
        tracer.debug("Finished.")

    def __read_requirement_set(self):
        '''Reads in the requirement set.
           First checks if this is already available in the object cache.'''
        req_set_vcs_id = \
            self.__input_handler.get_vcs_id_with_type(
                self.__commit, "requirements")
        req_set = self.__object_cache.get("RequirementSet", req_set_vcs_id)
        if req_set is None:
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

        topic_base = self.__input_handler.get_topic_base_file_info(
            self.__commit)
        tracer.debug("Topic base [%s]", topic_base)
        return Topic(self, self._config, self.__input_handler,
                     self.__commit, topic_base,
                     self.__complete_requirement_set)

    def __restrict_requirements_set(self):
        '''Restricts all the available requirements (as stored in the
           RequirementsSet variable) to the topics.'''
        available_topics = self.__topic.get_topic_names_flattened()
        return self.__complete_requirement_set \
            .restrict_to_topics(available_topics)

    def get_requirement_set(self):
        '''Returns the requirement set for the whole topic set.'''
        return self.__requirement_set

    def get_master_topic(self):
        '''Return the main topic.'''
        return self.__topic

    # pylint: disable=invalid-name
    def get_complete_requirement_set_count(self):
        '''Return the number of requirements in this RequirementSet.  This
           is e.g. needed for statistics.'''
        return self.__complete_requirement_set.get_requirements_cnt()

    def execute(self, executor, func_prefix):
        '''Execute the parts which are needed for TopicsSet.'''
        if self.__topic is not None:
            self.__topic.execute(executor, func_prefix)

    @staticmethod
    def create_makefile_name(name, topicn):
        """Create the name for the Makefile"""
        return "TOPIC_%s_%s_DEPS" % (name, topicn)
