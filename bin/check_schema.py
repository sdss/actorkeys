#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: José Sánchez-Gallego (gallegoj@uw.edu)
# @Date: 2021-12-25
# @Filename: check_schema.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

from __future__ import annotations

import json
import sys

from opscore.protocols.keys import KeysDictionary


def check_schema(schema: str, actor: str):
    """Compares a CLU JSONSchema definition with an actorkeys model."""

    schema_json = json.loads(open(schema).read())
    properties = schema_json["properties"]

    model = KeysDictionary.load(actor)
    for key in properties:
        if key not in model.keys:
            print(f"Key {key} is missing in actorkeys.")


if __name__ == "__main__":

    if len(sys.argv) != 3:
        raise ValueError("Usage: check_schema.py <SCHEMA> <ACTOR>")

    schema, actor = sys.argv[1:3]
    check_schema(schema, actor)
