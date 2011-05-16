# This is the initial test keys dictionary for APOGEE Calibration Box
#
KeysDictionary("apogeecal", (2,1), *(
    # Misc
    Key("text", String(), help="text for humans"),
    Key("version", String(), help="version string derived from svn info."),

    # Lamps 
    Key("calSourceNames",
        String()*(3,6),
        help="List of calibration lamp names"),
    Key("calSourceStatus",
        Bool("false", "true", invalid="?")*(3,6),
        help="Calibration lamp on (true) or off (false)"),
    Key("calShutter",
        Bool("closed", "open", invalid="?"),
        help="State of the CalBox shutter"),
    Key("calBoxController",
        Bool("off", "on", invalid="?"),
        help="State of the CalBox controller"),
))
