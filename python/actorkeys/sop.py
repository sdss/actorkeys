KeysDictionary("sop", (1,4),
               # misc
               Key("version", String(help="EUPS/SVN version")),
               Key("text", String(), help="text for humans"),
               Key("bypassed",
                   #CompoundValueType(String(), Bool("False", "True"))*9,
                   CompoundValueType(String(), Bool("False", "True")),
                   CompoundValueType(String(), Bool("False", "True")),
                   CompoundValueType(String(), Bool("False", "True")),
                   CompoundValueType(String(), Bool("False", "True")),
                   CompoundValueType(String(), Bool("False", "True")),
                   CompoundValueType(String(), Bool("False", "True")),
                   CompoundValueType(String(), Bool("False", "True")),
                   CompoundValueType(String(), Bool("False", "True")),
                   CompoundValueType(String(), Bool("False", "True")),
                   help="Which subsystems's failures are being ignored"),

               # Note that for lists of values Thing()*(n,m), the archiver stores 
               # m items if m is specified, but only n items if not (e.g. with "*(1,)").
               # I'm declaring that six stages is a resonable maximum. For gotoField,
               # I can see it spreading out to slew, hartmann, arc, flat, guider, science.
               #
               Key("commandState",
                   String("commandName", help="the name of the sop command"),
                   Enum('idle','active','done','failed',
                        help="state of the entire command"),
                   Enum('idle','inactive','pending','active','done','failed',
                        help="""state of all the individual stages of this command, as 
                                identified by the commandStages keyword.""")*(1,6)),
               Key("commandStages",
                   String("commandName", help="the name of the sop command"),
                   String("stageName", help="the name of a stage of this sop command")*(1,6)),
               Key("stageState",
                   String("subStageName", 
                          help="""dotted name of a substage. The name will always 
                                  start with the commandName.stageName"""),
                   Enum('starting', 'prepped', 'started', 'done', 'failed',
                        help="the state of this substage."),

                   Float("startTime", units="sec", 
                         help="start of the substage, in MJD TAI seconds"),
                   Float("duration", units="sec", 
                         help="expected duration for the substage. If short or unknown, 0.0")),
                   
               )
