'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Topic
   This holds one topic - and all subtopics of this topic
   
 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import os

from rmtoo.lib.storagebackend.txtfile.TxtRecord import TxtRecord
from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.storagebackend.txtfile.TxtIOConfig import TxtIOConfig
from rmtoo.lib.logging.EventLogging import tracer
from rmtoo.lib.FuncCall import FuncCall

class Topic(Digraph.Node):
    '''Each topic has a level - which indicates the identation of the text
       element. 
       Each topic does link to it's super-topic.  This is the way to detect
       cycles. 
       This needs to be a digraph node, to handle dependencies within the
       topics - e.g. handling of makefile dependencies.'''

    def __read(self, tname, input_handler, commit, file_info, req_set):
        '''Read in the topic and create all the tags.'''
        self.__tags = TxtRecord.from_string(file_info.get_content(),
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
                if self.__topic_name != None:
                    # TODO: Multiple Names
                    assert(False)
                self.__topic_name = tag.get_content()
            elif tag.get_tag() == "IncludeRequirements":
                if tag.get_content() != "full":
                    raise RMTException(113, "IncludeRequirements value not "
                                       "supported [%s]" % tag.get_content(),
                           self.name)
                self.__requirements = req_set.restrict_to_topics(tname)
                tracer.debug("Found [%d] requirements for topic [%s]."
                             % (self.__requirements.get_requirements_cnt(),
                                tname))
        # Check for the existence of the name
        if self.__topic_name == None:
            raise RMTException(62, "Mandatory tag 'Name' not given in topic",
                               self.name)

    def __init__(self, digraph, config, input_handler, commit, file_info,
                 req_set):
        tname = file_info.get_filename_sub_part()[:-4]
        # The 'name' in the digraph node is the ID
        Digraph.Node.__init__(self, tname)
        # This is the name of the topic (short description)
        self.__topic_name = None
        self._config = config
        tracer.debug("Called: name [%s]." % tname)
        self.__digraph = digraph
        self.__requirements = None
        self.__read(tname, input_handler, commit, file_info, req_set)

    def get_topic_names_flattened(self):
        '''Returns all the names of the complete topic hirarchy in one set.'''
        tracer.debug("Called: name [%s]." % self.name)
        result = set()
        result.add(self.name)
        for topic in self.outgoing:
            result = result.union(topic.get_topic_names_flattened())
        return result

    def execute(self, executor, func_prefix):
        '''Execute the parts which are needed for TopicsContinuum.'''
        tracer.debug("Calling pre [%s]." % self.name)
        FuncCall.pcall(executor, func_prefix + "topic_pre", self)
        tracer.debug("Calling sub [%s]." % self.name)
        for tag in self.__tags:
            rtag = tag.get_tag()
            if rtag == "Name":
                FuncCall.pcall(executor, func_prefix + "topic_name",
                               tag.get_content())
                continue
            if rtag == "SubTopic":
                subtopic = self.__digraph.find(tag.get_content())
                assert subtopic != None
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

        tracer.debug("Calling post [%s]." % self.name)
        FuncCall.pcall(executor, func_prefix + "topic_post", self)
        tracer.debug("Finished [%s]." % self.name)

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

    def UNUSED__init__(self, tdir, tname, dg, txtioconfig, cfg, tlevel=0,
                 tsuper=None):
        tracer.info("called: directory [%s] name [%s]" % (tdir, tname))
        Digraph.Node.__init__(self, tname)
        self.dir = tdir
        # Master map is needed for deciping requirements into the
        # appropriate topic.
        self.digraph = dg
        self.txtioconfig = txtioconfig
        self.cfg = cfg
        # Idendation level of this topic
        self.level = tlevel
        self.super = tsuper
        # This is a list of requirements which contain to this topic.
        self.reqs = []
        # The name of the Topic is mandatory (and also position
        # independent)
        # Note: there is also a .name field inherited from the
        # Digraph.Node (which hold in this case the topic's id).
        self.topic_name = None

        # This must only be done if there is a directory given
        if self.dir != None:
            self.read()
            self.extract_name()
        else:
            # In this case the tag list is (initally) empty
            self.t = []

    def UNUSED___str__(self):
        return "name [" + self.name + "]"

    # Extract the name from the list (it's mandatory!)
    def UNUSED_extract_name(self):
        for nt in self.t:
            if nt.get_tag() == "Name":
                self.topic_name = nt.get_content()
                del(nt)
                return
        raise RMTException(62, "Mandatory tag 'Name' not given in topic",
                           self.name)

    # Create Makefile Dependencies
    def UNUSED_cmad(self, reqscont, ofile, tname):
        reqs_dir = reqscont.config.get_value('requirements.input.directory')
        for req in self.reqs:
            # Add all the included requirements
            ofile.write(" %s.req" %
                         os.path.join(reqs_dir, req.name))
        # Add all the subtopics
        for n in self.outgoing:
            ofile.write(" ${TOPIC_%s_%s_DEPS}" % (tname, n.name))

    # Read in a specific topic
    def UNUSED_read(self):
        self.digraph.add_node(self)
        fd = file(os.path.join(self.dir, self.name + ".tic"))
        self.t = TxtRecord.from_fd(fd, self.name, self.txtioconfig)
        for tag in self.t:
            # If the topic has subtopics, read them also in.
            if tag.get_tag() == "SubTopic":
                ntopic = Topic(self.dir, tag.get_content(), self.digraph,
                               self.txtioconfig, self.cfg, self.level + 1,
                               self)
                #self.outgoing.append(ntopic)
                Digraph.create_edge(self, ntopic)
                #self.outgoing.append(ntopic)
        fd.close()

    def UNUSED_add_req(self, req):
        self.reqs.append(req)

    # Returns the name of the game
    def UNUSED_get_name(self):
        return self.topic_name

