# Based on what the TCC knows about the perms widget
KeysDictionary('gcam',(0, 1),
    Key("expState",
        String(help="exposure state; one of: idle, flushing, integrating, paused, reading, processing, aborting, done or aborted"),
        String(help="start time; ISO format UTC"),
        Float(help="remaining time for this state (sec; 0 if none, short or unknown)"),
        Float(help="total time for this state (sec; 0 if none, short or unknown)"),
    ),
    Key("files",
        String(help="type; one of: guide, flat, dark..."),
        String(help="base directory for these files (relative to image root)"),
        String(help="name of fully processed image file"),
        String(help="name of mask file"),
        doCache = False,
    ),
    # can have additional fields which provide supplementary info; how to express that?
    Key("guideState", 
        Enum("off", "starting", "on", "stopping", help="state of guider"),
        Enum(False, True, help="correct pointing and rotation?"),
        Enum(False, True, help="correct scale?"),
        Enum(False, True, help="correct offset?"),
    )
    Key("guideProbe",
        String(help="type character: c = centroid, f = findStars, g = guide star"),
        Int(help="index; identifies the star within a list of stars returned by the command"),
        Float(help="x, y centroid")*2,
        Float(help="standard deviation of centroid; major axis, minor axis, angle of major axis from image x in deg")*3,
        Float(help="radius of centroid region"),
        Float(help="asymmetry: a measure of the asymmetry of the object"),
        Float(help="FWHM along the major axis"),
        Float(help="FWHM along the minor axis"),
        Float(help="angle of ellipse major axis (deg)"),
        Float(help="chi squared for fit to model star"),
        Float(help="sum of all umasked pixels within the centroid radius"),
        Float(help="estimated background level"),
        Float(help="x, y predicted centroid")*2,
        help="Data about a star; lengths and positions are in binned pixels and intensities are in ADUs",
        doCache = False,
    ),
# and many more keywords, including exposure status, information about the net correction (both the measured correction and the amount actually applied), parameters...
)
