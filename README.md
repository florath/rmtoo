[//]: # (copyright 2010-2012,2017,2020,2022,2025 by flonatel GmbH & Co. KG / Andreas Florath)
[//]: # ( )
[//]: # (SPDX-License-Identifier: GPL-3.0-or-later)
[//]: # ( )
[//]: # (This file is part of rmtoo.)
[//]: # ( )  
[//]: # (rmtoo is free software: you can redistribute it and/or modify)
[//]: # (it under the terms of the GNU General Public License as published by)
[//]: # (the Free Software Foundation, either version 3 of the License, or)
[//]: # (at your option any later version.)
[//]: # ( )
[//]: # (rmtoo is distributed in the hope that it will be useful,)
[//]: # (but WITHOUT ANY WARRANTY; without even the implied warranty of)
[//]: # (MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the)
[//]: # (GNU General Public License for more details.)
[//]: # ( )  
[//]: # (You should have received a copy of the GNU General Public License)
[//]: # (along with rmtoo.  If not, see <https://www.gnu.org/licenses/>.)

# rmToo

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

```bash
# Install rmToo
pip install rmtoo

# Create your first project
cp -r "$(rmtoo-contrib-dir)/template_project" MyProject
cd MyProject
source ./setenv.sh VENV
make

# View generated artifacts
ls artifacts/
```

## 📚 Documentation

**Complete documentation is available in the [`docs/`](docs/) directory:**

- **[📖 User Guide](docs/user-guide/)** - Installation, getting started, and usage
- **[🔧 Developer Guide](docs/developer-guide/)** - Contributing and development
- **[❓ FAQ](docs/faq.md)** - Frequently asked questions

### Quick Links

- **[Installation Guide](docs/user-guide/installation/)** - Install on Linux, macOS, or Windows
- **[Getting Started](docs/user-guide/getting-started/overview.md)** - Overview and features
- **[Requirements vs Constraints](docs/user-guide/requirements/constraints.md)** - Core concepts

## Platform Support

- **Linux**: Full support
- **macOS**: Community supported
- **Windows**: Community supported (via Cygwin or WSL)

## Key Features

- **Text-based requirements**: Use your favorite editor
- **Multiple output formats**: HTML, PDF, graphs, statistics
- **Git integration**: Full version control support
- **Quality analytics**: Automated requirement quality checks
- **Dependency management**: Automatic dependency tracking
- **Template projects**: Ready-to-use project templates

## Getting Help

- **Documentation**: See [`docs/`](docs/) directory
- **Issues**: [GitHub Issues](https://github.com/florath/rmtoo/issues)
- **Contact**: rmtoo@florath.net

## License

Copyright (c) 2010-2012,2017,2020,2022,2025 by flonatel GmbH & Co. KG

rmToo is free software licensed under the GNU General Public License v3.0 or later.
See [COPYING](COPYING) for details.