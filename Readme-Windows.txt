
rmtoo can be used under Windows.

It was successfully tested using cygwin [1].  Please download the
cygwin setup.exe file and follow the install instructions.  Choose the 
following additional packages:
o gnuplot
o make
o tetex
o python

Additionally the graphviz package must be installed [2]. This is not
part of cygwin.  Download and install graphviz. 

Before running 'make' please add the graphviz binaries to the path: 
export PATH=$PATH:/cygwin/c/Program Files(x86)/Graphviz2.26.2/bin
(You might want to adapt the path to reflect your local directory
structure.)

If you have any additional hints for using rmtoo under Windows, please
contact me.

Andreas Florath
sf@flonatel.org
2011-05-14


[1] http://cygwin.com/install.html
[2] http://www.graphviz.org/Download_windows.php