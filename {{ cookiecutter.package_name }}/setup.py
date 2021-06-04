#!/usr/bin/env python
from setuptools import setup, find_packages


packages = find_packages(where="src")
packages.append("{{ cookiecutter.module_name }}.resources")

package_dir = {
    "": "src",
    "{{ cookiecutter.module_name }}.resources": "resources",
}

package_data = {
    "{{ cookiecutter.module_name }}.resources": ["*.yaml", "**/*.yaml", "**/**/*.yaml"],
}

setup(
    packages=packages,
    package_dir=package_dir,
    package_data=package_data,
)