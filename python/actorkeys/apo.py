KeysDictionary('apo', (0,2),
    Key('pressure',
        Float(units='inches Hg', strFmt='%.3f', reprFmt='%.3f'),
		help='Barometric pressure'
    ),
    Key('windd',
        Float(units='degrees', strFmt='%.1f', reprFmt='%.1f'),
		help='Average wind direction'
    ),
    Key('winds',
        Float(units='mph', strFmt='%.1f', reprFmt='%.1f'),
		help='Average wind speed'
    ),
    Key('gustd',
        Float(units='degrees', strFmt='%.1f', reprFmt='%.1f'),
		help='Average gust direction'
    ),
    Key('gusts',
        Float(units='mph', strFmt='%.1f', reprFmt='%.1f'),
		help='Average gust speed'
    ),
    Key('temp',
        Float(units='C', strFmt='%.1f', reprFmt='%.1f'),
		help='Site air temperature'
    ),
    Key('dpTemp',
        Float(units='C', strFmt='%.1f', reprFmt='%.1f'),
		help='Site dewpoint temperature'
    ),
    Key('dpErr',
        String(strFmt='%s', reprFmt='%s'),
		help='Site hygrothermometer sensor error status'
    ),
    Key('humidity',
        Float(units='%', strFmt='%.1f', reprFmt='%.1f'),
		help='Site humidity'
    ),
    Key('dusta',
        Float(units='#/0.1 ft^3', strFmt='%d', reprFmt='%d'),
		help='PT outside dust density, 0.3 microns'
    ),
    Key('dustb',
        Float(units='#/0.1 ft^3', strFmt='%d', reprFmt='%d'),
		help='PT outside dust density, 1.0 micron'
    ),
    Key('dustc',
        Float(units='#/0.1 ft^3', strFmt='%d', reprFmt='%d'),
		help='35m enclosure dust density, 0.3 microns'
    ),
    Key('dustd',
        Float(units='#/0.1 ft^3', strFmt='%d', reprFmt='%d'),
		help='35m enclosure dust density, 1.0 micron'
    ),
    Key('windd25m',
        Float(units='degrees', strFmt='%.1f', reprFmt='%.1f'),
		help='25m wind direction'
    ),
    Key('winds25m',
        Float(units='mph', strFmt='%.1f', reprFmt='%.1f'),
		help='25m wind speed'
    ),
    Key('encl25m',
        Int(units='', strFmt='%d', reprFmt='%d'),
		help='25m enclosure position: <0 unknown, 0 closed, >0 open'
    ),
    Key('truss25m',
        Float(units='C', strFmt='%.2f', reprFmt='%.2f'),
		help='25m median truss temperature'
    ),
    Key('airTempPT',
        Float(units='C', strFmt='%.1f', reprFmt='%.1f'),
		help='PT air temperature'
    ),
    Key('dpTempPT',
        Float(units='C', strFmt='%.1f', reprFmt='%.1f'),
		help='PT dewpoint temperature'
    ),
    Key('humidPT',
        Float(units='%', strFmt='%.1f', reprFmt='%.1f'),
		help='PT humidity'
    ),
    Key('dimmflux1',
        Float(units='ADU', strFmt='%.1f', reprFmt='%.1f'),
		help='DIMM image 1 flux'
    ),
    Key('dimmflux2',
        Float(units='ADU', strFmt='%.1f', reprFmt='%.1f'),
		help='DIMM image 2 flux'
    ),
    Key('irscmean',
        Float(units='ADU', strFmt='%.1f', reprFmt='%.1f'),
		help='IRSC mean flux'
    ),
    Key('irscsd',
        Float(units='ADU', strFmt='%.1f', reprFmt='%.1f'),
		help='IRSC flux standard deviation'
    ),
)
