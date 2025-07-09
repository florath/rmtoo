# Installation Guide

This section covers installing rmToo on different operating systems.

## Choose Your Platform

### [🐧 Linux](linux.md)
**Fully supported** - Complete installation guide for major Linux distributions including Ubuntu, CentOS, Fedora, openSUSE, and Arch Linux.

### [🍎 macOS](macos.md)
**Community supported** - Installation guide using macports. Some users have reported success, but this is not officially supported.

### [🪟 Windows](windows.md)
**Community supported** - Installation guide using Cygwin or WSL. Tested but not officially supported.

## Quick Start

For most users, the recommended approach is:

1. **Install Python 3.9+** and system dependencies for your platform
2. **Create a virtual environment**:
   ```bash
   python3 -m venv rmtoo-env
   source rmtoo-env/bin/activate  # On Windows: rmtoo-env\Scripts\activate
   ```
3. **Install rmToo**:
   ```bash
   pip install rmtoo
   ```
4. **Create your first project**:
   ```bash
   cp -r "$(rmtoo-contrib-dir)/template_project" MyProject
   cd MyProject
   source ./setenv.sh VENV
   make
   ```

## Dependencies

### Required
- **Python 3.9+** - Core runtime
- **LaTeX** - For PDF output generation
- **Graphviz** - For dependency graphs

### Optional
- **NumPy/SciPy** - For statistical analysis
- **Gnuplot** - For statistical plots
- **Git** - For version control integration

## Installation Methods

### Package Manager (Recommended)
```bash
pip install rmtoo
```

### Development Installation
```bash
git clone https://github.com/florath/rmtoo.git
cd rmtoo
pip install -e .
```

### Virtual Environment (Recommended)
```bash
python3 -m venv venv
source venv/bin/activate
pip install rmtoo
```

## Verification

After installation, verify rmToo is working:
```bash
rmtoo --version
rmtoo-contrib-dir
```

## Next Steps

After installation:
1. Read the [Getting Started](../getting-started/) guide
2. Try the [Template Project](../getting-started/template-project.md)
3. Learn about [Configuration](../configuration/)

## Troubleshooting

If you encounter issues:
- Check the platform-specific installation guide
- Review the [FAQ](../../faq.md)
- Report issues on [GitHub](https://github.com/florath/rmtoo/issues)