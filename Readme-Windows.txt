
PLEASE NOTE: rmtoo WAS SUCCESSFULLY TESTED UNDER WINDOWS - 
BUT IT IS NOT OFFICIALLY SUPPORTED UNDER WINDOWS.

This document gives some hints to get rmtoo up and running 
under Windows.

* cygwin
  rmtoo was successfully tested using cygwin [1].  Please download the 
  cygwin setup.exe file and follow the install instructions.  Choose the 
  following additional packages:
  o gnuplot
  o make
  o tetex
  o python

* scipy
  To use most of the rmtoo statistic modules, you need numpy [3] and 
  scipy [4].
  There are reports that it is possible to run this under Windows -
  but it looks that this is not straight forward,
  There are also some insallable versions of numpy and scipy - but
  they do not work with cygwin. [5]

* graphviz
  Additionally the graphviz package must be installed [6]. This is not
  part of cygwin.  Download and install graphviz. 

  Before running 'make' please add the graphviz binaries to the path: 
  export PATH=$PATH:"/cygdrive/c/Program Files (x86)/Graphviz2.28/bin"
  (You might want to adapt the path to reflect your local directory
  structure and / or the current version.  Depending on the used cygwin
  the path might start with /cygwin and depending on the graphviz library
  the version might be different.)

If you have any additional hints for using rmtoo under Windows, please
contact me.

Andreas Florath
rmtoo@florath.net
2011-11-30

[1] http://cygwin.com/install.html
[2] http://www.python.org/download/releases/
[3] http://sourceforge.net/projects/numpy/
[4] http://sourceforge.net/projects/scipy/
[5] http://www.lfd.uci.edu/~gohlke/pythonlibs/
[6] http://www.graphviz.org/Download_windows.php
