KeysDictionary("sop", (1,15),
    # misc
    Key("version", String(help="EUPS/SVN version")),
    Key("text", String(), help="text for humans"),
    
    # The archiver allocates enough space for the largest possible list...
    Key("bypassNames",
       String()*(1,9),
       help="names of the systems whose errors can be ignored. Matches the values in the 'bypass' keyword"),
    Key("bypassed",
       Bool(0,1)*(1,9),
       help="Which of the bypassNamed subsystems are being ignored"),
    
    Key("surveyCommands", String()*(1,8),
        help="List of SOP commands which are appropriate to and required for the loaded plate's  operations"),
               
    Key("subStageState",
       String("subStageName", 
              help="""dotted name of a substage. The name will always 
                      start with the commandName.stageName"""),
       Enum('starting', 'prepping', 'running', 'done', 'failed', 'aborted',
            help="the state of this substage."),
    
       Float("startTime", units="sec", 
             help="start of the substage, in MJD TAI seconds"),
       Float("duration", units="sec", 
             help="expected duration for the substage. If short or unknown, 0.0"),
       String("text", help="perhaps useful text to be displayed"),
       doCache=False),                   
    
    Key("doCalibsStages", String()*(1,6), help="names of the doCalibs stages"),
    Key("doCalibsState",
       Enum('idle',                'running','done','failed','aborted',
            help="state of the entire command"),
       String("text", help="perhaps useful text to be displayed"),
       Enum('idle','off','pending','running','done','failed','aborted',
            help="state of all the individual stages of this command, " + \
                 "as identified by the commandStages keyword.")*(1,6)),
    
    Key("doCalibs_nBias", Int(help="index of the active bias"), Int(help="number of biases requested")),
    Key("doCalibs_nDark", Int(help="index of the active dark"), Int(help="number of darks requested")),
    Key("doCalibs_nFlat", Int(help="index of the active flat"), Int(help="number of flats requested")),
    Key("doCalibs_nArc", Int(help="index of the active arc"), Int(help="number of arces requested")),
    
    Key("doCalibs_darkTime", Float(help="flat exposure time", units="sec"), Float(help="default value", units="sec")),
    Key("doCalibs_arcTime", Float(help="arc exposure time", units="sec"), Float(help="default value", units="sec")),
    Key("doCalibs_flatTime", Float(help="flat exposure time", units="sec"), Float(help="default value", units="sec")),
    Key("doCalibs_guiderFlatTime", Float(help="guider flat exposure time", units="sec"), Float(help="default value", units="sec")),
    
    Key("doScienceStages", String()*(1,6), help="names of the doScience stages"),
    Key("doScienceState",
       Enum('idle',                'running','done','failed','aborted',
            help="state of the entire command"),
       String("text", help="perhaps useful text to be displayed"),
       Enum('idle','off','pending','running','done','failed','aborted',
            help="state of all the individual stages of this command, " + \
                 "as identified by the commandStages keyword.")*(1,6)),
    
    Key("doScience_nExp", Int(help="index of the active exposure"), Int(help="number of exposures completed")),
    Key("doScience_expTime", Float(help="exposure time", units="sec"), Float(help="default", units="sec")),
    
    Key("doApogeeScienceStages", String()*(1,6), help="names of the doApogeeScience stages"),
    Key("doApogeeScienceState",
       Enum('idle',                'running','done','failed','aborted',
            help="state of the entire command"),
       String("text", help="perhaps useful text to be displayed"),
       Enum('idle','off','pending','running','done','failed','aborted',
            help="state of all the individual stages of this command, " + \
                 "as identified by the commandStages keyword.")*(1,6)),
    
    Key("doApogeeScience_ditherSeq", String(help="dither positions in a sequence"), String(help="default dither sequence")),
    Key("doApogeeScience_seqCount", Int(help="number of times to run ditherSeq"), Int(help="default")),
    Key("doApogeeScience_expTime", Float(help="exposure time", units="sec"), Float(help="default", units="sec")),
    Key("doApogeeScience_sequenceState", String(help="full exposure sequence. Basically ditherSeq * seqCount"),
        Int(help="index of running exposure")),
    
    Key("gotoFieldStages", String()*(1,6), help="names of the gotoField stages"),
    Key("gotoFieldState",
       Enum('idle',                'running','done','failed','aborted',
            help="state of the entire command"),
       String("text", help="perhaps useful text to be displayed"),
       Enum('idle','off','pending','running','done','failed','aborted',
            help="state of all the individual stages of this command, " + \
                 "as identified by the commandStages keyword.")*(1,6)),
    
    Key("gotoField_arcTime", Float(help="arc exposure time", units="sec"), Float(help="default value", units="sec")),
    Key("gotoField_flatTime", Float(help="flat exposure time", units="sec"), Float(help="default value", units="sec")),
    Key("gotoField_guiderExpTime", Float(help="guider exposure time", units="sec"), Float(help="default value", units="sec")),
    Key("gotoField_guiderFlatTime", Float(help="guider flat exposure time", units="sec"), Float(help="default value", units="sec")),
    
    Key("gotoInstrumentChangeStages", String()*(1,6), help="names of the gotoInstrumentChange stages"),
    Key("gotoInstrumentChangeState",
       Enum('idle',                'running','done','failed','aborted',
            help="state of the entire command"),
       String("text", help="perhaps useful text to be displayed"),
       Enum('idle','off','pending','running','done','failed','aborted',
            help="state of all the individual stages of this command, " + \
                 "as identified by the commandStages keyword.")*(1,6)),

    Key("gotoStowStages", String()*(1,6), help="names of the gotoStow stages"),
    Key("gotoStowState",
       Enum('idle',                'running','done','failed','aborted',
            help="state of the entire command"),
       String("text", help="perhaps useful text to be displayed"),
       Enum('idle','off','pending','running','done','failed','aborted',
            help="state of all the individual stages of this command, " + \
                 "as identified by the commandStages keyword.")*(1,6)),
    
    Key("gotoGangChangeStages", String()*(1,6), help="names of the gotoGangChange stages"),
    Key("gotoGangChangeState",
       Enum('idle',                'running','done','failed','aborted',
            help="state of the entire command"),
       String("text", help="perhaps useful text to be displayed"),
       Enum('idle','off','pending','running','done','failed','aborted',
            help="state of all the individual stages of this command, " + \
                 "as identified by the commandStages keyword.")*(1,6)),
    
    Key("ditheredFlatChangeStages", String()*(1,6), help="names of the ditheredFlatChange stages"),
    Key("ditheredFlatChangeState",
       Enum('idle',                'running','done','failed','aborted',
            help="state of the entire command"),
       String("text", help="perhaps useful text to be displayed"),
       Enum('idle','off','pending','running','done','failed','aborted',
            help="state of all the individual stages of this command, " + \
                 "as identified by the commandStages keyword.")*(1,6)),
    
    Key("ditheredFlat_expTime", Float(help="exposure time", units="sec"), Float(help="default", units="sec")),
# MISSING KEYS due to unknown format: nStep, nTick (these want defaults!), sp1 and sp2
    
    Key("hartmannStages", String()*(1,6), help="names of the hartmann stages"),
    Key("hartmannState",
       Enum('idle',                'running','done','failed','aborted',
            help="state of the entire command"),
       String("text", help="perhaps useful text to be displayed"),
       Enum('idle','off','pending','running','done','failed','aborted',
            help="state of all the individual stages of this command, " + \
                 "as identified by the commandStages keyword.")*(1,6)),
    
    Key("hartmann_expTime", Float(help="exposure time", units="sec"), Float(help="default", units="sec")),
# MISSING KEYS due to unknown format: sp1 and sp2
    
    Key("lampsOffStages", String()*(1,6), help="names of the lampsOff stages"),
    Key("lampsOffState",
       Enum('idle',                'running','done','failed','aborted',
            help="state of the entire command"),
       String("text", help="perhaps useful text to be displayed"),
       Enum('idle','off','pending','running','done','failed','aborted',
            help="state of all the individual stages of this command, " + \
                 "as identified by the commandStages keyword.")*(1,6)),
    
    Key("setScaleStages", String()*(1,6), help="names of the setScale stages"),
    Key("setScaleState",
       Enum('idle',                'running','done','failed','aborted',
            help="state of the entire command"),
       String("text", help="perhaps useful text to be displayed"),
       Enum('idle','off','pending','running','done','failed','aborted',
            help="state of all the individual stages of this command, " + \
                 "as identified by the commandStages keyword.")*(1,6)),
    
    Key("setScale_delta", Float(name="delta", help="change scale by (1 + 0.01*delta)", units="%"), Float(help="default value", units="%")),
    
)
