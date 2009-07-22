KeysDictionary("boss",(1,3),
    # ICC Keywords
    Key('exposureState',
        Enum('IDLE','FLUSHING','INTEGRATING','PAUSED','READING'),
        Int()*2,
        help='The current state of the exposure.'
    ),
    Key('hardwareStatus',
        Bits('sp1cam','sp2cam','sp1mech','sp2mech','sp1daq','sp2daq'),
        help='Connection status of each current piece of hardware.'
    ),
    # specMech Keywords
    Key('shutterStatus',
        Bits('sp1Shutter','sp2Shutter'),
        help = "Status of the shutters, 0 closed, 1 open."
    ),
    Key('screenStatus',
        Bits('sp1Left:2','sp1Right:2','sp2Left:2','sp2Right:2'),
        help = "Status of the hartman screens, the left bit represents the closed sensor and the right bit the open sensor."
        ),
    Key('motorPosition',
        Int()*6,
        help = "The position of the motors in ticks of both spectographs."
        ),
    Key('motorStatus',
        Bits('OnTarget','LimitSwitch','MotorOff','SlewMode',':1','Slave','FindEdge','Stopped')*6,
        help = "Status of the motors. Six to represent sp1MotorA-sp2MotorC."
        ),
    Key('specMechVersion',
        String()*2,
        help = "Version string of sp1mech and sp2mech."
        ),
    # DAQ Keywords
    # Cam Micro Keywords
    # camStatus
    Key('SP1LN2Fill',
        Enum('ON','OFF'),
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
        Enum('FWD','REV','UNKOWN')
    ),
    Key('SP1BlueParallelState',
        Enum('CLOCK','STOPPED','UNKOWN')
    ),
    Key('SP1RedParallelDir',
        Enum('FWD','REV','UNKOWN')
    ),
    Key('SP1RedParallelState',
        Enum('CLOCK','STOPPED','UNKOWN')
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
        Enum('UNACKNOWLEDGED','ACKNOWLEDGED')
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
        Enum('ON','OFF'),
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
        Enum('FWD','REV','UNKOWN')
    ),
    Key('SP2BlueParallelState',
        Enum('CLOCK','STOPPED','UNKOWN')
    ),
    Key('SP2RedParallelDir',
        Enum('FWD','REV','UNKOWN')
    ),
    Key('SP2RedParallelState',
        Enum('CLOCK','STOPPED','UNKOWN')
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
        Enum('UNACKNOWLEDGED','ACKNOWLEDGED')
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
    # Version String
    Key('camForthVersion',
        String()*2,
        help = "Version strings for the cam micros."
        ),
    # SHOW_VOLTS
    Key('SP1BVPcDRead',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3+ from the  SP1 camForth"
    ),


    Key('SP1BVPcDNom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3+ from the  SP1 camForth"
    ),


    Key('SP1BVPcDBias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3+ from the  SP1 camForth"
    ),


    Key('SP2BVPcDRead',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3+ from the  SP2 camForth"
    ),


    Key('SP2BVPcDNom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3+ from the  SP2 camForth"
    ),


    Key('SP2BVPcDBias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3+ from the  SP2 camForth"
    ),


    Key('SP1BVSc2Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS+ from the  SP1 camForth"
    ),


    Key('SP1BVSc2Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS+ from the  SP1 camForth"
    ),


    Key('SP1BVSc2Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS+ from the  SP1 camForth"
    ),


    Key('SP2BVSc2Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS+ from the  SP2 camForth"
    ),


    Key('SP2BVSc2Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS+ from the  SP2 camForth"
    ),


    Key('SP2BVSc2Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS+ from the  SP2 camForth"
    ),


    Key('SP1BINegTrim3Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM1 from the  SP1 camForth"
    ),


    Key('SP1BINegTrim3Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM1 from the  SP1 camForth"
    ),


    Key('SP1BINegTrim3Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM1 from the  SP1 camForth"
    ),


    Key('SP2BINegTrim3Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM1 from the  SP2 camForth"
    ),


    Key('SP2BINegTrim3Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM1 from the  SP2 camForth"
    ),


    Key('SP2BINegTrim3Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM1 from the  SP2 camForth"
    ),


    Key('SP1BVRoffRead',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VSW- from the  SP1 camForth"
    ),


    Key('SP1BVRoffNom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VSW- from the  SP1 camForth"
    ),


    Key('SP1BVRoffBias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VSW- from the  SP1 camForth"
    ),


    Key('SP2BVRoffRead',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VSW- from the  SP2 camForth"
    ),


    Key('SP2BVRoffNom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VSW- from the  SP2 camForth"
    ),


    Key('SP2BVRoffBias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VSW- from the  SP2 camForth"
    ),


    Key('SP1BVPbDRead',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3- from the  SP1 camForth"
    ),


    Key('SP1BVPbDNom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3- from the  SP1 camForth"
    ),


    Key('SP1BVPbDBias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3- from the  SP1 camForth"
    ),


    Key('SP2BVPbDRead',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3- from the  SP2 camForth"
    ),


    Key('SP2BVPbDNom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3- from the  SP2 camForth"
    ),


    Key('SP2BVPbDBias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3- from the  SP2 camForth"
    ),


    Key('SP1BINegTrim4Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM2 from the  SP1 camForth"
    ),


    Key('SP1BINegTrim4Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM2 from the  SP1 camForth"
    ),


    Key('SP1BINegTrim4Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM2 from the  SP1 camForth"
    ),


    Key('SP2BINegTrim4Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM2 from the  SP2 camForth"
    ),


    Key('SP2BINegTrim4Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM2 from the  SP2 camForth"
    ),


    Key('SP2BINegTrim4Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM2 from the  SP2 camForth"
    ),


    Key('SP1BIPosTrim4Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM2 from the  SP1 camForth"
    ),


    Key('SP1BIPosTrim4Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM2 from the  SP1 camForth"
    ),


    Key('SP1BIPosTrim4Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM2 from the  SP1 camForth"
    ),


    Key('SP2BIPosTrim4Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM2 from the  SP2 camForth"
    ),


    Key('SP2BIPosTrim4Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM2 from the  SP2 camForth"
    ),


    Key('SP2BIPosTrim4Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM2 from the  SP2 camForth"
    ),


    Key('SP1BIPosTrim3Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM1 from the  SP1 camForth"
    ),


    Key('SP1BIPosTrim3Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM1 from the  SP1 camForth"
    ),


    Key('SP1BIPosTrim3Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM1 from the  SP1 camForth"
    ),


    Key('SP2BIPosTrim3Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM1 from the  SP2 camForth"
    ),


    Key('SP2BIPosTrim3Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM1 from the  SP2 camForth"
    ),


    Key('SP2BIPosTrim3Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM1 from the  SP2 camForth"
    ),


    Key('SP1BVDD3Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD1 from the  SP1 camForth"
    ),


    Key('SP1BVDD3Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD1 from the  SP1 camForth"
    ),


    Key('SP1BVDD3Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD1 from the  SP1 camForth"
    ),


    Key('SP2BVDD3Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD1 from the  SP2 camForth"
    ),


    Key('SP2BVDD3Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD1 from the  SP2 camForth"
    ),


    Key('SP2BVDD3Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD1 from the  SP2 camForth"
    ),


    Key('SP1BVLG34Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VLG from the  SP1 camForth"
    ),


    Key('SP1BVLG34Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VLG from the  SP1 camForth"
    ),


    Key('SP1BVLG34Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VLG from the  SP1 camForth"
    ),


    Key('SP2BVLG34Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VLG from the  SP2 camForth"
    ),


    Key('SP2BVLG34Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VLG from the  SP2 camForth"
    ),


    Key('SP2BVLG34Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VLG from the  SP2 camForth"
    ),


    Key('SP1BVSb2Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS- from the  SP1 camForth"
    ),


    Key('SP1BVSb2Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS- from the  SP1 camForth"
    ),


    Key('SP1BVSb2Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS- from the  SP1 camForth"
    ),


    Key('SP2BVSb2Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS- from the  SP2 camForth"
    ),


    Key('SP2BVSb2Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS- from the  SP2 camForth"
    ),


    Key('SP2BVSb2Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS- from the  SP2 camForth"
    ),


    Key('SP1BVDD4Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD2 from the  SP1 camForth"
    ),


    Key('SP1BVDD4Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD2 from the  SP1 camForth"
    ),


    Key('SP1BVDD4Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD2 from the  SP1 camForth"
    ),


    Key('SP2BVDD4Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD2 from the  SP2 camForth"
    ),


    Key('SP2BVDD4Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD2 from the  SP2 camForth"
    ),


    Key('SP2BVDD4Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD2 from the  SP2 camForth"
    ),


    Key('SP1BVRD4Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD2 from the  SP1 camForth"
    ),


    Key('SP1BVRD4Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD2 from the  SP1 camForth"
    ),


    Key('SP1BVRD4Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD2 from the  SP1 camForth"
    ),


    Key('SP2BVRD4Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD2 from the  SP2 camForth"
    ),


    Key('SP2BVRD4Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD2 from the  SP2 camForth"
    ),


    Key('SP2BVRD4Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD2 from the  SP2 camForth"
    ),


    Key('SP1BHeaterVRead',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of HEATERV from the  SP1 camForth"
    ),


    Key('SP1BHeaterVNom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of HEATERV from the  SP1 camForth"
    ),


    Key('SP1BHeaterVBias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of HEATERV from the  SP1 camForth"
    ),


    Key('SP2BHeaterVRead',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of HEATERV from the  SP2 camForth"
    ),


    Key('SP2BHeaterVNom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of HEATERV from the  SP2 camForth"
    ),


    Key('SP2BHeaterVBias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of HEATERV from the  SP2 camForth"
    ),


    Key('SP1BVPcCRead',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12+ from the  SP1 camForth"
    ),


    Key('SP1BVPcCNom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12+ from the  SP1 camForth"
    ),


    Key('SP1BVPcCBias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12+ from the  SP1 camForth"
    ),


    Key('SP2BVPcCRead',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12+ from the  SP2 camForth"
    ),


    Key('SP2BVPcCNom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12+ from the  SP2 camForth"
    ),


    Key('SP2BVPcCBias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12+ from the  SP2 camForth"
    ),


    Key('SP1BVPbCRead',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12- from the  SP1 camForth"
    ),


    Key('SP1BVPbCNom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12- from the  SP1 camForth"
    ),


    Key('SP1BVPbCBias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12- from the  SP1 camForth"
    ),


    Key('SP2BVPbCRead',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12- from the  SP2 camForth"
    ),


    Key('SP2BVPbCNom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12- from the  SP2 camForth"
    ),


    Key('SP2BVPbCBias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12- from the  SP2 camForth"
    ),


    Key('SP1BVRD3Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD1 from the  SP1 camForth"
    ),


    Key('SP1BVRD3Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD1 from the  SP1 camForth"
    ),


    Key('SP1BVRD3Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD1 from the  SP1 camForth"
    ),


    Key('SP2BVRD3Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD1 from the  SP2 camForth"
    ),


    Key('SP2BVRD3Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD1 from the  SP2 camForth"
    ),


    Key('SP2BVRD3Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD1 from the  SP2 camForth"
    ),


    Key('SP1RVERASERead',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3+ from the  SP1 camForth"
    ),


    Key('SP1RVERASENom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3+ from the  SP1 camForth"
    ),


    Key('SP1RVERASEBias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3+ from the  SP1 camForth"
    ),


    Key('SP2RVERASERead',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3+ from the  SP2 camForth"
    ),


    Key('SP2RVERASENom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3+ from the  SP2 camForth"
    ),


    Key('SP2RVERASEBias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3+ from the  SP2 camForth"
    ),


    Key('SP1RVSc2Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS+ from the  SP1 camForth"
    ),


    Key('SP1RVSc2Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS+ from the  SP1 camForth"
    ),


    Key('SP1RVSc2Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS+ from the  SP1 camForth"
    ),


    Key('SP2RVSc2Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS+ from the  SP2 camForth"
    ),


    Key('SP2RVSc2Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS+ from the  SP2 camForth"
    ),


    Key('SP2RVSc2Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS+ from the  SP2 camForth"
    ),


    Key('SP1RINegTrim3Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM1 from the  SP1 camForth"
    ),


    Key('SP1RINegTrim3Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM1 from the  SP1 camForth"
    ),


    Key('SP1RINegTrim3Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM1 from the  SP1 camForth"
    ),


    Key('SP2RINegTrim3Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM1 from the  SP2 camForth"
    ),


    Key('SP2RINegTrim3Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM1 from the  SP2 camForth"
    ),


    Key('SP2RINegTrim3Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM1 from the  SP2 camForth"
    ),


    Key('SP1RVRonRead',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VSW- from the  SP1 camForth"
    ),


    Key('SP1RVRonNom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VSW- from the  SP1 camForth"
    ),


    Key('SP1RVRonBias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VSW- from the  SP1 camForth"
    ),


    Key('SP2RVRonRead',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VSW- from the  SP2 camForth"
    ),


    Key('SP2RVRonNom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VSW- from the  SP2 camForth"
    ),


    Key('SP2RVRonBias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VSW- from the  SP2 camForth"
    ),


    Key('SP1RVPURGRead',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3- from the  SP1 camForth"
    ),


    Key('SP1RVPURGNom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3- from the  SP1 camForth"
    ),


    Key('SP1RVPURGBias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3- from the  SP1 camForth"
    ),


    Key('SP2RVPURGRead',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3- from the  SP2 camForth"
    ),


    Key('SP2RVPURGNom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3- from the  SP2 camForth"
    ),


    Key('SP2RVPURGBias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3- from the  SP2 camForth"
    ),


    Key('SP1RINegTrim4Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM2 from the  SP1 camForth"
    ),


    Key('SP1RINegTrim4Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM2 from the  SP1 camForth"
    ),


    Key('SP1RINegTrim4Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM2 from the  SP1 camForth"
    ),


    Key('SP2RINegTrim4Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM2 from the  SP2 camForth"
    ),


    Key('SP2RINegTrim4Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM2 from the  SP2 camForth"
    ),


    Key('SP2RINegTrim4Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM2 from the  SP2 camForth"
    ),


    Key('SP1RVSR2Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS- from the  SP1 camForth"
    ),


    Key('SP1RVSR2Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS- from the  SP1 camForth"
    ),


    Key('SP1RVSR2Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS- from the  SP1 camForth"
    ),


    Key('SP2RVSR2Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS- from the  SP2 camForth"
    ),


    Key('SP2RVSR2Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS- from the  SP2 camForth"
    ),


    Key('SP2RVSR2Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS- from the  SP2 camForth"
    ),


    Key('SP1RIPosTrim4Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM2 from the  SP1 camForth"
    ),


    Key('SP1RIPosTrim4Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM2 from the  SP1 camForth"
    ),


    Key('SP1RIPosTrim4Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM2 from the  SP1 camForth"
    ),


    Key('SP2RIPosTrim4Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM2 from the  SP2 camForth"
    ),


    Key('SP2RIPosTrim4Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM2 from the  SP2 camForth"
    ),


    Key('SP2RIPosTrim4Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM2 from the  SP2 camForth"
    ),


    Key('SP1RIPosTrim3Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM1 from the  SP1 camForth"
    ),


    Key('SP1RIPosTrim3Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM1 from the  SP1 camForth"
    ),


    Key('SP1RIPosTrim3Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM1 from the  SP1 camForth"
    ),


    Key('SP2RIPosTrim3Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM1 from the  SP2 camForth"
    ),


    Key('SP2RIPosTrim3Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM1 from the  SP2 camForth"
    ),


    Key('SP2RIPosTrim3Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM1 from the  SP2 camForth"
    ),


    Key('SP1RVDD3Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD1 from the  SP1 camForth"
    ),


    Key('SP1RVDD3Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD1 from the  SP1 camForth"
    ),


    Key('SP1RVDD3Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD1 from the  SP1 camForth"
    ),


    Key('SP2RVDD3Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD1 from the  SP2 camForth"
    ),


    Key('SP2RVDD3Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD1 from the  SP2 camForth"
    ),


    Key('SP2RVDD3Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD1 from the  SP2 camForth"
    ),


    Key('SP1RVLG3Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VT- from the  SP1 camForth"
    ),


    Key('SP1RVLG3Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VT- from the  SP1 camForth"
    ),


    Key('SP1RVLG3Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VT- from the  SP1 camForth"
    ),


    Key('SP2RVLG3Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VT- from the  SP2 camForth"
    ),


    Key('SP2RVLG3Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VT- from the  SP2 camForth"
    ),


    Key('SP2RVLG3Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VT- from the  SP2 camForth"
    ),


    Key('SP1RVLG2Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VLG from the  SP1 camForth"
    ),


    Key('SP1RVLG2Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VLG from the  SP1 camForth"
    ),


    Key('SP1RVLG2Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VLG from the  SP1 camForth"
    ),


    Key('SP2RVLG2Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VLG from the  SP2 camForth"
    ),


    Key('SP2RVLG2Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VLG from the  SP2 camForth"
    ),


    Key('SP2RVLG2Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VLG from the  SP2 camForth"
    ),


    Key('SP1RVPcCRead',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12- from the  SP1 camForth"
    ),


    Key('SP1RVPcCNom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12- from the  SP1 camForth"
    ),


    Key('SP1RVPcCBias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12- from the  SP1 camForth"
    ),


    Key('SP2RVPcCRead',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12- from the  SP2 camForth"
    ),


    Key('SP2RVPcCNom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12- from the  SP2 camForth"
    ),


    Key('SP2RVPcCBias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12- from the  SP2 camForth"
    ),


    Key('SP1RVSUBSRead',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VR from the  SP1 camForth"
    ),


    Key('SP1RVSUBSNom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VR from the  SP1 camForth"
    ),


    Key('SP1RVSUBSBias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VR from the  SP1 camForth"
    ),


    Key('SP2RVSUBSRead',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VR from the  SP2 camForth"
    ),


    Key('SP2RVSUBSNom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VR from the  SP2 camForth"
    ),


    Key('SP2RVSUBSBias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VR from the  SP2 camForth"
    ),


    Key('SP1RVDD4Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD2 from the  SP1 camForth"
    ),


    Key('SP1RVDD4Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD2 from the  SP1 camForth"
    ),


    Key('SP1RVDD4Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD2 from the  SP1 camForth"
    ),


    Key('SP2RVDD4Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD2 from the  SP2 camForth"
    ),


    Key('SP2RVDD4Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD2 from the  SP2 camForth"
    ),


    Key('SP2RVDD4Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD2 from the  SP2 camForth"
    ),


    Key('SP1RVRD4Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD2 from the  SP1 camForth"
    ),


    Key('SP1RVRD4Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD2 from the  SP1 camForth"
    ),


    Key('SP1RVRD4Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD2 from the  SP1 camForth"
    ),


    Key('SP2RVRD4Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD2 from the  SP2 camForth"
    ),


    Key('SP2RVRD4Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD2 from the  SP2 camForth"
    ),


    Key('SP2RVRD4Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD2 from the  SP2 camForth"
    ),


    Key('SP1RHeaterVRead',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of HEATERV from the  SP1 camForth"
    ),


    Key('SP1RHeaterVNom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of HEATERV from the  SP1 camForth"
    ),


    Key('SP1RHeaterVBias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of HEATERV from the  SP1 camForth"
    ),


    Key('SP2RHeaterVRead',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of HEATERV from the  SP2 camForth"
    ),


    Key('SP2RHeaterVNom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of HEATERV from the  SP2 camForth"
    ),


    Key('SP2RHeaterVBias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of HEATERV from the  SP2 camForth"
    ),


    Key('SP1RVPRCRead',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12+ from the  SP1 camForth"
    ),


    Key('SP1RVPRCNom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12+ from the  SP1 camForth"
    ),


    Key('SP1RVPRCBias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12+ from the  SP1 camForth"
    ),


    Key('SP2RVPRCRead',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12+ from the  SP2 camForth"
    ),


    Key('SP2RVPRCNom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12+ from the  SP2 camForth"
    ),


    Key('SP2RVPRCBias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12+ from the  SP2 camForth"
    ),


    Key('SP1RVLG4Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VT+ from the  SP1 camForth"
    ),


    Key('SP1RVLG4Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VT+ from the  SP1 camForth"
    ),


    Key('SP1RVLG4Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VT+ from the  SP1 camForth"
    ),


    Key('SP2RVLG4Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VT+ from the  SP2 camForth"
    ),


    Key('SP2RVLG4Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VT+ from the  SP2 camForth"
    ),


#    Key('SP2RVLG4Bias',
#        Float(units='volts',strFormat='%.3f'),
#        help = "Translated value of VT+ from the  SP2 camForth"
#    ),


    Key('SP1RVRD3Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD1 from the  SP1 camForth"
    ),


    Key('SP1RVRD3Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD1 from the  SP1 camForth"
    ),


    Key('SP1RVRD3Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD1 from the  SP1 camForth"
    ),


    Key('SP2RVRD3Read',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD1 from the  SP2 camForth"
    ),


    Key('SP2RVRD3Nom',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD1 from the  SP2 camForth"
    ),


    Key('SP2RVRD3Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD1 from the  SP2 camForth"
    ),
    Key('SP1BVPcDCheck',
        Int(strFormat='%.3f'),
        help = "Translated value of VP3+ from the  SP1 camForth"
    ),
    Key('SP1BVPcDErr',
        Int(strFormat='%.3f'),
        help = "Translated value of VP3+ from the  SP1 camForth"
    ),


    Key('SP1BVPcDTolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VP3+ from the  SP1 camForth"
    ),


    Key('SP2BVPcDCheck',
        Int(strFormat='%.3f'),
        help = "Translated value of VP3+ from the  SP2 camForth"
    ),

    Key('SP2BVPcDErr',
        Int(strFormat='%.3f'),
        help = "Translated value of VP3+ from the  SP2 camForth"
    ),


    Key('SP2BVPcDTolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VP3+ from the  SP2 camForth"
    ),


    Key('SP1BVSc2Check',
        Int(strFormat='%.3f'),
        help = "Translated value of VS+ from the  SP1 camForth"
    ),


    Key('SP1BVSc2Err',
        Int(strFormat='%.3f'),
        help = "Translated value of VS+ from the  SP1 camForth"
    ),


    Key('SP1BVSc2Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VS+ from the  SP1 camForth"
    ),


    Key('SP2BVSc2Check',
        Int(strFormat='%.3f'),
        help = "Translated value of VS+ from the  SP2 camForth"
    ),


    Key('SP2BVSc2Err',
        Int(strFormat='%.3f'),
        help = "Translated value of VS+ from the  SP2 camForth"
    ),


    Key('SP2BVSc2Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VS+ from the  SP2 camForth"
    ),


    Key('SP1BINegTrim3Check',
        Int(strFormat='%.3f'),
        help = "Translated value of I-TRIM1 from the  SP1 camForth"
    ),


    Key('SP1BINegTrim3Err',
        Int(strFormat='%.3f'),
        help = "Translated value of I-TRIM1 from the  SP1 camForth"
    ),


    Key('SP1BINegTrim3Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of I-TRIM1 from the  SP1 camForth"
    ),


    Key('SP2BINegTrim3Check',
        Int(strFormat='%.3f'),
        help = "Translated value of I-TRIM1 from the  SP2 camForth"
    ),


    Key('SP2BINegTrim3Err',
        Int(strFormat='%.3f'),
        help = "Translated value of I-TRIM1 from the  SP2 camForth"
    ),


    Key('SP2BINegTrim3Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of I-TRIM1 from the  SP2 camForth"
    ),


    Key('SP1BVRoffCheck',
        Int(strFormat='%.3f'),
        help = "Translated value of VSW- from the  SP1 camForth"
    ),


    Key('SP1BVRoffErr',
        Int(strFormat='%.3f'),
        help = "Translated value of VSW- from the  SP1 camForth"
    ),


    Key('SP1BVRoffTolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VSW- from the  SP1 camForth"
    ),


    Key('SP2BVRoffCheck',
        Int(strFormat='%.3f'),
        help = "Translated value of VSW- from the  SP2 camForth"
    ),


    Key('SP2BVRoffErr',
        Int(strFormat='%.3f'),
        help = "Translated value of VSW- from the  SP2 camForth"
    ),


    Key('SP2BVRoffTolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VSW- from the  SP2 camForth"
    ),


    Key('SP1BVPbDCheck',
        Int(strFormat='%.3f'),
        help = "Translated value of VP3- from the  SP1 camForth"
    ),


    Key('SP1BVPbDErr',
        Int(strFormat='%.3f'),
        help = "Translated value of VP3- from the  SP1 camForth"
    ),


    Key('SP1BVPbDTolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VP3- from the  SP1 camForth"
    ),


    Key('SP2BVPbDCheck',
        Int(strFormat='%.3f'),
        help = "Translated value of VP3- from the  SP2 camForth"
    ),


    Key('SP2BVPbDErr',
        Int(strFormat='%.3f'),
        help = "Translated value of VP3- from the  SP2 camForth"
    ),


    Key('SP2BVPbDTolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VP3- from the  SP2 camForth"
    ),


    Key('SP1BINegTrim4Check',
        Int(strFormat='%.3f'),
        help = "Translated value of I-TRIM2 from the  SP1 camForth"
    ),


    Key('SP1BINegTrim4Err',
        Int(strFormat='%.3f'),
        help = "Translated value of I-TRIM2 from the  SP1 camForth"
    ),


    Key('SP1BINegTrim4Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of I-TRIM2 from the  SP1 camForth"
    ),


    Key('SP2BINegTrim4Check',
        Int(strFormat='%.3f'),
        help = "Translated value of I-TRIM2 from the  SP2 camForth"
    ),


    Key('SP2BINegTrim4Err',
        Int(strFormat='%.3f'),
        help = "Translated value of I-TRIM2 from the  SP2 camForth"
    ),


    Key('SP2BINegTrim4Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of I-TRIM2 from the  SP2 camForth"
    ),


    Key('SP1BIPosTrim4Check',
        Int(strFormat='%.3f'),
        help = "Translated value of I+TRIM2 from the  SP1 camForth"
    ),


    Key('SP1BIPosTrim4Err',
        Int(strFormat='%.3f'),
        help = "Translated value of I+TRIM2 from the  SP1 camForth"
    ),


    Key('SP1BIPosTrim4Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of I+TRIM2 from the  SP1 camForth"
    ),


    Key('SP2BIPosTrim4Check',
        Int(strFormat='%.3f'),
        help = "Translated value of I+TRIM2 from the  SP2 camForth"
    ),


    Key('SP2BIPosTrim4Err',
        Int(strFormat='%.3f'),
        help = "Translated value of I+TRIM2 from the  SP2 camForth"
    ),


    Key('SP2BIPosTrim4Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of I+TRIM2 from the  SP2 camForth"
    ),


    Key('SP1BIPosTrim3Check',
        Int(strFormat='%.3f'),
        help = "Translated value of I+TRIM1 from the  SP1 camForth"
    ),


    Key('SP1BIPosTrim3Err',
        Int(strFormat='%.3f'),
        help = "Translated value of I+TRIM1 from the  SP1 camForth"
    ),


    Key('SP1BIPosTrim3Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of I+TRIM1 from the  SP1 camForth"
    ),


    Key('SP2BIPosTrim3Check',
        Int(strFormat='%.3f'),
        help = "Translated value of I+TRIM1 from the  SP2 camForth"
    ),


    Key('SP2BIPosTrim3Err',
        Int(strFormat='%.3f'),
        help = "Translated value of I+TRIM1 from the  SP2 camForth"
    ),


    Key('SP2BIPosTrim3Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of I+TRIM1 from the  SP2 camForth"
    ),


    Key('SP1BVDD3Check',
        Int(strFormat='%.3f'),
        help = "Translated value of VDD1 from the  SP1 camForth"
    ),


    Key('SP1BVDD3Err',
        Int(strFormat='%.3f'),
        help = "Translated value of VDD1 from the  SP1 camForth"
    ),


    Key('SP1BVDD3Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VDD1 from the  SP1 camForth"
    ),


    Key('SP2BVDD3Check',
        Int(strFormat='%.3f'),
        help = "Translated value of VDD1 from the  SP2 camForth"
    ),


    Key('SP2BVDD3Err',
        Int(strFormat='%.3f'),
        help = "Translated value of VDD1 from the  SP2 camForth"
    ),


    Key('SP2BVDD3Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VDD1 from the  SP2 camForth"
    ),


    Key('SP1BVLG34Check',
        Int(strFormat='%.3f'),
        help = "Translated value of VLG from the  SP1 camForth"
    ),


    Key('SP1BVLG34Err',
        Int(strFormat='%.3f'),
        help = "Translated value of VLG from the  SP1 camForth"
    ),


    Key('SP1BVLG34Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VLG from the  SP1 camForth"
    ),


    Key('SP2BVLG34Check',
        Int(strFormat='%.3f'),
        help = "Translated value of VLG from the  SP2 camForth"
    ),


    Key('SP2BVLG34Err',
        Int(strFormat='%.3f'),
        help = "Translated value of VLG from the  SP2 camForth"
    ),


    Key('SP2BVLG34Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VLG from the  SP2 camForth"
    ),


    Key('SP1BVSb2Check',
        Int(strFormat='%.3f'),
        help = "Translated value of VS- from the  SP1 camForth"
    ),


    Key('SP1BVSb2Err',
        Int(strFormat='%.3f'),
        help = "Translated value of VS- from the  SP1 camForth"
    ),


    Key('SP1BVSb2Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VS- from the  SP1 camForth"
    ),


    Key('SP2BVSb2Check',
        Int(strFormat='%.3f'),
        help = "Translated value of VS- from the  SP2 camForth"
    ),


    Key('SP2BVSb2Err',
        Int(strFormat='%.3f'),
        help = "Translated value of VS- from the  SP2 camForth"
    ),


    Key('SP2BVSb2Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VS- from the  SP2 camForth"
    ),


    Key('SP1BVDD4Check',
        Int(strFormat='%.3f'),
        help = "Translated value of VDD2 from the  SP1 camForth"
    ),


    Key('SP1BVDD4Err',
        Int(strFormat='%.3f'),
        help = "Translated value of VDD2 from the  SP1 camForth"
    ),


    Key('SP1BVDD4Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VDD2 from the  SP1 camForth"
    ),


    Key('SP2BVDD4Check',
        Int(strFormat='%.3f'),
        help = "Translated value of VDD2 from the  SP2 camForth"
    ),


    Key('SP2BVDD4Err',
        Int(strFormat='%.3f'),
        help = "Translated value of VDD2 from the  SP2 camForth"
    ),


    Key('SP2BVDD4Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VDD2 from the  SP2 camForth"
    ),


    Key('SP1BVRD4Check',
        Int(strFormat='%.3f'),
        help = "Translated value of VRD2 from the  SP1 camForth"
    ),


    Key('SP1BVRD4Err',
        Int(strFormat='%.3f'),
        help = "Translated value of VRD2 from the  SP1 camForth"
    ),


    Key('SP1BVRD4Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VRD2 from the  SP1 camForth"
    ),


    Key('SP2BVRD4Check',
        Int(strFormat='%.3f'),
        help = "Translated value of VRD2 from the  SP2 camForth"
    ),


    Key('SP2BVRD4Err',
        Int(strFormat='%.3f'),
        help = "Translated value of VRD2 from the  SP2 camForth"
    ),


    Key('SP2BVRD4Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VRD2 from the  SP2 camForth"
    ),


    Key('SP1BHeaterVCheck',
        Int(strFormat='%.3f'),
        help = "Translated value of HEATERV from the  SP1 camForth"
    ),


    Key('SP1BHeaterVErr',
        Int(strFormat='%.3f'),
        help = "Translated value of HEATERV from the  SP1 camForth"
    ),


    Key('SP1BHeaterVTolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of HEATERV from the  SP1 camForth"
    ),


    Key('SP2BHeaterVCheck',
        Int(strFormat='%.3f'),
        help = "Translated value of HEATERV from the  SP2 camForth"
    ),


    Key('SP2BHeaterVErr',
        Int(strFormat='%.3f'),
        help = "Translated value of HEATERV from the  SP2 camForth"
    ),


    Key('SP2BHeaterVTolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of HEATERV from the  SP2 camForth"
    ),


    Key('SP1BVPcCCheck',
        Int(strFormat='%.3f'),
        help = "Translated value of VP12+ from the  SP1 camForth"
    ),


    Key('SP1BVPcCErr',
        Int(strFormat='%.3f'),
        help = "Translated value of VP12+ from the  SP1 camForth"
    ),


    Key('SP1BVPcCTolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VP12+ from the  SP1 camForth"
    ),


    Key('SP2BVPcCCheck',
        Int(strFormat='%.3f'),
        help = "Translated value of VP12+ from the  SP2 camForth"
    ),


    Key('SP2BVPcCErr',
        Int(strFormat='%.3f'),
        help = "Translated value of VP12+ from the  SP2 camForth"
    ),


    Key('SP2BVPcCTolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VP12+ from the  SP2 camForth"
    ),


    Key('SP1BVPbCCheck',
        Int(strFormat='%.3f'),
        help = "Translated value of VP12- from the  SP1 camForth"
    ),


    Key('SP1BVPbCErr',
        Int(strFormat='%.3f'),
        help = "Translated value of VP12- from the  SP1 camForth"
    ),


    Key('SP1BVPbCTolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VP12- from the  SP1 camForth"
    ),


    Key('SP2BVPbCCheck',
        Int(strFormat='%.3f'),
        help = "Translated value of VP12- from the  SP2 camForth"
    ),


    Key('SP2BVPbCErr',
        Int(strFormat='%.3f'),
        help = "Translated value of VP12- from the  SP2 camForth"
    ),


    Key('SP2BVPbCTolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VP12- from the  SP2 camForth"
    ),


    Key('SP1BVRD3Check',
        Int(strFormat='%.3f'),
        help = "Translated value of VRD1 from the  SP1 camForth"
    ),


    Key('SP1BVRD3Err',
        Int(strFormat='%.3f'),
        help = "Translated value of VRD1 from the  SP1 camForth"
    ),


    Key('SP1BVRD3Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VRD1 from the  SP1 camForth"
    ),


    Key('SP2BVRD3Check',
        Int(strFormat='%.3f'),
        help = "Translated value of VRD1 from the  SP2 camForth"
    ),


    Key('SP2BVRD3Err',
        Int(strFormat='%.3f'),
        help = "Translated value of VRD1 from the  SP2 camForth"
    ),


    Key('SP2BVRD3Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VRD1 from the  SP2 camForth"
    ),


    Key('SP1RVERASECheck',
        Int(strFormat='%.3f'),
        help = "Translated value of VP3+ from the  SP1 camForth"
    ),


    Key('SP1RVERASEErr',
        Int(strFormat='%.3f'),
        help = "Translated value of VP3+ from the  SP1 camForth"
    ),


    Key('SP1RVERASETolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VP3+ from the  SP1 camForth"
    ),


    Key('SP2RVERASECheck',
        Int(strFormat='%.3f'),
        help = "Translated value of VP3+ from the  SP2 camForth"
    ),


    Key('SP2RVERASEErr',
        Int(strFormat='%.3f'),
        help = "Translated value of VP3+ from the  SP2 camForth"
    ),


    Key('SP2RVERASETolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VP3+ from the  SP2 camForth"
    ),


    Key('SP1RVSc2Check',
        Int(strFormat='%.3f'),
        help = "Translated value of VS+ from the  SP1 camForth"
    ),


    Key('SP1RVSc2Err',
        Int(strFormat='%.3f'),
        help = "Translated value of VS+ from the  SP1 camForth"
    ),


    Key('SP1RVSc2Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VS+ from the  SP1 camForth"
    ),


    Key('SP2RVSc2Check',
        Int(strFormat='%.3f'),
        help = "Translated value of VS+ from the  SP2 camForth"
    ),


    Key('SP2RVSc2Err',
        Int(strFormat='%.3f'),
        help = "Translated value of VS+ from the  SP2 camForth"
    ),


    Key('SP2RVSc2Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VS+ from the  SP2 camForth"
    ),


    Key('SP1RINegTrim3Check',
        Int(strFormat='%.3f'),
        help = "Translated value of I-TRIM1 from the  SP1 camForth"
    ),


    Key('SP1RINegTrim3Err',
        Int(strFormat='%.3f'),
        help = "Translated value of I-TRIM1 from the  SP1 camForth"
    ),


    Key('SP1RINegTrim3Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of I-TRIM1 from the  SP1 camForth"
    ),


    Key('SP2RINegTrim3Check',
        Int(strFormat='%.3f'),
        help = "Translated value of I-TRIM1 from the  SP2 camForth"
    ),


    Key('SP2RINegTrim3Err',
        Int(strFormat='%.3f'),
        help = "Translated value of I-TRIM1 from the  SP2 camForth"
    ),


    Key('SP2RINegTrim3Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of I-TRIM1 from the  SP2 camForth"
    ),


    Key('SP1RVRonCheck',
        Int(strFormat='%.3f'),
        help = "Translated value of VSW- from the  SP1 camForth"
    ),


    Key('SP1RVRonErr',
        Int(strFormat='%.3f'),
        help = "Translated value of VSW- from the  SP1 camForth"
    ),


    Key('SP1RVRonTolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VSW- from the  SP1 camForth"
    ),


    Key('SP2RVRonCheck',
        Int(strFormat='%.3f'),
        help = "Translated value of VSW- from the  SP2 camForth"
    ),


    Key('SP2RVRonErr',
        Int(strFormat='%.3f'),
        help = "Translated value of VSW- from the  SP2 camForth"
    ),


    Key('SP2RVRonTolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VSW- from the  SP2 camForth"
    ),


    Key('SP1RVPURGCheck',
        Int(strFormat='%.3f'),
        help = "Translated value of VP3- from the  SP1 camForth"
    ),


    Key('SP1RVPURGErr',
        Int(strFormat='%.3f'),
        help = "Translated value of VP3- from the  SP1 camForth"
    ),


    Key('SP1RVPURGTolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VP3- from the  SP1 camForth"
    ),


    Key('SP2RVPURGCheck',
        Int(strFormat='%.3f'),
        help = "Translated value of VP3- from the  SP2 camForth"
    ),


    Key('SP2RVPURGErr',
        Int(strFormat='%.3f'),
        help = "Translated value of VP3- from the  SP2 camForth"
    ),


    Key('SP2RVPURGTolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VP3- from the  SP2 camForth"
    ),


    Key('SP1RINegTrim4Check',
        Int(strFormat='%.3f'),
        help = "Translated value of I-TRIM2 from the  SP1 camForth"
    ),


    Key('SP1RINegTrim4Err',
        Int(strFormat='%.3f'),
        help = "Translated value of I-TRIM2 from the  SP1 camForth"
    ),


    Key('SP1RINegTrim4Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of I-TRIM2 from the  SP1 camForth"
    ),


    Key('SP2RINegTrim4Check',
        Int(strFormat='%.3f'),
        help = "Translated value of I-TRIM2 from the  SP2 camForth"
    ),


    Key('SP2RINegTrim4Err',
        Int(strFormat='%.3f'),
        help = "Translated value of I-TRIM2 from the  SP2 camForth"
    ),


    Key('SP2RINegTrim4Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of I-TRIM2 from the  SP2 camForth"
    ),


    Key('SP1RVSR2Check',
        Int(strFormat='%.3f'),
        help = "Translated value of VS- from the  SP1 camForth"
    ),


    Key('SP1RVSR2Err',
        Int(strFormat='%.3f'),
        help = "Translated value of VS- from the  SP1 camForth"
    ),


    Key('SP1RVSR2Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VS- from the  SP1 camForth"
    ),


    Key('SP2RVSR2Check',
        Int(strFormat='%.3f'),
        help = "Translated value of VS- from the  SP2 camForth"
    ),


    Key('SP2RVSR2Err',
        Int(strFormat='%.3f'),
        help = "Translated value of VS- from the  SP2 camForth"
    ),


    Key('SP2RVSR2Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VS- from the  SP2 camForth"
    ),


    Key('SP1RIPosTrim4Check',
        Int(strFormat='%.3f'),
        help = "Translated value of I+TRIM2 from the  SP1 camForth"
    ),


    Key('SP1RIPosTrim4Err',
        Int(strFormat='%.3f'),
        help = "Translated value of I+TRIM2 from the  SP1 camForth"
    ),


    Key('SP1RIPosTrim4Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of I+TRIM2 from the  SP1 camForth"
    ),


    Key('SP2RIPosTrim4Check',
        Int(strFormat='%.3f'),
        help = "Translated value of I+TRIM2 from the  SP2 camForth"
    ),


    Key('SP2RIPosTrim4Err',
        Int(strFormat='%.3f'),
        help = "Translated value of I+TRIM2 from the  SP2 camForth"
    ),


    Key('SP2RIPosTrim4Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of I+TRIM2 from the  SP2 camForth"
    ),


    Key('SP1RIPosTrim3Check',
        Int(strFormat='%.3f'),
        help = "Translated value of I+TRIM1 from the  SP1 camForth"
    ),


    Key('SP1RIPosTrim3Err',
        Int(strFormat='%.3f'),
        help = "Translated value of I+TRIM1 from the  SP1 camForth"
    ),


    Key('SP1RIPosTrim3Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of I+TRIM1 from the  SP1 camForth"
    ),


    Key('SP2RIPosTrim3Check',
        Int(strFormat='%.3f'),
        help = "Translated value of I+TRIM1 from the  SP2 camForth"
    ),


    Key('SP2RIPosTrim3Err',
        Int(strFormat='%.3f'),
        help = "Translated value of I+TRIM1 from the  SP2 camForth"
    ),


    Key('SP2RIPosTrim3Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of I+TRIM1 from the  SP2 camForth"
    ),


    Key('SP1RVDD3Check',
        Int(strFormat='%.3f'),
        help = "Translated value of VDD1 from the  SP1 camForth"
    ),


    Key('SP1RVDD3Err',
        Int(strFormat='%.3f'),
        help = "Translated value of VDD1 from the  SP1 camForth"
    ),


    Key('SP1RVDD3Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VDD1 from the  SP1 camForth"
    ),


    Key('SP2RVDD3Check',
        Int(strFormat='%.3f'),
        help = "Translated value of VDD1 from the  SP2 camForth"
    ),


    Key('SP2RVDD3Err',
        Int(strFormat='%.3f'),
        help = "Translated value of VDD1 from the  SP2 camForth"
    ),


    Key('SP2RVDD3Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VDD1 from the  SP2 camForth"
    ),


    Key('SP1RVLG3Check',
        Int(strFormat='%.3f'),
        help = "Translated value of VT- from the  SP1 camForth"
    ),


    Key('SP1RVLG3Err',
        Int(strFormat='%.3f'),
        help = "Translated value of VT- from the  SP1 camForth"
    ),


    Key('SP1RVLG3Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VT- from the  SP1 camForth"
    ),


    Key('SP2RVLG3Check',
        Int(strFormat='%.3f'),
        help = "Translated value of VT- from the  SP2 camForth"
    ),


    Key('SP2RVLG3Err',
        Int(strFormat='%.3f'),
        help = "Translated value of VT- from the  SP2 camForth"
    ),


    Key('SP2RVLG3Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VT- from the  SP2 camForth"
    ),


    Key('SP1RVLG2Check',
        Int(strFormat='%.3f'),
        help = "Translated value of VLG from the  SP1 camForth"
    ),


    Key('SP1RVLG2Err',
        Int(strFormat='%.3f'),
        help = "Translated value of VLG from the  SP1 camForth"
    ),


    Key('SP1RVLG2Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VLG from the  SP1 camForth"
    ),


    Key('SP2RVLG2Check',
        Int(strFormat='%.3f'),
        help = "Translated value of VLG from the  SP2 camForth"
    ),


    Key('SP2RVLG2Err',
        Int(strFormat='%.3f'),
        help = "Translated value of VLG from the  SP2 camForth"
    ),


    Key('SP2RVLG2Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VLG from the  SP2 camForth"
    ),


    Key('SP1RVPcCCheck',
        Int(strFormat='%.3f'),
        help = "Translated value of VP12- from the  SP1 camForth"
    ),


    Key('SP1RVPcCErr',
        Int(strFormat='%.3f'),
        help = "Translated value of VP12- from the  SP1 camForth"
    ),


    Key('SP1RVPcCTolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VP12- from the  SP1 camForth"
    ),


    Key('SP2RVPcCCheck',
        Int(strFormat='%.3f'),
        help = "Translated value of VP12- from the  SP2 camForth"
    ),


    Key('SP2RVPcCErr',
        Int(strFormat='%.3f'),
        help = "Translated value of VP12- from the  SP2 camForth"
    ),


    Key('SP2RVPcCTolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VP12- from the  SP2 camForth"
    ),


    Key('SP1RVSUBSCheck',
        Int(strFormat='%.3f'),
        help = "Translated value of VR from the  SP1 camForth"
    ),


    Key('SP1RVSUBSErr',
        Int(strFormat='%.3f'),
        help = "Translated value of VR from the  SP1 camForth"
    ),


    Key('SP1RVSUBSTolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VR from the  SP1 camForth"
    ),


    Key('SP2RVSUBSCheck',
        Int(strFormat='%.3f'),
        help = "Translated value of VR from the  SP2 camForth"
    ),


    Key('SP2RVSUBSErr',
        Int(strFormat='%.3f'),
        help = "Translated value of VR from the  SP2 camForth"
    ),


    Key('SP2RVSUBSTolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VR from the  SP2 camForth"
    ),


    Key('SP1RVDD4Check',
        Int(strFormat='%.3f'),
        help = "Translated value of VDD2 from the  SP1 camForth"
    ),


    Key('SP1RVDD4Err',
        Int(strFormat='%.3f'),
        help = "Translated value of VDD2 from the  SP1 camForth"
    ),


    Key('SP1RVDD4Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VDD2 from the  SP1 camForth"
    ),


    Key('SP2RVDD4Check',
        Int(strFormat='%.3f'),
        help = "Translated value of VDD2 from the  SP2 camForth"
    ),


    Key('SP2RVDD4Err',
        Int(strFormat='%.3f'),
        help = "Translated value of VDD2 from the  SP2 camForth"
    ),


    Key('SP2RVDD4Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VDD2 from the  SP2 camForth"
    ),


    Key('SP1RVRD4Check',
        Int(strFormat='%.3f'),
        help = "Translated value of VRD2 from the  SP1 camForth"
    ),


    Key('SP1RVRD4Err',
        Int(strFormat='%.3f'),
        help = "Translated value of VRD2 from the  SP1 camForth"
    ),


    Key('SP1RVRD4Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VRD2 from the  SP1 camForth"
    ),


    Key('SP2RVRD4Check',
        Int(strFormat='%.3f'),
        help = "Translated value of VRD2 from the  SP2 camForth"
    ),


    Key('SP2RVRD4Err',
        Int(strFormat='%.3f'),
        help = "Translated value of VRD2 from the  SP2 camForth"
    ),


    Key('SP2RVRD4Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VRD2 from the  SP2 camForth"
    ),


    Key('SP1RHeaterVCheck',
        Int(strFormat='%.3f'),
        help = "Translated value of HEATERV from the  SP1 camForth"
    ),


    Key('SP1RHeaterVErr',
        Int(strFormat='%.3f'),
        help = "Translated value of HEATERV from the  SP1 camForth"
    ),


    Key('SP1RHeaterVTolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of HEATERV from the  SP1 camForth"
    ),


    Key('SP2RHeaterVCheck',
        Int(strFormat='%.3f'),
        help = "Translated value of HEATERV from the  SP2 camForth"
    ),


    Key('SP2RHeaterVErr',
        Int(strFormat='%.3f'),
        help = "Translated value of HEATERV from the  SP2 camForth"
    ),


    Key('SP2RHeaterVTolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of HEATERV from the  SP2 camForth"
    ),


    Key('SP1RVPRCCheck',
        Int(strFormat='%.3f'),
        help = "Translated value of VP12+ from the  SP1 camForth"
    ),


    Key('SP1RVPRCErr',
        Int(strFormat='%.3f'),
        help = "Translated value of VP12+ from the  SP1 camForth"
    ),


    Key('SP1RVPRCTolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VP12+ from the  SP1 camForth"
    ),


    Key('SP2RVPRCCheck',
        Int(strFormat='%.3f'),
        help = "Translated value of VP12+ from the  SP2 camForth"
    ),


    Key('SP2RVPRCErr',
        Int(strFormat='%.3f'),
        help = "Translated value of VP12+ from the  SP2 camForth"
    ),


    Key('SP2RVPRCTolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VP12+ from the  SP2 camForth"
    ),


    Key('SP1RVLG4Check',
        Int(strFormat='%.3f'),
        help = "Translated value of VT+ from the  SP1 camForth"
    ),


    Key('SP1RVLG4Err',
        Int(strFormat='%.3f'),
        help = "Translated value of VT+ from the  SP1 camForth"
    ),


    Key('SP1RVLG4Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VT+ from the  SP1 camForth"
    ),


    Key('SP2RVLG4Check',
        Int(strFormat='%.3f'),
        help = "Translated value of VT+ from the  SP2 camForth"
    ),


    Key('SP2RVLG4Err',
        Int(strFormat='%.3f'),
        help = "Translated value of VT+ from the  SP2 camForth"
    ),


    Key('SP2RVLG4Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VT+ from the  SP2 camForth"
    ),


    Key('SP1RVRD3Check',
        Int(strFormat='%.3f'),
        help = "Translated value of VRD1 from the  SP1 camForth"
    ),


    Key('SP1RVRD3Err',
        Int(strFormat='%.3f'),
        help = "Translated value of VRD1 from the  SP1 camForth"
    ),


    Key('SP1RVRD3Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VRD1 from the  SP1 camForth"
    ),


    Key('SP2RVRD3Check',
        Int(strFormat='%.3f'),
        help = "Translated value of VRD1 from the  SP2 camForth"
    ),


    Key('SP2RVRD3Err',
        Int(strFormat='%.3f'),
        help = "Translated value of VRD1 from the  SP2 camForth"
    ),


    Key('SP2RVRD3Tolerance',
        Int(strFormat='%.3f'),
        help = "Translated value of VRD1 from the  SP2 camForth"
    )
)