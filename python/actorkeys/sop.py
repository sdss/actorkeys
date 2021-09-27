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
)
