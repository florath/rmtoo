# Contributing to rmToo

We'd love to accept your patches and contributions to this project. There are just a few small guidelines you need to follow.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally
3. **Set up the development environment** (see [Development Guide](hacking.md))
4. **Create a feature branch** for your changes
5. **Make your changes** and add tests
6. **Submit a pull request**

## Contributor License Agreement

When you actively push changes to one of our development platforms (e.g., using a pull or merge request), you agree that your contribution is placed under GPL3 for the complete project - except the contents of the `contrib/template_project` folder which is placed under Apache 2 license.

## Code Requirements

### License Headers
New files must include an appropriate license header including the SPDX license identifier:

```python
# Copyright (c) 2025 by Your Name
# 
# SPDX-License-Identifier: GPL-3.0-or-later
#
# This file is part of rmtoo.
#
# rmtoo is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# rmtoo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with rmtoo.  If not, see <https://www.gnu.org/licenses/>.
```

### Code Style
- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings for public functions and classes
- Keep functions small and focused
- Add type hints where appropriate

### Testing
- Add tests for new features
- Ensure all existing tests pass
- Maintain or improve code coverage
- Test on multiple Python versions using tox

## Development Workflow

### 1. Setting Up Development Environment

```bash
# Clone your fork
git clone https://github.com/your-username/rmtoo.git
cd rmtoo

# Create virtual environment
python3 -m venv dev-env
source dev-env/bin/activate

# Install in development mode
pip install -e .
```

### 2. Making Changes

```bash
# Create a feature branch
git checkout -b feature-your-feature-name

# Make your changes
# ... edit files ...

# Add tests
# ... add or update tests ...

# Run tests
tox

# Run linting
tox -e pep8
tox -e pylint
```

### 3. Testing Your Changes

```bash
# Run full test suite
tox

# Run specific test categories
pytest tests/RMTTest-Unit/
pytest tests/RMTTest-Blackbox/
pytest tests/RMTTest-Output/

# Check code coverage
pytest --cov=lib --cov=inputs --cov=outputs --cov-report=html tests
```

### 4. Submitting Changes

```bash
# Commit your changes
git add .
git commit -m "Add feature: brief description"

# Push to your fork
git push origin feature-your-feature-name

# Create pull request on GitHub
```

## Types of Contributions

### Bug Fixes
- Include a clear description of the bug
- Add a test case that reproduces the issue
- Ensure the fix doesn't break existing functionality

### New Features
- Discuss the feature in an issue first
- Include comprehensive tests
- Update documentation as needed
- Follow the existing architecture patterns

### Documentation
- Fix typos and improve clarity
- Add examples and use cases
- Update outdated information
- Follow the documentation style guide

### Plugin Development
- See the [Plugin Development Guide](plugins/)
- Follow the plugin architecture patterns
- Include tests and documentation
- Register plugins in setup.py

## Code Review Process

### Pull Request Requirements
1. **Clear description** of what the PR does
2. **Tests** that verify the functionality
3. **Documentation** updates if needed
4. **All tests pass** in CI
5. **Code follows** style guidelines

### Review Criteria
- Code quality and maintainability
- Test coverage and quality
- Documentation completeness
- Compatibility with existing features
- Performance implications

## Architecture Guidelines

### Plugin System
- Use the existing plugin architecture
- Follow the stevedore extension patterns
- Add entry points in setup.py
- Include proper error handling

### Configuration
- Use the hierarchical configuration system
- Support both JSON and YAML formats
- Include proper validation
- Document configuration options

### Output Formats
- Extend ExecutorTopicContinuum for output plugins
- Support the standard lifecycle methods
- Include proper error handling
- Add comprehensive tests

## Getting Help

### Development Questions
- Check existing [GitHub issues](https://github.com/florath/rmtoo/issues)
- Review the [architecture documentation](architecture.md)
- Ask questions in pull requests
- Contact maintainers: rmtoo@florath.net

### Resources
- [Development Guide](hacking.md)
- [Plugin Development](plugins/)
- [Testing Guide](testing.md)
- [Architecture Overview](architecture.md)

## Community Guidelines

### Be Respectful
- Treat all contributors with respect
- Provide constructive feedback
- Help newcomers get started
- Follow the code of conduct

### Communication
- Use clear and concise language
- Explain your reasoning
- Be patient with questions
- Share knowledge and resources

## Recognition

All contributors are acknowledged in the project's release notes and documentation. Thank you for helping make rmToo better!

## License

By contributing, you agree that your contributions will be licensed under the GPL-3.0-or-later license, except for contributions to the `contrib/template_project` folder which are licensed under Apache 2.0.