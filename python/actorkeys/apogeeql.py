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
        Int(name='expNum', help='Exposure number for this plate'),
        String(name='expName', help='Exposure name'),
        Float(name='exptime', help='Exposure time', units='seconds'),
        Float(name='numReads', help='Number of UTR Reads'),
        Float(name='snrGoal', help='The target S/N for this exposure.'),
        Float(name='ditherPos', help='measured dither Position', units='pixels'),
        Float(name='snr', help='S/N obtained (at reference H mag) for this exposure'),
        Float(name='netExptime', help='Total exposure time for this plate', units='seconds'),
        Float(name='netSnr', help='Cumulative S/N (at reference H mag) for this plate'),
        String(name='expType', help='type of the exposure'),
        Enum("A", "B", "?", name="namedDitherPos", help="name of measured dither Position"),
    ),

    # (S/N)^2 at H=12.0 vs Time Data Keywords (broadcasted with status or when it changes)
    Key('snrAxisRange',
        Float()*2,
        help='Low, High limits of the Y-Axis (S/N) plot (broadcasted once)'),
    
    Key('snrGoal',
        Float(name='snrGoal', help='Target S/N for specified H magnitude'),
        Float(name='hMag', help='Magnitude of the stars in the H-band'),
    ),

    # (S/N)^2 at H=12.0 vs Time Data Keywords (updated at every UTR read ~10sec)
    Key('utrData',
        String(name='expName', help='Exposure name'),
        Int(name='readNum', help='Read number counter'),
        Float(name='snr', help='S/N value (at reference H mag) for this read'),
        Float(name='snrTotalLinFit', help='(S/N)^2 to readNum Linear fit to all the reads so far: y intercept, slope')*2,
        Float(name='snrRecentLinFit', help='(S/N)^2 to readNum Linear fit of most recent reads: y intercept, slope')*2,
        Bits('fitsBad', 'ditherBad', 'skyBad', 'waveBad', help='bitwise status (1=bad, 0=OK)'),
        Float(name='measDitherPos', help='Measured dither position'),
        Float(name='cmdDitherPos', help='Commanded dither position'),
        Float(name='waveOffset', help='Average wavelength solution offset between measured and expected for 3 chips'),
        Float(name='exptimeEst', help='Estimated exposure time to reach snrGoal'),
        Float(name='numReadsToTarget', help='Estimated number of UTR reads to reach snrGoal'),
        Int(name='nReads', help='Total number of UTR reads requested'),
        Float(name='deltaSNR', help="Change in S/N (at reference H mag) from previous read"),
        String(name='expType', help='type of the exposure'),
        Enum("A", "B", "?", name="namedDitherPos", help="name of measured dither Position"),
        help='Data about the most recent up-the-ramp read'),

    # Predicted exposure (calculated by apgquicklook)
    Key('predictedExposure',
        Int(name='plateId', help='Plate ID number'),
        Int(name='expNum', help='Exposure number for this plate'),
        String(name='expName', help='Exposure name'),
        Float(name='exptime', help='Exposure time', units='seconds'),
        Float(name='numReads', help='Number of UTR Reads'),
        Float(name='snrGoal', help='The target S/N for this exposure.'),
        String(name='expType', help='type of the exposure'),
        Float(name='ditherPos', help='measured dither Position', units='pixels'),
        Enum("A", "B", "?", name="namedDitherPos", help="name of measured dither Position"),
    ),

    # Missing fibers (determined by apgquicklook)
    Key('missingFibers',
        String(name='expName', help='Exposure name'),
        Int(name='readNum', help='Read number counter'),
        Int(name='numMissing', invalid="nan", help='Number of missing fibers'),
        Int(name='fiberId', help='List of missing fiber IDs, if any; note fiber IDs start at 1')*(0,),
    ),


    Key("icsDiskAlarm", 
        Enum("Ok", "Warning", "Serious", "Critical", name="alertState", help="state of free space on ICS disk"),
        Int(name='freeSpace', units="GB", invalid="nan"),
        help="ICS data disk space low enough to trigger an Alarm"),

    Key("qlDiskAlarm", 
        Enum("Ok", "Warning", "Serious", "Critical", name="alertState", help="state of free space on apogee-ql disk"),
        Int(name='freeSpace', units="GB", invalid="nan"),
        help="apogee-ql data disk space low enough to trigger an Alarm"),

    Key("archDiskAlarm", 
        Enum("Ok", "Warning", "Serious", "Critical", name="alertState", help="state of free space on archive disk"),
        Int(name='freeSpace', units="GB", invalid="nan"),
        help="archive data disk space low enough to trigger an Alarm"),

    Key("freeDiskSpace", 
        Int(name='IcsFreeSpace', units="GB", invalid="nan"),
        Int(name='DataFreeSpace', units="GB", invalid="nan"),
        Int(name='ArchFreeSpace', units="GB", invalid="nan"),
        help="returns the amount of free disk space (GB)"),

))
