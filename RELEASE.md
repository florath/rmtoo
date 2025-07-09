# Release Process

This document describes the automated release process for rmToo.

## Overview

The release process now includes:
1. **GitHub Releases**: Automatic creation with release notes
2. **PyPI Publishing**: Automatic upload to Python Package Index
3. **Traditional Tarballs**: Full distribution with documentation
4. **Documentation**: Generated PDF and graphs

## Quick Release Steps

1. **Update version** in `setup.py`:
   ```bash
   # Update version (replace X.Y.Z with your version)
   sed -i "s/VERSION = '[^']*'/VERSION = 'X.Y.Z'/" setup.py
   
   # Example for version 26.0.0:
   sed -i "s/VERSION = '[^']*'/VERSION = '26.0.0'/" setup.py
   ```

2. **Create/update release notes** in `doc/release_notes/XX.md` (or `.rst`)

3. **Commit version update**:
   ```bash
   git add setup.py
   git commit -m "Bump version to X.Y.Z"
   ```

4. **Create and push git tag**:
   ```bash
   git tag vX.Y.Z
   git push origin vX.Y.Z
   
   # Example for version 26.0.0:
   git tag v26.0.0
   git push origin v26.0.0
   ```

5. **GitHub Actions automatically**:
   - Builds documentation (PDF, graphs)
   - Creates Python packages (wheel + source)
   - Creates traditional full tarball
   - Publishes to PyPI
   - Creates GitHub release with assets

## PyPI Setup (One-time)

To enable automatic PyPI publishing, you need to set up **trusted publishing**:

1. **Go to PyPI**: https://pypi.org/manage/account/publishing/
2. **Add GitHub Publisher** with these settings:
   - **PyPI project name**: `rmtoo`
   - **Owner**: `florath` (your GitHub username)
   - **Repository name**: `rmtoo`
   - **Workflow filename**: `release.yml`
   - **Environment name**: (leave empty)

This is more secure than API keys - GitHub Actions will authenticate automatically.

## Complete Example: Releasing Version 26.0.0

Here are the exact commands to release version 26.0.0:

```bash
# 1. Update version in setup.py
sed -i "s/VERSION = '[^']*'/VERSION = '26.0.0'/" setup.py

# 2. Commit the version update
git add setup.py
git commit -m "Bump version to 26.0.0"

# 3. Create and push the tag
git tag v26.0.0
git push origin v26.0.0

# 4. Monitor the release (optional)
echo "Release started! Monitor at:"
echo "- GitHub Actions: https://github.com/florath/rmtoo/actions"
echo "- PyPI: https://pypi.org/project/rmtoo/"
echo "- Releases: https://github.com/florath/rmtoo/releases"
```

**That's it!** The automated workflow will handle everything else.

## Release Notes Format

### For New Releases (Recommended: Markdown)

Create `doc/release_notes/XX.md`:
```markdown
## 25.0.2

### User visible changes
- Add rmtoo-contrib-dir command for reliable contrib directory access
- Updated documentation with new command usage

### Internal changes
- Improved packaging configuration
- Enhanced test coverage
```

### Legacy Format (RST/TXT)

Current format in `doc/release_notes/XX.rst`:
```rst
25.0.2
======

User visible changes
--------------------

* Add rmtoo-contrib-dir command for reliable contrib directory access
* Updated documentation with new command usage
```

## Generated Release Assets

Each release will include:

### PyPI Packages
- `rmtoo-X.Y.Z-py3-none-any.whl` - Python wheel (recommended)
- `rmtoo-X.Y.Z.tar.gz` - Source distribution

### GitHub Release Assets
- `rmtoo-X.Y.Z-full.tar.gz` - Complete tarball (like build_tar.sh)
- `requirements.pdf` - Generated documentation
- `req-graph1.png` - Requirements dependency graph
- `req-graph2.png` - Requirements dependency graph (alternative)

### Traditional vs PyPI Packages

- **Traditional tarball**: Includes generated docs, full project structure
- **PyPI packages**: Optimized for Python installation, no generated docs

## Troubleshooting

### PyPI Publishing Fails
- Check trusted publishing setup at pypi.org
- Verify repository name and workflow filename match

### Documentation Generation Fails
- Check that required system packages are available
- Verify LaTeX installation and graphviz dependencies

### Release Notes Not Found
- Ensure file exists: `doc/release_notes/XX.md` (or `.rst`/`.txt`)
- Check version number matches tag (e.g., v25.0.2 → 25.md)

## Migration from build_tar.sh

The new process **replaces** `build_tar.sh` with these advantages:

- ✅ **Automatic**: No manual steps after tagging
- ✅ **PyPI publishing**: Easier installation for users
- ✅ **GitHub releases**: Better discoverability
- ✅ **Documentation**: Still generates PDFs and graphs
- ✅ **Traditional tarballs**: Still available for those who need them

The traditional full tarball (`rmtoo-X.Y.Z-full.tar.gz`) contains the same files as `build_tar.sh` would create.