# Development Roadmap

This is a description of the next and next-next generation features to be implemented in rmToo.

## Important Notes

- **No exact timeline**: The amount of time spent on this tool varies depending on many factors
- **Version numbers may change**: Customer requests and bug fixes may affect the roadmap
- **Bug-fix releases**: May be released between major versions
- **Historical context**: The history of implemented features can be found in the release notes

## Current Focus Areas

### Version 24+ Features
- Create ready-to-use VM for AWS EC2
- Include requirements of rmToo and EMailClient into Python package
- Fix: Emacs highlighting on GUI VM

## High Priority Features

### GUI Development
**Status**: Design phase

- **Server component**: Backend service for requirements management
- **Client applications**: Multiple client interfaces
- **Protocol/Interface**: Communication layer between server and clients
- **Requirements**: Add requirements from roadmap to main project

### Module Unification
**Goal**: Modules should run (at least partially) for topic-based output
- Investigate ways to unify processing approaches
- Improve consistency across output formats

## Future Features

### User Interface Enhancements
- **GUI for configuration**: Visual configuration editor
- **Tasks/Issues support**: Integration with issue tracking
  - Possible Bugzilla import capability
- **Web interface**: Browser-based requirements management

### Documentation and Help
- **Enhanced man pages**: Complete documentation for all commands
  - graph and graph2 commands
  - EfEU (Effort Estimation Unit) commands
- **FAQ improvements**: Add max level of topic inclusion
- **Presentation updates**: Include latest changes

### Testing and Quality
- **More test cases**: Expand test coverage
- **Archive management**: Maintain version history
- **Quality improvements**: Address user-reported issues

### Advanced Features

#### SCRUM and Agile Support
- **Burndown diagrams**: Sprint progress visualization
- **Gantt chart integration**: Use finished date and duration data
- **Due dates**: Optional due dates for requirements
- **Requirement states**: Add postponed and withdrawn states

#### Enhanced Output Formats
- **Sub-graphs in documentation**: Include detailed dependency graphs
  - Topic-based graphs (all requirements of a topic)
  - Requirement-based graphs (dependencies for specific requirements)
- **Dot file integration**: Generic way to include graphviz files
- **Change tracking**: Mark additions, changes, and deletions between versions

#### Requirements Management Features
- **Requirement states**: Enhanced status tracking
  - Postponed requirements
  - Withdrawn requirements
- **Traceability**: Track requirement changes and impacts
- **Dependency analysis**: List all dependent requirements for changes

### Long-term Vision

#### Data Storage and Access
**Focus**: Define who can access (read, write, change) which data

Key considerations:
- **Write requirements**: Define data access patterns
- **Collaborate with other projects**: Integration with ganttproject, freemind, etc.
- **Architecture decisions**: Storage vs. Bus-System approach
- **Availability**: System availability requirements
- **Fault tolerance**: Failure handling and recovery
- **Collaboration**: Multi-user support
- **Concurrency**: Simultaneous access handling

#### Internationalization
- **Multi-language support**: Define new tag sets for each language
- **Translation framework**: Support for localized content
- **Cultural considerations**: Adapt to different regional requirements

#### Advanced Analytics
- **Change impact analysis**: Understand ripple effects of changes
- **Requirement quality metrics**: Automated quality assessment
- **Statistical analysis**: Trend analysis and projections
- **Predictive modeling**: Forecast project completion

## Technical Improvements

### Build System
- **Makefile dependencies**: Improve dependency tracking
- **Configuration dependencies**: Link .rmtoo_dependencies to ConfigX.py
- **Output level configuration**: Make prios.py output level configurable

### Code Quality
- **Clean up code**: Address XXX and TODO comments
- **Use MemLog**: Replace print statements with proper logging
- **Version information**: Add version number to rmtoo -v command

### Feature Completeness
- **Roadmap feature**: Self-hosting roadmap management
- **TODO list feature**: Integrated task management
- **Glossary support**: Complete glossary implementation
- **Emacs mode**: Topic (.tic) file editing support

## Integration Ideas

### External Tool Integration
- **Version control**: Enhanced git integration
- **Build systems**: Better CI/CD integration
- **Testing frameworks**: Automated requirement verification
- **Documentation tools**: Integration with documentation generators

### API Development
- **RESTful API**: Programmatic access to requirements
- **Plugin system**: Third-party extension support
- **Import/Export**: Data exchange with other tools
- **Notification system**: Change notifications and alerts

## Community and Ecosystem

### Package Management
- **Distribution packages**: Maintain packages for major distributions
- **Container support**: Docker and container deployment
- **Cloud deployment**: Cloud-native deployment options

### Documentation
- **User tutorials**: Step-by-step guides for common use cases
- **Video tutorials**: Visual learning resources
- **Best practices**: Documented patterns and approaches
- **Case studies**: Real-world usage examples

## Philosophy and Design Principles

### Unix Philosophy
Following the Unix principle: "let one thing do one thing (but this very well)"

**Current approach**:
- Plain text files for input/output
- Command-line tools for processing
- Interoperability with standard tools

**Challenges in requirements management**:
- Complex data structures
- Proprietary file formats
- Limited program interoperability
- Data ownership issues

### Interoperability Goals
- **Data preservation**: Programs should not lose unknown data
- **Format stability**: Consistent data representation
- **Tool independence**: Avoid vendor lock-in
- **Standard compliance**: Use open formats where possible

## Contributing to the Roadmap

### How to Influence Development
1. **Report bugs**: Use GitHub issues for bug reports
2. **Feature requests**: Propose new features with use cases
3. **Code contributions**: Submit pull requests for improvements
4. **Documentation**: Help improve documentation and examples
5. **Testing**: Contribute test cases and validation

### Priority Factors
- **User demand**: Features requested by multiple users
- **Technical complexity**: Implementation difficulty
- **Compatibility**: Impact on existing functionality
- **Maintenance**: Long-term maintenance requirements

## Getting Involved

### For Users
- **Feedback**: Share your experience and suggestions
- **Testing**: Help test new features and releases
- **Documentation**: Contribute examples and use cases
- **Community**: Help other users in forums and discussions

### For Developers
- **Code review**: Participate in code reviews
- **Architecture**: Contribute to design discussions
- **Implementation**: Help implement roadmap features
- **Testing**: Develop and maintain test suites

## Contact and Communication

- **GitHub Issues**: Feature requests and bug reports
- **Mailing List**: rmtoo@florath.net
- **Documentation**: Contribute to docs and examples
- **Community**: Join discussions and help others

---

*This roadmap is a living document that evolves based on user needs, technical constraints, and available resources. For the most current information, check the project repository and recent release notes.*