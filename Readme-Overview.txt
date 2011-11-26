--- Overview ---

rmtoo is a free and open source requirements management tool.

rmtoo uses a different approach than most other requirements
management tools: it comes as a command line tool which is optimized
for handling requirements. The power of rmtoo lies in the fact that
the development environment can handle the input and output files -
there is no need for a special tool set environment.

Example: if you need to handle baselines (and there often is), rmtoo
can be configured using a revision control system (e.g. git). The
revision control system can handle different revisions, baselining,
tagging, branching and many other things extremely well - there is no
reason to reinvent the wheel and making it less efficient.

Let one thing do one thing.


--- Unique Feature Set ---

rmtoo fits perfectly in a development environment using text editors
and command line tools such as emacs, vi, eclipse, make, maven. 

o Use simple text files as input - use your favorite editor
o Many different output formats and artifacts are supported:
  * PDF - with links to dependent requirements
  * HTML - also with links to dependent requirements
  * Requirements dependency graph
  * Requirement count history graph
  * Lists of unfinished requirements including priority and effort
    estimation - e.g. for use in agile project development 
o Fully integrated revision control system: git. Usages: history,
  statistics and baseline handling. 
o A topic based output handling provides a common set of files for
  different types of output (PDF, HTML, ...) 
o Complete support for automatic checking of constraints.
o Analytics modules: Heuristics help to evaluate the quality of
  requirements 
o Modules to support commercial biddings based on a given set of
  requirements 
o Emacs mode files for editing requirements and topics included
o Experimental output in XML
o Fully integrated with Makefile handling of all artifacts
o Fully modular design: additional output requires minimal effort
o During parsing most common problems are detected: all syntax errors
  and also many semantic errors. 
o Fully automated test environment - tests about 95% of the code and
  is shipped with rmtoo packages to check for possible problems in
  different environments. 

rmtoo is not a fully integrated, tries-to-do-everything tool with a
colorful GUI or different database backends. 
