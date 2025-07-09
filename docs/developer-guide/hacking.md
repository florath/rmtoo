# Development Guide

This guide covers setting up a development environment for rmToo and contributing to the project.

## Development Environment Setup

### Prerequisites

#### System Dependencies
```bash
# Debian/Ubuntu
sudo apt install -y make graphviz texlive-latex-extra
sudo apt install -y python3-dev python3-venv

# CentOS/RHEL
sudo yum install -y make graphviz texlive python3-devel

# Fedora
sudo dnf install -y make graphviz texlive python3-devel
```

#### Python Environment
```bash
# Clone the repository
git clone https://github.com/florath/rmtoo.git
cd rmtoo

# Create virtual environment
python3 -m venv dev-env
source dev-env/bin/activate

# Install in development mode
pip install -e .
```

### Environment Variables
```bash
export PYTHONPATH=${PWD}
```

## Testing

### Running Tests Locally

#### Full Test Suite
```bash
cd rmtoo
pytest --junit-xml=result.xml --cov-report term --cov-report xml --cov=lib --cov=inputs --cov=outputs tests
```

#### Specific Test Categories
```bash
# Unit tests only
pytest tests/RMTTest-Unit/

# Blackbox tests only
pytest tests/RMTTest-Blackbox/

# Output tests only
pytest tests/RMTTest-Output/

# Syntax tests only
pytest tests/RMTTest-Syntax/
```

#### Using tox (Recommended)
```bash
# Run tests for all supported Python versions
tox

# Run specific environment
tox -e py39
tox -e py310
tox -e py311

# Run linting
tox -e pep8
tox -e pylint
```

### Test Structure

rmToo uses pytest with specific naming conventions:
- **Test files**: `RMTTest*.py`
- **Test classes**: `RMTTest*`
- **Test methods**: `rmttest*`

#### Test Categories
- **Unit tests**: `tests/RMTTest-Unit/` - Core component testing
- **Blackbox tests**: `tests/RMTTest-Blackbox/` - Full integration tests
- **Output tests**: `tests/RMTTest-Output/` - Testing specific output formats
- **Syntax tests**: `tests/RMTTest-Syntax/` - Input syntax validation

### XML Comparison Testing

For output modules that generate XML, rmToo includes custom XML comparison utilities:

#### Background
- Until version 19, rmToo used the `xmldiff` library
- `xmldiff` was too slow for large documents (20+ minutes for big files)
- Custom XML comparison was implemented for better performance

#### Requirements
- Not only node content must match, but also order
- Supports both directly generated files and library-generated files

## Code Quality

### Linting
```bash
# Run flake8
flake8

# Run pylint
pylint rmtoo

# Using tox
tox -e pep8
tox -e pylint
```

### Code Coverage
```bash
# Generate coverage report
pytest --cov=lib --cov=inputs --cov=outputs --cov-report=html tests

# View coverage report
open htmlcov/index.html
```

## Contributing

### Development Workflow
1. **Fork the repository** on GitHub
2. **Create a feature branch**: `git checkout -b feature-name`
3. **Make your changes** and add tests
4. **Run the test suite**: `tox`
5. **Submit a pull request**

### Code Style
- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings for public functions and classes
- Keep functions small and focused

### Testing Requirements
- Add tests for new features
- Ensure all existing tests pass
- Maintain or improve code coverage
- Test on multiple Python versions using tox

## Architecture Overview

### Core Components
- **Input Plugins**: Parse requirement tags and dependencies
- **Output Plugins**: Generate different artifact formats
- **Analytics**: Quality checking modules
- **Configuration**: Hierarchical config system

### Plugin Development
See the [Plugin Development Guide](plugins/) for details on creating new input and output plugins.

## Release Process

### Building Packages
```bash
# Build source distribution
python setup.py sdist

# Build wheel
python setup.py bdist_wheel --universal
```

### Testing with TestPyPI
```bash
# Upload to TestPyPI
python setup.py sdist upload -r testpypi
python setup.py bdist_wheel --universal upload -r testpypi

# Install from TestPyPI
pip install -i https://testpypi.python.org/pypi rmtoo
```

## Community and Forks

### Notable Forks
Several forks have been created over the years. Some interesting ones to review:

- **apre/rmtoo**: GUI branch
- **andipla/rmtoo**: SIL (Safety Integrity Level) feature
- **joesteeve/rmtoo**: Virtualenv support (merged)

### Contributing Back
When reviewing forks, consider:
1. Cherry-picking useful features
2. Contacting fork maintainers
3. Coordinating integration efforts

## Getting Help

### Development Questions
- Check existing [GitHub issues](https://github.com/florath/rmtoo/issues)
- Review the [architecture documentation](architecture.md)
- Contact the maintainers: rmtoo@florath.net

### Documentation
- Update documentation when adding features
- Test documentation examples
- Follow the documentation style guide

## Tools and Resources

### Required Tools
- **make**: Build automation
- **graphviz**: Graph generation
- **texlive**: LaTeX processing
- **python3-dev**: Python development headers

### Optional Tools
- **tox**: Testing across Python versions
- **coverage**: Code coverage analysis
- **pytest**: Test runner
- **flake8**: Linting
- **pylint**: Advanced linting