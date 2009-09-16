KeysDictionary('guider', (0, 2),
    # parameters
    Key("cartridgeLoaded",
        Int(name="cartridgeID", invalid=-1, help="Cartridge number"),
        Int(name="plateID", invalid=-1, help="Plate number"),
        String(name="pointing", invalid="?", help="The pointing being observed"),
        Int(name="fscanMJD", invalid=-1, help="MJD when the plate was mapped"),
        Int(name="fscanID", invalid=-1, help="Which of the mappings on fscanMJD we are using"),
    ),
    Key("expTime", Float(), help="exposure time"),
    Key("guideEnable",
        Bool(False, True, name="axis", help="move azimuth, altitude and rotation to correct pointing"),
        Bool(False, True, name="focus", help="move the secondary mirror to correct focus"),
        Bool(False, True, name="scale", help="move the primary and secondary mirrors to correct plate scale"),
        help="Which guiding corrections are enabled",
    ),
    # there will be parameters for the PID loop
    # status
    Key("files",
        String(help="type; one of: guide, flat, dark..."),
        String(help="base directory for these files (relative to image root)"),
        String(help="name of fully processed image file"),
        String(help="name of mask file"),
        doCache = False,
    ),
    Key("guideProbe",
        Bits("broken", "unused", "disabled", "noStarFound"),
        Int(name="index", help="identifies the star within a list of stars returned separately"),
        Float(help="x, y centroid")*2,
        Float(help="standard deviation of centroid; major axis, minor axis, angle of major axis from image x in deg")*3,
        Float(help="radius of centroid region"),
        Float(help="asymmetry: a measure of the asymmetry of the object"),
        Float(name="FWHM", help="FWHM along the major axis, minor axis and angle of major axis")*3,
        Float(help="chi squared for fit to model star"),
        Float(help="sum of all umasked pixels within the centroid radius"),
        Float(help="estimated background level"),
        Float(help="x, y predicted centroid")*2,
        help="Data about a star; lengths and positions are in binned pixels and intensities are in ADUs",
        doCache = False,
    ),
    Key("guideState", 
        Enum("off", "starting", "on", "stopping", help="state of guider"),
    ),
    Key("processing", String(), help="path of file being processed"),
    # corrections
    Key("pid",
        String(help="What is being servoed"),
        Float(help="Proportional gain"),
        Float(help="Integral time", units="seconds"),
        Float(help="derivative time", units="seconds"),
        Float(help="Max integral error"),
        ),
    Key("axisError",
        Float(help="measured pointing error: az, alt, rot", units="deg")*3,
    ),
    Key("axisChange",
        Float(help="applied pointing correction: az, alt, rot", units="deg")*3,
        Bool("disabled", "enabled", help="is this correction enabled (was it applied)?"),
    ),
    Key("focusError",
        Float(help="measured focus error", units="um"),
    ),
    Key("focusChange",
        Float(help="applied focus correction", units="um"),
        Bool("disabled", "enabled", help="is this correction enabled (was it applied)?"),
    ),
    Key("scaleError",
        Float(help="measured scale error"),
    ),
    Key("scaleChange",
        Float(help="applied scale correction"),
        Bool("disabled", "enabled", help="is this correction enabled (was it applied)?"),
    ),
    # misc
    Key("text", String(), help="text for humans"),
    Key("scales",
        Float(name="plugPlateScale", units="mm/deg", help="Plug plate scale"),
        Float(name="gcameraMagnification", help="Guide camera scale relative to the plug plate"),
        Float(name="gcameraPixelSize", units="microns/pixel", help="Guide camera pixel size"),
        Float(name="dSecondary_dmm", units="mm/mm", help="Motion of secondary to move focus at plugplate"),
        help="plate scales relevant to guiding"),
)
