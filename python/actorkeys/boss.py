KeysDictionary("boss",(1,2),
    # ICC Keywords
    Key('exposureState',
        Enum('IDLE','FLUSHING','INTEGRATING','PAUSED','ReadING'),
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
    Key('camForthVersion',
        String()*2,
        help = "Version strings for the cam micros."
        ),
    
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


    Key('SP2RVLG4Bias',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VT+ from the  SP2 camForth"
    ),


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

)
