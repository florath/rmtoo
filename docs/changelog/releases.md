# Release Notes

## Version 26.0.0 (January 2025)

*Release Date: January 2025*

This release represents over 4 years of continuous development and modernization efforts since rmToo 25.0.0 (August 2020). The focus has been on improving usability, expanding platform support, enhancing security, and modernizing the development infrastructure.

### 🎉 Major New Features

#### New rmtoo-contrib-dir Command
- **New command**: `rmtoo-contrib-dir` provides reliable access to contrib directory
- **Cross-platform**: Works consistently across pip, system packages, and development installs
- **Template project access**: `cp -r "$(rmtoo-contrib-dir)/template_project" MyProject`
- **Replaces manual path finding**: No more hunting for contrib files after installation

#### YAML File Format Support
- **YAML storage backend**: Full support for YAML format in requirements and topics
- **Simplified configuration**: YAML provides cleaner, more readable configuration files
- **Backwards compatible**: Existing text-based files continue to work

### 🐍 Python Support Updates

#### Expanded Python Version Support
- **Added support for**: Python 3.8, 3.9, 3.10, 3.11, 3.12, 3.13
- **Modernized codebase**: Removed Python 2 compatibility layers
- **Removed legacy dependencies**: Eliminated `six` and `future` libraries
- **Native Python 3**: Full migration to Python 3 native methods and imports

### 🔧 Development Infrastructure

#### Modern CI/CD Pipeline
- **GitHub Actions**: Replaced Travis CI with GitHub Actions
- **Multi-version testing**: Automated testing across Python 3.8-3.13
- **Automated releases**: New release workflow with PyPI publishing
- **Quality assurance**: SonarCloud integration for code quality monitoring

#### Enhanced Testing
- **YAML storage backend tests**: Comprehensive unit tests for YAML functionality
- **Improved coverage**: Enhanced test coverage reporting
- **Better test isolation**: Improved test environment setup

### 🛡️ Security Improvements

#### Security Vulnerability Fixes
- **GitPython update**: Fixed security vulnerabilities by updating to GitPython 3.1.41
- **Jinja2 security**: Fixed auto-escaping security issue in LatexJinja2 output
- **Logging security**: Fixed security issue with publicly writable directory usage in logging

### 📚 Documentation & Usability

#### Updated Documentation
- **Modern README**: Converted from RST to Markdown with updated examples
- **Command examples**: All examples now use `rmtoo-contrib-dir` command
- **Installation guide**: Updated installation instructions with current best practices
- **Man pages**: Updated all man pages to reference new commands and workflows

#### Template Project Improvements
- **Easier access**: Use `rmtoo-contrib-dir` for reliable template project location
- **Updated examples**: All documentation examples use the new command
- **Cross-platform consistency**: Same commands work on Windows, macOS, and Linux

### 🔧 Technical Improvements

#### Code Quality
- **Dependency cleanup**: Removed unused dependencies and legacy code
- **Refactoring**: Eliminated duplicate code in LaTeX output classes
- **Bug fixes**: Fixed syntax errors in tracer reconfiguration and logging
- **Modernization**: Updated code to use modern Python 3 idioms

#### Build System
- **Improved packaging**: Enhanced setup.py with better metadata
- **Release automation**: Streamlined release process with GitHub Actions
- **PyPI publishing**: Automated PyPI package publishing

### 🐛 Bug Fixes

#### Documentation Fixes
- **Status requirement**: Fixed incomplete Status requirement documentation in man pages
- **Broken links**: Removed links to non-existing web pages
- **Header updates**: Updated copyright headers to reflect current year

#### Configuration Fixes
- **Tracer logging**: Fixed tracer logging configuration not being applied
- **YAML parsing**: Improved YAML file parsing and error handling

#### Statistics and Estimation Fixes
- **Date overflow error**: Fixed crash when linear regression produces unrealistic end date estimates
- **Variable name collision**: Fixed bug in statistics calculation where loop variables conflicted
- **Gradient bounds checking**: Added validation for extremely small gradients indicating no meaningful progress

### 🔄 Migration Guide

#### For Existing Users
- **No breaking changes**: All existing functionality continues to work
- **Optional upgrades**: You can gradually adopt new features like YAML and `rmtoo-contrib-dir`
- **Template projects**: Update your scripts to use `rmtoo-contrib-dir` for future compatibility

#### For New Users
- **Easier installation**: `pip install rmtoo` now works more reliably
- **Simpler setup**: Use `rmtoo-contrib-dir` to find templates and resources
- **Better documentation**: Updated guides and examples throughout

### 📊 Statistics
- **55+ commits** since version 25.0.0
- **4+ years** of continuous development
- **6 new Python versions** supported (3.8-3.13)
- **Multiple security fixes** and improvements
- **Enhanced testing** across all supported platforms

---

## Version 25.0.1 (August 2020)

### User Visible Changes
- Added the long_description for PyPI

---

## Version 25.0.0 (August 2020)

### User Visible Changes
- **Drop support for Python 2** - which is EOL
- **Include support/tests for all currently supported Python versions**: 3.5, 3.6, 3.7, 3.8
- **Effort estimation**: Introduce flag to allow any value for the effort estimation

---

## Historical Releases

For detailed information about releases prior to 25.0.0, see the individual release notes in the `doc/release_notes/` directory:

- [Version 24](../doc/release_notes/24.rst)
- [Version 23](../doc/release_notes/23.txt)
- [Version 22](../doc/release_notes/22.txt)
- [Version 21](../doc/release_notes/21.txt)
- [Version 20](../doc/release_notes/20.txt)
- [Version 19](../doc/release_notes/19.txt)
- [Version 18](../doc/release_notes/18.txt)
- [Version 17](../doc/release_notes/17.txt)
- [Version 16](../doc/release_notes/16.txt)
- [Version 15](../doc/release_notes/15.txt)
- [Version 14](../doc/release_notes/14.txt)
- [Version 13](../doc/release_notes/13.txt)
- [Version 12](../doc/release_notes/12.txt)
- [Version 11](../doc/release_notes/11.txt)
- [Version 10](../doc/release_notes/10.txt)
- [Version 9](../doc/release_notes/09.txt)
- [Version 8](../doc/release_notes/08.txt)
- [Version 7](../doc/release_notes/07.txt)
- [Version 6](../doc/release_notes/06.txt)
- [Version 5](../doc/release_notes/05.txt)
- [Version 4](../doc/release_notes/04.txt)
- [Version 3](../doc/release_notes/03.txt)
- [Version 2](../doc/release_notes/02.txt)

## 🙏 Acknowledgments

Thanks to all contributors who helped improve rmToo over the years through bug reports, feature suggestions, and code contributions.

---

*For detailed technical changes, see the git commit history. For questions or support, visit the [project repository](https://github.com/florath/rmtoo).*