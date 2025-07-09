# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

rmToo is a free and open-source requirements management tool written in Python. It processes requirements and topics from text files and generates various artifacts like HTML documentation, LaTeX/PDF documents, dependency graphs, and statistical reports.

## General Important Rules

* Never implement any fallbacks or defaults. Fail early!
* Keep the source code and examples separate! Never ever use special example identifiers or behaviour in the source code.

## Common Development Commands

### Testing
```bash
# Run all tests with coverage
make tests

# Run tests using tox for multiple Python versions
tox

# Run specific test
cd rmtoo && pytest tests/RMTTest-Unit/RMTTest-Core/RMTTest-Requirement.py

# Run linting
tox -e pep8
tox -e pylint

# Run flake8 directly
flake8
```

Each run of rmtoo (with DEBUG enabled) creates a log file /tmp/rmtoo-<PID>.log.
The output including stdout and stderr of each run is in a directory /tmp/rmtoo-tst-*.

### Building and Installation
```bash
# Install in development mode
pip install -e .

# Build source distribution
python setup.py sdist

# Install from source
python setup.py install

# Install with prefix (used by Makefile)
python setup.py install --prefix=${DESTDIR}/usr --install-scripts=${DESTDIR}/usr/bin
```

### Example Project Workflow
```bash
# Set up template project using rmtoo-contrib-dir
cp -r "$(rmtoo-contrib-dir)/template_project" MyProject
cd MyProject
source ./setenv.sh VENV
make clean && make
```

### Using rmtoo-contrib-dir Command
```bash
# Get the contrib directory path
rmtoo-contrib-dir

# Copy template project to start a new project
cp -r "$(rmtoo-contrib-dir)/template_project" MyProject

# Access other contrib resources
ls "$(rmtoo-contrib-dir)"
gnuplot "$(rmtoo-contrib-dir)/gnuplot_stats_reqs_cnt.inc"
```

### Git / GitHub
* You can use "git" to check older versions.
* You can use "git" to commit after a step is done. This needs explicit confirmation by the user.
* You can use "gh" to check for open issues.
* You can use "gh api". Example: Dependabots alerts "gh api repos/florath/rmtoo/dependabot/alerts"

## Architecture Overview

### Core Data Flow
1. **Input Phase**: Requirements and topics parsed from .req/.tic files using input plugins
2. **Processing Phase**: TopicContinuumSet created with dependency resolution and validation
3. **Analytics Phase**: Quality analysis modules check requirement coherence and completeness
4. **Output Phase**: Multiple output formats generated in parallel (HTML, LaTeX, graphs, etc.)

### Plugin Architecture
- **Input Plugins** (`rmtoo/inputs/`): Parse requirement tags and dependencies (e.g., ReqName, ReqDescription, RDepDependsOn)
- **Output Plugins** (`rmtoo/outputs/`): Generate different artifact formats (html, latex2, graph2, xml1, etc.)
- **Plugin Loading**: Uses stevedore extension manager with entry points defined in setup.py

### Key Components
- **RmtooMain.py**: Main entry point and orchestration logic
- **TopicContinuumSet**: Version-controlled collection of requirements and topics
- **Configuration**: Hierarchical config system supporting JSON/YAML with variable substitution
- **Analytics**: Quality checking modules (DescWords, HotSpot, TopicCohe, ReqTopicCohe)

### Data Models
- **Requirement**: Individual requirement with tags, dependencies, and metadata
- **Topic**: Hierarchical container for requirements and subtopics
- **TopicContinuum**: Time-based versioning of topic collections

## File Structure Patterns

- `rmtoo/inputs/`: Input tag parsers (Req*, RDep*)
- `rmtoo/outputs/`: Output format generators
- `rmtoo/lib/`: Core library components
- `rmtoo/lib/storagebackend/`: Storage backend implementations (txtfile, yamlfile)
- `rmtoo/tests/`: Test suite (Unit, Blackbox, Output, Syntax)
- `doc/requirements/`: Example requirements files
- `contrib/template_project/`: Template for new projects

## Testing Approach

The project uses pytest with specific naming conventions:
- Test files: `RMTTest*.py`
- Test classes: `RMTTest*`
- Test methods: `rmttest*`

Test categories:
- **Unit tests**: `rmtoo/tests/RMTTest-Unit/` (Core, Analytics, Digraph, Tag, Topic, xmlcmp)
- **Blackbox tests**: `rmtoo/tests/RMTTest-Blackbox/` (Full integration tests with expected outputs)
- **Output tests**: `rmtoo/tests/RMTTest-Output/` (Testing specific output formats)
- **Syntax tests**: `rmtoo/tests/RMTTest-Syntax/` (Input syntax validation)

The tox configuration supports Python 3.8-3.13 and includes pep8/pylint environments.

## Configuration Files

Configuration uses hierarchical merging:
1. Default values
2. Config files (JSON/YAML)
3. Command line parameters

Supports variable substitution: `"${variable_name}"` and environment variables.

## Extension Development

### Adding Input Plugins
1. Create class in `rmtoo/inputs/` inheriting from appropriate base
2. Add entry point in setup.py under `rmtoo.input.plugin`
3. Implement required methods for tag parsing

### Adding Output Plugins  
1. Create class in `rmtoo/outputs/` inheriting from `ExecutorTopicContinuum`
2. Add entry point in setup.py under `rmtoo.output.plugin`
3. Implement lifecycle methods for artifact generation
