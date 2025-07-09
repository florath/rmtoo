# Internal Development Notes

This document contains internal notes and information for rmToo developers.

## Development Tracking

### Exception Numbers
The project maintains internal tracking numbers for exceptions and error codes. The current status is tracked in development files for consistency across the codebase.

**Current Status**: Next free exception number: 118

This helps ensure that error codes and exception identifiers don't conflict across different parts of the system.

## Development Conventions

### Error Code Management
- Exception numbers are assigned sequentially
- Developers should use the next available number when creating new exceptions
- Update the tracking file when assigning new numbers
- Document exception purposes for future reference

### Code Organization
- Maintain consistency in error handling
- Use standard exception types where appropriate
- Follow Python exception handling best practices
- Include meaningful error messages

## Internal File Organization

### Development Files
The project includes various internal files for development tracking:
- Exception number tracking
- Development notes
- Internal documentation
- Build system helpers

### Maintenance
- Keep internal tracking files up to date
- Review and clean up obsolete tracking information
- Maintain consistency across development team
- Document significant changes

## For Contributors

### When Adding New Exceptions
1. Check the current next available number
2. Use the next sequential number for your exception
3. Update the tracking file with the new next number
4. Document the exception purpose
5. Follow project coding standards

### Development Best Practices
- Use meaningful exception names
- Include helpful error messages
- Follow the established numbering system
- Update documentation as needed

## See Also

- [Contributing Guide](contributing.md) - How to contribute to rmToo
- [Development Guide](hacking.md) - Setting up development environment