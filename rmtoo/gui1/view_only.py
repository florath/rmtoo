'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  First GUI:
    This is read only.
   
 (c) 2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import pygtk
pygtk.require('2.0')
import gtk
import gobject

import sys

from rmtoo.lib.logging import configure_logging
from rmtoo.lib.main.MainHelper import MainHelper
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.TopicContinuumSet import TopicContinuumSet

class GUI1ViewOnly:

    def selection_received(self, widget, selection_data, data):
        print("SELECTED [%s] [%s]" % (selection_data, data))

    def on_selection_changed(self, selection, *args):
        store, paths = selection.get_selected_rows()
        print("SELECTED A [%s]" % (selection))
        print("SELECTED B [%s]" % (store))
        print("SELECTED C [%s]" % (paths))
        giter = store.get_iter(paths[0])
        print("SELECTED D [%s]" % (giter))
        print("SELECTED E [%s]" % (dir(giter)))

    def __store_add_requirements(self, store, iter, node):
        liter = store.append(iter)
        store.set(liter, 0, node.get_id())
        for n in node.outgoing:
            self.__store_add_requirements(store, liter, n)

    def __store_add_topic(self, tree_store, iter_topic, topic):
        titer = tree_store.append(iter_topic, [topic.get_id()])
        for n in topic.outgoing:
            self.__store_add_topic(tree_store, titer, n)

    def __store_add_vcs_commit_ids(self, tree_store, name, continuum,
                                   iter_continuum):
        for commit_id in continuum.get_vcs_commit_ids():
            iter_commit = tree_store.append(iter_continuum, [commit_id])
            iter_topic = tree_store.append(iter_commit, ["topics"])
            iter_requirements = tree_store.append(iter_commit, ["requirements"])

            topic_set = continuum.get_topic_set(commit_id.get_commit())
            req_set = topic_set.get_requirement_set()

            master_topic = topic_set.get_master_topic()
            self.__store_add_topic(tree_store, iter_topic, master_topic)

            req_set.find_master_nodes()
            for master_node in req_set.get_master_nodes():
                self.__store_add_requirements(tree_store, iter_requirements,
                                              master_node)

    def __store_add_topic_continuum_set(self, tree_store, topic_continuum_set):
        for name, continuum in iter(sorted(
                        topic_continuum_set.get_continuum_dict().items())):
            iter_continuum = tree_store.append(None, [name])
            self.__store_add_vcs_commit_ids(tree_store, name, continuum,
                                            iter_continuum)

    def create_tree(self, topic_continuum_set):
        # Create a new scrolled window, with scrollbars only if needed
        scrolled_window = gtk.ScrolledWindow()
        scrolled_window.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)

        tree_store = gtk.TreeStore(gobject.TYPE_STRING)

        tree_view = gtk.TreeView(tree_store)
        scrolled_window.add_with_viewport (tree_view)
        tree_view.show()

        selection = tree_view.get_selection()
        selection.connect('changed', self.on_selection_changed)

        self.__store_add_topic_continuum_set(tree_store, topic_continuum_set)

        cell = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Requirements", cell, text=0)
        tree_view.append_column(column)

        return scrolled_window

    # Add some text to our text widget - this is a callback that is invoked
    # when our window is realized. We could also force our window to be
    # realized with GtkWidget.realize, but it would have to be part of a
    # hierarchy first
    def insert_text(self, buffer):
        iter = buffer.get_iter_at_offset(0)
        buffer.insert(iter,
                      "From: pathfinder@nasa.gov\n"
                      "To: mom@nasa.gov\n"
                      "Subject: Made it!\n"
                      "\n"
                      "We just got in this morning. The weather has been\n"
                      "great - clear but cold, and there are lots of fun sights.\n"
                      "Sojourner says hi. See you soon.\n"
                      " -Path\n")

    # Create a scrolled text area that displays a "message"
    def create_text(self):
        view = gtk.TextView()
        buffer = view.get_buffer()
        scrolled_window = gtk.ScrolledWindow()
        scrolled_window.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        scrolled_window.add(view)
        self.insert_text(buffer)
        scrolled_window.show_all()
        return scrolled_window


    def __init__(self, config, input_mods, _mstdout, mstderr):
        try:
            topic_continuum_set = TopicContinuumSet(input_mods, config)
        except RMTException, rmte:
            mstderr.write("+++ ERROR: Problem reading in the continuum [%s]\n"
                      % rmte)
            return

        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("rmtoo - Read only GUI")
        self.window.set_default_size(800, 600)

        # create a vpaned widget and add it to our toplevel window
        hpaned = gtk.HPaned()
        self.window.add(hpaned)
        hpaned.show()

        # Now create the contents of the two halves of the window
        list = self.create_tree(topic_continuum_set)
        hpaned.add1(list)
        list.show()

        text = self.create_text()
        hpaned.add2(text)
        text.show()

        self.window.show()

    def main(self):
        gtk.main()

def execute_cmds(config, input_mods, _mstdout, mstderr):
    view_only = GUI1ViewOnly(config, input_mods, _mstdout, mstderr)
    view_only.main()

def main_impl(args, mstdout, mstderr):
    '''The real implementation of the main function:
       o get config
       o set up logging
       o do everything'''
    config, input_mods = MainHelper.main_setup(args, mstdout, mstderr)
    configure_logging(config, mstderr)
    return execute_cmds(config, input_mods, mstdout, mstderr)

def main(args, mstdout, mstderr, main_func=main_impl, exitfun=sys.exit):
    '''The main entry function
    This calls the main_func function and does the exception handling.'''
    try:
        exitfun(not main_func(args, mstdout, mstderr))
    except RMTException, rmte:
        mstderr.write("+++ ERROR: Exception occurred: %s\n" % rmte)
        exitfun(1)

if __name__ == "__main__":
    main(sys.argv[1:], sys.stdout, sys.stderr)

