# Running rmToo on rmToo

rmToo uses rmToo for its own requirements management, making it a great example of the tool's capabilities.

## Overview

Because rmToo uses rmToo for requirements management, it is possible to use rmToo as an example for rmToo's features. The rmToo project itself contains requirements files that demonstrate real-world usage patterns.

## Optional Documentation Generation

**Note**: The following procedure is optional and not needed for using rmToo in your projects.

### Purpose

When you want to create all the documentation for rmToo itself, you can execute the steps described in this section. This is useful for:
- Understanding how rmToo works internally
- Seeing a complete example of a requirements management project
- Contributing to rmToo development

### Using the Source Package

If you're using the source/tar ball distribution:

```bash
# Set up environment
source setenv.sh

# Build all documentation
make

# Run tests
make tests
```

The configuration files for output artifacts are located in `doc/requirements/ConfigX.py`.
All created documents are stored in the `artifacts/` directory.

### Using the Debian Package

If you're using the Debian package:

```bash
# Navigate to the rmToo directory
cd /usr/share/pyshared/rmtoo

# Run tests
nosetests -v -s
```

**Note**: Some test cases will fail because they assume that there is a git history available, which is not included in the package.

The generated documents can be found under `/usr/share/doc/rmtoo`.

## Version Control History

rmToo is by default configured to create the complete history of rmToo requirements itself. When using the tar ball or Debian package, the git history is not available.

### Common Error

You might encounter an error like:

```
Traceback (most recent call last):
  File "./bin/rmtoo", line 14, in <module>
    main(sys.argv[1:], sys.stdout, sys.stderr)
  File "/path/to/rmtoo/lib/RmtooMain.py", line 123, in main
    exitfun(not main_impl(args, mstdout, mstderr))
  File "/path/to/rmtoo/lib/RmtooMain.py", line 119, in main_impl
    return execute_cmds(opts, config, mods, mstdout, mstderr)
  File "/path/to/rmtoo/lib/RmtooMain.py", line 55, in execute_cmds
    reqs = rc.continuum_latest()
  File "/path/to/rmtoo/lib/ReqsContinuum.py", line 46, in continuum_latest
    return self.continuum[self.continuum_order[0]]
IndexError: list index out of range
make: *** [artifacts/.rmtoo_dependencies] Error 1
```

### Solution

If this happens, change the version control interval configuration to `["FILES", "FILES"]` in your configuration file. This tells rmToo to use file-based processing instead of git history.

## Learning from the Example

### Requirements Structure

The rmToo project includes:
- **Requirements files**: Located in `doc/requirements/`
- **Topics files**: Located in `doc/topics/`
- **Configuration files**: Various `Config*.py` files
- **Generated artifacts**: HTML, LaTeX, graphs, and statistics

### Key Features Demonstrated

1. **Hierarchical requirements organization**
2. **Dependency management between requirements**
3. **Multiple output formats (HTML, PDF, graphs)**
4. **Quality analytics and statistics**
5. **Version control integration**
6. **Constraint checking**

### Study Areas

When exploring rmToo's self-hosted requirements:

1. **Requirement writing patterns**: Look at how requirements are structured
2. **Dependency relationships**: Study how requirements depend on each other
3. **Topic organization**: See how requirements are grouped into topics
4. **Configuration examples**: Learn from real configuration files
5. **Output customization**: Examine how different outputs are configured

## Development Workflow

### Making Changes

When contributing to rmToo:

1. **Modify requirements**: Edit `.req` files in `doc/requirements/`
2. **Update topics**: Edit `.tic` files in `doc/topics/`
3. **Regenerate documentation**: Run `make` to update artifacts
4. **Test changes**: Run `make tests` to verify everything works
5. **Review artifacts**: Check generated HTML, PDF, and graphs

### Configuration Files

rmToo uses multiple configuration files:
- `doc/requirements/Config*.py`: Different configurations for different output sets
- Each configuration demonstrates different features and output combinations

## Benefits of Self-Hosting

1. **Real-world example**: See how rmToo is used in practice
2. **Feature demonstration**: All major features are used in the project
3. **Quality assurance**: The tool is tested on itself
4. **Documentation by example**: Learn by seeing actual usage
5. **Continuous validation**: Changes are tested against the tool itself

## GitPython Integration

**Historical Note**: Starting with rmToo version 11, GitPython was shipped with rmToo. The API of GitPython changed rapidly at that time, with three different APIs available. The plan was to remove the bundled GitPython once the API stabilized and use the OS/distribution version instead.

GitPython is used for:
- Version control integration
- Historical analysis
- Baseline management
- Change tracking

For more information about GitPython, see the [GitPython project page](https://github.com/gitpython-developers/GitPython).

## Next Steps

After exploring rmToo's self-hosted requirements:

1. **Create your own project**: Use the template project as a starting point
2. **Apply learned patterns**: Use the patterns you observed in rmToo
3. **Customize for your needs**: Adapt the configuration and structure
4. **Contribute improvements**: Help improve rmToo based on your experience