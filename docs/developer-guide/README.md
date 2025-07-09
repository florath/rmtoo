# Developer Guide

Complete guide for rmToo developers, contributors, and advanced users.

## Getting Started

### Development Setup
- **[Development Environment](hacking.md)** - Setting up your development environment
- **[Contributing](contributing.md)** - How to contribute to rmToo
- **[Self-Hosting](self-hosting.md)** - Running rmToo on rmToo's own requirements

### Planning and Vision
- **[Roadmap](roadmap.md)** - Future development plans and features
- **[Internal Notes](internal-notes.md)** - Development tracking and conventions

## Architecture Overview

### Core Components
rmToo follows a plugin-based architecture:

#### Input Processing
- **Input Plugins**: Parse requirement tags and dependencies (e.g., ReqName, ReqDescription, RDepDependsOn)
- **Storage Backend**: Support for text files and YAML formats
- **Validation**: Syntax and semantic error checking

#### Processing Engine
- **TopicContinuumSet**: Version-controlled collection of requirements and topics
- **Dependency Resolution**: Automatic dependency graph creation
- **Analytics**: Quality checking modules (DescWords, HotSpot, TopicCohe, ReqTopicCohe)

#### Output Generation
- **Output Plugins**: Generate different artifact formats (html, latex2, graph2, xml1, etc.)
- **Template System**: Jinja2-based template processing
- **Multi-format Support**: Parallel generation of multiple output types

### Plugin Architecture
All plugins are registered through setuptools entry points:

```python
entry_points={
    'rmtoo.input.plugin': [
        'ReqName = rmtoo.inputs.ReqName:ReqName',
        # ...
    ],
    'rmtoo.output.plugin': [
        'html = rmtoo.outputs.html:html',
        # ...
    ],
}
```

## Development Workflow

### Setting Up Development Environment
1. Clone the repository
2. Create virtual environment
3. Install in development mode: `pip install -e .`
4. Run tests: `tox` or `pytest`

### Making Changes
1. Create feature branch
2. Implement changes with tests
3. Run full test suite
4. Submit pull request

### Testing
- **Unit Tests**: Core component testing
- **Blackbox Tests**: Full integration testing
- **Output Tests**: Format-specific validation
- **Syntax Tests**: Input validation

Run tests with: `tox` (recommended) or `pytest`

### Code Quality
- Follow PEP 8 standards
- Use meaningful names
- Add docstrings for public interfaces
- Include type hints where appropriate

## Extending rmToo

### Adding Input Plugins
1. Create class in `rmtoo/inputs/` inheriting from appropriate base
2. Add entry point in setup.py
3. Implement required methods for tag parsing
4. Add tests

### Adding Output Plugins
1. Create class in `rmtoo/outputs/` inheriting from `ExecutorTopicContinuum`
2. Add entry point in setup.py
3. Implement lifecycle methods for artifact generation
4. Add tests

### Configuration System
- Hierarchical configuration merging
- JSON/YAML format support
- Variable substitution: `"${variable_name}"`
- Environment variable support

## Key Development Areas

### Quality Assurance
- Comprehensive test coverage (95%+)
- Multiple Python version support (3.8-3.13)
- Continuous integration with GitHub Actions
- Code quality monitoring with SonarCloud

### Performance Considerations
- Efficient dependency graph processing
- Optimized template rendering
- Memory-conscious large requirement set handling

### Compatibility
- Cross-platform support (Linux, macOS, Windows)
- Multiple Python versions
- Backward compatibility maintenance

## Getting Help

### Development Resources
- **GitHub Repository**: [florath/rmtoo](https://github.com/florath/rmtoo)
- **Issues**: [GitHub Issues](https://github.com/florath/rmtoo/issues)
- **Contact**: rmtoo@florath.net

### Documentation
- Man pages: `man rmtoo`
- Code documentation: Well-documented source code
- Example projects: Template project and email client example

## Contributing

We welcome contributions! Please:
1. Read the [Contributing Guide](contributing.md)
2. Set up your [Development Environment](hacking.md)
3. Follow our coding standards
4. Include tests with your changes
5. Submit pull requests for review

Ready to contribute? Start with the [Contributing Guide](contributing.md)!