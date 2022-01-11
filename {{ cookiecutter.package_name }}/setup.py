#!/usr/bin/env python
import os
from setuptools import setup, find_packages


packages = find_packages(where="src")
packages.append("{{ cookiecutter.module_name }}.resources")

package_dir = {
    "": "src",
    "{{ cookiecutter.module_name }}.resources": "resources",
}


def package_yaml_files(directory):
    paths = []
    for path, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(".yaml"):
                paths.append(os.path.join("..", path, filename))
    return paths


package_data = {
    "{{ cookiecutter.module_name }}.resources": package_yaml_files("resources"),
}

setup(
    packages=packages,
    package_dir=package_dir,
    package_data=package_data,
)
