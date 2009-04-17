# Based on the TCC keywords documented at (with guide camera keywords omitted):
# http://www.apo.nmsu.edu/Telescopes/TCC/MessageKeywords.html

KeysDictionary("tcc", (3, 2), 
    Key("airTemp", Float(invalidValue="NaN", units="C"), help="Temperature of the outside air. Used for refraction correction."),
    Key("axePos", Float(invalidValue="NaN", units="deg", invalid="NaN", help="Order is Az, Alt, Rot")*3, help=
        """Actual mount position of azimuth, altitude and instrument rotator, as reported by
        the axes controllers. Not many digits past the decimal but very useful for status displays."""
    ), 
    Key("azAltDist", Float(invalidValue="NaN"), doCache=False), 
    Key("azDTime", Float(invalidValue="NaN", units="s")), 
    Key("altDTime", Float(invalidValue="NaN", units="s")), 
    Key("rotDTime", Float(invalidValue="NaN", units="s")), 
    Key("azErr", Float(invalidValue="NaN", units="as")*3, doCache=False), 
    Key("altErr", Float(invalidValue="NaN", units="as")*3, doCache=False), 
    Key("rotErr", Float(invalidValue="NaN", units="as")*3, doCache=False), 
    Key("azLim", Float(invalidValue="NaN", units="deg")*2, Float(invalidValue="NaN", units="deg/s"), Float(invalidValue="NaN", units="deg/s^2"), Float(invalidValue="NaN", units="deg/s^3")), 
    Key("altLim", Float(invalidValue="NaN", units="deg")*2, Float(invalidValue="NaN", units="deg/s"), Float(invalidValue="NaN", units="deg/s^2"), Float(invalidValue="NaN", units="deg/s^3")), 
    Key("rotLim", Float(invalidValue="NaN", units="deg")*2, Float(invalidValue="NaN", units="deg/s"), Float(invalidValue="NaN", units="deg/s^2"), Float(invalidValue="NaN", units="deg/s^3")), 
    Key("azMSStat", Float(invalidValue="NaN", units="as")*2, String()), 
    Key("altMSStat", Float(invalidValue="NaN", units="as")*2, String()), 
    Key("rotMSStat", Float(invalidValue="NaN", units="as")*2, String()), 
    Key("azPosRejected", Float(invalidValue="NaN", units="deg")*3, doCache=False), 
    Key("altPosRejected", Float(invalidValue="NaN", units="deg")*3, doCache=False), 
    Key("rotPosRejected", Float(invalidValue="NaN", units="deg")*3, doCache=False), 
    Key("azStat", Float(invalidValue="NaN", units="deg"), Float(invalidValue="NaN", units="deg/s"), Double(invalid="NaN", units="s"), Hex(invalid="NaN", )), 
    Key("altStat", Float(invalidValue="NaN", units="deg"), Float(invalidValue="NaN", units="deg/s"), Double(invalid="NaN", units="s"), Hex(invalid="NaN", )), 
    Key("rotStat", Float(invalidValue="NaN", units="deg"), Float(invalidValue="NaN", units="deg/s"), Double(invalid="NaN", units="s"), Hex(invalid="NaN", )), 
    Key("axisBadStatusMask", Hex(invalid="NaN", )), 
    Key("axisCmdState", Enum("Drifting", "Halted", "Halting", "Slewing", "Tracking", "NotAvailable", invalid="?")*3), 
    Key("axisErrCode", String(invalid="?")*3), 
    Key("axisInit", String(), doCache=False), 
    Key("axisMaxDTime", Float(invalidValue="NaN", units="s"), doCache=False), 
    Key("axisNoSlew", String(), doCache=False), 
    Key("axisNoTrack", String(), doCache=False), 
    Key("axisStop", String(), doCache=False), 
    Key("axisWarnStatusMask", Hex(invalid="NaN", )), 
    Key("azWrapPref", Enum("None", "Near", "Neg", "Middle", "Pos"), doCache=False), 
    Key("badCmd"), 
    Key("badAzStatus"), 
    Key("badAltStatus"), 
    Key("badRotStatus"), 
    Key("badAzDTime"), 
    Key("badAltDTime"), 
    Key("badRotDTime"), 
    Key("badUser", UInt(invalidValue="NaN"), doCache=False), 
    Key("blockInfo", String(), UInt(invalidValue="NaN")*2, doCache=False), 
    Key("boresight", Float(invalidValue="NaN", units="deg"), Float(invalidValue="NaN", units="deg/s"), Double(invalid="NaN", units="s"), Float(invalidValue="NaN", units="deg"), Float(invalidValue="NaN", units="deg/s"), Double(invalid="NaN", units="s")), 
    Key("broadcast", String(), doCache=False), 
    Key("calibOff", Float(invalidValue="NaN", units="deg"), Float(invalidValue="NaN", units="deg/s"), Double(invalid="NaN", units="s"), Float(invalidValue="NaN", units="deg"), Float(invalidValue="NaN", units="deg/s"), Double(invalid="NaN", units="s"), Float(invalidValue="NaN", units="deg"), Float(invalidValue="NaN", units="deg/s"), Double(invalid="NaN", units="s")), 
    Key("cmd", String(), doCache=False), 
    Key("cmdDTime", Float(invalidValue="NaN", units="s"), doCache=False), 
    Key("primConstRMS", Float(invalidValue="NaN", units="um")), 
    Key("secConstRMS", Float(invalidValue="NaN", units="um")), 
    Key("convAng", Float(invalidValue="NaN", units="deg"), Float(invalidValue="NaN", units="deg/s"), Double(invalid="NaN", units="s"), doCache=False), 
    Key("convPM", Float(invalidValue="NaN", units="as/century")*2, Float(invalidValue="NaN", units="as"), Float(invalidValue="NaN", units="km/s"), doCache=False), 
    Key("convPos", Float(invalidValue="NaN", units="deg"), Float(invalidValue="NaN", units="deg/s"), Double(invalid="NaN", units="s"), Float(invalidValue="NaN", units="deg"), Float(invalidValue="NaN", units="deg/s"), Double(invalid="NaN", units="s"), doCache=False), 
    Key("currArcOff", Float(invalidValue="NaN", units="deg"), Float(invalidValue="NaN", units="deg/s"), Double(invalid="NaN", units="s"), Float(invalidValue="NaN", units="deg"), Float(invalidValue="NaN", units="deg/s"), Double(invalid="NaN", units="s")), 
    Key("currUsers", UInt(invalidValue="NaN")), 
    Key("deadProc", String()*(1,), doCache=False), 
    Key("disabledProc", String()*(1,), doCache=False), 
    Key("duration", Float(invalidValue="NaN", units="s"), doCache=False), 
    Key("eText", String(), doCache=False), 
    Key("expected", String(), doCache=False), 
    Key("expTime", Float(invalidValue="NaN", units="s"), doCache=False), 
    Key("facil", String(), doCache=False), 
    Key("failed"), 
    Key("flushedFromBox", String(), doCache=False), 
    Key("humidity", Float(invalidValue="NaN")), 
    Key("iimCtr", Float(invalidValue="NaN", units="pixels")*2), 
    Key("iimLim", Float(invalidValue="NaN", units="pixels")*4), 
    Key("iimScale", Float(invalidValue="NaN", units="pixels/deg")*2), 
    Key("inst", String()), 
    Key("instPos", Enum("NA1", "NA2", "BC1", "TR1", "TR2", "SK1", "SK2", "SK3", "SK4", "CA1", "non")), 
    Key("ipConfig", String()), 
    Key("iter", UInt(invalidValue="NaN"), doCache=False), 
    Key("job", String(), doCache=False), 
    Key("lockInfo", String(), UInt(invalidValue="NaN")*2, String()*2, UInt(invalidValue="NaN"), String()*2, doCache=False), 
    Key("lst", Float(invalidValue="NaN", units="deg")), 
    Key("maxDuration", Float(invalidValue="NaN", units="s"), doCache=False), 
    Key("maxIter", UInt(invalidValue="NaN"), doCache=False), 
    Key("maxUsers", UInt(invalidValue="NaN")), 
    Key("meas2PredErr", Float(invalidValue="NaN", units="as"), doCache=False), 
    Key("primActMount", Float(invalidValue="NaN")*(1,)), 
    Key("secActMount", Float(invalidValue="NaN")*(1,)), 
    Key("primCmdMount", Float(invalidValue="NaN")*(1,)), 
    Key("secCmdMount", Float(invalidValue="NaN")*(1,)), 
    Key("primDesOrient", Float(invalidValue="NaN", units="um"), Float(invalidValue="NaN", units="as")*2, Float(invalidValue="NaN", units="um")*2), 
    Key("secDesOrient", Float(invalidValue="NaN", units="um"), Float(invalidValue="NaN", units="as")*2, Float(invalidValue="NaN", units="um")*2), 
    Key("primDesOrientAge", Float(invalidValue="NaN", units="s"), doCache=False), 
    Key("secDesOrientAge", Float(invalidValue="NaN", units="s"), doCache=False), 
    Key("primF_BFTemp", Float(invalidValue="NaN", units="deg")*2), 
    Key("secF_BFTemp", Float(invalidValue="NaN", units="deg")*2), 
    Key("primOrient", Float(invalidValue="NaN", units="um"), Float(invalidValue="NaN", units="as")*2, Float(invalidValue="NaN", units="um")*2), 
    Key("secOrient", Float(invalidValue="NaN", units="um"), Float(invalidValue="NaN", units="as")*2, Float(invalidValue="NaN", units="um")*2), 
    Key("primStat", String()*(1,)), 
    Key("secStat", String()*(1,)), 
    Key("modu", String(), doCache=False), 
    Key("moved"), 
    Key("moveItems", String(), doCache=False), 
    Key("msgsLost", UInt(invalidValue="NaN"), doCache=False), 
    Key("noEnd"), 
    Key("noFacil"), 
    Key("noRotOrScaleCorr"), 
    Key("notEnoughData"), 
    Key("noVMSMsg"), 
    Key("objArcOff", Float(invalidValue="NaN", units="deg"), Float(invalidValue="NaN", units="deg/s"), Double(invalid="NaN", units="s"), Float(invalidValue="NaN", units="deg"), Float(invalidValue="NaN", units="deg/s"), Double(invalid="NaN", units="s")), 
    Key("objInstAng", Float(invalidValue="NaN", units="deg"), Float(invalidValue="NaN", units="deg/s"), Double(invalid="NaN", units="s")), 
    Key("objMag", Float(invalidValue="NaN", units="mag")), 
    Key("objName", String()), 
    Key("objNetPos", Float(invalidValue="NaN", units="deg"), Float(invalidValue="NaN", units="deg/s"), Double(invalid="NaN", units="s"), Float(invalidValue="NaN", units="deg"), Float(invalidValue="NaN", units="deg/s"), Double(invalid="NaN", units="s")), 
    Key("objOff", Float(invalidValue="NaN", units="deg"), Float(invalidValue="NaN", units="deg/s"), Double(invalid="NaN", units="s"), Float(invalidValue="NaN", units="deg"), Float(invalidValue="NaN", units="deg/s"), Double(invalid="NaN", units="s")), 
    Key("objPM", Float(invalidValue="NaN", units="as/century")*2, Float(invalidValue="NaN", units="as"), Float(invalidValue="NaN", units="km/s")), 
    Key("objPos", Float(invalidValue="NaN", units="deg"), Float(invalidValue="NaN", units="deg/s"), Double(invalid="NaN", units="s"), Float(invalidValue="NaN", units="deg"), Float(invalidValue="NaN", units="deg/s"), Double(invalid="NaN", units="s")), 
    Key("objSys", Enum("ICRS", "FK5", "FK4", "Gal", "Geo", "None", "Topo", "Obs", "Phys", "Mount", "Inst", "GImage"), Float(invalidValue="NaN")), 
    Key("objWavelength", Float(invalidValue="NaN", units="A")), 
    Key("objZPMPos", Float(invalidValue="NaN", units="deg"), Float(invalidValue="NaN", units="deg/s"), Double(invalid="NaN", units="s"), Float(invalidValue="NaN", units="deg"), Float(invalidValue="NaN", units="deg/s"), Double(invalid="NaN", units="s")), 
    Key("predFWHM", Float(invalidValue="NaN", units="as"), doCache=False), 
    Key("pressure", Float(invalidValue="NaN", units="Pa")), 
    Key("ptRefPos", Float(invalidValue="NaN", units="deg"), Float(invalidValue="NaN", units="deg/s"), Double(invalid="NaN", units="s"), Float(invalidValue="NaN", units="deg"), Float(invalidValue="NaN", units="deg/s"), Double(invalid="NaN", units="s"), doCache=False), 
    Key("ptRefRadius", Float(invalidValue="NaN", units="deg"), doCache=False), 
    Key("ptScanSize", Float(invalidValue="NaN", units="deg"), doCache=False), 
    Key("received", String(), doCache=False), 
    Key("rejectedAxisErrCode", String(invalid="?")*3, doCache=False), 
    Key("rotID", UInt(invalidValue="NaN")*2), 
    Key("rotMount", Float(invalidValue="NaN", units="deg"), Float(invalidValue="NaN", units="deg/s"), Double(invalid="NaN", units="s"), doCache=False), 
    Key("rotPhys", Float(invalidValue="NaN", units="deg"), Float(invalidValue="NaN", units="deg/s"), Double(invalid="NaN", units="s"), doCache=False), 
    Key("rotPos", Float(invalidValue="NaN", units="deg"), Float(invalidValue="NaN", units="deg/s"), Double(invalid="NaN", units="s")), 
    Key("rotType", Enum("None", "Obj", "Horiz", "Phys", "Mount")), 
    Key("rotWrapPref", Enum("None", "Near", "Negative", "Middle", "Positive"), doCache=False), 
    Key("scaleFac", Float(invalidValue="NaN")), 
    Key("scaleFacRange", Float(invalidValue="NaN")*2), 
    Key("schMoveTimes", Float(invalidValue="NaN")*10, doCache=False), 
    Key("secFocus", Float(invalidValue="NaN", units="um")), 
    Key("secTrussTemp", Float(invalidValue="NaN", units="C"),
        help="Average temperature of the secondary truss elements. Used for automatic focus correction."
    ), 
    Key("slewAdvTime", Float(invalidValue="NaN", units="s")), 
    Key("slewBeg", Double(invalid="NaN", units="s"), doCache=False), 
    Key("slewDuration", Float(invalidValue="NaN", units="s"), doCache=False), 
    Key("slewEnd"), 
    Key("slewSuperseded"), 
    Key("spiderInstAng", Float(invalidValue="NaN", units="deg"), Float(invalidValue="NaN", units="deg/s"), Double(invalid="NaN", units="s")), 
    Key("started"), 
    Key("stInterval", Float(invalidValue="NaN", units="s")*2, doCache=False), 
    Key("superseded"), 
    Key("tai", Double(invalid="NaN", units="s"), refreshCmd="show time"), 
    Key("tccDTime", Float(invalidValue="NaN", units="s"), doCache=False), 
    Key("tccPos", Float(invalidValue="NaN", units="deg", invalid="NaN", strFmt="%+07.2f")*3), 
    Key("tccStatus", String()*2), 
    Key("tdiCorr"), 
    Key("telMount", Float(invalidValue="NaN", units="deg"), Float(invalidValue="NaN", units="deg/s"), Double(invalid="NaN", units="s"), Float(invalidValue="NaN", units="deg"), Float(invalidValue="NaN", units="deg/s"), Double(invalid="NaN", units="s"), doCache=False), 
    Key("telPhys", Float(invalidValue="NaN", units="deg"), Float(invalidValue="NaN", units="deg/s"), Double(invalid="NaN", units="s"), Float(invalidValue="NaN", units="deg"), Float(invalidValue="NaN", units="deg/s"), Double(invalid="NaN", units="s"), doCache=False), 
    Key("text", String(), doCache=False), 
    Key("timeStamp", Double(invalid="NaN", units="s"), doCache=False), 
    Key("tLapse", Float(invalidValue="NaN", units="C/km")), 
    Key("trackAdvTime", Float(invalidValue="NaN", units="s"), doCache=False), 
    Key("userAdded"), 
    Key("userDeleted"), 
    Key("userInfo", UInt(invalidValue="NaN"), Hex(invalid="NaN", ), UInt(invalidValue="NaN"), Int(invalidValue="NaN"), UInt(invalidValue="NaN")*2), 
    Key("userNum", UInt(invalidValue="NaN")), 
    Key("ut1", Double(invalid="NaN", units="s")), 
    Key("utc_TAI", Float(invalidValue="NaN", units="s")), 
    Key("vmsMsg", String(), doCache=False), 
    Key("warnAzStatus"), 
    Key("warnAltStatus"), 
    Key("warnRotStatus"), 
    Key("windDir", Float(invalidValue="NaN", units="deg")), 
    Key("windSpeed", Float(invalidValue="NaN", units="m/s")), 
    Key("yourUserNum", UInt(invalidValue="NaN")), 
    # added for guide camera
    Key("guideOff", Float(invalidValue="NaN", units="deg"), Float(invalidValue="NaN", units="deg/s"), Double(invalid="NaN", units="s"), Float(invalidValue="NaN", units="deg"), Float(invalidValue="NaN", units="deg/s"), Double(invalid="NaN", units="s"), Float(invalidValue="NaN", units="deg"), Float(invalidValue="NaN", units="deg/s"), Double(invalid="NaN", units="s")), 
    Key("gCamCmd", String(), doCache=False), 
    Key("gcFocus", Float(invalidValue="NaN", units="um")), 
    Key("gcView", String()), 
    Key("gcNFilt", UInt(invalidValue="NaN")), 
    Key("gimScale", Float(invalidValue="NaN", units="pixels/deg")*2), 
    Key("gimCtr", Float(invalidValue="NaN", units="pixels")*2), 
    Key("gimLim", Float(invalidValue="NaN", units="pixels")*4), 
    # not yet in docs:
    Key("primStatus", UInt(invalidValue="NaN")*6), 
    Key("secStatus", UInt(invalidValue="NaN")*5), 
)
