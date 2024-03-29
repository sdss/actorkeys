KeysDictionary("mirror", (1,0), *(
    Key("text",
        String(),
        help = "Text message",
    ),
    Key("yourUserID",
        Int(),
        help = "Your user ID number; use this to recognize replies triggered by your commands; never 0",
    ),
    Key("numUsers",
        Int(),
        help = "Number of connected users",
    ),
    Key("userInfo",
        Int(name="id", help = "user ID"),
        String(name="address", help = "socket address"),
        help = "Basic information about one user",
    ),
    Key("unknownCommand",
        String(help = "command verb"),
        help = "The command verb (the first word of your command string) is not supported by this actor",
    ),
    Key("version",
        String(invalid="?"),
        help = "The version of the actor",
    ),
    Key("refCount",
        Int(name="refCount", help = "refcount"),
        String(name="object", help = "object"),
        help = "The reference count for an object",
    ),
    Key("galilConnState",
        Enum("Connecting", "Authorizing", "Connected",
            "Disconnecting", "Disconnected", "Failing", "Failed",
        name="galilConnState",    
        help = "Connection State"
        ),
        String(name="text", help = "Reason for this state, if any"),
        help =  "State of connection to the Galil (a device the mirror controller talks to)",
    ),
#     Key("superseded", help = "The command was superseded by some other command"),
#     Key("timeout", help = "The command timed out"),

    Key("desOrient",
        Float(name="piston", help="piston", units="um", invalid="NaN"),
        Float(name="xTilt", help="x tilt", units="arcsec", invalid="NaN"),
        Float(name="yTilt", help="y tilt", units="arcsec", invalid="NaN"),
        Float(name="xTransl", help="x translation", units="um", invalid="NaN"),
        Float(name="yTranls", help="y translation", units="um", invalid="NaN"),
        Float(name="zRotate", help="z rotation", units="arcsec", invalid="NaN"),
        help = "desired mirror orientation",
    ),
    Key("desOrientAge",
        Float(units = "seconds", invalid="NaN"),
        help = "Elapsed time since a desired orientation was set",
    ),
    Key("cmdMount",
        Float(units="microsteps", invalid="NaN") * (3,6),
        help = "Commanded actuator lengths",
    ),
    Key("modelMount",
        Float(units="microsteps", invalid="NaN") * (3,6),
        help = "Actuator lengths determined from desOrient and the mirror model",
    ),
    Key("netMountOffset",
        Float(units="microsteps", invalid="NaN") * (3,6),
        help = "Offset applied to a model mount at the beginning of a move, " + \
            "to prevent motion for a null move and speed up convergence for a small move. " + \
            "It primarily  compensates for systematic error in the mirror model.",
    ),
    Key("mountErr",
        Float(units="microsteps", invalid="NaN") * (3,6),
        help = "Error in length for a given iteration. Apply this delta to cmdMount each iteration.",
    ),
    Key("cmd",
        String(name = "cmdVerb"),
        help = "Current command (verb) executing",
    ),
    Key("orient",
        Float(name="piston",help="piston", units="um", invalid="NaN"),
        Float(name="xTilt",help="x tilt", units="arcsec", invalid="NaN"),
        Float(name="yTilt", help="y tilt", units="arcsec", invalid="NaN"),
        Float(name="xTransl", help="x translation", units="um", invalid="NaN"),
        Float(name="yTransl",help="y translation", units="um", invalid="NaN"),
        Float(name="zRotate",help="z rotation", units="arcsec", invalid="NaN"),
        help = "desired mirror orientation",
    ),
    Key("actMount",
        Float(units = "microsteps", invalid="NaN") * (3,6),
        help = "Actuator lengths determined from encMount and the mirror model. " + \
            "This may not match cmdMount, even if the actuators move as commanded, " + \
            "due to systematic errors in the mirror model. " + \
            "For an actuator without an encoder, the commanded actuator mount is used. ",
    ),
    Key("desEncMount",
        Float(units = "microsteps", invalid="NaN") * (3,6),
        help = "Desired encoder lengths, in actuator microsteps, based on desOrient and the mirror model. " + \
            "There is one entry per actuator, rather than one per encoder: " + \
            "for an actuator without an encoder, the commanded actuator mount is used.",
    ),
    Key("encMount",
        Float(units = "microsteps", invalid="NaN") * (3,6),
        help = "Reported encoder lengths, in actuator microsteps. " + \
            "There is one entry per actuator, rather than one per encoder: " + \
            "for an actuator without an encoder, the commanded actuator mount is used.",
    ),
    Key("axisHomed",
        Bool('0', '1', invalid="?") * (3,6),
        help = "Axes that are homed",
    ),
    Key("status",
        Bits('stopcode:8', 'statusword:24') * (3,6), # should we breakdown status word into individual bits?
        help = "see http://www.apo.nmsu.edu/Telescopes/HardwareControllers/GalilMirrorControllers.html#StatusWord",
    ),
    Key("state",
        String(name="state", help="State of device, one of: Moving, Done, Homing, Failed, NotHomed"),
        UInt(name="iter", help="current iteration; 0 if state is not Moving"),
        UInt(name="iterMax", help="max iterations; 0 if state is not Moving"),
        Float(name="timeRemain",invalid="NaN", units="seconds", help="remaining time for command, if known, else 0"),
        Float(name="timeTotal", invalid="NaN", units="seconds", help="total time for command, if known, else 0"),
        help = "summarizes current state of galil and any remaning time or move iterations",
    ),
    Key("maxIter",
        UInt(),
        help = "Maximum allowed iterations for a move",
    ),
    Key("moving",
        Bool('0', '1', invalid="?"),
        help = "Mirror currently moving",
    ),
    Key("homing",
        Bool('0', '1', invalid="?") * (3,6),
        help = "Axes that are currently homing",
    ),
    Key("unparsedReply",
        String(),
        help = "This Galil reply could not be parsed and so is being ignored",
    ),
    Key("unknownReplyKey",
        String(name="key", help="data key"),
        String(name="data", help="data"),
        String(name="replay", help="full reply"),
        help = "One item of Galil data had an unrecognized key",
    ),
    Key("badGalilReply",
        String(),
        help = "Parsed Galil reply that confused the actor",
    ),
    Key("galilSoftwareVersion",
        String(),
        help = "Software Version on Galil",
    ),
    Key("deviceSoftwareVersion",
        String(),
        help = "Software version for additional device-specific code",
    ),
    Key("galilNAXES",
        Int(),
        help = "Number of axes (1-6). Note: 3.5m M3 mirror has 6 axes, although only 3 may be used",
    ),
    Key("galilDOAUX",
        Int(),
        help = "If nonzero, status info emitted from aux serial port",
    ),
    Key("galilMOFF",
        Int(),
        help = "Turn off all motors after each move, if nonzero",
    ),
    Key("galilNCORR",
        Int(),
        help = "Number of encoder-based corrections after each move",
    ),
    Key("galilWTIME",
        Float(units = "seconds"),
        help = "Settling time after a move",
    ),
    Key("galilENCTIME",
        Float(units = "seconds"),
        help = "Settling time after a move and after WTIME, before encoders are read",
    ),
    Key("galilLSTIME",
        Float(units = "seconds"),
        help = "Max time required to back out of a limit at low speed",
    ),
    Key("galilHalfRNG",
        Int(units="microsteps") * (3,6),
        help = "Half the range of motion",
    ),
    Key("galilSPD",
        Int(units="microsteps/sec") * (3,6),
        help = "Max speed",
    ),
    Key("galilHMSPD",
        Int(units="microsteps/sec") * (3,6),
        help = "Max speed for finding home switch",
    ),
    Key("galilACC",
        Int(units="microsteps/sec^2") * (3,6),
        help = "Maximum acceleration and deceleration of each axis",
    ),
    Key("galilMINCORR",
        Int(units="microsteps") * (3,6),
        help = "The mininimum error that will be corrected, 0 means correct any error",
    ),
    Key("galilMAXCORR",
        Int(units="microsteps") * (3,6),
        help = "The max error that will be corrected at the end of a move. Set to 0 if no encoder or no correction is desired",
    ),
    Key("galilST_FS",
        Int(units="microsteps/full step") * (3,6),
        help = "Step resolution; 1 for a servo motor",
    ),
    Key("galilMARG",
        Int(units="microsteps") * (3,6),
        help = "Margin between the hard and soft reverse limits",
    ),
    Key("galilINDSEP",
        Int(units="microsteps") * (3,6),
        help = "If this axis has an index pulse encoder and it is used for homing, then set to the separation between index pulses",
    ),
    Key("galilENCRES",
        Float(units="ticks/microstep") * (3,6),
        help = "Resolution of encremental auxiliary encoder; 0 if no encoder",
    ),
    # keywords for a piezo mirror
    Key("piezoStatus",
        Int(invalid = "NaN"),
        help = "1: piezo correction task halted. 2: piezo correction pause requested. 3: piezo corrections disabled",
    ),
    Key("piezoCorr",
        Float(units="microsteps", invalid="NaN")*3,
        help = "piezo Corrections (microsteps)",
    ),
    Key("piezoMaxPos",
        Float(units="microsteps"),
        help = "Max piezo postion (microsteps)",
    ),
    Key("piezoMinPos",
        Float(units="microsteps"),
        help = "Min piezo postion (microsteps)",
    ),
    Key("piezoNSteps",
        Int(),
        help = "number of steps of piezo position",
    ),
    Key("piezoResolution",
        Int(units="microsteps/piezo ctrl bit"),
        help = "resolution (microsteps/piezo ctrl bit)"
    ),
))
