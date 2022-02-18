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
    Key("yourUserID", Int(), help="Your user ID number."),
    Key("num_users", Int(), help="Number of connected users"),
    Key(
        "userInfo",
        Int(name="id", help="user ID"),
        String(name="address", help="socket address"),
        help="Basic information about one user",
    ),
    Key("version", String(help="Actor version")),
    Key("text", String() * (0,)),
    Key(
        "error",
        String(name="camera", help="camera name"),
        String(help="Error message"),
    ),
    Key(
        "status",
        String(name="camera"),
        String(name="node"),
        String(name="model"),
        String(name="serial"),
        Int(name="fwrev"),
        Int(name="hwrev"),
        Int(name="hbin"),
        Int(name="vbin"),
        Int(name="visible_ul_x"),
        Int(name="visible_ul_y"),
        Int(name="visible_lr_x"),
        Int(name="visible_lr_y"),
        Int(name="ul_x"),
        Int(name="ul_y"),
        Int(name="lr_x"),
        Int(name="lr_y"),
        Float(name="temperature_ccd"),
        Float(name="temperature_base"),
        Float(name="exposure_time_left"),
        Float(name="cooler_power"),
        help="Status of the camera",
    ),
    Key(
        "exposure_state",
        String() * (0,),
        help="Status of the exposure",
    ),
    Key(
        "filename",
        String(name="camera"),
        String(name="node"),
        String(name="filename", help="the file path"),
    ),
    Key(
        "filename_bundle",
        String() * (0,),
        help="Files written in as part of the same exposure.",
    ),
    Key(
        "container",
        String(name="camera", help="camera name"),
        String(name="container"),
    ),
    Key(
        "volume",
        String(name="camera", help="camera name"),
        String(name="volume"),
        Bool("F", "T", help="Whether the volume has been created."),
        String(name="path"),
    ),
    Key(
        "node",
        String(name="camera", help="camera name"),
        String(name="host"),
        String(name="daemon"),
        Bool("F", "T"),
        Bool("F", "T"),
    ),
    Key("enabledNodes", String() * (0,)),
)
