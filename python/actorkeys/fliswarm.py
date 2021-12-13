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
    Key("text",
        String(name="camera", help="camera name"),
        String(help="Text for humans")),
    Key("error",
        String(name="camera", help='camera name'),
        String(help="Error message")),
    Key("status", String() * (0,), help="Status of the camera"),
    Key("exposure_state", String() * (0,), help="Status of the exposure"),
    Key("filename",
        String(name="camera", help='camera name'),
        String(name="filename", help='the file path')),
    Key("filename_bundle",
        String() * (0,),
        help="Files written in as part of the same exposure."),
    Key("container",
        String(name="camera", help='camera name'),
        String(name="container")),
    Key("volume",
        String(name="camera", help='camera name'),
        String(name="volume"),
        Bool(False, True, help="Whether the volume has been created.").
        String(name="path")),
    Key("node",
        String(name="camera", help='camera name'),
        String(name="host"),
        String(name="daemon")
        Bool(False, True),
        Bool(False, True)),
    Key("enabledNodes", String() * (0,))
)
