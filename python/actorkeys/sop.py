KeysDictionary("sop", (1,20),
    # misc
    Key("version", String(help="EUPS/SVN version")),
    Key("text", String(), help="text for humans"),
    
    # The archiver allocates enough space for the largest possible list...
    Key("bypassNames",
       String()*(1,25),
       help="names of the systems whose errors can be ignored. Matches the values in the 'bypass' keyword"),
    Key("bypassed",
       Bool(0,1)*(1,25),
       help="Which of the bypassNamed subsystems are being ignored"),
    
    Key("surveyCommands", String()*(1,12),
        help="List of SOP commands which are appropriate to and required for the loaded plate's operations"),
               
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
    
    Key("doBossCalibsStages", String()*(1,6), help="names of the doBossCalibs stages"),
    Key("doBossCalibsState",
        Enum('idle',                'running','done','failed','aborted',
             help="state of the entire command"),
        String("text", help="perhaps useful text to be displayed"),
        Enum('idle','off','pending','running','done','failed','aborted',
             help="state of all the individual stages of this command, " + \
             "as identified by the commandStages keyword.")*(1,6)),
    
    Key("doBossCalibs_nBias", Int(help="index of the active bias"), Int(help="number of biases requested")),
    Key("doBossCalibs_nDark", Int(help="index of the active dark"), Int(help="number of darks requested")),
    Key("doBossCalibs_nFlat", Int(help="index of the active flat"), Int(help="number of flats requested")),
    Key("doBossCalibs_nArc", Int(help="index of the active arc"), Int(help="number of arces requested")),
    
    Key("doBossCalibs_darkTime", Float(help="flat exposure time", units="sec"), Float(help="default value", units="sec")),
    Key("doBossCalibs_arcTime", Float(help="arc exposure time", units="sec"), Float(help="default value", units="sec")),
    Key("doBossCalibs_flatTime", Float(help="flat exposure time", units="sec"), Float(help="default value", units="sec")),
    Key("doBossCalibs_guiderFlatTime", Float(help="guider flat exposure time", units="sec"), Float(help="default value", units="sec")),
    
    Key("doBossScienceStages", String()*(1,6), help="names of the doBossScience stages"),
    Key("doBossScienceState",
        Enum('idle',                'running','done','failed','aborted',
             help="state of the entire command"),
        String("text", help="perhaps useful text to be displayed"),
        Enum('idle','off','pending','running','done','failed','aborted',
             help="state of all the individual stages of this command, " + \
             "as identified by the commandStages keyword.")*(1,6)),
    
    Key("doBossScience_nExp", Int(help="index of the active exposure"), Int(help="number of exposures completed")),
    Key("doBossScience_expTime", Float(help="exposure time", units="sec"), Float(help="default", units="sec")),

    Key("doMangaDitherStages", String()*(1,6), help="names of the doMangaDither stages"),
    Key("doMangaDitherState",
       Enum('idle',                'running','done','failed','aborted',
            help="state of the entire command"),
       String("text", help="perhaps useful text to be displayed"),
       Enum('idle','off','pending','running','done','failed','aborted',
            help="state of all the individual stages of this command, " + \
                 "as identified by the commandStages keyword.")*(1,6)),
    
    Key("doMangaDither_dither", String(help="requested mangaDither position"), String(help="default mangaDither position")),
    Key("doMangaDither_expTime", Float(help="exposure time", units="sec"), Float(help="default exposure time", units="sec")),
    
    Key("doMangaSequenceStages", String()*(1,6), help="names of the doMangaSequence stages"),
    Key("doMangaSequenceState",
       Enum('idle',                'running','done','failed','aborted',
            help="state of the entire command"),
       String("text", help="perhaps useful text to be displayed"),
       Enum('idle','off','pending','running','done','failed','aborted',
            help="state of all the individual stages of this command, " + \
                 "as identified by the commandStages keyword.")*(1,6)),

    Key("doMangaSequence_count", Int(help="number of dither sets requested"), Int(help="default number of dither sets")),
    Key("doMangaSequence_dithers", String(help="manga dithers requested"), String(help="default manga dithers")),
    Key("doMangaSequence_expTime", Float(help="exposure time", units="sec"), Float(help="default exposure time", units="sec")),
    Key("doMangaSequence_arcTime", Float(help="mid-sequence arc exposure time", units="sec"), Float(help="default arc exposure time", units="sec")),

    Key("doMangaSequence_ditherSeq", String(help="Total dither sequence"), String(help="dithers completed"), Int(help="index of currently-operating dither")),
               
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
    Key("doApogeeScience_comment", String(help="For some FITS headers"), String(help="default value")),

    Key("doApogeeDomeFlatStages", String()*(1,6), help="names of the doApogeeDomeFlat stages"),
    Key("doApogeeDomeFlatState",
       Enum('idle',                'running','done','failed','aborted',
            help="state of the entire command"),
       String("text", help="perhaps useful text to be displayed"),
       Enum('idle','off','pending','running','done','failed','aborted',
            help="state of all the individual stages of this command, " + \
                 "as identified by the commandStages keyword.")*(1,6)),
    
    Key("doApogeeSkyFlatsStages", String()*(1,6), help="names of the doApogeeSkyFlats stages"),
    Key("doApogeeSkyFlatsState",
       Enum('idle',                'running','done','failed','aborted',
            help="state of the entire command"),
       String("text", help="perhaps useful text to be displayed"),
       Enum('idle','off','pending','running','done','failed','aborted',
            help="state of all the individual stages of this command, " + \
                 "as identified by the commandStages keyword.")*(1,6)),
    
    Key("doApogeeSkyFlats_ditherSeq", String(help="dither positions in a sequence"), String(help="default dither sequence")),
    Key("doApogeeSkyFlats_expTime", Float(help="exposure time", units="sec"), Float(help="default", units="sec")),
    Key("doApogeeSkyFlats_sequenceState", String(help="full exposure sequence. Basically ditherSeq * seqCount"),
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
    Key("gotoField_guiderTime", Float(help="guider exposure time", units="sec"), Float(help="default value", units="sec")),
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
    Key("gotoGangChange_alt",
        Float(help="desired altitude to slew to", units="deg"),
        Float(help="default", units="deg")),
    
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

    Key("availableScripts", String("name")*(1,),
        help="List of available SOP scripts."),
    Key("scriptState",
        String("name",help="Name of currently active SOP script."),
        Int("atStep",help="Currently active line number."),
        Int("length",help="Total length of this script."),
        Enum('idle','aborted','stopped','done','running',help="Current state of this script."),
        String("currentLine",help="The currently active line as a string."),
        help="status of currently active SOP script."),
    Key("scriptLine",
        String("name",help="Name of currently active SOP script."),
        Int("atStep",help="Line number."),
        Float("maxTime",help="Maximum time allowed for this step."),
        String("line",help="This script line as a string."),
        help="lines in currently active SOP script."),
)
