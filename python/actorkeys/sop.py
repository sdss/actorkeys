KeysDictionary("sop", (1,2),
    # misc
    Key("version", String(help="EUPS/SVN version")),
    Key("text", String(), help="text for humans"),
    Key("bypassed",
        #CompoundValueType(String(), Bool("False", "True"))*8,
        CompoundValueType(String(), Bool("False", "True")),
        CompoundValueType(String(), Bool("False", "True")),
        CompoundValueType(String(), Bool("False", "True")),
        CompoundValueType(String(), Bool("False", "True")),
        CompoundValueType(String(), Bool("False", "True")),
        CompoundValueType(String(), Bool("False", "True")),
        CompoundValueType(String(), Bool("False", "True")),
        CompoundValueType(String(), Bool("False", "True")),
        help="Which subsystems's failures are being ignored"),
)
