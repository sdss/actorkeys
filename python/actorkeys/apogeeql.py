# This is the initial test keys dictionary for APOGEEQL  (Quick Look)
#
KeysDictionary("apogeeql",(0,1),*(
    # misc
    Key("text", String(), help="text for humans"),
    Key("version", String(), help="version string derived from svn info."),

    # URL links to additional info (updated for every UTR read)
    Key('rootURL',
       String(),
       help='The root address of the HTTP server'),
    Key('exposureURL',
        String(),
        help='The URL where more information on the current exposure can be found.'),
    Key('fitsURL',
        String(),
        help='The URL where the full FITS header can be found.'),
    Key('ditherURL',
        String(),
        help='The URL where the full FITS header can be found.'),
    Key('skyURL',
        String(),
        help='The URL where the full Sky Flux analysis results can be found.'),
    Key('waveURL',
        String(),
        help='The URL where the results of the wavelength calibration can be found.'),


    # Exposure List for Current Plate Table Keywords
    # one for each exposure taken with the current plate
    Key('exposureData',
        Int(name='plateId', help='Plate ID number'),
        String(name='expName', help='Exposure name'),
        String(name='expName', help='Exposure Name'),
        Float(name='exptime', help='Exposure Time', units='seconds'),
        Float(name='numReads', help='Number of UTR Reads'),
        Float(name='snrGoal', help='The target SNR for this exposure.'),
        Float(name='ditherPos', help='dither Position', units='pixels'),
        Float(name='snrH12', help='SNR obtained for H=12.0 for this exposure'),
        Float(name='netExptime', help='Total exposure time for this plate', units='seconds'),
        Float(name='netSnrH12', help='Cumulative SNR obtained for H=12.0 for this plate')),

    # (S/N)^2 at H=12.0 vs Time Data Keywords (broadcasted with status or when it changes)
    Key('snrAxisRange',
        Float()*2,
        help='Low, High limits of the Y-Axis (SNR) plot (broadcasted once)'),
    
    Key('snrGoal',
        Float(name='snrGoal', help='Target S/N for specified H magnitude'),
        Float(name='hMag', help='Magnitude of the stars in the H-band'),
    ),

    # (S/N)^2 at H=12.0 vs Time Data Keywords (updated at every UTR read ~10sec)
    Key('utrData',
        String(name='expName', help='Exposure name'),
        Int(name='readNum', help='Read number counter'),
        Float(name='snrH12', help='SNR value for this read'),
        Float(name='snrTotalLinFit', help='SNR^2 to readNum Linear fit to all the reads so far: y intercept, slope')*2,
        Float(name='snrRecentLinFit', help='SNR^2 to readNum Linear fit of most recent reads: y intercept, slope')*2,
        Bits('fitsBad', 'ditherBad', 'skyBad', 'waveBad', help='bitwise status (1=bad, 0=OK)'),
        Float(name='measDitherPos', help='Measured dither position'),
        Float(name='cmdDitherPos', help='Commanded dither position'),
        Float(name='waveOffset', help='Average wavelength solution offset between measured and expected for 3 chips'),
        Float(name='exptimeEst', help='Estimated exposure time to reach snrGoal'),
        Float(name='numReadsToTarget', help='Estimated number of UTR reads to reach snrGoal'),
        Int(name='nReads', help='Total number of UTR reads requested'),
        Float(name='deltaSNRH12', help="Change in SNR from previous read"),
        help='Data about the most recent up-the-ramp read'),

))
