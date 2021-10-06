#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: José Sánchez-Gallego (gallegoj@uw.edu)
# @Date: 2021-10-06
# @Filename: apogeebpr.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

# type: ignore


KeysDictionary(
    'apogeebpr', (1, 1),

    Key('text',
        String(),
        help='text for humans'),
    Key('codeID',
        String(),
        help='code version'),
    Key('BPRMode', Enum('bpr', 'bypass', 'manual', 'emergencystop', name='value')),
    Key('BPREncTemp', Float(name='temperature', units='celsius', strFmt='%.1f')),
    Key('BPRInletTemp', Float(name='temperature', units='celsius', strFmt='%.1f')),
    Key('BPROutletTemp', Float(name='temperature', units='celsius', strFmt='%.1f')),
    Key('MKSSetPtPress', Float(name='pressure', units='torr', strFmt='%.1f')),
    Key('MKSPress', Float(name='pressure', units='torr', strFmt='%.1f')),
    Key('BPRManPress', Float(name='pressure', units='torr', strFmt='%.1f')),
    Key('BPRFillValve', Enum('open', 'closed', name='state')),
    Key('BPRVentValve', Enum('open', 'closed', name='state')),
    Key('BPRBypassValve', Enum('open', 'closed', name='state')),
    Key('BPRDumpValve', Enum('open', 'closed', name='state'))
)
