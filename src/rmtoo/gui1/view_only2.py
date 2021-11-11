'''
 rmtoo
   Free and Open Source Requirements Management Tool

  First GUI:
    This is read only.

 (c) 2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
import sys

from rmtoo.lib.main.MainHelper import MainHelper
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.TopicContinuumSet import TopicContinuumSet, \
    TopicContinuumSetIterator

import pgi
pgi.require_version('Gtk', '3.0')  # noqa: E402
from pgi.repository import Gtk, GObject  # noqa: E402


def advance(iter, n):
    for i in range(0, n):
        iter.next()


class GTMIterator:

    def __init__(self, iterator, type_name):
        self.__iterator = iterator
        self.__type_name = type_name
        self.__current = None
        self.next()

    def next(self):
        try:
            self.__current = self.__iterator.next()
        except StopIteration:
            return None
        return self.__current

    def current(self):
        return self.__current

    def type_name(self):
        return self.__type_name

    def inc(self, n):
        for i in range(0, n):
            self.next()

    def __str__(self):
        return "GTMIterator [%s] [%s]" % (self.__type_name, self.__iterator)

    def __repr__(self):
        return self.__str__()


class RmtooTreeModel(GObject.GObject, Gtk.TreeModel):

    column_names = ['Requirement', ]
#    column_types = (GdkPixbuf.Pixbuf, str,)
    column_types = (str,)

    def __init__(self, topic_continuum_set):
        GObject.GObject.__init__(self)
        self.__topic_continuum_set = topic_continuum_set

    def get_column_names(self):
        return self.column_names

    def on_get_flags(self):
        '''The model is a real tree and is not persistence against changes.'''
        return 0

    def on_get_n_columns(self):
        return len(self.column_types)

    def on_get_column_type(self, n):
        return self.column_types[n]

    def on_get_iter(self, path):
        print("NEW ITER PATH [%s]" % path)
        if path[0] == 0:
            return TopicContinuumSetIterator(self.__topic_continuum_set)
        assert False
        return self.files[path[0]]

    def on_get_path(self, rowref):
        assert False
        return self.files.index(rowref)

    def on_get_value(self, rowref, column):

        print("GET VALUE COL [%s]" % column)

        key, value = rowref.current()

        #        print("ON GET VALUE [%s] [%s]" % (rowref, column))
        print("Current value [%s] [%s]" % (key, value))
        print("TYPE KEY [%s]" % type(key))

        return key

        assert False
#        fname = os.path.join(self.dirname, rowref)
#        try:
#            filestat = os.stat(fname)
#        except OSError:
#            return None
#        mode = filestat.st_mode
#        if column is 0:
#            if stat.S_ISDIR(mode):
#                return folderpb
#            else:
#                return filepb
#        elif column is 1:
#            return rowref
#        elif column is 2:
#            return filestat.st_size
#        elif column is 3:
#            return oct(stat.S_IMODE(mode))
#        return time.ctime(filestat.st_mtime)

    def on_iter_next(self, rowref):
        print("ON ITER NEXT [%s]" % rowref)

        try:
            #            print("CURRENT2 [%s] [%s]" % rowref.current())
            return rowref.next()
        except StopIteration:
            return None

        assert False
        try:
            i = self.files.index(rowref) + 1
            return self.files[i]
        except IndexError:
            return None

    def on_iter_children(self, rowref):
        print("On ITER CHILDERN [%s]" % rowref)

        if rowref is not None:
            return rowref.iter_children()

#            print("ITER TYPE [%s]" % rowref.type_name())
#            if rowref.type_name() == "topic_continuum":
#                tcsetname, tcset = rowref.current()
#                return GTMIterator(
#                        tcset.get_vcs_commit_ids().__iter__(), "topics")

        assert False
        if rowref:
            return None
        return self.files[0]

    def on_iter_has_child(self, rowref):
        print("ON ITER HAS CHILD [%s]" % rowref)
#        print("ON ITER HAS CHILD [%s]" % dir(rowref))
#
#        key, value = rowref.current()
#        print("ON ITER HAS CHILD [%s] [%s]" % (key, value))
#        print("ON ITER HAS CHILD [%s]" % type(value))

        return rowref.has_child()

        type_name = rowref.type_name()
        if type_name == "topic_continuum":
            key, value = rowref.current()
            return len(value.get_vcs_commit_ids()) > 0
        if type_name == "topics":
            return rowref.current() is not None

        assert False
        return False

    def on_iter_n_children(self, rowref):
        assert False
        if rowref:
            return 0
        return len(self.files)

    def on_iter_nth_child(self, rowref, n):
        print("ON ITER NTH CHILD [%s] [%s]" % (rowref, n))

        if rowref is None:
            iter = TopicContinuumSetIterator(self.__topic_continuum_set)
            advance(iter, n)
            return iter

        assert False

        return None

        assert False
        if rowref:
            return None
        try:
            return self.files[n]
        except IndexError:
            return None

    def on_iter_parent(child):
        assert False
        return None


class GUI1ViewOnly:

    def on_selection_changed(self, selection, *args):
        model, paths = selection.get_selected_rows()
        print("SELECTED A [%s]" % (selection))
        print("SELECTED B [%s]" % (model))
        print("SELECTED C [%s]" % (paths))

    def __add_requirements(self, model, iter, node):
        liter = model.append(iter)
        model.set(liter, 0, node.get_id())
        for n in node.outgoing:
            self.__add_requirements(model, liter, n)

    def create_tree(self, topic_continuum_set):
        # Create a new scrolled window, with scrollbars only if needed
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_policy(
            Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)

        rmtoo_model = RmtooTreeModel(topic_continuum_set)

#        tree_view = Gtk.TreeView()
#        scrolled_window.add_with_viewport (tree_view)
#        tree_view.show()
#
#        selection = tree_view.get_selection()
#        selection.connect('changed', self.on_selection_changed)

        # create the TreeView
        self.treeview = Gtk.TreeView()

        # create the TreeViewColumns to display the data
        column_names = rmtoo_model.get_column_names()
        self.tvcolumn = [None] * len(column_names)
#        cellpb = Gtk.CellRendererPixbuf()
#        self.tvcolumn[0] = Gtk.TreeViewColumn(column_names[0],
#                                              cellpb, pixbuf=0)
#        cell = Gtk.CellRendererText()
#        self.tvcolumn[0].pack_start(cell, False)
#        self.tvcolumn[0].add_attribute(cell, 'text', 1)
#        self.treeview.append_column(self.tvcolumn[0])
        for n in range(0, len(column_names)):
            cell = Gtk.CellRendererText()
#            if n == 0:
#                cell.set_property('xalign', 1.0)
            self.tvcolumn[n] = Gtk.TreeViewColumn(column_names[n],
                                                  cell, text=n)
            self.treeview.append_column(self.tvcolumn[n])

        scrolled_window.add_with_viewport(self.treeview)
        self.treeview.set_model(rmtoo_model)
        self.treeview.show()

#        for name, continuum in iteritem(
#                 topic_continuum_set.get_continuum_dict()):
#            iter_continuum = model.append(None)
#            model.set(iter_continuum, 0, name)
#            for commit_id in continuum.get_vcs_commit_ids():
#                iter_commit = model.append(iter_continuum)
#                model.set(iter_commit, 0, commit_id)
#                topic_set = continuum.get_topic_set(commit_id.get_commit())
#                req_set = topic_set.get_requirement_set()
#
#                req_set.find_master_nodes()
#                for master_node in req_set.get_master_nodes():
#                    self.__add_requirements(model, iter_commit, master_node)
#
#
#        cell = Gtk.CellRendererText()
#        column = Gtk.TreeViewColumn("Requirements", cell, text=0)
#        tree_view.append_column(column)

        return scrolled_window

    # Add some text to our text widget - this is a callback that is invoked
    # when our window is realized. We could also force our window to be
    # realized with GtkWidget.realize, but it would have to be part of a
    # hierarchy first
    def insert_text(self, buffer):
        iter = buffer.get_iter_at_offset(0)
        buffer.insert(
            iter,
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
        view = Gtk.TextView()
        buffer = view.get_buffer()
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_policy(
            Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        scrolled_window.add(view)
        self.insert_text(buffer)
        scrolled_window.show_all()
        return scrolled_window

    def __init__(self, config, input_mods, _mstdout, mstderr):
        try:
            topic_continuum_set = TopicContinuumSet(input_mods, config)
        except RMTException as rmte:
            mstderr.write("+++ ERROR: Problem reading in the continuum [%s]\n"
                          % rmte)
            return

        self.window = Gtk.Window(Gtk.WindowType.TOPLEVEL)
        self.window.set_title("rmtoo - Read only GUI")
        self.window.set_default_size(800, 600)

        # create a vpaned widget and add it to our toplevel window
        hpaned = Gtk.HPaned()
        self.window.add(hpaned)
        hpaned.set_position(200)
        hpaned.show()

        # Now create the contents of the two halves of the window
        tree = self.create_tree(topic_continuum_set)
        hpaned.add1(tree)
        tree.show()

        text = self.create_text()
        hpaned.add2(text)
        text.show()

        self.window.show()

    def main(self):
        Gtk.main()


def execute_cmds(config, input_mods, _mstdout, mstderr):
    view_only = GUI1ViewOnly(config, input_mods, _mstdout, mstderr)
    view_only.main()


def main_impl(args, mstdout, mstderr):
    '''The real implementation of the main function:
       o get config
       o set up logging
       o do everything'''
    config, input_mods = MainHelper.main_setup(args, mstdout, mstderr)
#    configure_logging(config)
    return execute_cmds(config, input_mods, mstdout, mstderr)


def main(args, mstdout, mstderr, main_func=main_impl, exitfun=sys.exit):
    '''The main entry function
    This calls the main_func function and does the exception handling.'''
    try:
        exitfun(not main_func(args, mstdout, mstderr))
    except RMTException as rmte:
        mstderr.write("+++ ERROR: Exception occurred: %s\n" % rmte)
        exitfun(1)


if __name__ == "__main__":
    main(sys.argv[1:], sys.stdout, sys.stderr)
