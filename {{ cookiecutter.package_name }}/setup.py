#!/usr/bin/env python
import os
from pathlib import Path
from setuptools import setup, find_packages


packages = find_packages(where="src")
packages.append("{{ cookiecutter.module_name }}.resources")

package_dir = {
    "": "src",
    "{{ cookiecutter.module_name }}.resources": "resources",
}


def package_yaml_files(directory):
    paths = sorted(Path(directory).rglob("*.yaml"))
    return [str(p.relative_to(directory)) for p in paths]

package_data = {
    "{{ cookiecutter.module_name }}.resources": package_yaml_files("resources"),
}

setup(
    packages=packages,
    package_dir=package_dir,
    package_data=package_data,
)
