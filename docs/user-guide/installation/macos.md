# macOS Installation

> **Note**: There is no official support for macOS. However, users have reported successfully using rmToo under macOS.

## Prerequisites

### Package Manager
You'll need macports for installing dependencies:
```bash
# Install macports from https://www.macports.org/install.php
```

### Required Packages
Install the necessary system packages:
```bash
sudo port install texlive-fontutils gnuplot
sudo port install texlive
```

## Python Installation

### Using virtualenv (Recommended)
```bash
# Create project directory
mkdir RMTOO
cd RMTOO

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install rmToo
pip install --upgrade pip setuptools wheel
pip install --only-binary=numpy,scipy numpy scipy
pip install rmtoo
```

### Verification
Test the installation:
```bash
rmtoo --version
```

## First Project

### Create Template Project
```bash
# Navigate to your working directory
cd RMTOO

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
- **LaTeX not found**: Ensure texlive is properly installed and in PATH
- **Graphviz missing**: Install with `sudo port install graphviz`
- **Python dependencies**: Use the `--only-binary` flag for numpy/scipy to avoid compilation issues

### Getting Help
If you encounter issues specific to macOS, please:
1. Check the [FAQ](../../faq.md)
2. Report issues on [GitHub](https://github.com/florath/rmtoo/issues)
3. Include your macOS version and macports version in bug reports