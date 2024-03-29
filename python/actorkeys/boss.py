#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: José Sánchez-Gallego (gallegoj@uw.edu)
# @Date: 2019-12-29
# @Filename: boss.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

# type: ignore


KeysDictionary(
    "boss",
    (2, 18),
    *(
        Key("text", String(), help="text for humans"),
        Key("version", String(), help="version string derived from svn info."),
        # ICC Keywords
        Key(
            "exposureState",
            Enum(
                "IDLE",
                "FLUSHING",
                "INTEGRATING",
                "PAUSED",
                "PREREADING",
                "READING",
                "LEGIBLE",
                "ABORTED",
                name="state",
            ),
            Float(
                name="totalTime",
                help="esimated total time for this state; "
                "0 if too short to bother with a countdown timer",
                units="sec",
            ),
            Float(
                name="elapsedTime",
                help="elapsed time for this state; "
                "0 if too short to bother with a countdown timer",
                units="sec",
            ),
            help="The current state of the exposure and associated timings.",
        ),
        Key("exposureId", UInt(), help="last exposure number"),
        Key(
            "BeginExposure",
            UInt(name="time"),
            Float(name="mjd", units="mjd", strFmt="%.2f"),
            help="Time that an exposure began.",
        ),
        Key(
            "EndExposure",
            UInt(name="time"),
            Float(name="mjd", units="mjd", strFmt="%.2f"),
            help="Time that an exposure ended.",
        ),
        Key("daqVersion", String(), help="DAQ Interface python code version."),
        Key(
            "hardwareStatus",
            Bits("sp1cam", "sp2cam", "sp1mech", "sp2mech", "sp1daq", "sp2daq"),
            help="Connection status of each current piece of hardware.",
        ),
        Key("lastFlush", UInt(units="sec"), help="Time of last flush."),
        # specMech Keywords
        Key(
            "shutterStatus",
            Bits("OpenSwitch", "ClosedSwitch"),
            help="Status of the two shutter switches",
        ),
        Key(
            "screenStatus",
            Bits(
                "RightOpenSensor",
                "RightClosedSensor",
                "LeftOpenSensor",
                "LeftClosedSensor",
            ),
            help="Status of the hartman screens, the left bit represents "
            "the closed sensor and the right bit the open sensor.",
        ),
        Key(
            "motorPosition",
            *[
                Int(invalid="-9999999", name="sp%d_%s" % (spNum, axis))
                for spNum in (1,)
                for axis in ("A", "B", "C")
            ],
            help="The position of the motors in ticks of both spectographs."
        ),
        Key(
            "motorStatus",
            *[
                Bits(
                    "Stopped",
                    "FindEdge",
                    "Slave",
                    ":1",
                    "SlewMode",
                    "MotorOff",
                    "LimitSwitch",
                    "OnTarget",
                    name="sp%d_%s" % (spNum, axis),
                )
                for spNum in (1,)
                for axis in ("A", "B", "C")
            ],
            help="Status of the motors."
        ),
        Key("specMechVersion", String(), help="Version string of sp1mech."),
        Key("specMechProtocol", String(), help="Protocol string of sp1mech"),
        Key(
            "slitIDs",
            Int(name="sp1SlitID", help="slit ID reported by sp1 (normalized)"),
            help="slitIDs reported at the two slitheads. "
            "Should match each other and the mcp cartridge ID",
        ),
        Key(
            "sp1LastShutterTime",
            Float(name="openTime", help="last measured open transit time", units="sec"),
            Float(
                name="closeTime", help="last measured open transit time", units="sec"
            ),
            help="last measured open and close transit times for sp1 shutter",
        ),
        Key(
            "sp1Humidity",
            Float(name="hartmann", help="humidity at hartmann doors", units="percent"),
            Float(
                name="centralOptics", help="humidity at central optics", units="percent"
            ),
            help="humidity inside sp1",
        ),
        Key(
            "sp1Temp",
            Float(name="median", help="median of temp measurements", units="degreesC"),
            Float(
                name="hartmannTop",
                help="temp at top of hartmann doors",
                units="degreesC",
            ),
            Float(name="redCamTop", help="temp at top of red camera", units="degreesC"),
            Float(
                name="blueCamTop", help="temp at top of blue camera", units="degreesC"
            ),
            Float(
                name="redCamBottom",
                help="temp at bottom of red camera",
                units="degreesC",
            ),
            Float(
                name="blueCamBottom",
                help="temp at bottom of blue camera",
                units="degreesC",
            ),
            help="temperatures inside sp1",
        ),
        # DAQ Keywords
        Key(
            "sp1ReadoutErrors",
            Int(name="exposureID", help="the exposure ID for the errors"),
            Int(name="errorCnt", help="the total number of errors for the exposure"),
            Int(
                name="syncErrorCnt",
                help="the number of lines with line synchronization errors",
            ),
            Int(
                name="pixelErrorCnt", help="the number of lines with pixel count errors"
            ),
            Int(
                name="frameErrorCnt",
                help="the number of lines with insufficient or extra pixels",
            ),
            help="Errors noted by the DAQ during sp1 readout.",
        ),
        # LN2 status keywords
        Key("sp1camLN2Fill", String()),
        Key("sp1camFillTime", Int()),
        Key("sp1camNextFill", Int()),
        Key("sp1camSecondaryDewarPress", Int()),
        Key("sp1camNormRetrig", Int()),
        Key("sp1camWarmFillTime", Int()),
        Key("sp1camWarmFills", Int()),
        Key("sp1camWarmRetrig", Int()),
        Key("sp1camFillFault", String()),
        Key("sp1camEmptyTrigger", String()),
        # Cam Micro Keywords
        Key(
            "camCheck",
            String() * (0,),
            help="A list of strings of keywords that are out of spec.",
        ),
        Key(
            "camCheckAlert",
            String(name="name", help="keyword name"),
            String(name="value", help="keyword str(value)"),
            help="keyword is reported out of spec by camCheck",
        ),
        Key(
            "aliveAt",
            Int(),
            help="Unix seconds at which point the ICC was declared alive",
        ),
        Key(
            "sp1camRawText",
            String(),
            help="Raw text of TDS command",
        ),
        Key(
            "SP1RedIonPumpLatched",
            Float(),
            help="Unix seconds when error was seen",
        ),
        Key(
            "SP1BlueIonPumpLatched",
            Float(),
            help="Unix seconds when error was seen",
        ),
        Key("ln2stat", String()),
        # camStatus
        Key(
            "SP1LN2Fill",
            Enum("ON", "OFF", "FAULT!!!"),
        ),
        Key("SP1CameraMonitor", Enum("ON", "OFF")),
        Key("SP1Cam00", Int()),
        Key("SP1Cam01", Int()),
        Key("SP1Cam02", Int()),
        Key("SP1Cam03", Int()),
        Key("SP1SerialSpeed", String()),
        Key("SP1Pixels", Int()),
        Key("SP1BinnedPixels", Int()),
        Key("SP1BlueParallelDir", Enum("FWD", "REV", "UNKNOWN")),
        Key("SP1BlueParallelState", Enum("CLOCK", "STOPPED", "UNKNOWN")),
        Key("SP1RedParallelDir", Enum("FWD", "REV", "UNKNOWN")),
        Key("SP1RedParallelState", Enum("CLOCK", "STOPPED", "UNKNOWN")),
        Key("SP1DataMode", Enum("FRAME", "CONTINUOUS")),
        Key("SP1Lines", Int()),
        Key("SP1BinnedLines", Int()),
        Key("SP1DataState", Enum("IDLE", "READING", "DRIFTSCANNING", "CLOCKING")),
        Key("SP1Linestart", Enum("ENABLED", "DISABLED")),
        Key("SP1LinestartPeriod", String()),
        Key("SP1DacsSet", Enum("OK", "ERROR")),
        Key("SP1ExecBoot", Enum("UNACKNOWLEDGED", "ACKNOWLEDGED")),
        Key("SP1PhaseBoot", Enum("UNACKNOWLEDGED", "ACKNOWLEDGED", "BUSY")),
        Key("SP1USR1", Int()),
        Key("SP1USR2", Int()),
        Key("SP1USR3", Int()),
        Key("SP1SecondaryDewarPress", Int()),
        Key("SP1RedIonPump", Float(strFmt="%.2f")),
        Key("SP1BlueIonPump", Float(strFmt="%.2f")),
        # Cam Check keywords
        Key(
            "camCheckResponse",
            String() * (0,),
            help="A list of strings that indicate the out of range values. "
            "Possible values include DacsSet, ExecBoot, PhaseBoot, LN2Fill, "
            "LN2EmptyDewar, SecondaryDewarPress, and any of the read voltages.",
        ),
        # Version String
        Key(
            "camForthVersion",
            String() * (0,),
            help="Version strings for the cam micros.",
        ),
        # VOLTS
        # Machine generated keys:
        Key(
            "SP1B3HeaterVNom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_HEATERV on SP1 B3",
        ),
        Key(
            "SP1B3HeaterVRead",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_HEATERV on SP1 B3",
        ),
        Key(
            "SP1R1VSb2Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VS- on SP1 R1",
        ),
        Key(
            "SP1R1VSb2Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VS- on SP1 R1",
        ),
        Key(
            "SP1R1VSb2Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VS- on SP1 R1",
        ),
        Key(
            "SP1R1VSc2Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VS+ on SP1 R1",
        ),
        Key(
            "SP1R1VSc2Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VS+ on SP1 R1",
        ),
        Key(
            "SP1R1VSc2Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VS+ on SP1 R1",
        ),
        Key(
            "SP1B2LN2TempNom",
            Float(units="deg K", strFmt="%.3f"),
            help="Translated value of B2_LN2TEMP on SP1 B2",
        ),
        Key(
            "SP1B2LN2TempRead",
            Float(units="deg K", strFmt="%.3f"),
            help="Translated value of B2_LN2TEMP on SP1 B2",
        ),
        Key(
            "SP1R0TZeroBias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_TZERO on SP1 R0",
        ),
        Key(
            "SP1R0TZeroNom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_TZERO on SP1 R0",
        ),
        Key(
            "SP1R0TZeroRead",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_TZERO on SP1 R0",
        ),
        Key(
            "SP1R1HeaterVNom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_HEATERV on SP1 R1",
        ),
        Key(
            "SP1R1HeaterVRead",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_HEATERV on SP1 R1",
        ),
        Key(
            "SP1R1VLG2Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VLG on SP1 R1",
        ),
        Key(
            "SP1R1VLG2Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VLG on SP1 R1",
        ),
        Key(
            "SP1R1VLG2Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VLG on SP1 R1",
        ),
        Key(
            "SP1R0VRD2Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VRD2 on SP1 R0",
        ),
        Key(
            "SP1R0VRD2Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VRD2 on SP1 R0",
        ),
        Key(
            "SP1R0VRD2Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VRD2 on SP1 R0",
        ),
        Key(
            "SP1R1VDD4Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VDD2 on SP1 R1",
        ),
        Key(
            "SP1R1VDD4Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VDD2 on SP1 R1",
        ),
        Key(
            "SP1R1VDD4Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VDD2 on SP1 R1",
        ),
        Key(
            "SP1R1VDD3Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VDD1 on SP1 R1",
        ),
        Key(
            "SP1R1VDD3Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VDD1 on SP1 R1",
        ),
        Key(
            "SP1R1VDD3Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VDD1 on SP1 R1",
        ),
        Key(
            "SP1R1VLG4Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VT+ on SP1 R1",
        ),
        Key(
            "SP1R1VLG4Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VT+ on SP1 R1",
        ),
        Key(
            "SP1R1VLG4Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VT+ on SP1 R1",
        ),
        Key(
            "SP1B2VRD1Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VRD1 on SP1 B2",
        ),
        Key(
            "SP1B2VRD1Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VRD1 on SP1 B2",
        ),
        Key(
            "SP1B2VRD1Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VRD1 on SP1 B2",
        ),
        Key(
            "SP1B2VRD2Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VRD2 on SP1 B2",
        ),
        Key(
            "SP1B2VRD2Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VRD2 on SP1 B2",
        ),
        Key(
            "SP1B2VRD2Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VRD2 on SP1 B2",
        ),
        Key(
            "SP1R1VLG3Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VT- on SP1 R1",
        ),
        Key(
            "SP1R1VLG3Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VT- on SP1 R1",
        ),
        Key(
            "SP1R1VLG3Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VT- on SP1 R1",
        ),
        Key(
            "SP1B3VPbCBias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_VP12- on SP1 B3",
        ),
        Key(
            "SP1B3VPbCNom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_VP12- on SP1 B3",
        ),
        Key(
            "SP1B3VPbCRead",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_VP12- on SP1 B3",
        ),
        Key(
            "SP1B3VPcCBias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_VP12+ on SP1 B3",
        ),
        Key(
            "SP1B3VPcCNom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_VP12+ on SP1 B3",
        ),
        Key(
            "SP1B3VPcCRead",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_VP12+ on SP1 B3",
        ),
        Key(
            "SP1B2VDD2Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VDD2 on SP1 B2",
        ),
        Key(
            "SP1B2VDD2Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VDD2 on SP1 B2",
        ),
        Key(
            "SP1B2VDD2Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VDD2 on SP1 B2",
        ),
        Key(
            "SP1B2VDD1Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VDD1 on SP1 B2",
        ),
        Key(
            "SP1B2VDD1Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VDD1 on SP1 B2",
        ),
        Key(
            "SP1B2VDD1Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VDD1 on SP1 B2",
        ),
        Key(
            "SP1B3VPcDBias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_VP3+ on SP1 B3",
        ),
        Key(
            "SP1B3VPcDNom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_VP3+ on SP1 B3",
        ),
        Key(
            "SP1B3VPcDRead",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_VP3+ on SP1 B3",
        ),
        Key(
            "SP1B3VPbDBias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_VP3- on SP1 B3",
        ),
        Key(
            "SP1B3VPbDNom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_VP3- on SP1 B3",
        ),
        Key(
            "SP1B3VPbDRead",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_VP3- on SP1 B3",
        ),
        Key(
            "SP1B3VLG34Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_VLG on SP1 B3",
        ),
        Key(
            "SP1B3VLG34Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_VLG on SP1 B3",
        ),
        Key(
            "SP1B3VLG34Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_VLG on SP1 B3",
        ),
        Key(
            "SP1B2VPcABias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VP12+ on SP1 B2",
        ),
        Key(
            "SP1B2VPcANom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VP12+ on SP1 B2",
        ),
        Key(
            "SP1B2VPcARead",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VP12+ on SP1 B2",
        ),
        Key(
            "SP1B2VPbABias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VP12- on SP1 B2",
        ),
        Key(
            "SP1B2VPbANom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VP12- on SP1 B2",
        ),
        Key(
            "SP1B2VPbARead",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VP12- on SP1 B2",
        ),
        Key(
            "SP1R0VTbBias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VT+ on SP1 R0",
        ),
        Key(
            "SP1R0VTbNom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VT+ on SP1 R0",
        ),
        Key(
            "SP1R0VTbRead",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VT+ on SP1 R0",
        ),
        Key(
            "SP1B2CCDTempNom",
            Float(units="deg C", strFmt="%.3f"),
            help="Translated value of B2_CCDTEMP on SP1 B2",
        ),
        Key(
            "SP1B2CCDTempRead",
            Float(units="deg C", strFmt="%.3f"),
            help="Translated value of B2_CCDTEMP on SP1 B2",
        ),
        Key(
            "SP1R1INegTrim4Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_I-TRIM2 on SP1 R1",
        ),
        Key(
            "SP1R1INegTrim4Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_I-TRIM2 on SP1 R1",
        ),
        Key(
            "SP1R1INegTrim4Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_I-TRIM2 on SP1 R1",
        ),
        Key(
            "SP1R0VTcBias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VT- on SP1 R0",
        ),
        Key(
            "SP1R0VTcNom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VT- on SP1 R0",
        ),
        Key(
            "SP1R0VTcRead",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VT- on SP1 R0",
        ),
        Key(
            "SP1R1INegTrim3Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_I-TRIM1 on SP1 R1",
        ),
        Key(
            "SP1R1INegTrim3Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_I-TRIM1 on SP1 R1",
        ),
        Key(
            "SP1R1INegTrim3Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_I-TRIM1 on SP1 R1",
        ),
        Key(
            "SP1R1IPosTrim3Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_I+TRIM1 on SP1 R1",
        ),
        Key(
            "SP1R1IPosTrim3Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_I+TRIM1 on SP1 R1",
        ),
        Key(
            "SP1R1IPosTrim3Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_I+TRIM1 on SP1 R1",
        ),
        Key(
            "SP1R1IPosTrim4Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_I+TRIM2 on SP1 R1",
        ),
        Key(
            "SP1R1IPosTrim4Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_I+TRIM2 on SP1 R1",
        ),
        Key(
            "SP1R1IPosTrim4Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_I+TRIM2 on SP1 R1",
        ),
        Key(
            "SP1B2INegTrim1Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_I-TRIM1 on SP1 B2",
        ),
        Key(
            "SP1B2INegTrim1Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_I-TRIM1 on SP1 B2",
        ),
        Key(
            "SP1B2INegTrim1Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_I-TRIM1 on SP1 B2",
        ),
        Key(
            "SP1B2INegTrim2Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_I-TRIM2 on SP1 B2",
        ),
        Key(
            "SP1B2INegTrim2Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_I-TRIM2 on SP1 B2",
        ),
        Key(
            "SP1B2INegTrim2Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_I-TRIM2 on SP1 B2",
        ),
        Key(
            "SP1B2VPcBBias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VP3+ on SP1 B2",
        ),
        Key(
            "SP1B2VPcBNom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VP3+ on SP1 B2",
        ),
        Key(
            "SP1B2VPcBRead",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VP3+ on SP1 B2",
        ),
        Key(
            "SP1B2VPbBBias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VP3- on SP1 B2",
        ),
        Key(
            "SP1B2VPbBNom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VP3- on SP1 B2",
        ),
        Key(
            "SP1B2VPbBRead",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VP3- on SP1 B2",
        ),
        Key(
            "SP1R0VSWbBias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VSW- on SP1 R0",
        ),
        Key(
            "SP1R0VSWbNom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VSW- on SP1 R0",
        ),
        Key(
            "SP1R0VSWbRead",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VSW- on SP1 R0",
        ),
        Key(
            "SP1R0VSb1Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VS- on SP1 R0",
        ),
        Key(
            "SP1R0VSb1Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VS- on SP1 R0",
        ),
        Key(
            "SP1R0VSb1Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VS- on SP1 R0",
        ),
        Key(
            "SP1R0VSc1Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VS+ on SP1 R0",
        ),
        Key(
            "SP1R0VSc1Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VS+ on SP1 R0",
        ),
        Key(
            "SP1R0VSc1Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VS+ on SP1 R0",
        ),
        Key(
            "SP1B3VDD3Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_VDD1 on SP1 B3",
        ),
        Key(
            "SP1B3VDD3Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_VDD1 on SP1 B3",
        ),
        Key(
            "SP1B3VDD3Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_VDD1 on SP1 B3",
        ),
        Key(
            "SP1R0VDD1Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VDD1 on SP1 R0",
        ),
        Key(
            "SP1R0VDD1Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VDD1 on SP1 R0",
        ),
        Key(
            "SP1R0VDD1Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VDD1 on SP1 R0",
        ),
        Key(
            "SP1R0VDD2Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VDD2 on SP1 R0",
        ),
        Key(
            "SP1R0VDD2Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VDD2 on SP1 R0",
        ),
        Key(
            "SP1R0VDD2Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VDD2 on SP1 R0",
        ),
        Key(
            "SP1B3VDD4Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_VDD2 on SP1 B3",
        ),
        Key(
            "SP1B3VDD4Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_VDD2 on SP1 B3",
        ),
        Key(
            "SP1B3VDD4Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_VDD2 on SP1 B3",
        ),
        Key(
            "SP1B2VSb1Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VS- on SP1 B2",
        ),
        Key(
            "SP1B2VSb1Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VS- on SP1 B2",
        ),
        Key(
            "SP1B2VSb1Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VS- on SP1 B2",
        ),
        Key(
            "SP1R0VPbBBias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VP3+ on SP1 R0",
        ),
        Key(
            "SP1R0VPbBNom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VP3+ on SP1 R0",
        ),
        Key(
            "SP1R0VPbBRead",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VP3+ on SP1 R0",
        ),
        Key(
            "SP1R0VPcBBias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VP3- on SP1 R0",
        ),
        Key(
            "SP1R0VPcBNom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VP3- on SP1 R0",
        ),
        Key(
            "SP1R0VPcBRead",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VP3- on SP1 R0",
        ),
        Key(
            "SP1B3VRoffBias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_VSW- on SP1 B3",
        ),
        Key(
            "SP1B3VRoffNom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_VSW- on SP1 B3",
        ),
        Key(
            "SP1B3VRoffRead",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_VSW- on SP1 B3",
        ),
        Key(
            "SP1B2VSc1Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VS+ on SP1 B2",
        ),
        Key(
            "SP1B2VSc1Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VS+ on SP1 B2",
        ),
        Key(
            "SP1B2VSc1Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VS+ on SP1 B2",
        ),
        Key(
            "SP1R1VRonBias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VSW- on SP1 R1",
        ),
        Key(
            "SP1R1VRonNom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VSW- on SP1 R1",
        ),
        Key(
            "SP1R1VRonRead",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VSW- on SP1 R1",
        ),
        Key(
            "SP1B3VSb2Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_VS- on SP1 B3",
        ),
        Key(
            "SP1B3VSb2Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_VS- on SP1 B3",
        ),
        Key(
            "SP1B3VSb2Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_VS- on SP1 B3",
        ),
        Key(
            "SP1R0VLG1Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VLG on SP1 R0",
        ),
        Key(
            "SP1R0VLG1Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VLG on SP1 R0",
        ),
        Key(
            "SP1R0VLG1Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VLG on SP1 R0",
        ),
        Key(
            "SP1B3VSc2Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_VS+ on SP1 B3",
        ),
        Key(
            "SP1B3VSc2Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_VS+ on SP1 B3",
        ),
        Key(
            "SP1B3VSc2Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_VS+ on SP1 B3",
        ),
        Key(
            "SP1R0INegTrim2Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_I-TRIM2 on SP1 R0",
        ),
        Key(
            "SP1R0INegTrim2Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_I-TRIM2 on SP1 R0",
        ),
        Key(
            "SP1R0INegTrim2Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_I-TRIM2 on SP1 R0",
        ),
        Key(
            "SP1R0INegTrim1Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_I-TRIM1 on SP1 R0",
        ),
        Key(
            "SP1R0INegTrim1Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_I-TRIM1 on SP1 R0",
        ),
        Key(
            "SP1R0INegTrim1Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_I-TRIM1 on SP1 R0",
        ),
        Key(
            "SP1R0TSetBias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_TSET on SP1 R0",
        ),
        Key(
            "SP1R0TSetNom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_TSET on SP1 R0",
        ),
        Key(
            "SP1R0TSetRead",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_TSET on SP1 R0",
        ),
        Key(
            "SP1R0CCDTempNom",
            Float(units="deg C", strFmt="%.3f"),
            help="Translated value of R0_CCDTEMP on SP1 R0",
        ),
        Key(
            "SP1R0CCDTempRead",
            Float(units="deg C", strFmt="%.3f"),
            help="Translated value of R0_CCDTEMP on SP1 R0",
        ),
        Key(
            "SP1R1VRedPurgeBias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VP3- on SP1 R1",
        ),
        Key(
            "SP1R1VRedPurgeNom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VP3- on SP1 R1",
        ),
        Key(
            "SP1R1VRedPurgeRead",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VP3- on SP1 R1",
        ),
        Key(
            "SP1R1VRedEraseBias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VP3+ on SP1 R1",
        ),
        Key(
            "SP1R1VRedEraseNom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VP3+ on SP1 R1",
        ),
        Key(
            "SP1R1VRedEraseRead",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VP3+ on SP1 R1",
        ),
        Key(
            "SP1R1VPbCBias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VP12+ on SP1 R1",
        ),
        Key(
            "SP1R1VPbCNom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VP12+ on SP1 R1",
        ),
        Key(
            "SP1R1VPbCRead",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VP12+ on SP1 R1",
        ),
        Key(
            "SP1R1VPcCBias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VP12- on SP1 R1",
        ),
        Key(
            "SP1R1VPcCNom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VP12- on SP1 R1",
        ),
        Key(
            "SP1R1VPcCRead",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VP12- on SP1 R1",
        ),
        Key(
            "SP1B2IPosTrim2Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_I+TRIM2 on SP1 B2",
        ),
        Key(
            "SP1B2IPosTrim2Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_I+TRIM2 on SP1 B2",
        ),
        Key(
            "SP1B2IPosTrim2Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_I+TRIM2 on SP1 B2",
        ),
        Key(
            "SP1B2IPosTrim1Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_I+TRIM1 on SP1 B2",
        ),
        Key(
            "SP1B2IPosTrim1Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_I+TRIM1 on SP1 B2",
        ),
        Key(
            "SP1B2IPosTrim1Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_I+TRIM1 on SP1 B2",
        ),
        Key(
            "SP1B2VSWbBias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VSW- on SP1 B2",
        ),
        Key(
            "SP1B2VSWbNom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VSW- on SP1 B2",
        ),
        Key(
            "SP1B2VSWbRead",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VSW- on SP1 B2",
        ),
        Key(
            "SP1R0VRD1Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VRD1 on SP1 R0",
        ),
        Key(
            "SP1R0VRD1Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VRD1 on SP1 R0",
        ),
        Key(
            "SP1R0VRD1Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VRD1 on SP1 R0",
        ),
        Key(
            "SP1B3IPosTrim4Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_I+TRIM2 on SP1 B3",
        ),
        Key(
            "SP1B3IPosTrim4Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_I+TRIM2 on SP1 B3",
        ),
        Key(
            "SP1B3IPosTrim4Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_I+TRIM2 on SP1 B3",
        ),
        Key(
            "SP1B3IPosTrim3Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_I+TRIM1 on SP1 B3",
        ),
        Key(
            "SP1B3IPosTrim3Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_I+TRIM1 on SP1 B3",
        ),
        Key(
            "SP1B3IPosTrim3Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_I+TRIM1 on SP1 B3",
        ),
        Key(
            "SP1B3INegTrim3Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_I-TRIM1 on SP1 B3",
        ),
        Key(
            "SP1B3INegTrim3Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_I-TRIM1 on SP1 B3",
        ),
        Key(
            "SP1B3INegTrim3Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_I-TRIM1 on SP1 B3",
        ),
        Key(
            "SP1B3INegTrim4Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_I-TRIM2 on SP1 B3",
        ),
        Key(
            "SP1B3INegTrim4Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_I-TRIM2 on SP1 B3",
        ),
        Key(
            "SP1B3INegTrim4Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_I-TRIM2 on SP1 B3",
        ),
        Key(
            "SP1R1VRD3Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VRD1 on SP1 R1",
        ),
        Key(
            "SP1R1VRD3Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VRD1 on SP1 R1",
        ),
        Key(
            "SP1R1VRD3Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VRD1 on SP1 R1",
        ),
        Key(
            "SP1R1VRD4Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VRD2 on SP1 R1",
        ),
        Key(
            "SP1R1VRD4Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VRD2 on SP1 R1",
        ),
        Key(
            "SP1R1VRD4Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VRD2 on SP1 R1",
        ),
        Key(
            "SP1B2TSetBias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_TSET on SP1 B2",
        ),
        Key(
            "SP1B2TSetNom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_TSET on SP1 B2",
        ),
        Key(
            "SP1B2TSetRead",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_TSET on SP1 B2",
        ),
        Key(
            "SP1B2TZeroBias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_TZERO on SP1 B2",
        ),
        Key(
            "SP1B2TZeroNom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_TZERO on SP1 B2",
        ),
        Key(
            "SP1B2TZeroRead",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_TZERO on SP1 B2",
        ),
        Key(
            "SP1R0VPcABias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VP12- on SP1 R0",
        ),
        Key(
            "SP1R0VPcANom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VP12- on SP1 R0",
        ),
        Key(
            "SP1R0VPcARead",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VP12- on SP1 R0",
        ),
        Key(
            "SP1R0VPbABias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VP12+ on SP1 R0",
        ),
        Key(
            "SP1R0VPbANom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VP12+ on SP1 R0",
        ),
        Key(
            "SP1R0VPbARead",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_VP12+ on SP1 R0",
        ),
        Key(
            "SP1B2VTbBias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VT- on SP1 B2",
        ),
        Key(
            "SP1B2VTbNom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VT- on SP1 B2",
        ),
        Key(
            "SP1B2VTbRead",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VT- on SP1 B2",
        ),
        Key(
            "SP1B2VTcBias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VT+ on SP1 B2",
        ),
        Key(
            "SP1B2VTcNom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VT+ on SP1 B2",
        ),
        Key(
            "SP1B2VTcRead",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VT+ on SP1 B2",
        ),
        Key(
            "SP1B2VRonBias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VR on SP1 B2",
        ),
        Key(
            "SP1B2VRonNom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VR on SP1 B2",
        ),
        Key(
            "SP1B2VRonRead",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VR on SP1 B2",
        ),
        Key(
            "SP1R1VSubsBias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VR on SP1 R1",
        ),
        Key(
            "SP1R1VSubsNom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VR on SP1 R1",
        ),
        Key(
            "SP1R1VSubsRead",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R1_VR on SP1 R1",
        ),
        Key(
            "SP1R0LN2TempNom",
            Float(units="deg K", strFmt="%.3f"),
            help="Translated value of R0_LN2TEMP on SP1 R0",
        ),
        Key(
            "SP1R0LN2TempRead",
            Float(units="deg K", strFmt="%.3f"),
            help="Translated value of R0_LN2TEMP on SP1 R0",
        ),
        Key(
            "SP1R0IPosTrim1Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_I+TRIM1 on SP1 R0",
        ),
        Key(
            "SP1R0IPosTrim1Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_I+TRIM1 on SP1 R0",
        ),
        Key(
            "SP1R0IPosTrim1Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_I+TRIM1 on SP1 R0",
        ),
        Key(
            "SP1R0IPosTrim2Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_I+TRIM2 on SP1 R0",
        ),
        Key(
            "SP1R0IPosTrim2Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_I+TRIM2 on SP1 R0",
        ),
        Key(
            "SP1R0IPosTrim2Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of R0_I+TRIM2 on SP1 R0",
        ),
        Key(
            "SP1B3VRD4Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_VRD2 on SP1 B3",
        ),
        Key(
            "SP1B3VRD4Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_VRD2 on SP1 B3",
        ),
        Key(
            "SP1B3VRD4Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_VRD2 on SP1 B3",
        ),
        Key(
            "SP1B3VRD3Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_VRD1 on SP1 B3",
        ),
        Key(
            "SP1B3VRD3Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_VRD1 on SP1 B3",
        ),
        Key(
            "SP1B3VRD3Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B3_VRD1 on SP1 B3",
        ),
        Key(
            "SP1B2VLG12Bias",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VLG on SP1 B2",
        ),
        Key(
            "SP1B2VLG12Nom",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VLG on SP1 B2",
        ),
        Key(
            "SP1B2VLG12Read",
            Float(units="volts", strFmt="%.3f"),
            help="Translated value of B2_VLG on SP1 B2",
        ),
    )
)
