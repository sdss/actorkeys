#!/usr/bin/env python
"""Install this package. Requires setuptools.

To use:
python setup.py install
"""
import sdss3tools

sdss3tools.setup(
    name = "actorkeys",
    description = "Command and keyword data dictionaries for actors in the SDSS-III operations system",
)
