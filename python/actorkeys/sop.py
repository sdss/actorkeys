KeysDictionary("sop", (1,11),
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
               )
