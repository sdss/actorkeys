KeysDictionary("boss",(1,2),
    # ICC Keywords
    Key('ExposureState',
        Enum('IDLE','FLUSHING','INTEGRATING','PAUSED','READING'),
        help='The current state of the exposure.'
    ),
    Key('HardwareStatus',
        Bits('sp1cam','sp2cam','sp1mech','sp2mech','sp1daq','sp2daq'),
        help='Connection status of each current piece of hardware.'
    ),
    # specMech Keywords
    Key('ShutterStatus',
        Bits('sp1Shutter','sp2Shutter'),
        help = "Status of the shutters, 0 closed, 1 open."
    ),
    Key('ScreenStatus',
        Bits('sp1Left','sp1Right','sp2Left','sp2Right'),
        help = "Status of the hartman screens, 0 out, 1 in."
        ),
    Key('MotorPosition',
        Int()*6,
        help = "The position of the motors in ticks of both spectographs."
        ),
    Key('MotorStatus',
        Bits('OnTarget','LimitSwitch','MotorOff','SlewMode',':1','Slave','FindEdge','Stopped')*6,
        help = "Status of the motors. Six to represent sp1MotorA-sp2MotorC."
        ),
    Key('SpecMechVersion',
        String()*2,
        help = "Version string of sp1mech and sp2mech."
        ),
    # DAQ Keywords
    # Cam Micro Keywords
    Key('CamForthVersion',
        String()*2,
        help = "Version strings for the cam micros."
        ),
    
    Key('SP1BVPcDREAD',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3+ from the  SP1 camForth"
    ),


    Key('SP1BVPcDNOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3+ from the  SP1 camForth"
    ),


    Key('SP1BVPcDBIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3+ from the  SP1 camForth"
    ),


    Key('SP2BVPcDREAD',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3+ from the  SP2 camForth"
    ),


    Key('SP2BVPcDNOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3+ from the  SP2 camForth"
    ),


    Key('SP2BVPcDBIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3+ from the  SP2 camForth"
    ),


    Key('SP1BVSc2READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS+ from the  SP1 camForth"
    ),


    Key('SP1BVSc2NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS+ from the  SP1 camForth"
    ),


    Key('SP1BVSc2BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS+ from the  SP1 camForth"
    ),


    Key('SP2BVSc2READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS+ from the  SP2 camForth"
    ),


    Key('SP2BVSc2NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS+ from the  SP2 camForth"
    ),


    Key('SP2BVSc2BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS+ from the  SP2 camForth"
    ),


    Key('SP1BINegTrim3READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM1 from the  SP1 camForth"
    ),


    Key('SP1BINegTrim3NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM1 from the  SP1 camForth"
    ),


    Key('SP1BINegTrim3BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM1 from the  SP1 camForth"
    ),


    Key('SP2BINegTrim3READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM1 from the  SP2 camForth"
    ),


    Key('SP2BINegTrim3NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM1 from the  SP2 camForth"
    ),


    Key('SP2BINegTrim3BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM1 from the  SP2 camForth"
    ),


    Key('SP1BVRoffREAD',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VSW- from the  SP1 camForth"
    ),


    Key('SP1BVRoffNOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VSW- from the  SP1 camForth"
    ),


    Key('SP1BVRoffBIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VSW- from the  SP1 camForth"
    ),


    Key('SP2BVRoffREAD',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VSW- from the  SP2 camForth"
    ),


    Key('SP2BVRoffNOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VSW- from the  SP2 camForth"
    ),


    Key('SP2BVRoffBIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VSW- from the  SP2 camForth"
    ),


    Key('SP1BVPbDREAD',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3- from the  SP1 camForth"
    ),


    Key('SP1BVPbDNOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3- from the  SP1 camForth"
    ),


    Key('SP1BVPbDBIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3- from the  SP1 camForth"
    ),


    Key('SP2BVPbDREAD',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3- from the  SP2 camForth"
    ),


    Key('SP2BVPbDNOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3- from the  SP2 camForth"
    ),


    Key('SP2BVPbDBIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3- from the  SP2 camForth"
    ),


    Key('SP1BINegTrim4READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM2 from the  SP1 camForth"
    ),


    Key('SP1BINegTrim4NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM2 from the  SP1 camForth"
    ),


    Key('SP1BINegTrim4BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM2 from the  SP1 camForth"
    ),


    Key('SP2BINegTrim4READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM2 from the  SP2 camForth"
    ),


    Key('SP2BINegTrim4NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM2 from the  SP2 camForth"
    ),


    Key('SP2BINegTrim4BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM2 from the  SP2 camForth"
    ),


    Key('SP1BIPosTrim4READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM2 from the  SP1 camForth"
    ),


    Key('SP1BIPosTrim4NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM2 from the  SP1 camForth"
    ),


    Key('SP1BIPosTrim4BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM2 from the  SP1 camForth"
    ),


    Key('SP2BIPosTrim4READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM2 from the  SP2 camForth"
    ),


    Key('SP2BIPosTrim4NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM2 from the  SP2 camForth"
    ),


    Key('SP2BIPosTrim4BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM2 from the  SP2 camForth"
    ),


    Key('SP1BIPosTrim3READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM1 from the  SP1 camForth"
    ),


    Key('SP1BIPosTrim3NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM1 from the  SP1 camForth"
    ),


    Key('SP1BIPosTrim3BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM1 from the  SP1 camForth"
    ),


    Key('SP2BIPosTrim3READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM1 from the  SP2 camForth"
    ),


    Key('SP2BIPosTrim3NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM1 from the  SP2 camForth"
    ),


    Key('SP2BIPosTrim3BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM1 from the  SP2 camForth"
    ),


    Key('SP1BVDD3READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD1 from the  SP1 camForth"
    ),


    Key('SP1BVDD3NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD1 from the  SP1 camForth"
    ),


    Key('SP1BVDD3BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD1 from the  SP1 camForth"
    ),


    Key('SP2BVDD3READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD1 from the  SP2 camForth"
    ),


    Key('SP2BVDD3NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD1 from the  SP2 camForth"
    ),


    Key('SP2BVDD3BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD1 from the  SP2 camForth"
    ),


    Key('SP1BVLG34READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VLG from the  SP1 camForth"
    ),


    Key('SP1BVLG34NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VLG from the  SP1 camForth"
    ),


    Key('SP1BVLG34BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VLG from the  SP1 camForth"
    ),


    Key('SP2BVLG34READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VLG from the  SP2 camForth"
    ),


    Key('SP2BVLG34NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VLG from the  SP2 camForth"
    ),


    Key('SP2BVLG34BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VLG from the  SP2 camForth"
    ),


    Key('SP1BVSb2READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS- from the  SP1 camForth"
    ),


    Key('SP1BVSb2NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS- from the  SP1 camForth"
    ),


    Key('SP1BVSb2BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS- from the  SP1 camForth"
    ),


    Key('SP2BVSb2READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS- from the  SP2 camForth"
    ),


    Key('SP2BVSb2NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS- from the  SP2 camForth"
    ),


    Key('SP2BVSb2BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS- from the  SP2 camForth"
    ),


    Key('SP1BVDD4READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD2 from the  SP1 camForth"
    ),


    Key('SP1BVDD4NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD2 from the  SP1 camForth"
    ),


    Key('SP1BVDD4BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD2 from the  SP1 camForth"
    ),


    Key('SP2BVDD4READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD2 from the  SP2 camForth"
    ),


    Key('SP2BVDD4NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD2 from the  SP2 camForth"
    ),


    Key('SP2BVDD4BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD2 from the  SP2 camForth"
    ),


    Key('SP1BVRD4READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD2 from the  SP1 camForth"
    ),


    Key('SP1BVRD4NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD2 from the  SP1 camForth"
    ),


    Key('SP1BVRD4BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD2 from the  SP1 camForth"
    ),


    Key('SP2BVRD4READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD2 from the  SP2 camForth"
    ),


    Key('SP2BVRD4NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD2 from the  SP2 camForth"
    ),


    Key('SP2BVRD4BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD2 from the  SP2 camForth"
    ),


    Key('SP1BHeaterVREAD',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of HEATERV from the  SP1 camForth"
    ),


    Key('SP1BHeaterVNOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of HEATERV from the  SP1 camForth"
    ),


    Key('SP1BHeaterVBIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of HEATERV from the  SP1 camForth"
    ),


    Key('SP2BHeaterVREAD',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of HEATERV from the  SP2 camForth"
    ),


    Key('SP2BHeaterVNOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of HEATERV from the  SP2 camForth"
    ),


    Key('SP2BHeaterVBIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of HEATERV from the  SP2 camForth"
    ),


    Key('SP1BVPcCREAD',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12+ from the  SP1 camForth"
    ),


    Key('SP1BVPcCNOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12+ from the  SP1 camForth"
    ),


    Key('SP1BVPcCBIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12+ from the  SP1 camForth"
    ),


    Key('SP2BVPcCREAD',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12+ from the  SP2 camForth"
    ),


    Key('SP2BVPcCNOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12+ from the  SP2 camForth"
    ),


    Key('SP2BVPcCBIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12+ from the  SP2 camForth"
    ),


    Key('SP1BVPbCREAD',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12- from the  SP1 camForth"
    ),


    Key('SP1BVPbCNOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12- from the  SP1 camForth"
    ),


    Key('SP1BVPbCBIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12- from the  SP1 camForth"
    ),


    Key('SP2BVPbCREAD',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12- from the  SP2 camForth"
    ),


    Key('SP2BVPbCNOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12- from the  SP2 camForth"
    ),


    Key('SP2BVPbCBIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12- from the  SP2 camForth"
    ),


    Key('SP1BVRD3READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD1 from the  SP1 camForth"
    ),


    Key('SP1BVRD3NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD1 from the  SP1 camForth"
    ),


    Key('SP1BVRD3BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD1 from the  SP1 camForth"
    ),


    Key('SP2BVRD3READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD1 from the  SP2 camForth"
    ),


    Key('SP2BVRD3NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD1 from the  SP2 camForth"
    ),


    Key('SP2BVRD3BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD1 from the  SP2 camForth"
    ),


    Key('SP1RVERASEREAD',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3+ from the  SP1 camForth"
    ),


    Key('SP1RVERASENOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3+ from the  SP1 camForth"
    ),


    Key('SP1RVERASEBIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3+ from the  SP1 camForth"
    ),


    Key('SP2RVERASEREAD',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3+ from the  SP2 camForth"
    ),


    Key('SP2RVERASENOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3+ from the  SP2 camForth"
    ),


    Key('SP2RVERASEBIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3+ from the  SP2 camForth"
    ),


    Key('SP1RVSc2READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS+ from the  SP1 camForth"
    ),


    Key('SP1RVSc2NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS+ from the  SP1 camForth"
    ),


    Key('SP1RVSc2BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS+ from the  SP1 camForth"
    ),


    Key('SP2RVSc2READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS+ from the  SP2 camForth"
    ),


    Key('SP2RVSc2NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS+ from the  SP2 camForth"
    ),


    Key('SP2RVSc2BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS+ from the  SP2 camForth"
    ),


    Key('SP1RINegTrim3READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM1 from the  SP1 camForth"
    ),


    Key('SP1RINegTrim3NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM1 from the  SP1 camForth"
    ),


    Key('SP1RINegTrim3BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM1 from the  SP1 camForth"
    ),


    Key('SP2RINegTrim3READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM1 from the  SP2 camForth"
    ),


    Key('SP2RINegTrim3NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM1 from the  SP2 camForth"
    ),


    Key('SP2RINegTrim3BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM1 from the  SP2 camForth"
    ),


    Key('SP1RVRonREAD',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VSW- from the  SP1 camForth"
    ),


    Key('SP1RVRonNOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VSW- from the  SP1 camForth"
    ),


    Key('SP1RVRonBIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VSW- from the  SP1 camForth"
    ),


    Key('SP2RVRonREAD',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VSW- from the  SP2 camForth"
    ),


    Key('SP2RVRonNOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VSW- from the  SP2 camForth"
    ),


    Key('SP2RVRonBIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VSW- from the  SP2 camForth"
    ),


    Key('SP1RVPURGREAD',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3- from the  SP1 camForth"
    ),


    Key('SP1RVPURGNOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3- from the  SP1 camForth"
    ),


    Key('SP1RVPURGBIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3- from the  SP1 camForth"
    ),


    Key('SP2RVPURGREAD',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3- from the  SP2 camForth"
    ),


    Key('SP2RVPURGNOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3- from the  SP2 camForth"
    ),


    Key('SP2RVPURGBIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP3- from the  SP2 camForth"
    ),


    Key('SP1RINegTrim4READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM2 from the  SP1 camForth"
    ),


    Key('SP1RINegTrim4NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM2 from the  SP1 camForth"
    ),


    Key('SP1RINegTrim4BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM2 from the  SP1 camForth"
    ),


    Key('SP2RINegTrim4READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM2 from the  SP2 camForth"
    ),


    Key('SP2RINegTrim4NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM2 from the  SP2 camForth"
    ),


    Key('SP2RINegTrim4BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I-TRIM2 from the  SP2 camForth"
    ),


    Key('SP1RVSR2READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS- from the  SP1 camForth"
    ),


    Key('SP1RVSR2NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS- from the  SP1 camForth"
    ),


    Key('SP1RVSR2BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS- from the  SP1 camForth"
    ),


    Key('SP2RVSR2READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS- from the  SP2 camForth"
    ),


    Key('SP2RVSR2NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS- from the  SP2 camForth"
    ),


    Key('SP2RVSR2BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VS- from the  SP2 camForth"
    ),


    Key('SP1RIPosTrim4READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM2 from the  SP1 camForth"
    ),


    Key('SP1RIPosTrim4NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM2 from the  SP1 camForth"
    ),


    Key('SP1RIPosTrim4BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM2 from the  SP1 camForth"
    ),


    Key('SP2RIPosTrim4READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM2 from the  SP2 camForth"
    ),


    Key('SP2RIPosTrim4NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM2 from the  SP2 camForth"
    ),


    Key('SP2RIPosTrim4BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM2 from the  SP2 camForth"
    ),


    Key('SP1RIPosTrim3READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM1 from the  SP1 camForth"
    ),


    Key('SP1RIPosTrim3NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM1 from the  SP1 camForth"
    ),


    Key('SP1RIPosTrim3BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM1 from the  SP1 camForth"
    ),


    Key('SP2RIPosTrim3READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM1 from the  SP2 camForth"
    ),


    Key('SP2RIPosTrim3NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM1 from the  SP2 camForth"
    ),


    Key('SP2RIPosTrim3BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of I+TRIM1 from the  SP2 camForth"
    ),


    Key('SP1RVDD3READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD1 from the  SP1 camForth"
    ),


    Key('SP1RVDD3NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD1 from the  SP1 camForth"
    ),


    Key('SP1RVDD3BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD1 from the  SP1 camForth"
    ),


    Key('SP2RVDD3READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD1 from the  SP2 camForth"
    ),


    Key('SP2RVDD3NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD1 from the  SP2 camForth"
    ),


    Key('SP2RVDD3BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD1 from the  SP2 camForth"
    ),


    Key('SP1RVLG3READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VT- from the  SP1 camForth"
    ),


    Key('SP1RVLG3NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VT- from the  SP1 camForth"
    ),


    Key('SP1RVLG3BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VT- from the  SP1 camForth"
    ),


    Key('SP2RVLG3READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VT- from the  SP2 camForth"
    ),


    Key('SP2RVLG3NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VT- from the  SP2 camForth"
    ),


    Key('SP2RVLG3BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VT- from the  SP2 camForth"
    ),


    Key('SP1RVLG2READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VLG from the  SP1 camForth"
    ),


    Key('SP1RVLG2NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VLG from the  SP1 camForth"
    ),


    Key('SP1RVLG2BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VLG from the  SP1 camForth"
    ),


    Key('SP2RVLG2READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VLG from the  SP2 camForth"
    ),


    Key('SP2RVLG2NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VLG from the  SP2 camForth"
    ),


    Key('SP2RVLG2BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VLG from the  SP2 camForth"
    ),


    Key('SP1RVPcCREAD',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12- from the  SP1 camForth"
    ),


    Key('SP1RVPcCNOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12- from the  SP1 camForth"
    ),


    Key('SP1RVPcCBIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12- from the  SP1 camForth"
    ),


    Key('SP2RVPcCREAD',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12- from the  SP2 camForth"
    ),


    Key('SP2RVPcCNOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12- from the  SP2 camForth"
    ),


    Key('SP2RVPcCBIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12- from the  SP2 camForth"
    ),


    Key('SP1RVSUBSREAD',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VR from the  SP1 camForth"
    ),


    Key('SP1RVSUBSNOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VR from the  SP1 camForth"
    ),


    Key('SP1RVSUBSBIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VR from the  SP1 camForth"
    ),


    Key('SP2RVSUBSREAD',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VR from the  SP2 camForth"
    ),


    Key('SP2RVSUBSNOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VR from the  SP2 camForth"
    ),


    Key('SP2RVSUBSBIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VR from the  SP2 camForth"
    ),


    Key('SP1RVDD4READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD2 from the  SP1 camForth"
    ),


    Key('SP1RVDD4NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD2 from the  SP1 camForth"
    ),


    Key('SP1RVDD4BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD2 from the  SP1 camForth"
    ),


    Key('SP2RVDD4READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD2 from the  SP2 camForth"
    ),


    Key('SP2RVDD4NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD2 from the  SP2 camForth"
    ),


    Key('SP2RVDD4BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VDD2 from the  SP2 camForth"
    ),


    Key('SP1RVRD4READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD2 from the  SP1 camForth"
    ),


    Key('SP1RVRD4NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD2 from the  SP1 camForth"
    ),


    Key('SP1RVRD4BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD2 from the  SP1 camForth"
    ),


    Key('SP2RVRD4READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD2 from the  SP2 camForth"
    ),


    Key('SP2RVRD4NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD2 from the  SP2 camForth"
    ),


    Key('SP2RVRD4BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD2 from the  SP2 camForth"
    ),


    Key('SP1RHeaterVREAD',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of HEATERV from the  SP1 camForth"
    ),


    Key('SP1RHeaterVNOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of HEATERV from the  SP1 camForth"
    ),


    Key('SP1RHeaterVBIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of HEATERV from the  SP1 camForth"
    ),


    Key('SP2RHeaterVREAD',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of HEATERV from the  SP2 camForth"
    ),


    Key('SP2RHeaterVNOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of HEATERV from the  SP2 camForth"
    ),


    Key('SP2RHeaterVBIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of HEATERV from the  SP2 camForth"
    ),


    Key('SP1RVPRCREAD',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12+ from the  SP1 camForth"
    ),


    Key('SP1RVPRCNOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12+ from the  SP1 camForth"
    ),


    Key('SP1RVPRCBIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12+ from the  SP1 camForth"
    ),


    Key('SP2RVPRCREAD',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12+ from the  SP2 camForth"
    ),


    Key('SP2RVPRCNOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12+ from the  SP2 camForth"
    ),


    Key('SP2RVPRCBIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VP12+ from the  SP2 camForth"
    ),


    Key('SP1RVLG4READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VT+ from the  SP1 camForth"
    ),


    Key('SP1RVLG4NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VT+ from the  SP1 camForth"
    ),


    Key('SP1RVLG4BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VT+ from the  SP1 camForth"
    ),


    Key('SP2RVLG4READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VT+ from the  SP2 camForth"
    ),


    Key('SP2RVLG4NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VT+ from the  SP2 camForth"
    ),


    Key('SP2RVLG4BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VT+ from the  SP2 camForth"
    ),


    Key('SP1RVRD3READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD1 from the  SP1 camForth"
    ),


    Key('SP1RVRD3NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD1 from the  SP1 camForth"
    ),


    Key('SP1RVRD3BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD1 from the  SP1 camForth"
    ),


    Key('SP2RVRD3READ',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD1 from the  SP2 camForth"
    ),


    Key('SP2RVRD3NOM',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD1 from the  SP2 camForth"
    ),


    Key('SP2RVRD3BIAS',
        Float(units='volts',strFormat='%.3f'),
        help = "Translated value of VRD1 from the  SP2 camForth"
    ),

)
