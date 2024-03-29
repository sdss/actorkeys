#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: José Sánchez-Gallego (gallegoj@uw.edu)
# @Date: 2021-09-27
# @Filename: jaeger.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)
#
# type: ignore

KeysDictionary(
    "hal",
    (5, 0),
    Key("version", String(help="Actor version")),
    Key("text", String(help="Text for humans")),
    Key("schema", String(help="Schema definition")),
    Key("help", String(help="Help string")),
    Key("error", String(help="Error message")),
    Key("yourUserID", Int(help="User ID")),
    Key("UserInfo", Int(name="userID"), String(name="IP")),
    Key("num_users", Int(help="Number of users connected")),
    Key("available_scripts", String() * (0,), help="Available scripts"),
    Key("running_scripts", String() * (0,), help="Running scripts"),
    Key(
        "script_step",
        String(name="script_name"),
        String(name="step_description"),
        Int(name="current_step"),
        Int(name="total_steps"),
    ),
    Key("macros", String() * (0,), help="Available macros"),
    Key("running_macros", String() * (0,), help="Currently running macros"),
    Key("stages", String() * (0,), help="Macro stages"),
    Key("all_stages", String() * (0,), help="All possible macro stages"),
    Key("stage_status", String() * (0,), help="Status of macro stages"),
    Key(
        "stage_duration",
        String(name="macro_name", help="The name of the macro"),
        String(
            name="stage_name",
            help="The name of the stage. Names with colons indicate multiple "
            "stages running concurrently. Empty name refers to the duration "
            "for the entire macro.",
        ),
        Float(name="duration", help="The duration of the stage in seconds."),
    ),
    Key("bypasses", String() * (0,), help="Enabled bypasses"),
    Key(
        "exposure_state_apogee",
        Int(name="current_apogee", help="Current APOGEE exposure/dither"),
        Int(name="n_apogee", help="Total number of APOGEE exposures/dithers"),
        Bool("F", "T", name="pair", help="Are we dithering?"),
        String(name="dither_position", help="APOGEE dither position"),
        Float(name="etr_apogee", help="Remaining APOGEE exposure time"),
        Float(name="total_apogee", help="Total APOGEE exposure time"),
        Float(name="timestamp", help="Timestamp when the keyword was output"),
    ),
    Key(
        "exposure_state_boss",
        Int(name="current_boss", help="Current BOSS exposure"),
        Int(name="n_boss", help="Total number of BOSS exposures"),
        Float(name="etr_boss", help="Remaining BOSS exposure time"),
        Float(name="total_boss", help="Total BOSS time"),
        Float(name="timestamp", help="Timestamp when the keyword was output"),
    ),
    Key("auto_mode_message", String(), help="Message from the auto mode"),
    Key("expose_is_paused", Bool("F", "T"), help="Is the expose macro paused?"),
)
