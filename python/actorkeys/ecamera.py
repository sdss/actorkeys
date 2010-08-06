KeysDictionary('ecamera', (0, 3),
    Key("text", String(help="text for humans")),
    Key("version", String(help="EUPS/SVN version")),
    Key("simulating", 
       Bool('Off', 'On', help="Are we reading simulated/historical data, or taking new images?"),
       String(help="directory from which simulations are reading data."),
       Int(help="sequence number of the last read image")),
    Key("exposureState", 
       Enum('idle','integrating','reading','done','aborted'),
       Float(help="remaining time for this state (0 if none, short or unknown)", units="sec"),
       Float(help="total time for this state (0 if none, short or unknown)", units="sec")),
    Key("filename", 
       String(help='last read file')),
    Key("cooler",
        Float(name="setpoint", help="CCD temperature setpoint", units="degC"),
        Float(name="ccdTemp", help="CCD temperature reported by the camera", units="degC"),
        Float(name="heatsinkTemp", help="Heatsink temperature reported by the camera", units="degC"),
        Float(name="coolerLoad", help="Load on the cooler", units="percent"),
        Int(name="fanStatus", help="Fan status. Always 0 with this camera"),
        Enum('Off', 'RampingToSetPoint', 'Correcting', 'RampingToAmbient', 'AtAmbient', 'AtMax', 'AtMin', 'AtSetPoint', 'Invalid',
             name="coolerStatus",
             help="Cooler status. Correcting appears to be the normal state, All others should be considered bad. AtSetPoint does not appear to occur.")),
    )

