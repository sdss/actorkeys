KeysDictionary("sop", (2,1),
    # misc
    Key("version", String(help="EUPS/SVN version")),
    Key("text", String(), help="text for humans"),
    
    # The archiver allocates enough space for the largest possible list...
    Key("bypassNames",
       String()*(1,25),
       help="names of the systems whose errors can be ignored. Matches the values in the 'bypass' keyword"),
    Key("bypassed",
       Bool(0,1)*(1,25),
       help="Which of the bypassNamed subsystems are being ignored (deprecated by bypasedNames)"),
    Key("bypassedNames",
       String()*(0,25),
       help="List of named systems currently being bypassed."),

    Key("surveyCommands", String()*(1,12),
        help="List of SOP commands which are appropriate to and required for the loaded plate's operations"),
    
    Key("survey",
        String(name="plateType", invalid="?", help="The survey type of this plate."),
        String(name="surveyMode", invalid="?", help="The instrument driving this observation, and its observing mode."),
        help="Which surveys is this plate for, as SOP knows them to be (e.g., with bypasses).",
    ),
    
    Key("doBossCalibsStages", String()*(1,6), help="names of the doBossCalibs stages"),
    Key("doBossCalibsState",
        Enum('idle',                'running','done','failed','aborted',
             help="state of the entire command"),
        String("text", help="perhaps useful text to be displayed"),
        Enum('idle','off','pending','prepping','running','done','failed','aborted',
             help="state of all the individual stages of this command, " + \
             "as identified by the commandStages keyword.")*(1,6)),
    
    Key("doBossCalibs_nBias",
        Int('nBiasDone', help="index of the active bias"),
        Int('nBias', help="number of biases requested")),
    Key("doBossCalibs_nDark",
        Int('nDarkDone', help="index of the active dark"),
        Int('nDark', help="number of darks requested")),
    Key("doBossCalibs_nFlat",
        Int('nFlatDone', help="index of the active flat"),
        Int('nFlat', help="number of flats requested")),
    Key("doBossCalibs_nArc",
        Int('nArcDone', help="index of the active arc"),
        Int('nArc', help="number of arcs requested")),
    
    Key("doBossCalibs_darkTime",
        Float('darkTime', help="flat exposure time", units="sec"),
        Float('default', help="default value", units="sec")),
    Key("doBossCalibs_arcTime",
        Float('arcTime', help="arc exposure time", units="sec"),
        Float('default', help="default value", units="sec")),
    Key("doBossCalibs_flatTime",
        Float('flatTime', help="flat exposure time", units="sec"),
        Float('default', help="default value", units="sec")),
    Key("doBossCalibs_guiderFlatTime",
        Float('guiderFlatTime', help="guider flat exposure time", units="sec"),
        Float('default', help="default value", units="sec")),
    
    Key("doBossScienceStages", String()*(1,6), help="names of the doBossScience stages"),
    Key("doBossScienceState",
        Enum('idle',                'running','done','failed','aborted',
             help="state of the entire command"),
        String("text", help="perhaps useful text to be displayed"),
        Enum('idle','off','pending','prepping','running','done','failed','aborted',
             help="state of all the individual stages of this command, " + \
             "as identified by the commandStages keyword.")*(1,6)),
    
    Key("doBossScience_nExp",
        Int('nExpDone', help="index of the active exposure"),
        Int('nExp', help="number of exposures completed")),
    Key("doBossScience_expTime",
        Float('expTime', help="exposure time", units="sec"),
        Float('default', help="default", units="sec")),

    Key("doMangaDitherStages", String()*(1,6), help="names of the doMangaDither stages"),
    Key("doMangaDitherState",
       Enum('idle',                'running','done','failed','aborted',
            help="state of the entire command"),
       String("text", help="perhaps useful text to be displayed"),
        Enum('idle','off','pending','prepping','running','done','failed','aborted',
            help="state of all the individual stages of this command, " + \
                 "as identified by the commandStages keyword.")*(1,6)),
    
    Key("doMangaDither_dither",
        String('mangaDither', help="requested mangaDither position"),
        String('default', help="default mangaDither position")),
    Key("doMangaDither_expTime",
        Float('expTime', help="exposure time", units="sec"),
        Float('default', help="default exposure time", units="sec")),
    
    Key("doMangaSequenceStages", String()*(1,6), help="names of the doMangaSequence stages"),
    Key("doMangaSequenceState",
       Enum('idle',                'running','done','failed','aborted',
            help="state of the entire command"),
       String("text", help="perhaps useful text to be displayed"),
        Enum('idle','off','pending','prepping','running','done','failed','aborted',
            help="state of all the individual stages of this command, " + \
                 "as identified by the commandStages keyword.")*(1,6)),

    Key("doMangaSequence_count",
        Int('count', help="number of dither sets requested"),
        Int('default', help="default number of dither sets")),
    Key("doMangaSequence_dithers",
        String('dithers', help="manga dithers requested"),
        String('default', help="default manga dithers")),
    Key("doMangaSequence_expTime",
        Float('expTime', help="exposure time", units="sec"),
        Float('default', help="default exposure time", units="sec")),
    Key("doMangaSequence_arcTime",
        Float('arcTime', help="mid-sequence arc exposure time", units="sec"),
        Float('default', help="default arc exposure time", units="sec")),

    Key("doMangaSequence_ditherSeq",
        String('ditherSeq', help="Total dither sequence"),
        Int('index', help="index of currently-operating dither")),

    Key("doApogeeScienceStages", String()*(1,6), help="names of the doApogeeScience stages"),
    Key("doApogeeScienceState",
       Enum('idle',                'running','done','failed','aborted',
            help="state of the entire command"),
       String("text", help="perhaps useful text to be displayed"),
        Enum('idle','off','pending','prepping','running','done','failed','aborted',
            help="state of all the individual stages of this command, " + \
                 "as identified by the commandStages keyword.")*(1,6)),
    
    Key("doApogeeScience_ditherSeq",
        String('ditherSeq', help="dither positions in a sequence"),
        String('default', help="default dither sequence")),
    Key("doApogeeScience_seqCount",
        Int('seqCount', help="number of times to run ditherSeq"),
        Int('default', help="default")),
    Key("doApogeeScience_expTime",
        Float('expTime', help="exposure time", units="sec"),
        Float('default', help="default", units="sec")),
    Key("doApogeeScience_sequenceState",
        String('exposureSeq', help="full exposure sequence. Basically ditherSeq * seqCount"),
        Int('index', help="index of running exposure")),
    Key("doApogeeScience_comment",
        String('comment', help="For some FITS headers"),
        String('default', help="default value")),

    Key("doApogeeDomeFlatStages", String()*(1,6), help="names of the doApogeeDomeFlat stages"),
    Key("doApogeeDomeFlatState",
       Enum('idle',                'running','done','failed','aborted',
            help="state of the entire command"),
       String("text", help="perhaps useful text to be displayed"),
        Enum('idle','off','pending','prepping','running','done','failed','aborted',
            help="state of all the individual stages of this command, " + \
                 "as identified by the commandStages keyword.")*(1,6)),

    Key("doApogeeMangaDitherStages", String()*(1,6), help="names of the doApogeeMangaDither stages"),
    Key("doApogeeMangaDitherState",
       Enum('idle',                'running','done','failed','aborted',
            help="state of the entire command"),
       String("text", help="perhaps useful text to be displayed"),
        Enum('idle','off','pending','prepping','running','done','failed','aborted',
            help="state of all the individual stages of this command, " + \
                 "as identified by the commandStages keyword.")*(1,6)),

    Key("doApogeeMangaDither_mangaDither",
        String('mangaDither', help="requested mangaDither position"),
        String('default', help="default mangaDither position")),
    Key("doApogeeMangaDither_mangaExpTime",
        Float('mangaExpTime', help="MaNGA exposure time", units="sec"),
        Float('default', help="default MaNGA exposure time", units="sec")),
    Key("doApogeeMangaDither_apogeeExpTime",
        Float('apogeeExpTime', help="APOGEE exposure time", units="sec"),
        Float('default', help="APOGEE default exposure time", units="sec")),

    Key("doApogeeMangaSequenceStages", String()*(1,6), help="names of the doApogeeMangaSequence stages"),
    Key("doApogeeMangaSequenceState",
       Enum('idle',                'running','done','failed','aborted',
            help="state of the entire command"),
       String("text", help="perhaps useful text to be displayed"),
        Enum('idle','off','pending','prepping','running','done','failed','aborted',
            help="state of all the individual stages of this command, " + \
                 "as identified by the commandStages keyword.")*(1,6)),

    Key("doApogeeMangaSequence_count",
        Int(help="number of dither sets requested"),
        Int(help="default number of dither sets")),
    Key("doApogeeMangaSequence_mangaDithers",
        String('mangaDithers"', help="MaNGA dithers requested"),
        String('default', help="default MaNGA dithers")),
    Key("doApogeeMangaSequence_mangaExpTime",
        Float('mangaExpTime', help="MaNGA exposure time", units="sec"),
        Float('default', help="MaNGA default exposure time", units="sec")),
    Key("doApogeeMangaSequence_apogeeExpTime",
        Float('apogeeExpTime', help="APOGEE exposure time", units="sec"),
        Float('default', help="APOGEE default exposure time", units="sec")),

    Key("doApogeeMangaSequence_ditherSeq",
        String('mangaDitherSeq', help="Total MaNGA dither sequence"),
        Int('index', help="index of currently-operating MaNGA dither")),
    
    Key("doApogeeSkyFlatsStages", String()*(1,6), help="names of the doApogeeSkyFlats stages"),
    Key("doApogeeSkyFlatsState",
       Enum('idle',                'running','done','failed','aborted',
            help="state of the entire command"),
       String("text", help="perhaps useful text to be displayed"),
        Enum('idle','off','pending','prepping','running','done','failed','aborted',
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
        Enum('idle','off','pending','prepping','running','done','failed','aborted',
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
        Enum('idle','off','pending','prepping','running','done','failed','aborted',
            help="state of all the individual stages of this command, " + \
                 "as identified by the commandStages keyword.")*(1,6)),

    Key("gotoStowStages", String()*(1,6), help="names of the gotoStow stages"),
    Key("gotoStowState",
       Enum('idle',                'running','done','failed','aborted',
            help="state of the entire command"),
       String("text", help="perhaps useful text to be displayed"),
        Enum('idle','off','pending','prepping','running','done','failed','aborted',
            help="state of all the individual stages of this command, " + \
                 "as identified by the commandStages keyword.")*(1,6)),

    Key("gotoGangChangeStages", String()*(1,6), help="names of the gotoGangChange stages"),
    Key("gotoGangChangeState",
       Enum('idle',                'running','done','failed','aborted',
            help="state of the entire command"),
       String("text", help="perhaps useful text to be displayed"),
        Enum('idle','off','pending','prepping','running','done','failed','aborted',
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
        Enum('idle','off','pending','prepping','running','done','failed','aborted',
            help="state of all the individual stages of this command, " + \
                 "as identified by the commandStages keyword.")*(1,6)),
    
    Key("ditheredFlat_expTime", Float(help="exposure time", units="sec"), Float(help="default", units="sec")),
# MISSING KEYS due to unknown format: nStep, nTick (these want defaults!), sp1 and sp2
    
    Key("hartmannStages", String()*(1,6), help="names of the hartmann stages"),
    Key("hartmannState",
       Enum('idle',                'running','done','failed','aborted',
            help="state of the entire command"),
       String("text", help="perhaps useful text to be displayed"),
        Enum('idle','off','pending','prepping','running','done','failed','aborted',
            help="state of all the individual stages of this command, " + \
                 "as identified by the commandStages keyword.")*(1,6)),
    
    Key("hartmann_expTime", Float(help="exposure time", units="sec"), Float(help="default", units="sec")),
# MISSING KEYS due to unknown format: sp1 and sp2
    
    Key("lampsOffStages", String()*(1,6), help="names of the lampsOff stages"),
    Key("lampsOffState",
       Enum('idle',                'running','done','failed','aborted',
            help="state of the entire command"),
       String("text", help="perhaps useful text to be displayed"),
        Enum('idle','off','pending','prepping','running','done','failed','aborted',
            help="state of all the individual stages of this command, " + \
                 "as identified by the commandStages keyword.")*(1,6)),

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
