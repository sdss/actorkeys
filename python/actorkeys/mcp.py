# Based on what the TCC knows about the perms widget
KeysDictionary('mcp', (1,1),
    Key('command', String(), help="Command string"),
    Key('ffLeafStatus', Enum("?", "Open", "Closed", "Invalid")*8, help="State of flat field petals"),
    Key('ffLeafCommandedOn', Bool("false", "true"), help="Flat field petals commanded close/open"),
    Key('ffLeafSelected', Enum("None", "Bottom?", "Top?", "All"), help="Flat field petals enabled"),
    Key("ffLamp", Bool(0, 1)*4, help="Detected state of flat field lamps"
    Key('ffLampCommandedOn', Bool("false", "true"), help="Commanded state of flat-field lamps"),
    Key("neLamp", Bool(0, 1)*4, help="Detected state of neon lamps"
    Key('neLampCommandedOn', Bool("false", "true"), help="Commanded state of neon lamps"),
    Key("hgCdLamp", Bool(0, 1)*4, help="Detected state of mercury/cadmium lamps"
    Key('hgCdLampCommandedOn', Bool("false", "true"), help="Commanded state of mercury/cadmium lamps"),
    Key('whiteLampCommandedOn', Bool("false", "true"), help="Commanded state of white lamps"),
    Key('saddleIsMounted', Bool("false", "true")),
    Key('instrumentNum', Int(invalid=-1), help="Instrument ID; 0=no instrument; 14=imager; -1=switches inconsistent or could not get semaphore"),
    Key('instrumentNumConsistent', Bool("false", "true"), help="Do the three instrument ID switches agree? If not, instrumentNumValues is also output."),
    Key('instrumentNumValues', Int()*3, help="Reading from each instrument ID switch"),
    Key('azFiducialMaxCorr', Int()),
    Key('altFiducialMaxCorr', Int()),
    Key('rotFiducialMaxCorr', Int()),
    Key('azFiducialVersion', String()),
    Key('altFiducialVersion', String()),
    Key('rotFiducialVersion', String()),
    Key('goodFiducialVersions', Bool("false", "true"), help="The fiducial version numbers are consistent"),
    Key('plcFiducialVersion', Int()),
)
