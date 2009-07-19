#!/usr/bin/env python
"""Install this package. Requires setuptools.

To use:
python setup.py install
"""
import sys, subprocess
import sdss3tools

if len(sys.argv) > 1 and sys.argv[1] in ("build", "install"):
    subprocess.call(["make"], cwd="python/actorkeys")

sdss3tools.setup(
    description = "Command and keyword data dictionaries for actors in the SDSS-III operations system",
    )
