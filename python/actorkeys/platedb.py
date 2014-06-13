KeysDictionary("platedb", (1,6),
    Key("version", String(help="EUPS/SVN version")),
    Key("activePlugging",
        Int(name="cartridge", help="The cartridge in use", invalid=-1),
        Int(name="plate", help="The plate ID", invalid=-1),
        String(name="pointing", help="The active pointing", invalid="?"),
        Int(name="fscanMJD", help="MJD that this plate was mapped"),
        Int(name="fscanId", help="Unique plugging ID within fscanMJD"),
        Float(name="ra", help="The plate centre's right ascension"),
        Float(name="dec", help="The plate centre's declination"),
        Float(name="hour_angle", help="The hour_angle the plate was drilled for"),
        Float(name="temperature", help="The temperature the plate was drilled for"),
        help="The currently-mounted cartridge's properties",
    ),
    Key("plPlugMapM",
        Int(name="plate", help="The plate ID", invalid=-1),
        Int(name="fscanMJD", help="The day the plate was mapped"),
        Int(name="fscanId", help="The version of that day's mapping"),
        help="The currently-mounted cartridge's plPlugMap fingerprint",
    ),
    Key("gprobe",
        Int(name="cartridgeId", help="The cartridge the gprobe belongs to"),
        Int(name="gprobeId", help="The gprobe ID"),
        Bool("False", "True", name="enabled", help="Does this cartridge have this gprobe?"),
        Float(name="xcen", units="pixels", help="w.r.t (0.5, 0.5) at center of LL pixel"),
        Float(name="ycen", units="pixels", help="w.r.t (0.5, 0.5) at center of LL pixel"),
        Float(name="radius", help="pixels"),
        Float(name="rotation", units="degrees", help="+CCW, image Y to plate N. WRT offset image"),
        Float(name="xferruleOffset", units="microns", help="applied before rotation"),
        Float(name="yferruleOffset", units="microns", help="applied before rotation"),
        Float(name="focusOffset", units="microns", help="+ve towards sky,(inside focus probes)"),
        Enum("ACQUIRE", "GUIDE", "TRITIUM", name="fiberType", help="Type of gprobe"),
        help="The properties of a spectroscopic guide probe from platedb.gprobe",
    ),
    Key("gprobesInUse",
        String(name="gprobeStatus", help="See guider.gprobeBits for the docs on the gprobebits.")*(0,),
        help="A list of (id=BITS) values for all this cartridge's gprobes, from the plPlugMapM.",
    ),
    Key("gcamFiberInfoVersion",
        String(name="version", help="svn revision"),
        help="The version of the gcamFiberInfo.par file loaded into gprobes table",
    ),
    Key("guideInfo",
        Int(name="gprobeId", help="The gprobe ID"),
        Float(name="ra", help="The plate centre's right ascension"),
        Float(name="dec", help="The plate centre's declination"),
        Float(name="xFocal", units="mm", help="Hole x-axis position in focal plane"),
        Float(name="yFocal", units="mm", help="Hole y-axis position in focal plane"),
        Float(name="phi", units="degrees", help="Angle from guide hole to alignment hole"),
        Float(name="throughput", help="Fiber throughput ([0, 1], 0=no light)"),
        help="Information about the guide stars in this plate",
    ),
    Key("pointingInfo",
        Int(name="plate", help="The plate ID", invalid=-1),
        Int(name="cartridge", help="The cartridge in use", invalid=-1),
        String(name="pointing", help="The active pointing", invalid="?"),
        Float(name="ra", help="The plate centre's right ascension"),
        Float(name="dec", help="The plate centre's declination"),
        Float(name="hour_angle", help="The hour_angle the plate was drilled for"),
        Float(name="temperature", help="The temperature the plate was drilled for"),
        Float(name="lambda", help="The wavelength the plate was designed for"),
        String(name="survey",help="The survey type of plate", invalid="?"),
        String(name="surveyMode",help="The mode of this survey", invalid="?"),
        help="The currently loaded plate",
    ),
    # TBD: do I need this, or should it be part of pointingInfo?
    #Key("mangaDither",
    #    String("mangaDitherPattern",help="The dither pattern requested for this plate", invalid="?"),
    #    help="Information about the requested dithers for this plate."
    #),
    Key("text", String(), help="text for humans"),
)
