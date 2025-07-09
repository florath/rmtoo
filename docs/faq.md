# Frequently Asked Questions

## Getting Started with rmToo

### What is the input file format?

The file should be plain text containing a sequence of details. Each detail is a group of lines in `name: value` pairs. For multiline values, indent by one space on the lines after the first. You can leave blank lines between requirements for readability.

For detailed information, see the [Requirements Format](reference/file-formats/requirements.md) documentation.

### What tags are supported?

Currently the following tags are supported:
- **Class** - `implementable` or `detailable`
- **Solved by** - Dependencies to other requirements
- **Description** - Detailed description of the requirement
- **Effort estimation** - Symbolic effort points (SCRUM-style)
- **Invented by** - Author of the requirement
- **Invented on** - Date of creation
- **Name** - Requirement name/title
- **Owner** - Person responsible for the requirement
- **Priority** - Priority level
- **Rationale** - Justification for the requirement
- **Status** - `not done` or `finished`
- **Type** - `master requirement`, `requirement`, or `design decision`

For detailed semantics, see the [Requirements Format](reference/file-formats/requirements.md) documentation.

### Can I split a large set of requirements into separate files?

You must - each requirement must go in one file. This is a core design principle of rmToo.

### Does a requirement have a unique ID?

Yes - each requirement has an ID which is the case-sensitive name of the file where it's described, without the suffix.

**Example**: file name `OutputPrio.req` → ID `OutputPrio`

### Are there guidelines for requirement IDs?

- Write a unique phrase, the shorter the better
- You can use numbers if you want
- It's easier to handle requirements when the ID gives a hint about the content
- Make them descriptive but concise

### How do I specify dependencies?

Use the `Solved by` field to specify dependencies:
- Give only one `Solved by` field per requirement
- The value should be the IDs of requirements that solve your current requirement
- You must specify `Solved by` except for leaf requirements (those that cannot/should not be detailed further)

**Example**:
```
Solved by: DatabaseConnection NetworkModule
```

### How do I add paragraphs in the Rationale?

To start a new paragraph, write `\par` at the end of the current paragraph. This will be automatically converted to the appropriate output format.

### What are the guidelines for Effort estimation?

The effort estimation is meant to be a symbolic effort point number as used in SCRUM. It's a relative measure, not an absolute time estimate.

### What units are expected in the Effort estimation field?

None - this is a symbolic number representing relative effort, not time units.

### What values are valid for the Status field?

Supported values are:
- `not done` - Requirement is not yet implemented
- `finished` - Requirement has been completed

### What values are valid for the Type field?

Supported values are:
- `master requirement` - High-level requirement
- `requirement` - Standard requirement
- `design decision` - Architectural or design choice

### What does 'Class' do? How should it be used?

Class can be:
- `implementable` - Requirement is detailed enough to be implemented
- `detailable` (default) - Requirement needs further elaboration and dependent requirements

### How should I remove a requirement?

1. Remove it from the file system: `rm requirement.req`
2. Remove it from version control: `git rm requirement.req`
3. Commit the change: `git commit -m "Remove requirement"`

## Daily Usage

### Is it possible to rename the rmtoo directory?

No - this is not possible. Most Python files assume that the top-level directory is called `rmtoo`.

### rmtoo prints 'make: *** No rule to make target ...'

This typically happens when a requirement was removed or renamed. The automatically generated dependency file must be deleted:
```bash
rm .rmtoo_dependencies
# or
make force
```

### I cannot compile rmtoo. What should I do?

There is no need to compile rmToo. It comes as a set of Python modules. You can unpack and use it directly.

### I got the error 'ImportError: No module named rmtoo.lib.RmtooMain'

This indicates that the PYTHONPATH is not set correctly when using the tar packaged version of rmToo. Make sure you've followed the [installation instructions](user-guide/installation/).

### 'make test' displays low test coverage

Try removing all old .pyc files:
```bash
find . -name "*.pyc" | xargs rm
```

The coverage should then be correctly computed.

### The requirement looks fine but rmtoo complains about a missing tag

If you're using strange line delimiters (such as carriage return and linefeed - as used by Windows), rmToo cannot parse the requirements. Convert to the commonly used Unix format using only line feeds (LF, 0x0A).

You can convert line endings with:
```bash
dos2unix your-requirement.req
```

## Troubleshooting

### Installation Issues

**Problem**: pip install fails
**Solution**: Try using a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
pip install rmtoo
```

**Problem**: LaTeX not found
**Solution**: Install LaTeX for your platform:
```bash
# Ubuntu/Debian
sudo apt install texlive-latex-base texlive-latex-extra

# macOS
sudo port install texlive

# Windows (Cygwin)
# Install tetex package
```

### Runtime Issues

**Problem**: Graphviz not found
**Solution**: Install graphviz:
```bash
# Ubuntu/Debian
sudo apt install graphviz

# macOS
sudo port install graphviz

# Windows
# Download from graphviz.org and add to PATH
```

**Problem**: Permission denied errors
**Solution**: Check file permissions and use virtual environments

### Configuration Issues

**Problem**: Configuration not found
**Solution**: Ensure Config.json exists in your project directory

**Problem**: Invalid configuration
**Solution**: Validate your JSON/YAML syntax and check the [configuration guide](user-guide/configuration/)

## Getting More Help

- Check the [User Guide](user-guide/) for comprehensive documentation
- Review the [Reference Documentation](reference/) for detailed information
- Report bugs on [GitHub Issues](https://github.com/florath/rmtoo/issues)
- Contact: rmtoo@florath.net
- Man pages: `man rmtoo` for overview