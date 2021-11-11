'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Topic
   This holds one topic - and all subtopics of this topic

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals

from rmtoo.lib.Encoding import Encoding
from rmtoo.lib.storagebackend.txtfile.TxtRecord import TxtRecord
from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.logging import tracer
from rmtoo.lib.FuncCall import FuncCall


class Topic(Digraph.Node):
    '''Each topic has a level - which indicates the identation of the text
       element.
       Each topic does link to it's super-topic.  This is the way to detect
       cycles.
       This needs to be a digraph node, to handle dependencies within the
       topics - e.g. handling of makefile dependencies.'''

    # pylint: disable=too-many-arguments
    def __read(self, tname, input_handler, commit, file_info, req_set):
        '''Read in the topic and create all the tags.'''
        Encoding.check_unicode(tname)
        self.__tags = TxtRecord.from_string(
            file_info.get_content(),
            tname, input_handler.get_txt_io_config())

        for tag in self.__tags:
            # If the topic has subtopics, read them also in.
            if tag.get_tag() == "SubTopic":
                lfile_info = input_handler.get_file_info_with_type(
                    commit, "topics", tag.get_content() + ".tic")
                ntopic = Topic(self.__digraph, self._config, input_handler,
                               commit, lfile_info, req_set)
                self.__digraph.add_node(ntopic)
                Digraph.create_edge(self, ntopic)
            elif tag.get_tag() == "Name":
                if self.__topic_name is not None:
                    # There can (currently) be only one name
                    assert False
                self.__topic_name = tag.get_content()
            elif tag.get_tag() == "IncludeRequirements":
                if tag.get_content() != "full":
                    raise RMTException(113, "IncludeRequirements value not "
                                       "supported [%s]" % tag.get_content(),
                                       self.name)
                self.__requirements = req_set.restrict_to_topics(tname)
                tracer.debug("Found [%d] requirements for topic [%s]",
                             self.__requirements.get_requirements_cnt(), tname)
        # Check for the existence of the name
        if self.__topic_name is None:
            raise RMTException(62, "Mandatory tag 'Name' not given in topic",
                               self.name)

    def __init__(self, digraph, config, input_handler, commit, file_info,
                 req_set):
        tname = file_info.get_filename_sub_part()[:-4]
        # The 'name' in the digraph node is the ID
        Digraph.Node.__init__(self, tname)
        # This is the name of the topic (short description)
        self.__topic_name = None
        self.__tags = None
        self._config = config
        tracer.debug("Called: name [%s]", tname)
        self.__digraph = digraph
        self.__requirements = None
        self.__read(tname, input_handler, commit, file_info, req_set)

    def get_topic_names_flattened(self):
        '''Returns all the names of the complete topic hirarchy in one set.'''
        tracer.debug("Called: name [%s]", self.name)
        result = set()
        result.add(self.name)
        for topic in self.outgoing:
            result = result.union(topic.get_topic_names_flattened())
        return result

    def execute(self, executor, func_prefix):
        '''Execute the parts which are needed for TopicsContinuum.'''
        tracer.debug("Calling pre [%s]", self.name)
        FuncCall.pcall(executor, func_prefix + "topic_pre", self)
        tracer.debug("Calling sub [%s]", self.name)
        for tag in self.__tags:
            rtag = tag.get_tag()
            if rtag == "Name":
                FuncCall.pcall(executor, func_prefix + "topic_name",
                               tag.get_content())
                continue
            if rtag == "SubTopic":
                subtopic = self.__digraph.find(tag.get_content())
                assert subtopic is not None
                FuncCall.pcall(executor, func_prefix + "topic_sub_pre",
                               subtopic)
                subtopic.execute(executor, func_prefix)
                FuncCall.pcall(executor, func_prefix + "topic_sub_post",
                               subtopic)
                continue
            if rtag == "IncludeRequirements":
                self.__requirements.execute(executor, func_prefix)
                continue
            if rtag == "Text":
                FuncCall.pcall(executor, func_prefix + "topic_text",
                               tag.get_content())
                continue

            raise RMTException(114, "Unknown tag in topic [%s]" % rtag,
                               self.name)

        tracer.debug("Calling post [%s]", self.name)
        FuncCall.pcall(executor, func_prefix + "topic_post", self)
        tracer.debug("Finished [%s]", self.name)

    def get_requirement_set(self):
        '''Returns the requirement set for this topic.'''
        return self.__requirements

    def get_tags(self):
        '''Returns the list of tags.'''
        return self.__tags

    def get_topic_name(self):
        '''Returns the name (short description) of the topic.
           Note: This is NOT the id of the topic.'''
        return self.__topic_name

    def get_id(self):
        '''Returns the topic id.
           Note: This is NOT the short description - a la 'Name'.'''
        return self.name
