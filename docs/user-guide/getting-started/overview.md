# Overview

rmToo is a free and open source requirements management tool that takes a unique approach to requirements management.

## Philosophy

rmToo uses a different approach than most other requirements management tools: it comes as a command line tool which is optimized for handling requirements. The power of rmToo lies in the fact that the development environment can handle the input and output files - there is no need for a special tool set environment.

**Example**: If you need to handle baselines (and there often is), rmToo can be configured using a revision control system (e.g. git). The revision control system can handle different revisions, baselining, tagging, branching and many other things extremely well - there is no reason to reinvent the wheel and making it less efficient.

**Let one thing do one thing.**

## Unique Feature Set

rmToo fits perfectly in a development environment using text editors and command line tools such as emacs, vi, eclipse, make, maven.

### Input and Output
- **Simple text files as input** - use your favorite editor
- **Many different output formats and artifacts are supported**:
  - PDF - with links to dependent requirements
  - HTML - also with links to dependent requirements
  - Requirements dependency graph
  - Requirement count history graph
  - Lists of unfinished requirements including priority and effort estimation - e.g. for use in agile project development

### Version Control Integration
- **Fully integrated revision control system**: git
- **Usages**: history, statistics and baseline handling

### Organization and Quality
- **Topic based output handling** provides a common set of files for different types of output (PDF, HTML, ...)
- **Complete support for automatic checking of constraints**
- **Analytics modules**: Heuristics help to evaluate the quality of requirements
- **Modules to support commercial biddings** based on a given set of requirements

### Development Features
- **Emacs mode files** for editing requirements and topics included
- **Experimental output in XML**
- **Fully integrated with Makefile** handling of all artifacts
- **Fully modular design**: additional output requires minimal effort
- **During parsing most common problems are detected**: all syntax errors and also many semantic errors
- **Fully automated test environment** - tests about 95% of the code and is shipped with rmToo packages to check for possible problems in different environments

## What rmToo Is Not

rmToo is not a fully integrated, tries-to-do-everything tool with a colorful GUI or different database backends. It focuses on doing requirements management well in a text-based, command-line environment that integrates with your existing development workflow.