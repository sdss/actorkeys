#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: José Sánchez-Gallego (gallegoj@uw.edu)
# @Date: 2021-11-29
# @Filename: fliswarm.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

# type: ignore

KeysDictionary(
    "fliswarm",
    (1, 0),
    Key("version", String(help="Actor version")),
    Key("text", String(), help="Text for humans"),
    Key("error", String(), help="Error message"),
    Key("status", String() * (0,), help="Status of the camera"),
)
