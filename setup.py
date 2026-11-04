from pathlib import Path

from setuptools import setup
from setuptools.command.build_py import build_py


class BuildPyWithTypedMarkers(build_py):
    """Add a PEP 561 py.typed marker to every top-level package.

    The upstream NetBox source does not ship py.typed files, so they are
    generated in the build directory instead of the netbox submodule.
    """

    def run(self) -> None:
        super().run()
        for package in {name.split(".")[0] for name in self.packages or []}:
            Path(self.build_lib, package, "py.typed").touch()


setup(cmdclass={"build_py": BuildPyWithTypedMarkers})
