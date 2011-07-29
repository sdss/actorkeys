KeysDictionary("benchboss",(2,15),*(
    # misc
    Key("text", String(), help="text for humans"),
    Key("version", String(), help="version string derived from svn info."),
    
    # ICC Keywords
    Key('exposureState',
        Enum('IDLE','FLUSHING','INTEGRATING','PAUSED','PREREADING','READING','LEGIBLE','ABORTED', name="state"),
        Float(name="totalTime", help="esimated total time for this state; 0 if too short to bother with a countdown timer", units="sec"),
        Float(name="elapsedTime", help="elapsed time for this state; 0 if too short to bother with a countdown timer", units="sec"),
        help='The current state of the exposure and associated timings.'
    ),
    Key('exposureId',
        UInt(),
        help="last exposure number"),
    Key('BeginExposure',
        UInt(),
        Float(units="mjd",strFmt="%.2f"),
        help = "Time that an exposure began."
    ),
    Key('EndExposure',
        UInt(),
        Float(units = "mjd", strFmt = "%.2f"),
        help = "Time that an exposure ended."
    ),
    Key('daqVersion',
           String(),
           help='DAQ Interface python code version.'
    ),
    Key('hardwareStatus',
        Bits('sp1cam','sp2cam','sp1mech','sp2mech','sp1daq','sp2daq'),
        help='Connection status of each current piece of hardware.'
    ),
    Key('lastFlush',
        UInt(units = 'sec'),
        help = "Time of last flush."
    ),

    # specMech Keywords
    Key('shutterStatus',
        Bits('OpenSwitch', 'ClosedSwitch')*2,
        help = "Status of the two shutter switches"
    ),
    Key('screenStatus',
        Bits('RightOpenSensor', 'RightClosedSensor', 'LeftOpenSensor', 'LeftClosedSensor')*2,
        help = "Status of the hartman screens, the left bit represents the closed sensor and the right bit the open sensor."
        ),
    Key('motorPosition',
        Int()*6,
        help = "The position of the motors in ticks of both spectographs."
        ),
    Key('motorStatus',
        Bits('Stopped', 'FindEdge', 'Slave', ':1', 'SlewMode', 'MotorOff', 'LimitSwitch', 'OnTarget', )*6,
        help = "Status of the motors. Six to represent sp1MotorA-sp2MotorC."
        ),
    Key('specMechVersion',
        String()*2,
        help = "Version string of sp1mech and sp2mech."
        ),
    Key('specMechProtocol',
    	String()*2,
    	help = "Protocol string of sp1mech and sp2mech"
    	),
    Key('slitIDs', 
        Int(name='sp1SlitID', help='slit ID reported by sp1 (normalized)'),
        Int(name='sp2SlitID', help='slit ID reported by sp2'),
        help='slitIDs reported at the two slitheads. Should match each other and the mcp cartridge ID'),
    Key('sp1LastShutterTime', 
        Float(name='openTime', help='last measured open transit time', units='sec'),
        Float(name='closeTime', help='last measured open transit time', units='sec'),
        help='last measured open and close transit times for sp1 shutter'),
    Key('sp2LastShutterTime', 
        Float(name='openTime', help='last measured open transit time', units='sec'),
        Float(name='closeTime', help='last measured open transit time', units='sec'),
        help='last measured open and close transit times for sp2 shutter'),
    Key('sp1Humidity', 
        Float(name='hartmann', help='humidity at hartmann doors', units='percent'),
        Float(name='centralOptics', help='humidity at central optics', units='percent'),
        help='humidity inside sp1'),
    Key('sp2Humidity', 
        Float(name='hartmann', help='humidity at hartmann doors', units='percent'),
        Float(name='centralOptics', help='humidity at central optics', units='percent'),
        help='humidity inside sp2'),
    Key('sp1Temp', 
        Float(name='median', help='median of temp measurements', units='degreesC'),
        Float(name='hartmannTop', help='temp at top of hartmann doors', units='degreesC'),
        Float(name='redCamTop', help='temp at top of red camera', units='degreesC'),
        Float(name='blueCamTop', help='temp at top of blue camera', units='degreesC'),
        Float(name='redCamBottom', help='temp at bottom of red camera', units='degreesC'),
        Float(name='blueCamBottom', help='temp at bottom of blue camera', units='degreesC'),
        help='temperatures inside sp1'),
    Key('sp2Temp', 
        Float(name='median', help='median of temp measurements', units='degreesC'),
        Float(name='hartmannTop', help='temp at top of hartmann doors', units='degreesC'),
        Float(name='redCamTop', help='temp at top of red camera', units='degreesC'),
        Float(name='blueCamTop', help='temp at top of blue camera', units='degreesC'),
        Float(name='redCamBottom', help='temp at bottom of red camera', units='degreesC'),
        Float(name='blueCamBottom', help='temp at bottom of blue camera', units='degreesC'),
        help='temperatures inside sp2'),
  
    # DAQ Keywords
    Key('sp1ReadoutErrors',
        Int(name='exposureID', help="the exposure ID for the errors"),
        Int(name='errorCnt', help="the total number of errors for the exposure"),
        Int(name='syncErrorCnt', help="the number of lines with line synchronization errors"),
        Int(name='pixelErrorCnt', help="the number of lines with pixel count errors"),
        Int(name='frameErrorCnt', help="the number of lines with insufficient or extra pixels"),
        help='Errors noted by the DAQ during sp1 readout.'),
    Key('sp2ReadoutErrors',
        Int(name='exposureID', help="the exposure ID for the errors"),
        Int(name='errorCnt', help="the total number of errors for the exposure"),
        Int(name='syncErrorCnt', help="the number of lines with line synchronization errors"),
        Int(name='pixelErrorCnt', help="the number of lines with pixel count errors"),
        Int(name='frameErrorCnt', help="the number of lines with insufficient or extra pixels"),
        help='Errors noted by the DAQ during sp2 readout.'),

    # Cam Micro Keywords
    Key('camCheck',
        String()*(0,),
        help = "A list of strings of keywords that are out of spec."
        ),
	Key('camCheckAlert',
		String(help='keyword name'),
		String(help='keyword str(value)'),
		help = "keyword is reported out of spec by camCheck"
	),
	Key('aliveAt',
        Int(),
        help = "Unix seconds at which point the ICC was declared alive"
    ),
    Key('sp1camRawText',
    	String(),
    	help = "Raw text of TDS command",
    ),
    Key('sp2camRawText',
    	String(),
    	help = "Raw text of TDS command",
   	),
    Key('SP1RedIonPumpLatched',
    	Float(),
    	help = "Unix seconds when error was seen",
    ),
    Key('SP1BlueIonPumpLatched',
    	Float(),
    	help = "Unix seconds when error was seen",
    ),
    Key('SP2RedIonPumpLatched',
    	Float(),
    	help = "Unix seconds when error was seen",
    ),
    Key('SP2BlueIonPumpLatched',
    	Float(),
    	help = "Unix seconds when error was seen",
    ),
    Key('ln2stat',
    	String()
   	),
    # camStatus
    Key('SP1LN2Fill',
        Enum('ON','OFF','FAULT!!!'),
    ),
    Key('SP1CameraMonitor',
        Enum('ON','OFF')
    ),
    Key('SP1Cam00',
        Int()
    ),
    Key('SP1Cam01',
        Int()
    ),
    Key('SP1Cam02',
        Int()
    ),
    Key('SP1Cam03',
        Int()
    ),
    Key('SP1SerialSpeed',
        String()
    ),
    Key('SP1Pixels',
        Int()
    ),
    Key('SP1BinnedPixels',
        Int()
    ),
    Key('SP1BlueParallelDir',
        Enum('FWD','REV','UNKNOWN')
    ),
    Key('SP1BlueParallelState',
        Enum('CLOCK','STOPPED','UNKNOWN')
    ),
    Key('SP1RedParallelDir',
        Enum('FWD','REV','UNKNOWN')
    ),
    Key('SP1RedParallelState',
        Enum('CLOCK','STOPPED','UNKNOWN')
    ),
    Key('SP1DataMode',
        Enum('FRAME','CONTINUOUS')
    ),
    Key('SP1Lines',
        Int()
    ),
    Key('SP1BinnedLines',
        Int()
    ),
    Key('SP1DataState',
        Enum('IDLE','READING','DRIFTSCANNING','CLOCKING')
    ),
    Key('SP1Linestart',
        Enum('ENABLED','DISABLED')
    ),
    Key('SP1LinestartPeriod',
        String()
    ),
    Key('SP1DacsSet',
        Enum('OK','ERROR')
    ),
    Key('SP1ExecBoot',
        Enum('UNACKNOWLEDGED','ACKNOWLEDGED')
    ),
    Key('SP1PhaseBoot',
        Enum('UNACKNOWLEDGED','ACKNOWLEDGED','BUSY')
    ),
    Key('SP1USR1',
        Int()
    ),
    Key('SP1USR2',
        Int()
    ),
    Key('SP1USR3',
        Int()
    ),
    Key('SP2LN2Fill',
        Enum('ON','OFF','FAULT!!!'),
    ),
    Key('SP2CameraMonitor',
        Enum('ON','OFF')
    ),
    Key('SP2Cam00',
        Int()
    ),
    Key('SP2Cam01',
        Int()
    ),
    Key('SP2Cam02',
        Int()
    ),
    Key('SP2Cam03',
        Int()
    ),
    Key('SP2SerialSpeed',
        String()
    ),
    Key('SP2Pixels',
        Int()
    ),
    Key('SP2BinnedPixels',
        Int()
    ),
    Key('SP2BlueParallelDir',
        Enum('FWD','REV','UNKNOWN')
    ),
    Key('SP2BlueParallelState',
        Enum('CLOCK','STOPPED','UNKNOWN')
    ),
    Key('SP2RedParallelDir',
        Enum('FWD','REV','UNKNOWN')
    ),
    Key('SP2RedParallelState',
        Enum('CLOCK','STOPPED','UNKNOWN')
    ),
    Key('SP2DataMode',
        Enum('FRAME','CONTINUOUS')
    ),
    Key('SP2Lines',
        Int()
    ),
    Key('SP2BinnedLines',
        Int()
    ),
    Key('SP2DataState',
        Enum('IDLE','READING','DRIFTSCANNING','CLOCKING')
    ),
    Key('SP2Linestart',
        Enum('ENABLED','DISABLED')
    ),
    Key('SP2LinestartPeriod',
        String()
    ),
    Key('SP2DacsSet',
        Enum('OK','ERROR')
    ),
    Key('SP2ExecBoot',
        Enum('UNACKNOWLEDGED','ACKNOWLEDGED')
    ),
    Key('SP2PhaseBoot',
        Enum('UNACKNOWLEDGED','ACKNOWLEDGED','BUSY')
    ),
    Key('SP2USR1',
        Int()
    ),
    Key('SP2USR2',
        Int()
    ),
    Key('SP2USR3',
        Int()
    ),
    Key('SP1SecondaryDewarPress',
    	Int()
    ),
    Key('SP2SecondaryDewarPress',
    	Int()
    ),
    Key('SP1RedIonPump',
    	Float(strFmt='%.2f')
	),
	Key('SP1BlueIonPump',
    	Float(strFmt='%.2f')
	),
	Key('SP2RedIonPump',
    	Float(strFmt='%.2f')
	),
	Key('SP2BlueIonPump',
    	Float(strFmt='%.2f')
	),	
    # Cam Check keywords
    Key('camCheckResponse',
        String()*(0,),
        help = "A list of strings that indicate the out of range values. Possible values include DacsSet, ExecBoot, PhaseBoot, LN2Fill, LN2EmptyDewar, SecondaryDewarPress, and any of the read voltages."
    ),
    # Version String
    Key('camForthVersion',
        String()*2,
        help = "Version strings for the cam micros."
        ),
    # VOLTS
    
))

