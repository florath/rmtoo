
RmtooOnRmtoo
============

There is no need to compile rmtoo.

After unpacking the package (either the tar ball or the debian
package) rmtoo can directly be used.

*** THE FOLLOWING PROCEDURE IS OPTIONAL AND NOT
*** NEEDED FOR USING RMTOO.


--- Using rmtoo as example ---

Because rmtoo uses rmtoo for requirements management  it is possible
to use rmtoo as an example for rmtoo's features.


--- Check and create them all ---
When you want to create all the documentation for rmtoo itself, you
can execute the steps described in this section.  Please note that
this is not needed to use rmtoo in your project.  Also the
requirements documentation created, can be downloaded from the
project's download page.  For the link to the download page please
consult the Readme.txt file.

When using the tar ball, you can try a 
$ . setenv.sh
$ make 
$ make tests
The configuration file where the output artifacts are configured are
doc/requirements/ConfigX.py.
All created documents are stored in the artifacts directory.

When using the Debian package, it is possibe to run all the tests.
$ cd /usr/share/pyshared/rmtoo
$ nosetests -v -s
(Note that some test cases will fail, because they assume that
there is a git-history available - which is not.)
The documents can be found under '/usr/share/doc/rmtoo'.

Please note that rmtoo is by default delivered to create the comlete
history of rmtoo requirements itself.  When using the tar ball or the
debian package the history is not available.  You might get an error
like:
Traceback (most recent call last):
  File "./bin/rmtoo", line 14, in <module>
    main(sys.argv[1:], sys.stdout, sys.stderr)
  File "/home/florath/devel/rmtoo/rmtoo-15/rmtoo/lib/RmtooMain.py", line 123, in main
    exitfun(not main_impl(args, mstdout, mstderr))
  File "/home/florath/devel/rmtoo/rmtoo-15/rmtoo/lib/RmtooMain.py", line 119, in main_impl
    return execute_cmds(opts, config, mods, mstdout, mstderr)
  File "/home/florath/devel/rmtoo/rmtoo-15/rmtoo/lib/RmtooMain.py", line 55, in execute_cmds
    reqs = rc.continuum_latest()
  File "/home/florath/devel/rmtoo/rmtoo-15/rmtoo/lib/ReqsContinuum.py", line 46, in continuum_latest
    return self.continuum[self.continuum_order[0]]
IndexError: list index out of range
make: *** [artifacts/.rmtoo_dependencies] Error 1

If this happens, please change the interval to ["FILES", "FILES"].


