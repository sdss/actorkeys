#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: José Sánchez-Gallego (gallegoj@uw.edu)
# @Date: 2021-06-11
# @Filename: cherno.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

# type: ignore


KeysDictionary(
    "cherno",
    (0, 1),
    Key("version", String(help="actor version")),
    Key("text", String(), help="text for humans"),
    Key("error", String(), help="text for humans"),
    Key(
        "camera_solution",
        String("camera"),
        Int("exposure_no"),
        Bool("F", "T", name="solved"),
        Float("racen"),
        Float("deccen"),
        Float("x_rotation"),
        Float("y_rotation"),
        Float("rotation"),
    ),
    Key("acquisition_valid", Bool("F", "T")),
    Key("did_correct", Bool("F", "T")),
    Key("guider_status", String()),
    Key(
        "fwhm_camera",
        String("camera"),
        Int("exposure_no"),
        Float("fwhm"),
        Int("n_regions"),
        Int("n_valid"),
    ),
    Key(
        "astrometry_fit",
        Int("exposure_no"),
        Int("n_solved"),
        Float("racen"),
        Float("deccen"),
        Float("fwhm_median"),
        Float("ellipticity"),
        Float("camera_rotation"),
        Float("delta_ra"),
        Float("delta_dec"),
        Float("delta_rot"),
        Float("delta_scale"),
    ),
    Key(
        "focus_fit",
        Int("exposure_no"),
        Float("fwhm_fit"),
        Float("a"),
        Float("b"),
        Float("c"),
        Float("r2"),
        Float("delta_focus"),
    ),
    Key("guide_rms", Int("exposure_no"), Float("xrms"), Float("yrms"), Float("rms")),
    Key(
        "correction_applied",
        Float("ra"),
        Float("dec"),
        Float("rot"),
        Float("scale"),
        Float("focus"),
    ),
    Key("offset", String() * (3,), help="Telescope offset"),
    Key("enabled_axes", String() * (0,), help="Enabled axes"),
    Key("pid_radec", Float(name="kp", help="Proportional term in RA/Dec")),
    Key("pid_rot", Float(name="kp", help="Proportional term in rotation")),
    Key("scale_mean", Float(), help="Median scale over the last exposures"),
    Key("focus_data", Float() * (0,), help="Compilation of focus data for each GFA"),
)
