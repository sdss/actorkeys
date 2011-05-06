# This is the initial test keys dictionary for APOGEE Calibration Box
#
KeysDictionary("apogeecal", (1,0), *(
    # Misc
    Key("text", String(), help="text for humans"),
    Key("version", String(), help="version string derived from svn info."),

    # Lamps 
    Key("calSourceNames",
        String()*(3,10),
        help="List of calibartion names"),
    Key("calSourceStatus",
        Bool("false", "true", invalid="?")*3,
        help="Lamp ON status"),
    Key("calShutter",
        String(),
        help="State of the CalBox shutter (open | closed)"),
    Key("calBoxController",
        String(),
        help="State of the CalBox controller (on | off)"),

))
