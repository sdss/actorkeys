# This is the initial test keys dictionary for APOGEEQL  (Quick Look)
#
KeysDictionary("apogeeql",(0,1),*(
    # misc
    Key("text", String(), help="text for humans"),
    Key("version", String(), help="version string derived from svn info."),

    # Current Exposure Table keywords (updated at start of a new exposure)
    Key('exposureInfo',
        String(name='exposureName', help='Name of current exposure'),
        Int(name='plateId', help='Currently load plate number.'),
        Float(name='exptime', help='Exposure time for the current exposure (seconds).'),
        Float(name='snrGoal', help='The target SNR for this exposure.')),

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
        Int(name='expNum', help='Exposure number'),
        String(name='expName', help='Exposure Name'),
        Float(name='exptime', help='Exposure Time', units='seconds'),
        Float(name='numReads', help='Number of UTR Reads'),
        Float(name='ditherPos', help='dither Position', units='pixels'),
        Float(name='snrH12', help='SNR obtained for H=12.0 '),
        Float(name='netExptime', help='Total Exposure Time for this plate', units='seconds'),
        Float(name='netSnrH12', help='Total SNR obtained for H=12.0 for this plate')),

    # (S/N)^2 at H=12.0 vs Time Data Keywords (broadcasted with status or when it changes)
    Key('snrAxisRange',
        Float()*2,
        help='Low, High limits of the Y-Axis (SNR) plot (broadcasted once)'),

    # (S/N)^2 at H=12.0 vs Time Data Keywords (updated at every UTR read ~10sec)
    Key('utrData',
        Int(name='expNum', help='Instrument running exposure number'),
        Int(name='readNum', help='read number counter'),
        Float(name='snr2', help='SNR^2 value for this read'),
        Float(name='snrLinFit', help='SNR^2 to readNum Linear fit to all the reads so far')*2,
        Float(name='snrLast2LinFit', help='SNR^2 to readNum Linear fit of previous 2 reads')*2,
        Int(name='fitsValid', help='1 for valid, 0 for incomplete fits header'),
        Int(name='ditherValid', help='1 for valid, 0 for larger than expected by 0.1pix'),
        Float(name='ditherPos', help='measured/commanded dither position')*2,
        Int(name='skyValid', help='1 for valid, 0 for larger than expected'),
        Int(name='waveValid', help='1 for wavelength solution within 1.0A of expected solution, 0 otherwise'),
        Float(name='waveOffset', help='Average wavelength solution offset between measured and expected for 3 chips'),
        Float(name='snrH12', help='Signal to Noise Ratio (at H=12.0) for this UTR read (red if not met snrGoal)')*2,
        Float(name='exptimeEst', help='Estimated exposure time to reach snrGoal (red if larger than exptime)'),
        Float(name='numReadsToTarget', help='Estimated number of UTR reads to reach snrGoal'),
        help='SNR Data to update the SNR vs Time plot - a new row for each UTR read'),

    # There will be more stuff for the other plot when this gets defined

))
