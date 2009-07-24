KeysDictionary('gcamera', (0, 1),
    Key("text", String(help="text for humans")),
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
    )
           
