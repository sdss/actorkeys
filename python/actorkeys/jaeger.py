#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: José Sánchez-Gallego (gallegoj@uw.edu)
# @Date: 2019-05-22
# @Filename: jaeger.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)
#
# @Last modified by: José Sánchez-Gallego
# @Last modified time: 2019-11-11 14:00:48

# flake8: noqa

KeysDictionary(
    'jaeger', (0, 1),
    Key('version', String(help='actor version')),
    Key('text', String(), help='text for humans'),
    Key('status',
        Int(name='positioner_id', help='the ID of the positioner'),
        Float(name='alpha', help='the angle of the alpha arm', units='degrees'),
        Float(name='beta', help='the angle of the beta arm', units='degrees'),
        Int(name='status_bits', help='the status maskbit'),
        Bool(name='initialised', help='is the positioner initialised?')
        Bool(name='bootloader', help='is the position in bootloader mode?')
    )
)
