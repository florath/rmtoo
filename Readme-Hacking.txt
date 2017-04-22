
This file is not completed now - any might be in future.

* Development Environment

** Tools

*** Mandatory
    There are some mandatory tools to do development for rmtoo:
    Debian 6: $ apt-get install make graphviz texlive-latex-extra

* Testing

** Comparing XML
   There are many files containing XML data.  These files are either
   generated directly inside the rmtoo's output module or with the
   help of an external library.

*** History
    For some time (until version 19) an external library was used to
    compare XML files.  This library called xmldiff has a major
    drawback: because it tries to generate the diff (what is much more
    than really needed) it is very time consuming for bigger files.  
    
    The manual page of xmldiff notes that you can typically diff
    documents with about 100 nodes with the help of this library.

    Because the runtime of the comparison which was about 20 minutes
    for some bigger document xmldiff was dropped and an own
    function for comparing XML documents was established.

*** Directly Generated Files
    Directly generated files are generated with the help of an output
    module directly.  In this case a simple compare should be enough.
    It is defined that not only the (sub-) nodes should be equal but
    also the order in which they appear.

* Forks

  There are a couple of forks done during the last years; have a look
  and cherry-pick the interesing things

  http://forked.yannick.io/florath/rmtoo

  apre/rmtoo 			0 	0 	0 	9 months ago -> GUI branch!
  andipla/rmtoo 		0 	2 	1 	5 months ago -> SIL feature

** Done

*** joesteeve/rmtoo
    2017-04-15
    Patch to run rmtoo in an virtualenv.

*** No changes
    The following forks include no changes

    CrypticGator/rmtoo		2017-04-15
    drewm135/rmtoo		2017-04-15
    thangphuocnguyen/rmtoo	2017-04-15
    isaacde/rmtoo		2017-04-15
    willtecti/rmtoo		2017-04-15
    LucasReller/rmtoo		2017-04-15
    albertogomcas/rmtoo		2017-04-15
    kevin-canadian/rmtoo	2017-04-15
    pnouvel/rmtoo		2017-04-15
    huddy1985/rmtoo		2017-04-15
    samjaninf/rmtoo		2017-04-15


* pypi upload

** testpypi
   $ python setup.py sdist upload -r testpypi

   $ python setup.py bdist_wheel --universal upload

   Install:
   pip install -i https://testpypi.python.org/pypi rmtoo

Local Variables:
mode:outline
End:
