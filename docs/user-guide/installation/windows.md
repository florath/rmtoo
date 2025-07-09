# Windows Installation

> **Important**: rmToo was successfully tested under Windows but is not officially supported under Windows.

This document provides hints to get rmToo up and running under Windows.

## Installation Methods

### Method 1: Using Cygwin (Recommended)

rmToo was successfully tested using Cygwin, which provides a Unix-like environment on Windows.

#### Install Cygwin
1. Download the [Cygwin setup.exe](http://cygwin.com/install.html) file
2. Follow the installation instructions
3. Choose the following additional packages:
   - `gnuplot`
   - `make`
   - `tetex`
   - `python`

#### Install Python Dependencies
For most rmToo statistic modules, you need numpy and scipy:
```bash
pip install numpy scipy
```

> **Note**: There are reports that numpy/scipy can run under Windows, but it may not be straightforward. Some installable versions of numpy and scipy don't work with Cygwin.

#### Install Graphviz
1. Download and install [Graphviz for Windows](http://www.graphviz.org/Download_windows.php)
2. Add Graphviz binaries to your PATH before running `make`:
   ```bash
   export PATH=$PATH:"/cygdrive/c/Program Files (x86)/Graphviz2.28/bin"
   ```
   > **Note**: Adapt the path to reflect your local directory structure and current version. The path might start with `/cygwin` depending on your Cygwin setup.

#### Install rmToo
```bash
pip install rmtoo
```

### Method 2: Windows Subsystem for Linux (WSL)

For a more native Linux experience on Windows 10/11:

1. **Enable WSL**: Follow [Microsoft's WSL installation guide](https://docs.microsoft.com/en-us/windows/wsl/install)
2. **Install Ubuntu**: From the Microsoft Store
3. **Follow Linux installation**: Use the [Linux installation guide](linux.md)

## First Project

### Create Template Project
```bash
# Navigate to your working directory
cd /path/to/your/projects

# Copy the template project
cp -r "$(rmtoo-contrib-dir)/template_project" MyProject
cd MyProject

# Set up environment
source ./setenv.sh VENV

# Build the project
make
```

### Check Results
```bash
ls artifacts/
```

## Troubleshooting

### Common Issues
- **Path issues**: Ensure all tools (Python, LaTeX, Graphviz) are in your PATH
- **Line endings**: Use `git config core.autocrlf false` to avoid line ending issues
- **Cygwin permissions**: Run Cygwin as administrator if you encounter permission errors

### Performance Notes
- Building documentation may be slower on Windows
- Consider using WSL2 for better performance

## Getting Help

If you encounter Windows-specific issues:
1. Check the [FAQ](../../faq.md)
2. Report issues on [GitHub](https://github.com/florath/rmtoo/issues)
3. Include your Windows version and installation method in bug reports
4. Contact: rmtoo@florath.net

## Additional Resources

- [Cygwin Installation](http://cygwin.com/install.html)
- [Python Downloads](http://www.python.org/download/releases/)
- [NumPy Downloads](http://sourceforge.net/projects/numpy/)
- [SciPy Downloads](http://sourceforge.net/projects/scipy/)
- [Python Libraries for Windows](http://www.lfd.uci.edu/~gohlke/pythonlibs/)
- [Graphviz for Windows](http://www.graphviz.org/Download_windows.php)