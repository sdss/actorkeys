KeysDictionary("guider", (2, 6),
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
    Key("stack", Int(), help="number of itime gcamera integrations to request per exposure."),
    Key("pid",
        String(help="What is being servoed"),
        Float(name="propGain",help="Proportional gain"),
        Float(help="Integral time", units="seconds"),
        Float(help="derivative time", units="seconds"),
        Float(name="maxError",help="Max integral error"),
        Int(help="Number of input samples used in smoothing filter"),
    ),
    Key("scales",
        Float(name="plugPlateScale", units="mm/deg", help="Plug plate scale"),
        Float(name="gcameraMagnification", help="Guide camera scale relative to the plug plate"),
        Float(name="gcameraPixelSize", units="microns/pixel", help="Guide camera pixel size"),
        Float(name="dSecondary_dmm", units="mm/mm", help="Motion of secondary to move focus at plugplate"),
        help="plate scales relevant to guiding",
    ),
    Key("survey",
        String(name="plateType", invalid="?", help="The survey type of this plate"),
        String(name="surveyMode", invalid="?", help="The instrument driving this observation, and its observing mode"),
        help="Which surveys is this plate for",
    ),
    # status

    Key("file",
        String(name="basedir",help="base directory for these files (relative to image root)"),
        String(name="filename",help="name of fully processed image file"),
        doCache = False,
        help="names and directories of processed guider images",
    ),

    Key("gprobeBits",
        Bits("broken", "noStar", "disabled", "aboveFocus", "belowFocus",name="gprobebits",
        help="broken: known broken, labeled as such in plPlugMap; noStar: no star in plPlugMap (e.g. Tritium); disabled: disabled by observers; abovefocus: fiber above the focal plane; belowfocus: fiber below the focal plane.")*(0,50),
        help="Guide probe status bits.",
    ),
    Key("guideState", 
        Enum("off", "starting", "on", "stopping", "failed", help="state of guider"),
    ),
    Key("processing",
        String(),
        help="path of file being processed",
        doCache=False,
    ),
    Key("movieFile",
        String(name="filename",help="Filename of the last generated movie."),
        help="Most recently generated guider movie.",
    ),
    Key("movieStatus",
        Int(name="pid",help="Process ID of the current movie-generation Popen subprocess."),
        help="Status of currently running guider movie processing.",
    ),
    
    # measured and derived values
    
    Key("axisError",
        Float(name="RA",help="measured pointing correction in RA (distance across the sky)", units="arcsec"),
        Float(name="DEC",help="measured pointing correction in Dec (distance across on the sky)", units="arcsec"),
        Float(name="Rot",help="measured pointing correction in rotation", units="arcsec"),
        doCache=False,
        help="measured pointing corrections",
    ),
    Key("axisChange",
        Float(name="RA",help="applied pointing correction in RA (distance across the sky)", units="arcsec"),
        Float(name="DEC",help="applied pointing correction in Dec (distance across the sky)", units="arcsec"),
        Float(name="Rot",help="applied pointing correction in rotation", units="arcsec"),
        Bool("disabled", "enabled", help="is this correction enabled (was it applied)?"),
        doCache=False,
        help="applied pointing corrections",
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
        help="user specified offsets",
        
    ),
    Key("mangaDither",
        Enum('C','N','S','E', help="Named manga dither position", invalid='?')
    ),
    Key("focusError",
        Float(help="measured focus error", units="um"),
        doCache=False,
    ),
    Key("focusChange",
        Float(help="applied focus correction", units="um"),
        Bool("disabled", "enabled", help="is this correction enabled (was it applied)?"),
        doCache=False,
        help="applied focus correction",
    ),
    Key("fwhm",
        Int(name="expID", help="gcamera exposure number"),
        Float(name="tmean", help="trimmed mean FWHM(Gunn) of the in-focus (enabled) fibers", units="arcsec"),
        Int(name="nKept", help="number of FWHM values used for trimmed mean"),
        Int(name="nReject", help="number of FWHM value rejected for trimmed mean"),
        Float(name="mean", help="mean FWHM(Gunn) of the in-focus (enabled) fibers", units="arcsec"),
        doCache=False,
        help="FWHM values and trimming info",
    ),
    Key("guideRMS",
        Int(name="expID",   help="gcamera exposure number"),
        Float(name="RMSerror", help="RMS of guide star offset from the fiber center",units="arcsec"),
        Int(name="nStars",  help="Number of (enabled) guide star used"),
        Float(name="AzRMS", help="Az component of RMS ", units="arcsec"),
        Float(name="AltRMS",help="Alt component of RMS ", units="arcsec"),
        Float(name="xRMS",  help="guide camera x axis component of RMS", units="arcsec"),
        Float(name="yRMS",  help="guide camera y axis component of RMS", units="arcsec"),
        Float(name="fitRMS", help="RMS of fit to guide star offsets", units="arcsec"),
        Int(name="nFit",    help="Number of guide stars used for fit"),
        Int(name="nFitReject", help="Number of guide stars rejected from fit"),
        Float(name="RaRMS", help="RA component of RMS", units="arcsec"),
        Float(name="DecRMS", help="Dec component of RMS", units="arcsec"),
        doCache = False,
        help="RMS values of axis components",
    ),        
    Key("probe",
        Int(name="exposureID", help="gcamera exposure number"),
        Int(name="probeID", help="guide probe number, starting from 1"),
        Int(name="flags", help="gprobebits: 1:BROKEN, 2:NOSTAR, 4:DISABLED, 8:ABOVEFOCUS, 16:BELOWFOCUS"),
        Float(name="raError", help="measured RA error on the sky", units="arcsec"),
        Float(name="decError", help="measured Dec error on the sky", units="arcsec"),
        Float(name="FWHM", units="arcsec"),
        Float(name="focusOffset", help="offset of probe tip from focalplane; + is away from sky and M2", units="um"),
        Float(name="modelFlux", units="ADU",help="computed flux of guide star"),
        Float(name="modelMagnitude",help="computed magnitude of guide star"),
        Float(name="refMagnitude", help="known magnitude of guide star"),
        Float(name="skyFlux", help="mean sky, per-pixel", units="ADU/pixel"),
        Float(name="skyMagnitude", units="mags/square-arcsec"),
        doCache = False,
        help="individual probe values, including mags",
    ),
    Key("scaleError",
        Float(help="measured scale error (scale factor - 1)"),
        doCache=False,
    ),
    Key("scaleChange",
        Float(name="scale",help="applied scale correction (scale factor - 1)"),
        Bool("disabled", "enabled", help="is this correction enabled (was it applied)?"),
        doCache=False,
        help="scale corrections",
    ),
    Key("seeing", Float(), help="predicted seeing (FWHM, arcsec), a fit to RHL's focus model"),

    Key("refractionBalance", Float(), help="factor by which the provided refraction correction is adjusted; approximately 0 for BOSS and 1 for APOGEE"),
    Key("refractionWavelengths", Float(), Float(),
        help="endpoints of the refractionBalance interpolation. Obsolete; never output!"),
    Key("refractionOffset",
        Int(name="frameNum",help="frame number"),
        Int(name="probeNum",help="probe number"),
        Float(name="refrBal",help="refraction balance"),
        Float(name="dHA",units="degrees", help="dHA from the design HA"),
        Float(name="dRA",units="arcsec", help="dRA adjustment applied to the desired star position"),
        Float(name="dDec",units="arcsec", help="dDec adjustment applied to the desired star position"),
        help="refraction offset adjustment values",
    ),

    # for ecamera star finding (e.g., pointing models)
    Key("ecam_star",
        Int(name='expID',help="ecamera exposure number"),
        Float(name='xpos'),
        Float(name='ypos'),
        Float(name='fwhm'),
        Float(name='sky'),
        Float(name='ampl'),
        # Float(name='rad'),
        help="parameters of the brightest star in an ecam image.",
    ),

    # misc

    Key("text", String(), help="text for humans"),
)
