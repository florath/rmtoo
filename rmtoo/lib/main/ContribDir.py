'''
 rmtoo
   Free and Open Source Requirements Management Tool

 Get the path to the contrib directory.

 (c) 2025 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import sys
import os
import pkg_resources


def main_func(args, mstdout, mstderr):
    """The 'real' main function.

    Returns the path to the contrib directory.
    """
    try:
        # First try to find contrib as package data (installed mode)
        try:
            contrib_path = pkg_resources.resource_filename('rmtoo', 'contrib')
            if os.path.exists(contrib_path):
                mstdout.write("%s\n" % contrib_path)
                return True
        except Exception:
            pass

        # Try to find contrib in site-packages data files (PyPI install)
        try:
            import rmtoo
            rmtoo_path = os.path.dirname(rmtoo.__file__)
            # Go up to virtualenv root:
            # site-packages/rmtoo -> site-packages ->
            #   lib -> python3.x -> v-rmtoo
            site_packages = os.path.dirname(rmtoo_path)
            venv_root = os.path.dirname(
                os.path.dirname(os.path.dirname(site_packages)))
            contrib_path = os.path.join(venv_root, 'rmtoo', 'contrib')
            if os.path.exists(contrib_path):
                mstdout.write("%s\n" % contrib_path)
                return True
        except Exception:
            pass

        # Fallback: try to find contrib in development mode (relative to
        # package)
        try:
            package_path = pkg_resources.resource_filename('rmtoo', '')
            # Go up one level from rmtoo package to find contrib at
            # project root
            project_root = os.path.dirname(package_path)
            contrib_path = os.path.join(project_root, 'contrib')
            if os.path.exists(contrib_path):
                mstdout.write("%s\n" % contrib_path)
                return True
        except Exception:
            pass

        mstderr.write("ERROR: Could not locate contrib directory\n")
        return False

    except Exception as e:
        mstderr.write("ERROR: Could not locate contrib directory: %s\n"
                      % str(e))
        return False


def main_impl(args, mstdout, mstderr, local_main_func=main_func,
              exitfun=sys.exit):
    """Call the main_func and handle possible exceptions"""
    exitfun(not local_main_func(args, mstdout, mstderr))


def main():
    """Call the main_impl with the appropriate parameters.

    This is needed to be able to write test cases for the 'main_impl'
    function.
    """
    main_impl(sys.argv[1:], sys.stdout, sys.stderr)
