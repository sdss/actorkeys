KeysDictionary("guider", (1, 5),
    Key("version", String(), help="svn/eups version"),
    Key("guiderVersion", String(), help="historical svn/eups version"),

    # parameters

    Key("cartridgeLoaded",
        Int(name="cartridgeID", invalid=-1, help="Cartridge number"),
        Int(name="plateID", invalid=-1, help="Plate number"),
        String(name="pointing", invalid="?", help="The pointing being observed"),
        Int(name="fscanMJD", invalid=-1, help="MJD when the plate was mapped"),
        Int(name="fscanID", invalid=-1, help="Which of the mappings on fscanMJD we are using"),
    ),
    Key("guideEnable",
        Bool(False, True, name="axis", help="move azimuth, altitude and rotation to correct pointing"),
        Bool(False, True, name="focus", help="move the secondary mirror to correct focus"),
        Bool(False, True, name="scale", help="move the primary and secondary mirrors to correct plate scale"),
        help="Which guiding corrections are enabled",
    ),
    Key("expTime", Float(), help="exposure time"),
    Key("pid",
        String(help="What is being servoed"),
        Float(help="Proportional gain"),
        Float(help="Integral time", units="seconds"),
        Float(help="derivative time", units="seconds"),
        Float(help="Max integral error"),
        Int(help="Number of input samples used in smoothing filter"),
    ),
    Key("scales",
        Float(name="plugPlateScale", units="mm/deg", help="Plug plate scale"),
        Float(name="gcameraMagnification", help="Guide camera scale relative to the plug plate"),
        Float(name="gcameraPixelSize", units="microns/pixel", help="Guide camera pixel size"),
        Float(name="dSecondary_dmm", units="mm/mm", help="Motion of secondary to move focus at plugplate"),
        help="plate scales relevant to guiding",
    ),

    # status

    Key("file",
        String(help="base directory for these files (relative to image root)"),
        String(help="name of fully processed image file"),
        doCache = False,
    ),
    # Warning: the disabled bit is never set (ticket #433)
    # meanwhile use the deprecated keyword gprobes to get enabled information
    # or use keyword fullGprobeBits in STUI's model (which is what gprobeBits should be)
    Key("gprobeBits",
        Bits("broken", "unused", "disabled", help="Guide probe bits")*(0,),
    ),
    Key("guideState", 
        Enum("off", "starting", "on", "stopping", help="state of guider"),
    ),
    Key("processing",
        String(),
        help="path of file being processed",
        doCache=False,
    ),
    # Superseded by gprobeBits but cannot be removed until ticket #433 is fixed; see gprobeBits for more info
    Key("gprobes",
        String()*(0,),
        help="Which guide probes are enabled? Format: (<probe number>=True/False); probe number starts at 1",
    ),
    
    # measured and derived values
    
    Key("axisError",
        Float(help="measured pointing correction in RA (distance across the sky)", units="arcsec"),
        Float(help="measured pointing correction in Dec (distance across on the sky)", units="arcsec"),
        Float(help="measured pointing correction in rotation", units="arcsec"),
        doCache=False,
    ),
    Key("axisChange",
        Float(help="applied pointing correction in RA (distance across the sky)", units="arcsec"),
        Float(help="applied pointing correction in Dec (distance across the sky)", units="arcsec"),
        Float(help="applied pointing correction in rotation", units="arcsec"),
        Bool("disabled", "enabled", help="is this correction enabled (was it applied)?"),
        doCache=False,
    ),
    Key("decenter",
        Int(name="expID", help="gcamera exposure number"),
        Bool("disabled", "enabled", help="is decentered guiding mode enabled (was it applied)?"),
        Float(name="RA", help="User specified telescope guiding offset in RA from guider position", units="arcsec"),
        Float(name="DEC", help="User specified telescope offset in Dec from guider position", units="arcsec"),
        Float(name="Rot", help="User specified telescope offset in Rot from guider position", units="arcsec"),
        Float(name="Focus", help="User specified focus offset from guider focus ", units="um"),
        Float(name="Scale", help="User specified scale offset from guider scale ", units="um"),
        doCache = False,
    ),
    Key("focusError",
        Float(help="measured focus error", units="um"),
        doCache=False,
    ),
    Key("focusChange",
        Float(help="applied focus correction", units="um"),
        Bool("disabled", "enabled", help="is this correction enabled (was it applied)?"),
        doCache=False,
    ),
    Key("fwhm",
        Int(name="expID", help="gcamera exposure number"),
        Float(name="tmean", help="trimmed mean FWHM(Gunn) of the in-focus (enabled) fibers", units="arcsec"),
        Int(name="nKept", help="number of FWHM values used for mean"),
        Int(name="nReject", help="number of FWHM value rejected"),
        Float(name="mean", help="mean FWHM(Gunn) of the in-focus (enabled) fibers", units="arcsec"),
        doCache=False,
    ),
    Key("guideRMS",
        Int(name="expID",   help="gcamera exposure number"),
        Float("RMSerror",   help="RMS of guide star offset from the fiber center",units="arcsec"),
        Int(name="nStars",  help="Number of (enabled) guide star used"),
        Float(name="AzRMS", help="Az component of RMS ", units="arcsec"),
        Float(name="AltRMS",help="Alt component of RMS ", units="arcsec"),
        Float(name="xRMS",  help="guide camera x axis component of RMS", units="arcsec"),
        Float(name="yRMS",  help="guide camera y axis component of RMS", units="arcsec"),
        Float("fitRMS",     help="RMS of fit to guide star offsets", units="arcsec"),
        Int(name="nFit",    help="Number of guide stars used for fit"),
        Int(name="nFitReject", help="Number of guide stars rejected from fit"),
        doCache = False,
    ),        
    Key("probe",
        Int(name="exposureID", help="gcamera exposure number"),
        Int(name="probeID", help="guide probe number, starting from 1"),
        Int(name="flags", help="What is this? Document me!"),
        Float(name="raError", help="measured RA error on the sky", units="arcsec"),
        Float(name="decError", help="measured Dec error on the sky", units="arcsec"),
        Float(name="FWHM", units="arcsec"),
        Float(name="focusOffset", help="offset of probe tip from focalplane; + is away from sky and M2", units="um"),
        Float(name="modelFlux", units="ADU"),
        Float(name="modelMagnitude"),
        Float(name="refMagnitude", help="known magnitude of guide star"),
        Float(name="skyFlux", help="mean sky, per-pixel", units="ADU/pixel"),
        Float(name="skyMagnitude", units="mags/square-arcsec"),
        doCache = False,
    ),
    Key("scaleError",
        Float(help="measured scale error (scale factor - 1)"),
        doCache=False,
    ),
    Key("scaleChange",
        Float(help="applied scale correction (scale factor - 1)"),
        Bool("disabled", "enabled", help="is this correction enabled (was it applied)?"),
        doCache=False,
    ),
    Key("seeing", Float(), help="predicted seeing (FWHM, arcsec), a fit to RHL's focus model"),

    Key("refractionBalance", Float(), help="factor by which the provided refraction correction is adjusted. Nominally 0..1"),
    
    # misc

    Key("text", String(), help="text for humans"),
)
