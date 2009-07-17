KeysDictionary("mcp", (1,2),
    # Command-related keywords
    Key("badAxis", String(), doCache=False, help="Unknown telescope axis"),
    Key("badCharacter", Int(), doCache=False, help="ASCII code of invalid character"),
    Key("badCommand", String(), doCache=False, help="Invalid command string"),
    Key("badSpectrograph", Int(), doCache=False, help="Invalid spectrograph ID"),
    Key("badUserId", help="Your suggested userID was invalid"),
    Key("command", String(), doCache=False, help="Command string"),
    Key("commandIn", String(), doCache=False, help="Debugging information; will go away"),
    Key("commandTooLong", Int(help="length of command"), doCache=False, help="Command was too long to parse"),
    Key("controlLamps", help="Indicates that a lamps control command finished"),
    Key("lampsCommanded", Bool("false", "true"), doCache=False, help=""),
    Key("text", String(), doCache=False),
    Key("userId", String(), help="Name reported by user"),
    Key("yourUserNum", Int(), help="Your user ID number"),

    # Iack and semaphore
    Key("haveSemaphore", Bool("false", "true"), help="Do you have the semaphore?"),
    Key("needIack", Bool("false", "true"), help="If False, please send an iack"),
    Key("needSemaphore", help="Command rejected because you don't have the semaphore"),
    Key("semaphoreOwner", String(), help="Name of user (self-reported) who owns the semaphore"),
    
    # Flat field screens
    Key("ffsCloseFailed", Bool("false", "true"), doCache=False),
    Key("ffsCommanded", Bool("false", "true"), doCache=False),
    Key("ffsCommandedOn", Bool("false", "true"), help="Flat field petals commanded close/open"),
    Key("ffsMoved", Bool("false", "true"), doCache=False),
    Key("ffsOpenFailed", Bool("false", "true"), doCache=False),
    Key("ffsSelected", Enum("00", "01", "10", "11", descr=("None", "Half1", "Half2", "All")),
        help="Flat field petals enabled"),
    Key("ffsStatus", Enum("00", "01", "10", "11", descr=("?", "Closed", "Open", "Invalid"))*8,
        help="State of flat field petals 1-8"),

    # Lamps
    Key("ffLamp", Bool("0", "1")*4, help="Detected state of flat field lamps"),
    Key("ffLampCommandedOn", Bool("false", "true"), help="Commanded state of flat-field lamps"),
    Key("hgCdLamp", Bool("0", "1")*4, help="Detected state of mercury/cadmium lamps"),
    Key("hgCdLampCommandedOn", Bool("false", "true"), help="Commanded state of mercury/cadmium lamps"),
    Key("neLamp", Bool("0", "1")*4, help="Detected state of neon lamps"),
    Key("neLampCommandedOn", Bool("false", "true"), help="Commanded state of neon lamps"),
    Key("uvLampCommandedOn", Bool("false", "true"), help="Commanded state of UV lamps"),
    Key("whtLampCommandedOn", Bool("false", "true"), help="Commanded state of white lamps"),

    # Counterweights
    Key("cwAbort", Int(), doCache=False, help="Abort on counterweight 1,2,3 or 4 (only one abort is reported at a time)"),
    Key("cwPositions", Int()*4, help="Counterweight positions"),
    Key("cwStatus", Enum("..", "L.", ".U", "LU", descr=("InRange", "AtLowerLimit", "AtUpperLimit", "Invalid"))*4,
        help="Counterweight status"),

    # Other PLC signals
    Key("altWindscreenTouched", Enum("00", "01", "10", "11", descr=("None", "Down", "Up", "Both"))),
    Key("azWindscreenTouched", Enum("00", "01", "10", "11", descr=("None", "CW", "CCW", "Both"))),
    Key("instrumentNum", Int(invalid="-1"),
        help="Instrument ID; 0=no instrument; 14=imager; -1=switches inconsistent or could not get semaphore"),
    Key("instrumentNumConsistent", Bool("false", "true"),
        help="Do the three instrument ID switches agree? If not, instrumentNumValues is also output."),
    Key("instrumentNumValues", Int()*3, help="Reading from each instrument ID switch"),
    Key("saddleIsMounted", Bool("false", "true"), help="Imager saddle is mounted"),
    Key("sp1Slithead", 
        Enum("00", "01", "10", "11", descr=("?", "Open", "Closed", "Invalid")),
        Bool("0", "1", help="Latch extended"),
        Bool("0", "1", help="Slithead in place")),
    Key("sp2Slithead", 
        Enum("00", "01", "10", "11", descr=("?", "Open", "Closed", "Invalid")),
        Bool("0", "1", help="Latch extended"),
        Bool("0", "1", help="Slithead in place")),
    Key("tbarCommanded", Bool("false", "true"), doCache=False, help="Imager TBar move requested"),

    # Axis controller, in order Az, Alt, Rot
    Key("azMaxAccLimit", Float(units="deg/s^2"), help="Maximum acceleration allowed"),
    Key("azMaxAccRequested", Float(units="deg/s^2"), doCache=False, help="Maximum acceleration requested"),
    Key("azMaxVelLimit", Float(units="deg/s"), help="Maximum velocity allowed"),
    Key("azMaxVelRequested", Float(units="deg/s"), help="Maximum velocity"),
    Key("azMsOn", Bool("false", "true"), help="Fiducial corrections enabled requested"),
    Key("azPidCoeffs", Int(help="Proportional term"), Int(help="Integral term"), Int(help="Derivitive term"),
        Int(help="Accel_FF"), Int(help="Vel_FF"), Int(help="I_limit"), Int(help="Offset"),
        Int(help="DAC_limit"), Int(help="Shift"), Int(help="Friction_FF"),
        help="Servo loop tuning parameters; for details see the MEI manual"),

    Key("altMaxAccLimit", Float(units="deg/s^2"), help="Maximum acceleration allowed"),
    Key("altMaxAccRequested", Float(units="deg/s^2"), doCache=False, help="Maximum acceleration requested"),
    Key("altMaxVelLimit", Float(units="deg/s"), help="Maximum velocity allowed"),
    Key("altMaxVelRequested", Float(units="deg/s"), help="Maximum velocity requested"),
    Key("altMsOn", Bool("false", "true"), help="Fiducial corrections enabled"),
    Key("altPidCoeffs", Int(help="P: proportional term"), Int(help="I: integral term"), Int(help="D: derivitive term"),
        Int(help="Accel_FF"), Int(help="Vel_FF"), Int(help="I_limit"), Int(help="Offset"),
        Int(help="DAC_limit"), Int(help="Shift"), Int(help="Friction_FF"),
        help="Servo loop tuning parameters; for details see the MEI manual"),

    Key("rotBadFiducialDelta", Int(), help="Unknown fiducial: invalid delta between tape marks"),
    Key("rotMaxAccLimit", Float(units="deg/s^2"), help="Maximum acceleration allowed"),
    Key("rotMaxAccRequested", Float(units="deg/s^2"), doCache=False, help="Maximum acceleration requested"),
    Key("rotMaxVelLimit", Float(units="deg/s"), help="Maximum velocity allowed"),
    Key("rotMaxVelRequested", Float(units="deg/s"), help="Maximum velocity requested"),
    Key("rotMsOn", Bool("false", "true"), help="Fiducial corrections enabled"),
    Key("rotPidCoeffs", Int(help="Proportional term"), Int(help="Integral term"), Int(help="Derivitive term"),
        Int(help="Accel FF"), Int(help="Vel FF"), Int(help="Current limit"), Int(help="Offset"),
        Int(help="DAC limit"), Int(help="Shift"), Int(help="Friction FF"),
        help="Servo loop tuning parameters; for details see the MEI manual"),

    # Axis encoders and fiducials
    Key("minEncoderMismatch", Int()*3, help="Limit below which readings from paired encoders are considered equal (az, alt, rot)"),
    Key("msOnMaxCorrection", Int()*3, help="Maximum fiducial error which will be corrected (az, alt, rot)"),

    # Versions
    Key("goodFiducialVersions", Bool("false", "true"), help="The fiducial table version numbers are consistent"),
    Key("azFiducialVersion", String(), help="Version of fiducial table"),
    Key("altFiducialVersion", String(), help="Version of fiducial table"),
    Key("rotFiducialVersion", String(), help="Version of fiducial table"),
    Key("mcpVersion", String(), help="Version of MCP code"),
    Key("plcVersion", Int(), help="PLC version, if consistent (see also pclVersions)"),
    Key("plcVersions", Int()*2, help="PLC versions from the Allen-Bradley and data_collection.h"),

    # Actor housekeeping
    Key("keepAlive", UInt(units="s",help="Elapsed TAI(?) since unix epoch"), help="MCP 1 Hz keep-alive message"),
)
