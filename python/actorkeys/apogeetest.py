# This is the initial test keys dictionary for APOGEE
#
KeysDictionary("apogeetest",(0,3),*(
    # misc
    Key("text", String(), help="text for humans"),
    Key("version", String(), help="version string derived from svn info."),
    
    # ICC Keywords
    Key("exposureState",
        Enum("Exposing", "Done", "Stopping", "Stopped", "Failed", name="expState", help="state of exposure"),
        String(name="expType", help="type of exposure (object argument)"),
        Int(name="nReads", help="total number of UTR reads requested"),
        String(name="expName", help="name of exposure"),
    ),
    Key("exposureWroteFile",
        String(name="wrotefile"),
        help="Name of FITS file just written to disk"),
    Key("exposureWroteSummary",
        String(name="wrotesummary"),
        help="Name of CDS FITS file just written to disk"),
    Key("utrReadState",
        String(name="expName", help="name of exposure"),
        Enum("Reading", "Saving", "Done", "Failed", name="readState", help="state of UTR read"),
        Int(name="readNum", help="number of current UTR read, starting from 1"),
        Int(name="nReads", help="total number of UTR reads requested"),
    ),
    Key("utrReadTime", Float(units="sec"), help="time required for a UTR read"),


    # Spectrograph Setup/Status Keywords
    Key('arrayPower',
        Enum('ON','OFF','?'),
        help='Status of controller array power'),
    Key('dspload',
        String(),
        help='Name of DSP file currently in use'),
    Key('dspFiles',
        String()*10,
        help='List of available DSP files'),
    Key('isBSub',
        Enum('True','False'),
        help='Background subtract state'),
    Key('bSubBase',
        String(),
        help='Current Background filename'),
    Key('codeID',
        String(),
        help='currently running ICC version'),


    # Collimator Tip/Tilt/Focus Keywords
    Key('ttPosition',
        Float()*4,
        help='current and commanded X,Y tip/tilt mechanism position (pixels)'),
    Key('ttStepPosition',
        Int()*6,
        help='tip/tilt mechanism position (steps)'),
    Key('ttLimits',
        Float()*2,
        help='Valid Low,High limits for the tip/tilt motors in Absolute Steps'),

    # Detector Dither Keywords
    Key('ditherPosition',
        Float(name="X", units="pixels"),
        help='Pixels OFFSET from HOME of DITHER mechanism; NaN if not available'),
    Key('ditherLimits',
        Float()*2,
        help='Valid Low, High limits of DITHER mechanism (pixels)'),
    Key('ditherStepPosition',
        Float(),
        help='Current Motor absolute step position (steps)'),

    # Instrument Keywords
    Key('temps', 
        Float(units='degreesK')*10,
        help='temperatures inside apogee'),
    Key('tempInterval', 
        Float(name='time', units='sec'),
        help='Reporting interval of the temperatures and alarms; 0.0 turns automatic reporting off'),
    Key('tempAlarms', 
        Int()*10,
        help='Alarm status for each temperature sensor; 0=ok, 1=alarm'),
    Key('tempThresholds', 
        Float()*10,
        help='Threshold for each sensor (degreesK)'),
    Key('tempMin', 
        Float()*10,
        help='Expected minimum values (degreesK)'),
    Key('tempMax', 
        Float()*10,
        help='Expected maximum values (degreesK)'),
    Key('tempNames', 
        String()*10,
        help='Location name of each temperature sensor'),
    Key('vacuum', 
        Float(units='Torr'),
        help='Current vacumm; NaN if not available (Torr)'),
    Key('vacuumInterval', 
        Float(name='time', units='sec'),
        help='Reporting interval of the vacuum and alarms; 0.0 turns automatic reporting off'),
    Key('vacuumAlarm', 
        Int(),
        help='Vacuum Alarm state; 0=ok, 1=alarm'),
    Key('vacuumThreshold', 
        Float(),
        help='Vacuum Threshold (Torr)'),
    Key('vacuumLimits', 
        Float()*2,
        help='Expected Low, High Vacuum (Torr)'),
    Key('ln2Level', 
        Float(),
        help='Current level of LN2 in instrument (liters); NaN if not available'),
    Key('ln2Interval', 
        Float(name='time', units='sec'),
        help='Reporting interval of the LN2 level and alarms; 0.0 turns automatic reporting off'),
    Key('ln2Alarm', 
        Int(),
        help='LN2 Level Alarm state; 0=ok, 1=alarm'),
    Key('ln2Threshold', 
        Float(),
        help='LN2 Level below which an Alarm is triggered (liters)'),
    Key('ln2Limits', 
        Float()*2,
        help='Expected Low, High LN2 level (liters)'),

))
