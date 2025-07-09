# Linux Installation

rmToo is fully supported on Linux distributions. This guide covers installation methods for various Linux distributions.

## Prerequisites

### Python Requirements
rmToo requires Python 3.9 or later:
```bash
python3 --version  # Should be 3.9+
```

### System Dependencies

#### Ubuntu/Debian
```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
sudo apt install -y texlive-latex-base texlive-latex-extra texlive-font-utils
sudo apt install -y graphviz gnuplot
sudo apt install -y python3-numpy python3-scipy  # Optional: for statistics
```

#### CentOS/RHEL/Fedora
```bash
# CentOS/RHEL
sudo yum install -y python3 python3-pip
sudo yum install -y texlive graphviz gnuplot
sudo yum install -y python3-numpy python3-scipy

# Fedora
sudo dnf install -y python3 python3-pip
sudo dnf install -y texlive graphviz gnuplot
sudo dnf install -y python3-numpy python3-scipy
```

#### openSUSE
```bash
sudo zypper install -y python3 python3-pip
sudo zypper install -y texlive graphviz gnuplot
sudo zypper install -y python3-numpy python3-scipy
```

#### Arch Linux
```bash
sudo pacman -S python python-pip
sudo pacman -S texlive-core graphviz gnuplot
sudo pacman -S python-numpy python-scipy
```

## Installation Methods

### Method 1: Using pip (Recommended)

#### Global Installation
```bash
pip install rmtoo
```

#### User Installation
```bash
pip install --user rmtoo
```

#### Virtual Environment Installation (Recommended)
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

### Method 2: Development Installation

For development or latest features:
```bash
git clone https://github.com/florath/rmtoo.git
cd rmtoo
python3 -m venv venv
source venv/bin/activate
pip install -e .
```

## Verification

Test the installation:
```bash
rmtoo --version
rmtoo-contrib-dir
```

## First Project

### Create Template Project
```bash
# Navigate to your working directory
cd RMTOO  # or wherever you want your project

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

You should see various generated files including:
- HTML documentation
- LaTeX/PDF files
- Dependency graphs
- Statistics

## Optional Components

### For Statistics and Analytics
```bash
pip install numpy scipy matplotlib
```

### For Enhanced Graph Generation
```bash
sudo apt install -y graphviz-dev  # Development headers
pip install pygraphviz
```

### For Advanced LaTeX Features
```bash
sudo apt install -y texlive-full  # Complete LaTeX distribution
```

## Troubleshooting

### Common Issues

#### Permission Errors
```bash
# Use --user flag
pip install --user rmtoo

# Or use virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate
pip install rmtoo
```

#### Missing LaTeX Packages
```bash
# Install complete LaTeX distribution
sudo apt install texlive-full

# Or install specific packages as needed
sudo apt install texlive-latex-extra texlive-fonts-extra
```

#### Graphviz Issues
```bash
# Ensure graphviz is installed
which dot
sudo apt install graphviz

# For development headers
sudo apt install graphviz-dev
```

### Environment Issues
If you encounter issues with the environment setup:
```bash
# Check Python version
python3 --version

# Check pip version
pip --version

# List installed packages
pip list | grep rmtoo
```

## System Integration

### Man Pages
After installation, man pages are available:
```bash
man rmtoo
man rmtoo-analytics
```

### Shell Completion
For bash completion, add to your `.bashrc`:
```bash
eval "$(rmtoo --completion bash)"
```

## Getting Help

If you encounter issues:
1. Check the [FAQ](../../faq.md)
2. Review the [troubleshooting guide](../../troubleshooting.md)
3. Report issues on [GitHub](https://github.com/florath/rmtoo/issues)
4. Include your distribution and versions in bug reports