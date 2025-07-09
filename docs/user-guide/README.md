# User Guide

Complete guide to using rmToo effectively for requirements management.

## Installation

Install rmToo on your system:

- **[Linux Installation](installation/linux.md)** - Complete installation guide for Linux distributions
- **[macOS Installation](installation/macos.md)** - Installation using macports (community supported)
- **[Windows Installation](installation/windows.md)** - Installation using Cygwin or WSL (community supported)

## Getting Started

- **[Overview](getting-started/overview.md)** - What rmToo is and its unique features
- **[Requirements vs Constraints](requirements/constraints.md)** - Understanding the fundamental concepts

## Quick Start

1. **Install rmToo**:
   ```bash
   pip install rmtoo
   ```

2. **Create your first project**:
   ```bash
   cp -r "$(rmtoo-contrib-dir)/template_project" MyProject
   cd MyProject
   source ./setenv.sh VENV
   make
   ```

3. **View the generated artifacts**:
   ```bash
   ls artifacts/
   ```

## Key Concepts

### Requirements Management
rmToo uses a text-based approach where:
- Each requirement is stored in a separate `.req` file
- Requirements have tags like Name, Description, Status, Priority
- Dependencies are managed through `Solved by` relationships
- Constraints define limitations on the solution space

### Topics
- Topics organize requirements hierarchically
- Stored in `.tic` files 
- Provide structure for documentation output
- Support nested topic relationships

### Configuration
- JSON or YAML configuration files
- Control input sources, output formats, and processing options
- Support for variable substitution
- Hierarchical configuration merging

## Output Formats

rmToo can generate multiple output formats:
- **HTML documentation** with cross-references and navigation
- **LaTeX/PDF documents** for formal documentation
- **Dependency graphs** showing requirement relationships
- **Statistics and reports** for project tracking
- **Gantt charts** for project planning

## Basic Workflow

1. **Write requirements** in `.req` files using supported tags
2. **Organize with topics** in `.tic` files for hierarchical structure
3. **Configure outputs** in JSON/YAML configuration files
4. **Generate artifacts** using `make` or direct rmToo commands
5. **Review and iterate** on generated documentation

## Advanced Features

### Version Control Integration
- Git integration for requirement history
- Baseline management through version control
- Change tracking and impact analysis

### Quality Analytics
- Automated quality checks for requirements
- Metrics and statistics generation
- Consistency validation

### Extensibility
- Plugin architecture for custom inputs and outputs
- Custom analytics modules
- Integration with external tools

## Getting Help

- **[FAQ](../faq.md)** - Frequently asked questions and troubleshooting
- **[Developer Guide](../developer-guide/)** - For contributors and advanced users
- **Community**: [GitHub Issues](https://github.com/florath/rmtoo/issues)
- **Contact**: rmtoo@florath.net