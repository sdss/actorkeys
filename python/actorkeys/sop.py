#def makeCommandKeys(name, stages):
#    stateKey = Key("%sState" % (name),
#                   Enum('idle',                'running','done','failed','aborted',
#                        help="state of the entire command"),
#                   Enum('idle','off','pending','running','done','failed','aborted',
#                        help="""state of all the individual stages of this command, as 
#                                identified by the commandStages keyword.""")*(len(stages)))
#    stagesKey = Key("%sStages" % (name),
#                    String("commandName", help="the name of the sop command"),
#                    [String(s) for s in stages])
#
#    return stateKey, stagesKey

KeysDictionary("sop", (1,7),
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

               Key("gotoFieldState",
                   Enum('idle',                'running','done','failed','aborted',
                        help="state of the entire command"),
                   Enum('idle','off','pending','running','done','failed','aborted',
                        help="""state of all the individual stages of this command, as 
                                identified by the commandStages keyword.""")*4,
                   String("text", help="perhaps useful text to be displayed")),
               Key("gotoFieldStages",
                   String("slew"),
                   String("hartmann"),
                   String("calibs"),
                   String("guider"),
                   help="the names of the gotoField stages"),

               Key("gotoField_nArc", Int(help="number of arcs completed"), Int(help="number of arcs requested")),
               Key("gotoField_nFlat", Int(help="number of flats completed"), Int(help="number of flats requested")),
               Key("gotoField_arcTime", Float(help="arc exposure time")),
               Key("gotoField_flatTime", Float(help="flat exposure time")),
               Key("gotoField_guiderExpTime", Float(help="guider exposure time")),
               Key("gotoField_guiderFlatTime", Float(help="guider flat exposure time")),
               
               )
