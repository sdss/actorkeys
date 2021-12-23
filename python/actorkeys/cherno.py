#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: José Sánchez-Gallego (gallegoj@uw.edu)
# @Date: 2021-06-11
# @Filename: cherno.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

# type: ignore


KeysDictionary(
    'cherno', (0, 1),
    Key('version', String(help='actor version')),
    Key('text', String(), help='text for humans'),
    Key('error', String(), help='text for humans'),
    Key("camera_solution",
        String(),
        Int(),
        Bool("F", "T"),
        Float(),
        Float(),
        Float(),
        Float(),
        Float()),
    Key("acquisition_valid", Bool("F", "T")),
    Key("did_correct", Bool("F", "T")),
    Key("guider_status", String()),
    Key("fwhm_camera",
        String(),
        Int(),
        Float(),
        Float(),
        Float(),
        Float(),
        Int()),
    Key("astrometry_fit",
        Int(),
        Int(),
        Float(),
        Float(),
        Float(),
        Float(),
        Float(),
        Float(),
        Float(),
        Float(),
        Float()),
    Key("guide_rms",
        Int(),
        Float(),
        Float(),
        Float()),
    Key("correction_applied",
        Float(),
        Float(),
        Float(),
        Float()),

)
