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
    "sop",
    (4, 0),
    Key("version", String(help="Actor version")),
    Key("text", String(), help="Text for humans"),
    Key("error", String(), help="Error message"),
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
    Key("stages", String() * (2,), help="Macro stages"),
    Key("all_stages", String() * (2,), help="All possible macro stages"),
    Key("stage_status", String() * (3,), help="Status of macro stages"),
)
