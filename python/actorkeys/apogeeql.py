# This is the initial test keys dictionary for APOGEEQL  (Quick Look)
#
KeysDictionary("apogeeql",(0,1),*(
    # misc
    Key("text", String(), help="text for humans"),
    Key("version", String(), help="version string derived from svn info."),
    
    # Current Exposure Table keywords
    Key('exposureName',
        String(),
        help='The name of the current exposure.'),
    Key('exposureURL',
        String(),
        help='The URL where more information on the current exposure can be found.'),
    Key('readNumber', 
        Int(),
        help='Current Up-The-Ramp read number.'),
    Key('exptime',
        Float(units='secs'),
        help='Exposure time for the current exposure (seconds).'),
    Key('plate', 
        Int(),
        help='Currently load plate number.'),
    Key('fitsValid', 
        Enum('OK','BAD','?'),
        help='FITS header validation result.'),
    Key('fitsURL',
        String(),
        help='The URL where the full FITS header can be found.'),
    Key('ditherPosition',
        Float()*2,
        help='current and commanded dither mechanism position (pixels)'),
    Key('ditherURL',
        String(),
        help='The URL where the full FITS header can be found.'),
    Key('ditherValid',
        Enum('OK','BAD','?'),
        help='Dither Position validation result.'),
    Key('skyValid',
        Enum('OK','BAD','?'),
        help='Sky Flux level analysis result.'),
    Key('skyURL',
        String(),
        help='The URL where the full Sky Flux analysis results can be found.'),
    Key('waveOffset',
        Float(),
        help='Measured wavelength OFFSET for this UTR read (Angstrom)'),
    Key('waveLimits',
        Float()*2,
        help='valid Low,High limits for the wavelength offset (Angstrom)'),
    Key('waveURL',
        String(),
        help='The URL where the results of the wavelength calibration can be found.'),
    Key('snrH12',
        Float()*2,
        help='Signal to Noise Ratio (at H=12.0) for this UTR read and for this exposure.'),
    Key('snrH12Target',
        Float(),
        help='Targeted SNR for this exposure'),
    Key('exptimeEstimate',
        Float(),
        help='Estimated exposure time to reach the targeted SNR'),
    Key('exptimeValid',
        Enum('OK','LOW','HIGH','?'),
        help='Commanded exptime compared to Estimated exposure time to reach the targeted SNR'),


    # Exposure List for Current Plate Table Keywords
    # one for each exposure taken with the current plate
    Key('exposureList',
        Int(name='plateId', help='Plate ID number'),
        Int(name='expNum', help='Exposure number'),
        String(name='expName', help='Exposure Name'),
        Float(name='exptime', help='Exposure Time', units='seconds'),
        Float(name='numReads', help='Number of UTR Reads'),
        Float(name='ditherPos', help='dither Position', units='pixels'),
        Float(name='snrH12', help='SNR obtained for H=12.0 ')),
    Key('exposureListTotal',
        Float(name='exptime', help='Total Exposure Time for this plate', units='seconds'),
        Float(name='snrH12', help='Total SNR obtained for H=12.0 for this plate')),

    # (S/N)^2 at H=12.o vs Time Data Keywords
    Key('snrData',
        Float(name='snr'),
        Float(name='snrSquare'),
        Float(name='readNum'),
        help='SNR Data to update the SNR vs Time plot'),

    # There will be more stuff for the other plot when this gets defined

))
