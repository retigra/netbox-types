# netbox-types

A helper package for NetBox plugin and script developers that provides
development-time type hints and module resolution.

## Purpose

`netbox-types` makes it possible to install NetBox components as development
dependencies, enabling proper IDE support, type checking, and module resolution
when developing NetBox plugins and custom scripts. This allows you to import and
use NetBox modules like `dcim`, `ipam`, `circuits`, and others during
development without having a full NetBox installation.

## Important Note

**This package is a republish of the official NetBox source code in the form of
a types package.** The source code does not differ from NetBox itself - it's
simply repackaged to be installable as a development dependency.

## Installation

Install netbox-types as a **development dependency only**:

```bash
# Using uv
uv add --dev netbox-types

# Using pip
pip install --dev netbox-types

# Using poetry
poetry add --group dev netbox-types
```

⚠️ **Important**: Do NOT install this package in production environments. When
your plugin or script is deployed to an actual NetBox instance, the real NetBox
modules will be available via internal imports.

## Usage

### During Development

With netbox-types installed, you can develop your plugins and scripts with full
IDE support:

```python
# Your IDE will now resolve these imports during development
from dcim.models import Device, Site
from ipam.models import IPAddress, Prefix
from circuits.models import Circuit, Provider
from extras.scripts import Script
```

### In Production

When deployed to NetBox, your code uses the exact same imports, but they resolve
to the actual NetBox installation:

```python
# Same imports work in production - no changes needed!
from dcim.models import Device, Site
from ipam.models import IPAddress, Prefix
```

## Common Use Cases

- **Plugin Development**: Develop NetBox plugins with full type hints and
  autocomplete
- **Custom Scripts**: Write custom scripts with IDE support for NetBox models
- **Testing**: Run unit tests for your NetBox extensions locally
- **CI/CD**: Install in development mode for linting and type checking in your
  pipeline

## Example Project Setup

```toml
# pyproject.toml
[project]
name = "my-netbox-plugin"
dependencies = [
    # Your plugin's runtime dependencies (no netbox-types here!)
]

[project.optional-dependencies]
dev = [
    "netbox-types",
    "pytest",
    "ruff",
]
```

## Reporting Issues

If you encounter problems with missing modules, incorrect type hints, or any
other issues related to this package, please report them directly to this
repository. Since this package mirrors the NetBox source structure, issues are
typically related to:

- Missing modules that should be included
- Packaging or distribution problems
- Version mismatches

For issues with NetBox itself (not this types package), please report to the
[official NetBox repository](https://github.com/netbox-community/netbox).

## Version Compatibility

This package follows NetBox's versioning. Install a version that matches your
target NetBox version:

```bash
# For NetBox 4.0.x
uv add --dev netbox-types==4.0.*

# For NetBox 3.7.x
uv add --dev netbox-types==3.7.*
```

## What's Included

This package includes all standard NetBox modules:

- `circuits` - Circuit and provider management
- `core` - Core NetBox functionality
- `dcim` - Data center infrastructure management
- `extras` - Custom fields, scripts, webhooks, etc.
- `ipam` - IP address management
- `tenancy` - Multi-tenancy support
- `utilities` - Helper utilities and base classes
- `virtualization` - Virtual machine management
- `vpn` - VPN tunnel and termination management
- `wireless` - Wireless LAN management
- And more...

## License

This package contains NetBox source code and is distributed under the same
license as NetBox. See the [LICENSE.txt](netbox/LICENSE.txt) file for details.

## Related Links

- [NetBox Official Documentation](https://docs.netbox.dev/)
- [NetBox Plugin Development Guide](https://docs.netbox.dev/en/stable/plugins/development/)
- [NetBox GitHub Repository](https://github.com/netbox-community/netbox)
