# Installation Guide

## For Template Users

If you're using this repository as a **template** for your own project:

### 1. Clone the Template

```bash
git clone https://github.com/endavis/test3project.git my-project
cd my-project
```

### 2. Run Configuration Script

Run the interactive configuration wizard to customize the template:

```bash
python3 configure.py
```

This will prompt you for:
- Project name and description
- Package name (Python import name)
- PyPI package name
- Author information
- GitHub endavis

The script will automatically:
- Rename the package directory
- Update all template placeholders
- Self-destruct after completion

### 3. Install Dependencies

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Sync dependencies (includes dev tools)
uv sync --all-extras --dev

# Install pre-commit hooks
uv run pre-commit install
```

### 4. Start Developing

You're ready to go! See the [Usage Guide](../usage/basics.md) for development workflows.

---

## For Package Users

If you're installing this as a **package** (after it's been published):

## Requirements

- Python 3.12 or higher
- pip or uv

## Install from PyPI

### Using pip

```bash
pip install test3project
```

### Using uv (recommended)

```bash
uv pip install test3project
```

## Install from Source

### Clone the Repository

```bash
git clone https://github.com/endavis/test3project.git
cd test3project
```

### Install in Development Mode

```bash
# Using uv (recommended)
uv venv
source .venv/bin/activate
uv pip install -e ".[dev]"

# Using pip
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Optional Dependencies

### Security Auditing

Install security audit tools:

```bash
uv pip install -e ".[security]"
```

This adds:
- `pip-audit` - Security vulnerability scanner
- `bandit` - Security issue detector in Python code

### All Optional Dependencies

```bash
uv pip install -e ".[dev,security]"
```

## Verify Installation

Check that the package is installed correctly:

```python
import test3project
print(test3project.__version__)
```

Or from the command line (if CLI is available):

```bash
package-cli --version
```

## Upgrading

### From PyPI

```bash
pip install --upgrade test3project
```

### From Source

```bash
cd test3project
git pull
uv pip install -e ".[dev]"
```

## Uninstallation

```bash
pip uninstall test3project
```

## Troubleshooting

### Python Version Issues

Ensure you're using Python 3.12 or higher:

```bash
python --version
```

If you have multiple Python versions:

```bash
python3.12 -m pip install test3project
```

### Virtual Environment Issues

If you encounter issues, try creating a fresh virtual environment:

```bash
rm -rf .venv
uv venv
source .venv/bin/activate
uv pip install test3project
```

### Permission Errors

If you get permission errors, use a virtual environment instead of installing globally:

```bash
uv venv
source .venv/bin/activate
uv pip install test3project
```

## Next Steps

- Read the [Usage Guide](../usage/basics.md) to learn how to use the package
- Check the [API Reference](../reference/api.md) for detailed documentation
- See [Examples](../examples/README.md) for usage examples
