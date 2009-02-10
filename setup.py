#!/usr/bin/env python
"""Install the keys package. Requires setuptools.

To use:
python setup.py install

Alternatively you can copy python/keys to site-packages
"""

from setuptools import setup, find_packages
import sys
import os

Descr = "Command and keyword data dictionaries for actors in the SDSS-III operations system"
PkgName = "actorkeys"

PkgRoot = "python"
PkgDir = os.path.join(PkgRoot, PkgName)

setup(
    name = PkgName,
    description = Descr,
    package_dir = {PkgName: PkgDir},
    packages = find_packages(PkgRoot),
    include_package_data = True,
    scripts = [],
)
