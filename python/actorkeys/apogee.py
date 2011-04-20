# This is the initial test keys dictionary for APOGEE
#
KeysDictionary("apogee", (0,2), *(
    # misc
    Key("text", String(), help="text for humans"),
    Key("version", String(), help="version string derived from svn info."),
    
    # ICC Keywords
    Key('exposureState',
        Enum('READING','INTEGRATING','PROCESSING','DONE','ABORTING','ABORTED','UTR', name="state"),
        Float(name="time", help="esimated total time for this state; 0 if too short to bother with a countdown timer", units="sec"),
        Float(name="time_left", help="esimated remaining time for this state; 0 if too short to bother with a countdown timer", units="sec"),
#        Int(name="UTR_counter", help="Counter of just completed UTR read; 0 for the any state other than UTR", units="read"),
        help='The current state of the exposure and associated timings.'),
    Key('exposureWroteFile',
        String(name="wrotefile"),
        help="Name of FITS file just written to disk"),
    Key('exposureMode',
        Enum('fowler','sutr',),
        Float(name="nfowler", help="number of fowler samples or Up-the-Ramp frames to take"),
        help="number of fowler samples"),


    # Spectrograph Setup/Status Keywords
    Key('arrayPower',
        Enum('ON','OFF','?'),
        help='Status of controller array power'),
    Key('dspload',
        String(),
        help='Name of DSP file currently in use'),
    Key('dspFiles',
        String()*(0,10),
        help='List of available DSP files'),

    # Collimator Tip/Tilt/Focus Keywords
    Key('ttPosition',
        Float(units='pixels')*2,
        help='Commanded collimator tip/tilt'),
    Key('ttStepPosition',
        Float(units='microns')*3,
        help='Commanded collimator actuator position'),
    Key('ttLimits',
        Float(units='microns')*2,
        help='Low, high software limits for collimator actuator position'),

    # Detector Dither Keywords
    Key('ditherPosition',
        Float(units='pixels'),
        help='Commanded dither position offset from home'),
    Key('ditherLimits',
        Float(units='pixels')*2,
        help='Low, high software limits for dither actuator position'),
    Key('ditherStepPosition',
        Float(units='microns'),
        help='Commanded dither actuator position'),

    # Instrument Keywords
    Key('tempNames', 
        String()*20,
        help='Location name of each temperature sensor'),
    Key('temps', 
        Float(units='K')*20,
        help='temperatures inside apogee'),
    Key('tempInterval', 
        Float(units='sec'),
        help='Reporting interval of the temperatures and alarms; 0.0 turns automatic reporting off'),
    Key('tempAlarms', 
        Bool("0", "1")*20,
        help='Alarm status for each temperature sensor; 0=ok, 1=alarm'),
    Key('tempThresholds', 
        Float(units='K')*20,
        help='Threshold for each sensor (degreesK)'),
    Key('tempMin', 
        Float(units='K')*20,
        help='Expected minimum values (degreesK)'),
    Key('tempMax', 
        Float(units='K')*20,
        help='Expected maximum values (degreesK)'),
    Key('vacuum', 
        Float(units='Torr'),
        help='Current vacumm; NaN if not available (Torr)'),
    Key('vacuumInterval', 
        Float(units='sec'),
        help='Reporting interval of the vacuum and alarms; 0.0 turns automatic reporting off'),
    Key('vacuumAlarm', 
        Bool("0", "1"),
        help='Vacuum Alarm state; 0=ok, 1=alarm'),
    Key('vacuumThreshold', 
        Float(units='Torr'),
        help='Vacuum Threshold'),
    Key('vacuumLimits', 
        Float(units='Torr')*2,
        help='Expected Low, High Vacuum'),
    Key('ln2Level', 
        Float(units='liters'),
        help='Current level of LN2 in instrument; NaN if not available'),
    Key('ln2Interval', 
        Float(units='sec'),
        help='Reporting interval of the LN2 level and alarms; 0.0 turns automatic reporting off'),
    Key('ln2Alarm', 
        Bool("0", "1"),
        help='LN2 Level Alarm state; 0=ok, 1=alarm'),
    Key('ln2Threshold', 
        Float(units='liters'),
        help='LN2 Level below which an Alarm is triggered'),
    Key('ln2Limits', 
        Float(units='liters')*2,
        help='Expected Low, High LN2 level'),

))
