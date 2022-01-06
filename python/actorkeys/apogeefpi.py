#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: José Sánchez-Gallego (gallegoj@uw.edu)
# @Date: 2022-01-06
# @Filename: apogeefpi.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

# type: ignore

KeysDictionary(
    "apogeefpi",
    (0, 1),
    Key("version", String(help="Actor version")),
    Key("text", String(help="Text for humans")),
    Key("schema", String(help="Schema definition")),
    Key("help", String(help="Help string")),
    Key("error", String(help="Error message")),
    Key("yourUserID", Int(help="User ID")),
    Key("UserInfo", Int(name="userID"), String(name="IP")),
    Key("num_users", Int(help="Number of users connected")),
    Key(
        "shutter_position",
        Enum("open", "closed", "?", name="position", help="Position of the shutter"),
    ),
)
