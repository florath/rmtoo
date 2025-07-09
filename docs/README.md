# rmToo Documentation

Open Source Requirements Management Tool

[![image](https://img.shields.io/github/release/florath/rmtoo.svg)](https://github.com/florath/rmtoo/releases)
[![Build Status](https://github.com/florath/rmtoo/workflows/CI/badge.svg)](https://github.com/florath/rmtoo/actions)
[![image](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=florath_rmtoo&metric=coverage)](https://sonarcloud.io/summary/new_code?id=florath_rmtoo)
[![PyPI version](https://img.shields.io/pypi/v/rmtoo)](https://pypi.org/project/rmtoo/)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=florath_rmtoo&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=florath_rmtoo)

## What is rmToo?

rmToo is a free and open-source requirements management tool written in Python. It processes requirements and topics from text files and generates various artifacts like HTML documentation, LaTeX/PDF documents, dependency graphs, and statistical reports.

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

## Documentation Structure

### 📖 [User Guide](user-guide/)
Everything you need to know to use rmToo effectively:
- **[Installation](user-guide/installation/)** - Platform-specific installation guides
- **[Getting Started](user-guide/getting-started/)** - Your first steps with rmToo
- **[Configuration](user-guide/configuration/)** - Configure rmToo for your needs
- **[Requirements](user-guide/requirements/)** - Writing and managing requirements
- **[Topics](user-guide/topics/)** - Organizing requirements hierarchically
- **[Outputs](user-guide/outputs/)** - Generate documentation and reports
- **[Analytics](user-guide/analytics/)** - Quality checking and metrics

### 🔧 [Developer Guide](developer-guide/)
For contributors and plugin developers:
- **[Architecture](developer-guide/architecture.md)** - System design and components
- **[Plugin Development](developer-guide/plugins/)** - Creating input/output plugins
- **[Testing](developer-guide/testing.md)** - Running and writing tests
- **[Contributing](developer-guide/contributing.md)** - How to contribute to rmToo

### 📚 [Reference](reference/)
Detailed reference documentation:
- **[CLI Commands](reference/cli/)** - Command-line interface reference
- **[File Formats](reference/file-formats/)** - Requirements, topics, and config formats
- **[Configuration](reference/configuration/)** - All configuration options
- **[Analytics](reference/analytics/)** - Quality checking modules

### 💡 [Examples](examples/)
Real-world examples and templates:
- **[Template Project](examples/template-project/)** - Basic project structure
- **[Email Client](examples/email-client/)** - Complete example project

### 📝 [Changelog](changelog/)
Release notes and version history

### ❓ [FAQ](faq.md)
Frequently asked questions and troubleshooting

## Conventions

- `YY`: Version placeholder - replace with actual version number
- `$ cmd`: Command to type (don't include the `$` prompt)

## Platform Support

rmToo is fully supported on Linux and works on other platforms:
- **Linux**: Full support
- **macOS**: See [Installation - macOS](user-guide/installation/macos.md)
- **Windows**: See [Installation - Windows](user-guide/installation/windows.md)

## Getting Help

- **Documentation**: This documentation covers most use cases
- **Man Pages**: `man rmtoo` for overview, `man rmtoo-<topic>` for specifics
- **Issues**: [GitHub Issues](https://github.com/florath/rmtoo/issues)
- **Contact**: rmtoo@florath.net

## License

Copyright (c) 2010-2012,2017,2020,2022,2025 by flonatel GmbH & Co. KG

rmToo is free software licensed under the GNU General Public License v3.0 or later.
See [COPYING](../COPYING) for the license summary or [gpl-3.0.txt](../gpl-3.0.txt) for the full license text.