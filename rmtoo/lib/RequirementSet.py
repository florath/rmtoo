'''
 rmtoo
   Free and Open Source Requirements Management Tool

    Container object which holds the set of requirements.
   
 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import json
import copy

from rmtoo.lib.Requirement import Requirement
from rmtoo.lib.RequirementDNode import RequirementDNode
from rmtoo.lib.Constraint import Constraint
from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.storagebackend.RecordEntry import RecordEntry
from rmtoo.lib.logging import tracer, logger
from rmtoo.lib.UsableFlag import UsableFlag
from rmtoo.lib.CE3Set import CE3Set
from rmtoo.lib.CE3 import CE3
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.digraph.TopologicalSort import topological_sort
from rmtoo.lib.FuncCall import FuncCall
from rmtoo.lib.TestCase import TestCase
from rmtoo.lib.GenIterator import GenIterator
from rmtoo.lib.logging.LogFormatter import LogFormatter

class RequirementSet(Digraph, UsableFlag):
    '''A RequirementSet holds one DAG (directed acyclic graph)
       of requirements.'''

    def __init__(self, config):
        '''Constructs a RequirementSet.
           This does not read everything in: please
           use the appropriate method to do so.'''
        tracer.debug("Called.")
        Digraph.__init__(self)
        UsableFlag.__init__(self)
        self._config = config
        self.__master_nodes = None
        # The key is the id the value the constraint.
        self.__constraints = {}
        # This holds only ready to use CE3 objects.
        self.__ce3set = CE3Set()
        # All the test cases for this requirement set
        self.__testcases = {}
        tracer.debug("Finished.")

    def __str__(self):
        return "Master nodes [%s]  Requirements [%s]" % \
            (self.__master_nodes, self._named_nodes)

    def __read_one_requirement(self, fileinfo, input_mods, object_cache):
        '''Read in one requirement from the file info.'''
        tracer.debug("Called.")
        # Check for correct filename
        if not fileinfo.get_filename().endswith(".req"):
            tracer.info("skipping file [%s]" % fileinfo.get_filename())
            return
        # Handle caching.
        vcs_id = fileinfo.get_vcs_id()
        rid = fileinfo.get_filename_sub_part()[:-4]
        req = object_cache.get("Requirement", vcs_id)
        tracer.info("Reading requirement [%s]" % rid)

        if req == None:
            file_content = fileinfo.get_content()
            req = Requirement(file_content, rid, fileinfo.get_filename(),
                              input_mods, self._config)
            # Add the requirement to the cache.
            object_cache.add(vcs_id, "Requirement", req)

        self._adapt_usablility(req)

        if req.is_usable():
            dnreq = RequirementDNode(req)
            # Store in the map, so that it is easy to access the
            # node by id.
### ToDo: needed            self._add_requirement(req)
            self.add_node(dnreq)
            # Also store it in the digraph's node list for simple
            # access to the digraph algorithms.
            # self.nodes.append(req)
        else:
            logger.error(LogFormatter.format(
                45, "could not be parsed", req.id))
        tracer.debug("Finished.")

    def __read_all_requirements(self, input_handler, commit, input_mods,
                                object_cache):
        '''Read in all the requirements from the input handler.'''
        tracer.debug("Called.")
        fileinfos = input_handler.get_file_infos(commit, "requirements")
        for fileinfo in fileinfos:
            self.__read_one_requirement(fileinfo, input_mods, object_cache)
        tracer.debug("Finished.")

    def __handle_modules_reqdeps(self, input_mods):
        '''This is mostly the same functionality of similar method of the
           class Requirement - but with one major difference: for this
           implementation stop if an error occurred.'''
        for module_node in input_mods.get_reqdeps_sorted():
            state = module_node.get_module().rewrite(self)
            if state == False:
                # Some semantic error occurred.
                self._set_not_usable()
                # Do not continue - return immediately, because some
                # algorithms rely on the correct run from others.
                return

    def __all_tags_handled(self):
        '''Returns true iff all the different tags are handled.'''
        all_handled = True
        for req_node in self.get_iter_nodes_values():
            req = req_node.get_requirement()
            if len(req.brmo) > 0:
                logger.error(LogFormatter.format(
                           57, "No tag handler found for tag(s) '%s' "
                           "- Hint: typo in tag(s)?" % req.brmo.keys(),
                           req.get_id()))
                all_handled = False
        return all_handled

    def _handle_modules(self, input_mods):
        '''Handle all modules which are executed on the 
           requirement set level.
           (One '_' only because this is used by the unit tests.'''
        tracer.debug("Called.")
        # Dependencies can be done, if all requirements are successfully
        # read in.
        self.__handle_modules_reqdeps(input_mods)
        # If there was an error, the state flag is set:
        tracer.debug("Check usability.")
        if not self.is_usable():
            logger.error(LogFormatter.format(
                       43, "there was a problem handling the "
                       "requirement set modules"))
            return False

        # The must no be left
        tracer.debug("Check all handled.")
        if not self.__all_tags_handled():
            logger.error(LogFormatter.format(
                       56, "There were errors encountered during parsing "
                       "and checking - can't continue."))
            return False

        return True

    def __read_one_constraint(self, fileinfo, input_mods, object_cache):
        '''Read in one constraints from the file info.'''
        tracer.debug("Called.")
        # Check for correct filename
        if not fileinfo.get_filename().endswith(".ctr"):
            tracer.info("skipping file [%s]" % fileinfo.get_filename())
            return
        # Handle caching.
        vcs_id = fileinfo.get_vcs_id()
        rid = fileinfo.get_filename_sub_part()[:-4]
        ctr = object_cache.get("Constraint", vcs_id)
        tracer.info("Reading constraint [%s]" % rid)

        if ctr == None:
            file_content = fileinfo.get_content()
            ctr = Constraint(file_content, rid, fileinfo.get_filename(),
                             input_mods, self._config)
            # Add the requirement to the cache.
            object_cache.add(vcs_id, "Constraint", ctr)

        self._adapt_usablility(ctr)

        if ctr.is_usable():
            # Store in the map, so that it is easy to access the
            # node by id.
            self._add_constraint(ctr)
            # Also store it in the digraph's node list for simple
            # access to the digraph algorithms.
            # self.nodes.append(req)
        else:
            logger.error(LogFormatter.format(87, "could not be parsed", ctr.id))
        tracer.debug("Finished.")

#        everythings_fine = True
#        files = os.listdir(directory)
#        for f in files:
#            m = re.match("^.*\.ctr$", f)
#            if m == None:
#                continue
#            rid = f[:-4]
#            fd = codecs.open(os.path.join(directory, f), "r", "utf-8")
#            cnstrnt = Constraint(fd, rid, self, self.mods, self._config)
#            if cnstrnt.ok():
#                # Store in the map, so that it is easy to access the
#                # node by id.
#                self.constraints[cnstrnt.get_id()] = cnstrnt
#            else:
#                self.error(87, "could not be parsed", cnstrnt.get_id())
#                everythings_fine = False
#        self.ts = time.time()
#        return everythings_fine

    def __read_all_constraints(self, input_handler, commit, input_mods,
                               object_cache):
        '''Read in all the constraints from the input handler.'''
        tracer.debug("Called.");
        fileinfos = input_handler.get_file_infos(commit, "constraints")
        for fileinfo in fileinfos:
            self.__read_one_constraint(fileinfo, input_mods, object_cache)
        tracer.debug("Finished.");

    # TODO: double feature code with small adaptions only.
    def __read_one_testcase(self, fileinfo, input_mods, object_cache):
        '''Read in one testcase from the file info.'''
        tracer.debug("Called.")
        # Check for correct filename
        if not fileinfo.get_filename().endswith(".tec"):
            tracer.info("skipping file [%s]" % fileinfo.get_filename())
            return
        # Handle caching.
        vcs_id = fileinfo.get_vcs_id()
        rid = fileinfo.get_filename_sub_part()[:-4]
        testcase = object_cache.get("TestCase", vcs_id)
        tracer.info("Reading testcase [%s]" % rid)

        if testcase == None:
            file_content = fileinfo.get_content()
            testcase = TestCase(file_content, rid, fileinfo.get_filename(),
                                input_mods, self._config)
            # Add the requirement to the cache.
            object_cache.add(vcs_id, "TestCase", testcase)

        self._adapt_usablility(testcase)

        if testcase.is_usable():
            # Store in the map, so that it is easy to access the
            # node by id.
            self._add_testcase(testcase)
            # Also store it in the digraph's node list for simple
            # access to the digraph algorithms.
            # self.nodes.append(req)
        else:
            logger.error(LogFormatter.format(
                115, "could not be parsed", testcase.id))
        tracer.debug("Finished.")

    def __read_all_testcases(self, input_handler, commit, input_mods,
                               object_cache):
        '''Read in all the testcases from the input handler.'''
        tracer.debug("Called.");
        fileinfos = input_handler.get_file_infos(commit, "testcases")
        for fileinfo in fileinfos:
            self.__read_one_testcase(fileinfo, input_mods, object_cache)
        tracer.debug("Finished.");


    def read_requirements(self, input_handler, commit, input_mods,
                          object_cache):
        '''Reads in all the requirements from the input_handler.'''
        tracer.debug("Called; reading requirements.")
        self.__read_all_requirements(input_handler, commit, input_mods,
                                     object_cache)

        tracer.debug("Reading constrains.")
        self.__read_all_constraints(input_handler, commit, input_mods,
                                    object_cache)

        tracer.debug("Reading test cases.")
        self.__read_all_testcases(input_handler, commit, input_mods,
                                  object_cache)
#
#        if not everythings_fine:
#            self.error(86, "There were errors in the requirement set - "
#                       "in the constraints")
#            self._set_not_usable()
#            return False

        self._handle_modules(input_mods)
        tracer.debug("Finished.")

    def _add_constraint(self, ctr):
        '''Add constraint to the internal container.'''
        tracer.debug("Add constraint [%s]." % ctr.get_id())
        self.__constraints[ctr.get_id()] = ctr

    def _add_testcase(self, testcase):
        '''Add testcase to the internal container.'''
        tracer.debug("Add testcase [%s]." % testcase.get_id())
        self.__testcases[testcase.get_id()] = testcase

    def _add_ce3(self, name, ce3):
        '''Add the ce3 under the given name.'''
        tracer.debug("Add CE3 for requirement [%s]" % name)
        self.__ce3set.insert(name, ce3)

    def restrict_to_topics(self, topic_set):
        '''Restrict the list (dictionary) of requirements to the given
           topic set - i.e. only requirements are returned which belong to
           one of the topics in the topic set.'''
        tracer.debug("Called; TopicSet [%s]" % topic_set)
        restricted_reqs = RequirementSet(self._config)
        for req in self._named_nodes.values():
            if req.get_requirement().get_topic() in topic_set:
                tracer.debug("Restricting requirement [%s]" % 
                             req.get_requirement().get_id())
                # Here a deep copy is needed, because the internal
                # data structures must be adapted: the incoming and the
                # outgoing lists.
## ToDo: needed???                nreq = copy.deepcopy(req)
                nreq = copy.copy(req)
                # Smash the incoming and outgoing
# ToDo: check                nreq.incoming = []
# ToDo: check               nreq.outgoing = []
                nreq.clear_incoming()
                nreq.clear_outgoing()

                # Add to the internal map
                restricted_reqs.add_node(nreq)
                # Add to the common digraph structure
# ToDo: ???                restricted_reqs.add_node(nreq)
                # Add ce3 of the requirement
                restricted_reqs._add_ce3(
                    nreq.get_requirement().get_id(),
                    self.__ce3set.get(nreq.get_requirement().get_id()))
                ctrs = nreq.get_requirement().get_value("Constraints")
                if ctrs != None:
                    for cval in ctrs:
                        restricted_reqs._add_constraint(self.__constraints[cval])

                # Add testcases
                testcases = nreq.get_requirement().get_value("Test Cases")
                if testcases != None:
                    tracer.debug("Restricting testcases [%s]" % testcases)
                    for testcase in testcases:
                        restricted_reqs._add_testcase(self.__testcases[testcase])

# TODO refactor
        # Run through the old list of incoming and outgoing and 
        # only copy things over if they are also in the restricted 
        # graph.
        for req in restricted_reqs._named_nodes.values():
            old_req = self._named_nodes[req.get_requirement().get_id()]
            for incoming in old_req.get_iter_incoming():
                if incoming.get_requirement().get_topic() in topic_set:
                    nreq = restricted_reqs._named_nodes[
                        incoming.get_requirement().get_id()]
                    restricted_reqs.create_edge(req, nreq)
        for req in restricted_reqs._named_nodes.values():
            old_req = self._named_nodes[req.get_requirement().get_id()]
            for outgoing in old_req.get_iter_incoming():
                if outgoing.get_requirement().get_topic() in topic_set:
                    nreq = restricted_reqs._named_nodes[
                        outgoing.get_requirement().get_id()]
                    restricted_reqs.create_edge(req, nreq)

        tracer.debug("Finished; found [%d] requirements for TopicSet [%s]."
                     % (restricted_reqs.get_requirements_cnt(), topic_set))
        return restricted_reqs

    def execute(self, executor, func_prefix):
        '''Execute the parts which are needed for RequirementSet.'''
        tracer.debug("calling pre")
        FuncCall.pcall(executor, func_prefix + "requirement_set_pre", self)
        tracer.debug("calling sub requirement set")
        for requirement in executor.requirement_set_sort(
                            self._named_nodes.values()):
            requirement.execute(executor, func_prefix)
        tracer.debug("calling post")
        FuncCall.pcall(executor, func_prefix + "requirement_set_post", self)
        tracer.debug("finished")

    def __resolve_solved_by_one_req(self, req_node):
        '''Resolve the 'Solved by' for one requirement.'''
        assert isinstance(req_node, RequirementDNode)
        req = req_node.get_requirement()
        tracer.debug("Called: requirement id [%s]." % req.get_id())

        # It is a 'normal' case when there is no 'Solved by' (until now).
        if "Solved by" not in req.brmo:
            return True

        content = req.brmo["Solved by"].get_content()
        # If available, it must not empty
        if len(content) == 0:
            logger.error(LogFormatter.format(
                        77, "'Solved by' field has length 0", req.get_id()))
            return False

        # Step through the list
        dep_list = content.split()
        tracer.debug("dependent list [%s]" % dep_list)
        for dep in dep_list:
            if dep not in self._named_nodes:
                logger.error(LogFormatter.format(
                        74, "'Solved by' points to a "
                        "non-existing requirement '%s'" % dep, req.get_id()))
                return False
            # It is not allowed to have self-references: it does not
            # make any sense, that a requirement references itself.
            if dep == req.get_id():
                logger.error(LogFormatter.format(
                           75, "'Solved by' points to the "
                           "requirement itself", req.id))
                return False

            # Mark down the depends on...
            dep_req_node = self._named_nodes[dep]
            assert isinstance(dep_req_node, RequirementDNode)

            # This is exactly the other way as used in the 'Depends on'
            tracer.debug("Add edge [%s] -> [%s]" %
                         (dep_req_node.get_requirement().get_id(),
                          req.get_id()))
            Digraph.create_edge(self, req_node, dep_req_node)

        # Delete the original tag
        del req.brmo["Solved by"]
        return True

    def resolve_solved_by(self):
        '''Step through the internal list of collected requirements and
           evaluate the 'Solved by'.  This is done by creating the
           appropriate digraph nodes.'''
        tracer.debug("Called.")
        # Run through all the requirements and look for the 'Solved
        # by'
        success = True
        for req_node in self._named_nodes.values():
            if not self.__resolve_solved_by_one_req(req_node):
                tracer.info("Handling of requirement [%s] was not successful"
                             % req_node.get_requirement().get_id())
                success = False
        tracer.debug("Finished; success [%s]." % success)
        return success

    def __resolve_depends_on_one_req(self, req_node, also_solved_by):
        tracer.debug("Called.")
        req = req_node.get_requirement()
        if req.get_value("Type") == Requirement.rt_master_requirement:
            # There must no 'Depends on'
            if "Depends on" in req.brmo:
                print("+++ ERROR %s: initial requirement has "
                      "Depends on field." % (req.id))
                return False
            # It self does not have any depends on nodes
            req.graph_depends_on = None
            # This is the master!
            return True

        # For all other requirements types there must be a 'Depends on'
        if "Depends on" not in req.brmo:
            if also_solved_by:
                # Skip handling this requirement
                return True
            print("+++ ERROR %s: non-initial requirement has "
                  "no 'Depends on' field." % (req.id))
            return False

        t = req.brmo["Depends on"]

        # If available, it must not empty
        if len(t.get_content()) == 0:
            print("+++ ERROR %s: 'Depends on' field has len 0" %
                  (req.id))
            return False

        # Step through the list
        tl = t.get_content().split()
        for ts in tl:
            if ts not in self.get_all_requirement_ids():
                logger.error(LogFormatter.format(
                             47, "'Depends on' points to a "
                             "non-existing requirement '%s'" % ts, req.id))
                return False
            # It is not allowed to have self-references: it does not
            # make any sense, that a requirement references itself.
            if ts == req.id:
                logger.error(LogFormatter.format(
                      59, "'Depends on' points to the "
                      "requirement itself", req.id))
                return False

            # Mark down the depends on...
            dep_req_node = self._named_nodes[ts]
            # This is exactly the other way as used in the 'Depends on'
            tracer.debug("Add edge [%s] -> [%s]" %
                         (dep_req_node.get_requirement().get_id(),
                          req.get_id()))
            Digraph.create_edge(self, dep_req_node, req_node)

        # Copy and delete the original tag
        ## XXX Not neede any more? req.tags["Depends on"] = t.split()
        del req.brmo["Depends on"]
        return True

    def resolve_depends_on(self, also_solved_by):
        '''Step through the internal list of collected requirements and
           evaluate the 'Depends on'.  This is done by creating the 
           appropriate digraph node.'''
        tracer.debug("Called.")
        # Run through all the requirements and look for the 'Depend
        # on' (depending on the type of the requirement)
        success = True
        for req in self._named_nodes.values():
            if not self.__resolve_depends_on_one_req(req, also_solved_by):
                success = False
        tracer.debug("Finished; success [%s]." % success)
        return success

    @staticmethod
    def get_ctr_name(s):
        '''Extracts the name of the constrains file name.'''
        i = s.find("(")
        if i == -1:
            print("+++ Error: no '(' in constraints")
            print("ASSERT %s" % s)
            # Throw: does not contain (
            assert(False)
        return s[:i]

    def __create_local_ce3s(self):
        '''Create the local Constraint Execution Environments
           and evaluate the given statements.
           This method does two things:
           - evaluating the constraints in the CE3
           - Resetting the 'Constraints' entry in the requirement
           (instead of the TextRecord a map of name to constraint
            object is stored).'''
        tracer.debug("Called.")
        for req_name, req in self._named_nodes.items():
            # In each case store a (maybe empty) CE3 in the set.
            ce3 = CE3()
            cstrnts = req.get_requirement().get_value("Constraints")
            if cstrnts != None:
                sval = json.loads(cstrnts.get_content())
                cs = {}
                for s in sval:
                    ctr_name = self.get_ctr_name(s)
                    if not ctr_name in self.__constraints:
                        raise RMTException(88, "Constraint [%s] does not "
                                           "exists" % ctr_name)
                    rcs = self.__constraints.get(ctr_name)
                    ce3.eval(rcs, ctr_name, s)
                    cs[ctr_name] = rcs
                req.get_requirement().set_value("Constraints", cs)
            # Store the fresh create CE3 into the ce3set
            self.__ce3set.insert(req_name, ce3)
        tracer.debug("Finished. Number of constraints [%d]." %
                     self.__ce3set.length())

    def __unite_ce3s(self):
        '''Execute the unification of the CE3s:
           From the list of all incoming nodes and the value of the 
           current node compute the new value of the current node
           The ce3s must be executed in topological order.'''
        ce3tsort = topological_sort(self)
        for r in ce3tsort:
            # TODO Outgoing
            # Have a look for incoming nodes
            ince3s = []
            for i in r.get_iter_incoming():
                ince3s.append(self.__ce3set.get(i.get_requirement().get_id()))
            lce3 = self.__ce3set.get(r.get_requirement().get_id())
            lce3.unite(ince3s)

    def resolve_ce3(self):
        '''Handle the Constraint Execution Environments for this
           requirement set.'''
        tracer.debug("Called.")
        # The first step is to create local Constraint Execution Environments
        self.__create_local_ce3s()
        # Evaluate all the CE3 in topological order
        self.__unite_ce3s()
        tracer.debug("Finished.")

    def find_master_nodes(self):
        '''Find all the available master nodes and stored them in
           a class field.'''
#        assert False
#
#    This is completely wrong:
#    The digraph is only and always the digraph of the complete
#    requirement set (not restricted to a topic)
#    The only way to check, if a requirement is in the topic
#    is to check if it is available in the topic._requirements dict.
        tracer.debug("Looking for master nodes in [%d] nodes."
                     % self.get_node_cnt())
        self.__master_nodes = set()
        for req_node in self.get_iter_nodes_values():
            if req_node.get_incoming_cnt() == 0:
                tracer.debug("Found master nodes [%s]"
                             % req_node.get_requirement().get_id())
                self.__master_nodes.add(req_node)
            else:
                tracer.debug("[%s] is not a master node; incoming from "
                             % req_node.get_requirement().get_id())
                for i in req_node.get_iter_incoming():
                    tracer.debug("  -> [%s]" % i.get_requirement().get_id())
        tracer.info("Found [%d] master nodes" % len(self.__master_nodes))

    def get_master_nodes(self):
        '''Return the available master nodes.'''
        tracer.debug("Master nodes [%s]" % self.__master_nodes)
        if self.__master_nodes == None:
            self.find_master_nodes()
        return self.__master_nodes

    def get_requirements_cnt(self):
        '''Returns the number of requirements.'''
        return len(self._named_nodes)

    def get_all_requirement_ids(self):
        '''Return all requirement ids of the requirement set.'''
        return self._named_nodes.keys()

    def get_requirement(self, rid):
        '''Return the requirement with the given id.'''
        return self._named_nodes[rid]

    def get_requirements_iteritems(self):
        '''Return the iteritems() iterator of all requirements.'''
        return self._named_nodes.iteritems()

    def get_ce3set(self):
        '''Return the ce3 set which belongs to this requirement set.'''
        return self.__ce3set

    def get_constraints(self):
        '''Return the constraints.'''
        return self.__constraints

    def get_testcases(self):
        '''Return the testcases.'''
        return self.__testcases

    # Note: the following methods are of no use any more,
    # because the 'Depends on' will be gone in near future.

    # Note: the following methods work on the 'record' part
    # of the requirement! (Not on the values!)
    def normalize_dependencies(self):
        '''Normalize the dependencies to ''.'''
        tracer.debug("Called.")
        for r in self.get_iter_nodes_values():
            req = r.get_requirement()
            record = req.get_record()

            # Remove the old 'Depends on'
            if record.is_tag_available("Depends on"):
                tracer.debug("[%s] Remove 'Depends on'." % r.get_name())
                record.remove("Depends on")
            
            # Create the list of dependencies
            tracer.debug("[%s] Create list of dependencies." % r.get_name())
            onodes = []
            for n in r.get_iter_outgoing():
                onodes.append(n.get_name())

            # If the onodes is empty: There is no old 'Solved by'
            # tag available - if so something completey strange has
            # happens and it is better to stop directly.
            if len(onodes) == 0:
                assert(not record.is_tag_available("Solved by"))
                # Looks that everything is ok: continue
                continue

            onodes.sort()
            on = " ".join(onodes)

            # Check if there is already a 'Solved by'
            try:
                tracer.debug("[%s] Try to add 'Solved by' [%s]." % 
                             (r.get_name(), on))
                record.set_content("Solved by", on)
            except ValueError:
                tracer.debug("[%s] Try to append 'Solved by' [%s]." % 
                             (r.get_name(), on))
                record.append_entry(RecordEntry(
                        "Solved by", on,
                        "Added by rmtoo-normalize-dependencies"))

        return True

    def write_to_filesystem(self, directory):
        '''Write the requirements back to the filesystem.'''
        tracer.debug("Called.")
        for r in self.get_iter_nodes_values():
            tracer.debug("[%s] write requirement" % r.get_name())
            fd = file(directory + "/" + r.get_name() + ".req", "w")
            r.get_requirement().write_fd(fd)
            fd.close()
        return True

class RequirementSetIterator(GenIterator):

    def __init__(self, requirement_set):
        GenIterator.__init__(
            self, requirement_set.get_master_nodes().__iter__())

